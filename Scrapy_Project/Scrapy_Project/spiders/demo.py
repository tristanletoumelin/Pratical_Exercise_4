import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    # allowed_domains = ["Scrapy_Project.io"]
    def start_requests(self):
        urls = ['https://ti.rtu.lv']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
            sef.log(f"Saved file {fname}.")
