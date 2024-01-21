from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookItem

class Demo2Spider(CrawlSpider):
    name = "demo2"
    
    start_urls = ['https://www.shanghairanking.com/rankings/arwu/2023']

    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a", follow=True)),
        Rule(LinkExtractor(restrict_css=".product_prod > h3 > a", callback="parse_book")),
    )

    def parse_book(self, response):
        book_item = BookItem()

        book_item["image_url"] = response.urljoin(response.css(".item.active > img::attr(src)").get())
        book_item["title"] = response.css(".col-sm-6.product_main > h1::text").get()
        book_item["price"] = response.css(".price_color::text").get()
        book_item["upc"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
        book_item["url"] = response.url

        yield book_item
