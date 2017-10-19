# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymongo
from pymongo import IndexModel, ASCENDING
from JiashanRencai.items import CompanyItem, JobItem
from scrapy.exceptions import DropItem

from scrapy.pipelines.images import ImagesPipeline


class JiashanrencaiPipeline(object):
    def process_item(self, item, spider):
        return item


class CompanyMongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["rencai"]
        self.company = db["company"]

        idx = IndexModel([('company_id', ASCENDING)], unique=True)
        self.company.create_indexes([idx])

    def process_item(self, item, spider):
        """ 判断类型 存入MongoDB """
        if isinstance(item, CompanyItem):
            try:
                self.company.update_one({'company_id': item['company_id']}, {'$set': dict(item)}, upsert=True)
            except Exception:
                pass
        return item


class JobMongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["rencai"]
        self.job = db["job"]

        idx = IndexModel([('job_id', ASCENDING)], unique=True)
        self.job.create_indexes([idx])

    def process_item(self, item, spider):
        """ 判断类型 存入MongoDB """
        if isinstance(item, JobItem):
            try:
                self.job.update_one({'job_id': item['job_id']}, {'$set': dict(item)}, upsert=True)
            except Exception:
                pass
        return item


class PeopelImagePipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_urls'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
