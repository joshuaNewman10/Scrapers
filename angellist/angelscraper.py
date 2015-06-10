import scraper
reload(scraper)
from scraper import AngelScraper
import ipdb as ipdb # Debugging tools

scraperBot = AngelScraper();

results = scraperBot.findStartups(followMin = 2)

ipdb.set_trace()