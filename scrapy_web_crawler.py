import scrapy
from scrapy.crawler import CrawlerProcess


class ZuwendungsdatenbankSpider(scrapy.Spider):
    name = 'zuwendungsdatenbank'
    custom_settings = {
        'DOWNLOAD_DELAY': 3,
    }
    start_urls = ['https://www.berlin.de/sen/finanzen/service/zuwendungsdatenbank/?q=&name=&geber=--+Alles+--&art=--+Alles+--&jahr=--+Alles+--&anschrift=&politikbereich=--+Alles+--&zweck=#searchresults']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0])

    def parse(self, response):
        table_rows = response.css("table.result.table tbody tr")
        for table_row in table_rows:
            if table_row.css(".line_1"):
                result_dictionary = {}

                result_dictionary["Name"] = table_row.xpath("string(.//td[@headers='Name'])").get()
                result_dictionary["Geber"] = table_row.xpath("string(.//td[@headers='Geber'])").get()
                result_dictionary["Art"] = table_row.xpath("string(.//td[@headers='Art'])").get()
                result_dictionary["Jahr"] = table_row.xpath("string(.//td[@headers='Jahr'])").get()

            else:
                result_dictionary["Anschrift"] = table_row.xpath("string(.//td[@headers='Anschrift'])").get()
                result_dictionary["Politikbereich"] = table_row.xpath("string(.//td[@headers='Politikbereich'])").get()
                result_dictionary["Zweck"] = table_row.xpath("string(.//td[@headers='Zweck'])").get()
                result_dictionary["Betrag"] = table_row.xpath("string(.//td[@headers='Betrag'])").get()

                yield result_dictionary

        next_page = response.css("li.pager-item-next>a::attr(href)").get()
        # self.log(next_page)
        if next_page:
            yield response.follow(next_page,callback=self.parse)

    
process = CrawlerProcess(
    settings = {
        'FEED_URI' : 'data/raw_data.csv',
        'FEED_FORMAT' : 'csv'
    }
)

process.crawl(ZuwendungsdatenbankSpider)
process.start()