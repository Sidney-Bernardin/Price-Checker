from dataclasses import dataclass

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selectolax.parser import HTMLParser, Node


options: Options = Options()
options.add_argument("--headless=new")

driver: Chrome = Chrome(
    options=options,
    service=Service(executable_path="./chromedriver"),
)


class Product:
    url: str = ""
    dream_price: float = 0
    is_scraping: bool = False

    title: str = ""
    current_price: float = -1

    def __init__(self, url: str, dream_price: float) -> None:
        self.url = url
        self.dream_price = dream_price

    def scrape(self) -> None:
        self.is_scraping = True

        driver.get(self.url)
        self.parser: HTMLParser = HTMLParser(driver.page_source)

        self.title = self.parser.css_first("#productTitle").text(strip=True)

        whole = self.parser.css_first(".a-price-whole")
        fraction = self.parser.css_first(".a-price-fraction")
        self.current_price = float(
            f"{whole.text(strip=True)}{fraction.text(strip=True)}"
        )

        self.is_scraping = False

    def is_affordable(self) -> bool:
        return self.current_price != -1 and self.current_price <= self.dream_price
