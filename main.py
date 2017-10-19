from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "company"])
# execute(["scrapy", "crawl", "job"])
# execute(["scrapy", "crawl", "people"])

execute(["scrapy", "crawl", "baiduimage"])
