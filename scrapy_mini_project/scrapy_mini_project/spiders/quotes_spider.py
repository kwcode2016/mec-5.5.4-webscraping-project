import scrapy


class QuotesSpider(scrapy.Spider):
        name = "quotes"

        start_urls = [
            'http://quotes.toscrape.com/page/1/',
        ]

        def parse(self, response):
            for quote in response.css('div.quote'):
                yield{
                    'text': quote.css('span.text::text').get(),
                    'author': quote.css('small.author::text').get(),
                    'tags': quote.css('div.tags a.tag::text').getall(),
                }



            # fetch next page
            next_page = response.css('li.next a::attr(href)').get()


            # if next page exists, goto the next page and parse it
            # using response.follow instead of scrapy.Request uses relative url.
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

