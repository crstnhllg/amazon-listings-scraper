import pandas as pd
from amazon_scraper import AmazonScraper
import logging
import re

logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG to see more
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

def main():
    product = input('Please enter the product name: ')

    while not product.strip():
        product = input('Product name cannot be empty. Please enter the product name: ')

    try:
        pages = int(input('Please enter the number of pages to scrape: '))
    except ValueError:
        pages = 1

    scraper = AmazonScraper(product, pages)

    try:
        scraper.start()
    finally:
        if scraper.scraped_data:
            logging.info(f'Successfully scraped {len(scraper.scraped_data)} products.')
            filename = f'{re.sub(r'[^a-zA-Z0-9]', '', product).lower()}.csv'
            pd.DataFrame(scraper.scraped_data).to_csv(filename, index=False)
            logging.info('Successfully Saved Scraped Data.')
        else:
            logging.info('No data was scraped.')

if __name__ == '__main__':
    main()