from scrapy.spider import BaseSpider

from scrapy.selector import HtmlXPathSelector

from scrapy.contrib.loader import XPathItemLoader

from scrapy.contrib.loader.processor import MapCompose

from scrapy.contrib.loader.processor import Join

from scraper_app.items import AngelJobs

class AngelSpider(BaseSpider):
  """Spider for regularly updated Angellist data startups"""

  name='Angel'
  allowed_domains = ['angel.co']
  start_urls = ['https://angel.co/']

  companies_list_xpath = '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div'
  item_fields = {
    'test': '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/ul/li[1]/a',
  }

  def parse(self, response):
    """
    Default CB used by Scrapy to process download responses

    Testing Contracts:
    @url 'https://angel.co/companies?teches[]=Big+Data'
    @returns items 1
    @scrapes title link
    """

    #get response after making request to some site (data passed to our cb)
    selector = HtmlXPathSelector(response)

    for company in selector.select(self.companies_list_xpath):
      loader = XPathItemLoader(AngelJobs(), selector=company)

      loader.default_input_processor = MapCompose(unicode.strip)
      loader.deffault_input_processor = Join()

      for field, xpath in self.item_fields.iteritems():
        loader.add_xpath(field, xpath)

      yield loader.load_items()
