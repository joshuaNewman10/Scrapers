from sqlalchemy.orm import sessionmaker
from models import Companies, db_connect, create_companies_table

class AngelCompaniesPipeline(object):
  """AngelPipeline for storing scraped items in the db"""
  def __init__(self):
    """
    Initializes db connection and sessionmaker
    Creates deals table
    """
    engine = db_connect()
    create_companies_table(engine)
    self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
      """
      Save companies in database
      -Method called for every item pipeline component
      """

      session = self.Session()
      company = Companies(**item)

      try:
        session.add(item)
        session.commit()
      except:
        session.rollback()
        raise
      finally:
        session.close()
      return item