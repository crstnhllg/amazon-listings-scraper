from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument('--headless')

WEBSITE = 'https://www.amazon.com/'
RESULT_XPATH = '//div[@data-component-type="s-search-result"]'

class AmazonScraper:
    """
    AmazonScraper scrapes product listings from Amazon based on a search query.

    Attributes:
        product_name (str): The search keyword for the product.
        pages (int): Number of result pages to scrape.
        scraped_data (list): List of dictionaries containing product info.

    Methods:
        start(): Begins the scraping workflow.
        search_product(): Searches for the specified product.
        scrape_results(): Scrapes product descriptions, prices, and ratings.
        next_page(): Navigates to the next search results page.
    """
    def __init__(self, product, pages):
        """
        Initializes the scraper with product name, number of pages to scrape,
        and sets up the Chrome WebDriver.
        """
        self.product_name = product
        self.pages = pages
        self.scraped_data = []

        self.driver = webdriver.Chrome(options=CHROME_OPTIONS)
        self.wait = WebDriverWait(self.driver, 10)

    def start(self):
        """
        Launches the Amazon site, handles initial modal, and starts scraping.
        Ensures driver quits after scraping.
        """
        try:
            self.driver.get(WEBSITE)
            try:
                self.driver.find_element(By.XPATH, './/button[@type="submit"]').click()
            except:
                pass
            logging.info(f'Initiating scrape for {self.product_name}')
            self.search_product()
            self.scrape_results()
        finally:
            logging.info('Scraping Data Completed.')
            self.driver.quit()

    def search_product(self):
        """
        Searches for the specified product using Amazon's search bar.
        Exits if the search elements cannot be found.
        """
        try:
            search_box = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, './/input[@id="twotabsearchtextbox"]')
            ))
            search_button = self.driver.find_element(By.XPATH, './/input[@id="nav-search-submit-button"]')
            search_box.send_keys(self.product_name)
            search_button.click()
        except (NoSuchElementException, TimeoutException) as e:
            logging.error('Search Failed. Please rerun the scraper.')
            self.driver.quit()
            raise SystemExit()

    def scrape_results(self):
        """
        Iterates over search result pages and scrapes product details.
        Skips sponsored results and handles missing fields.
        """
        for i in range(self.pages):
            self.wait.until(EC.presence_of_element_located(
                (By.XPATH, RESULT_XPATH)
            ))
            results = self.driver.find_elements(By.XPATH, RESULT_XPATH)
            for result in results:
                if 'Sponsored' in result.text:
                    continue

                try:
                    description = result.find_element(By.XPATH, './/h2[@aria-label]').get_attribute('aria-label')

                    whole_price = result.find_element(By.XPATH, './/span[@class="a-price-whole"]').text.strip()
                    fraction_price = result.find_element(By.XPATH, './/span[@class="a-price-fraction"]').text.strip()
                    price = float(f'{whole_price.replace(",", "")}.{fraction_price}')

                    link = result.find_element(By.XPATH, './/a[contains(@class, "a-link-normal") and contains(@href, "/dp/")]').get_attribute('href')

                    try:
                        rating = result.find_element(By.XPATH, './/a[contains(@aria-label, '
                                                               '"ratings")]/span').text.strip()
                        rating = int(rating.replace(',', ''))
                    except (NoSuchElementException, TimeoutException):
                        rating = 0

                    product_data = {
                        'Product Description': description,
                        'Price': price,
                        'Ratings': rating,
                        'Product Link': link,
                    }
                    self.scraped_data.append(product_data)
                except (NoSuchElementException, TimeoutException, ValueError) as e:
                    logging.warning(f'Skipping result due to: {e}')
                    continue
            try:
                self.next_page()
            except Exception as e:
                logging.error(f'Failed to fetch next page: {e}')
                self.driver.quit()
                raise SystemExit('Exiting scraper')

    def next_page(self):
        """
        Navigates to the next page of Amazon search results.
        """
        next_page = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//a[contains(@class, "s-pagination-next")]')
        ))
        self.driver.execute_script("arguments[0].scrollIntoView"
                                   "({behavior: 'smooth', block: 'center'});", next_page)
        next_page.click()