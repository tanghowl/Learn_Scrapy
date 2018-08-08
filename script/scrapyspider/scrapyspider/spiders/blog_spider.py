from scrapy.spiders import Spider
from scrapyspider.items import DoubanBookItem
import scrapy


class BlogSpider(Spider):
    name = 'woodenrobot'
    start_urls = ['http://woodenrobot.me']

    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title.strip())


class DoubanBookTop250Spider(Spider):
    name = 'douban_books_top250'
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        item = DoubanBookItem()
        books = response.xpath('//ol[@class="grid_view"]/li')
        for book in books:
            item['rangking'] = book.xpath()


class QuotesSpider(Spider):
    name = 'quotes'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quptes-{}.html'.format(page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))
