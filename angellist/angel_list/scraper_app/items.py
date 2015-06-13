from scrapy.item import Item, Field

class AngelJobs(Item):
  """Angellist container (dict like obj) for scraped data"""
  angelLink = Field()
  blurb = Field()
  website = Field()
