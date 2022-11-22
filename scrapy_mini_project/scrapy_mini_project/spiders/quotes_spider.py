import scrapy


class QuotesSpider(scrapy.Spider):
        name = "quotes"

        def start_requests(self):
            urls = [
                'http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/',
                'http://quotes.toscrape.com/page/3/',
                'http://quotes.toscrape.com/page/4/',
                'http://quotes.toscrape.com/page/5/',
            ]
            for url in urls:
                print(url)
                yield scrapy.Request(url=url, callback=self.parse)

        """
        def parse(self, response):
            page = response.url.split("/")[-2]
            filename = 'quotes-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
        """
        



class SomethingSpider(scrapy.Spider):
        name = "something"

        def start_requests(self):
            urls = [
                'http://quotes.toscrape.com/page/6/',
                'http://quotes.toscrape.com/page/7/',
            ]
            for url in urls:
                print(url)
                yield scrapy.Request(url=url, callback=self.parse)

        def parse(self, response):
            page = response.url.split("/")[-2]
            filename = 'quotes-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)