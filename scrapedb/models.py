from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB


Base = declarative_base()


class Scrape(Base):
    __tablename__ = 'scrape'

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)

    def __repr__(self):
       return f"<Scraper(start_date=${self.start_date})>"


class ExtractedPage(Base):
    __tablename__ = 'extracted_page'

    id = Column(Integer, primary_key=True)
    scrape_id = Column(Integer, ForeignKey('scrape.id'))
    scrape = relationship("Scrape")

    def __repr__(self):
       return f"<Scraper(start_date=${self.start_date})>"
