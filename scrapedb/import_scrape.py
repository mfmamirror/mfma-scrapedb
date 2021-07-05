from sqlalchemy import create_engine
import json
import os
from sqlalchemy.orm import sessionmaker
from models import Scrape, ScrapeExtractedMenu, ScrapeExtractedPage, File
import sys


def main():
    jsonlines_path = sys.argv[1]
    start_date = sys.argv[2]

    engine = create_engine(os.environ.get("DATABASE_URL"), echo=True, future=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    scrape = session.query(Scrape).filter_by(start_date=start_date).first()
    if scrape is None:
        scrape = Scrape(start_date=start_date)
        session.add(scrape)

    with open(jsonlines_path, 'r') as jsonlines_file:
        for line in jsonlines_file.readlines():
            item = json.loads(line)
            if item["type"] == "page":
                scrape_extracted_page = ScrapeExtractedPage(
                    scrape=scrape,
                    original_url=item["original_url"],
                    extracted_data=item
                )
                session.add(scrape_extracted_page)
            elif item["type"] == "file":
                file_ = File(
                    scrape=scrape,
                    original_url=item["original_url"],
                    scrape_data=item
                )
                session.add(file_)
            elif item["type"] == "menu":
                scrape_extracted_menu = ScrapeExtractedMenu(
                    scrape=scrape,
                    extracted_data=item
                )
                session.add(scrape_extracted_menu)
            else:
                print(f"Unexpected type ${item['type']}")
    session.commit()



if __name__ == "__main__":
    main()
