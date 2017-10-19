# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field


class CompanyItem(Item):
    company_id = Field()
    name = Field()
    register_time = Field()
    visit_count = Field()
    comment = Field()
    area = Field()
    department = Field()
    c_property = Field()
    tel = Field()
    hangye = Field()
    address = Field()


class JobItem(Item):
    name = Field()
    public_time = Field()
    job_id = Field()
    company_id = Field()
    start_time = Field()
    end_time = Field()
    visit_count = Field()
    salar = Field()
    job_type = Field()
    job_num = Field()
    job_sex = Field()
    job_area = Field()
    job_label = Field()
    job_info = Field()


class PeopleItem(Item):
    image_urls = Field()
    image_paths = Field()