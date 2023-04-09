import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    # Scrapy will scrape the content, and it will pass this in second parameter
    # named response which is basically a parsed Python dictionary of data
    # We have to capture the title written on the span tag something like this:
    # <span class="title">A Standard for the Transmission of IP Datagrams on Avian Carriers</span>
    # There are 2 ways to capture this title string with scrapy using
    # 1.XPath
    # 2.Using CSS
    def parse(self, response):
        # Using CSS ::text is pseudo selector and get function will
        # get the first tag retrieved that matches the CSS.
        # If we wanted to get list of tags then we have to use getAll()
        # title = response.css('span.title::text').get()
        # Using same with XPath approach,
        title = response.xpath('//span[@class="title"]/text()').get()
        return {"title": title}
