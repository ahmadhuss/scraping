# Scraping

This repository contains various Python scripts to check web scraping techniques for certain sites.

**How we can use on our local machine?**

Make sure your OS has already installed `Python 3.x.x` , that comes with `pip`, `pip` is a package manager for Python and is included by default with the Python installer. It helps to install and uninstall Python packages (such as Django!).

**Setting up a virtual environment:**

After cloning this repo, enter the following command on your terminal:

    python -m venv venv

It will create the virtual environment for the following project, where we will install all our project dependencies. There is a `venv` directory automatically created in your project that Git will not track.

After that we have to activate the virtual environment and install the project dependencies there.

**For Windows:**

Enter the following command at the root of your cloned repo.

    venv\Scripts\activate

**For Unix:**

Enter the following command at the root of your cloned repo.

    . venv\bin\activate

**Install dependencies:**

    pip install -r requirements.txt

**Scrapy commands:**

**Scrapy start a new project in your virtual environment:**

    scrapy startproject ietf_scraper

Scrapy will create a template directory with all its stub files.

`cd ietf_scraper`

`ietf_scraper/scrapy.cfg` holds the configuration information.

`ietf_scraper/ietf_scraper/items.py` defines the objects or the entities that we are scraping.

`ietf_scraper/ietf_scraper/middlewares.py` contains various Scrapy hooks.

`ietf_scraper/ietf_scraper/pipelines.py` defined functions that create and filter items.

`ietf_scraper/ietf_scraper/settings.py` contains project settings.

`ietf_scraper/ietf_scraper/spiders/` scrapy project is basically collection of spiders. We have to tell scrapy each new spider we want to make with the new command.

**Create a new scrapy spider for the website pythonscraping.com:**

Go to the following directory in your virtual environment:

`cd ietf_scraper/ietf_scraper/spiders`

## Example 1:

We will create a new spider.

**Run the command:**

    scrapy genspider ietf pythonscraping.com

This command will create a file named `ietf.py` and that file will contain class definition:  
  
```py
import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        pass

```
  
  
**Modified:**  
  
```py
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
```
  
**Run the spider:**  
  
    scrapy runspider ietf.py

We will see a lot of output in the Terminal, please search and find following text in your Terminal:

```py
{'title': 'A Standard for the Transmission of IP Datagrams on Avian Carriers'}
```

It means the spider has run successfully.