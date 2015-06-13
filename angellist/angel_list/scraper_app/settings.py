BOT_NAME = 'Angel'

SPIDER_MODULES = ['scraper_app.spiders']

DATABASE = {
  'drivername': 'postgres',
  'host': 'localhost',
  'port': '5432',
  'username': 'Jslice',
  'password': '',
  'database': 'angel'
}

ITEM_PIPELINES = ['scraper_app.pipelines.AngelCompaniesPipeline']