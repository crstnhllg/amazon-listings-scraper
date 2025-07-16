# 🛒 Amazon Product Scraper

A lightweight Python tool that scrapes product listings from Amazon based on a search keyword. It extracts product titles, prices, ratings, and direct product link, and saves them into a CSV file.

> ⚠️ For educational purposes only. Web scraping Amazon may violate their Terms of Service.

---

## ✨ Features

-  Scrapes product listings based on a search keyword.
-  Extracts product description, price, number of ratings, and direct product link.
-  Supports scraping multiple pages.
-  Saves results to a clean, structured `.csv` file.
-  Handles missing data (e.g. unrated products).
-  Headless browser support for background scraping.
-  Logging for transparency and easier debugging.

---

## 📦 How to Use

1. **Clone the Repository**

   ```bash
   git clone https://github.com/crstnhllg/amazon-scraper.git
   cd amazon-scraper
````

2. **Install Dependencies**

   It's recommended to use a virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**

   ```bash
   python main.py
   ```

4. **Enter the Product Info**

   * Product name (e.g., `wireless mouse`)
   * Number of pages to scrape (e.g., `2`)

5. **Check the Output**

   A file named like `wirelessmouse_amazon.csv` will be created in your directory containing the scraped data.

---

## 🧾 Output Format

The resulting CSV file includes:

| Product Description | Price | Ratings | Product Link                                                           |
| ------------------- | ----- | ------- | ---------------------------------------------------------------------- |
| Example Title       | 25.99 | 1400    | [https://www.amazon.com/dp/example](https://www.amazon.com/dp/example) |

---

## 🧰 Requirements

* Python 3.7+
* Google Chrome browser
* [ChromeDriver](https://chromedriver.chromium.org/downloads) installed and available in your system PATH

---

## 📁 Project Structure

```
amazon-listings-scraper/
├── amazon_scraper.py           # Main scraper logic
├── main.py                     # Script entry point
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── laptop.csv                  # Sample/demonstration output

```

---

## ⚠️ Disclaimer

This scraper is intended for **educational purposes only**. Please use it responsibly. Web scraping Amazon may violate their [Terms of Service](https://www.amazon.com/gp/help/customer/display.html?nodeId=508088).

---

## 📬 License

This project is open-source and available under the [MIT License](LICENSE).

```

---

Let me know if you'd like a version with screenshots or if you want to include a demo CSV preview.
```
