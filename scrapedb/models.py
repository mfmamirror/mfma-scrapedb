from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB


Base = declarative_base()


class Scrape(Base):
    __tablename__ = 'scrape'

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)

    def __repr__(self):
       return f"<Scraper(start_date=${self.start_date})>"


class ScrapeExtractedPage(Base):
    __tablename__ = 'scrape_extracted_page'

    id = Column(Integer, primary_key=True)
    scrape_id = Column(Integer, ForeignKey('scrape.id'))
    scrape = relationship("Scrape")
    original_url = Column(String)
    extracted_data = Column(JSONB)

    def __repr__(self):
       return f"<ScrapeExtractedPage(scrape=${self.scrape} original_url=${self.original_url})>"


class ScrapeExtractedMenu(Base):
    __tablename__ = 'scrape_extracted_menu'

    id = Column(Integer, primary_key=True)
    scrape_id = Column(Integer, ForeignKey('scrape.id'))
    scrape = relationship("Scrape")
    extracted_data = Column(JSONB)

    def __repr__(self):
       return f"<ScrapeExtractedMenu(scrape=${self.scrape} original_url=${self.original_url})>"


class Page(Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    scrape_id = Column(Integer, ForeignKey('scrape.id'))
    scrape = relationship("Scrape")
    original_url = Column(String)
    headers = Column(JSONB)
    body = Column(String)

    def __repr__(self):
       return f"<Page(scrape=${self.scrape} original_url=${self.original_url})>"


class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    scrape_id = Column(Integer, ForeignKey('scrape.id'))
    scrape = relationship("Scrape")
    original_url = Column(String)
    scrape_data = Column(JSONB)

    def __repr__(self):
       return f"<File(scrape=${self.scrape} original_url=${self.original_url})>"
