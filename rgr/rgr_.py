import sys
from rgr.spiders.phone_spider import PhonesSpider
from scrapy.commands import BaseRunSpiderCommand
from scrapy.exceptions import UsageError
from scrapy.crawler import CrawlerProcess
from http import HTTPStatus


class Command(BaseRunSpiderCommand):

    requires_project = True


    def syntax(self):
        return ""

    def short_desc(self):
        return "Run a phone number collector"

    def run(self):
        stdin_ = sys.stdin
        f = open('stdin.txt', 'w')
        for l in stdin_:
        	f.write(l)
        f.close()      

        process = CrawlerProcess({
            'LOG_ENABLED': False, 
            'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
            'ROBOTSTXT_OBEY': True,
            'BOT_NAME': 'rgr',
            'HTTPERROR_ALLOWED_CODES': [code.value for code in HTTPStatus],
        })

        process.crawl(PhonesSpider)
        process.start() 
