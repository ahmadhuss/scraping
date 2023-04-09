import scrapy
import w3lib.html


class IetfFullSpider(scrapy.Spider):
    name = "ietf_full"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        # We will scrape full page data
        return {
            # <span class="rfc-no">1149</span>
            'number': response.xpath('//span[@class="rfc-no"]/text()').get(),
            # <meta name="DC.Title" content="Standard for the transmission of IP datagrams on avian carriers" />
            'title': response.xpath('//meta[@name="DC.Title"]/@content').get(),
            # 'title': response.xpath('//span[@class="title"]/text()').get(),
            'date': response.xpath('//span[@class="date"]/text()').get(),
            # <meta name="DC.Date.Issued" content="April, 1990" />
            # 'date': response.xpath('//meta[@name="DC.Date.Issued"]/@content').get()
            'description': response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),
            'author': response.xpath('//meta[@name="DC.Creator"]/@content').get(),
            # 'author': response.xpath('//span[@class="author-name"]/text()').get(),
            'company': response.xpath('//span[@class="author-company"]/text()').get(),
            'address': response.xpath('//span[@class="address"]/text()').get(),
            'text': w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get()),
            'headings': response.xpath('//span[@class="subheading"]/text()').getall()
        }
