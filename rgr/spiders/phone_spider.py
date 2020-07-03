import re
import json
import scrapy
import phonenumbers


class PhonesSpider(scrapy.Spider):
    name = "phones"

    def start_requests(self):
        f = open('stdin.txt', 'r')
        lines = f.readlines()
        f.close()
        urls = lines
        for url in urls:
            url = url.replace('\n', '')
            
            if url:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'phones-{page}.json'.format(page=page)
        image_links = re.findall('src="([^"]+)"', response.text)
        logo_link = ''
        known_phones = []
        for l in image_links:
            if l.lower().find('logo') != -1:
                logo_link = l
                break
        with open(filename, 'w') as f:
            has_phone = False
            for m in phonenumbers.PhoneNumberMatcher(response.text, None):
                phone_ = phonenumbers.format_number(m.number, phonenumbers.PhoneNumberFormat.E164)
                if phone_ not in known_phones:
                    known_phones.append(phone_)
                    has_phone = True
                    j = {'logo': r"https://{}{}".format(response.url, logo_link), 'phones': phone_, 'website': response.url}
                    f.write(json.dumps(j))
                    print(j)

            if not has_phone:
                j = {'logo': r"https://{}{}".format(response.url, logo_link), 'phones': '', 'website': response.url}
                print(j)

            f.close()
        self.log('Saved file %s' % filename)
