# # main.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

class SourceScraper:
    def __init__(self, emulate_browser=True):
        self.chrome_options = Options()
        if emulate_browser:
            self.chrome_options.add_argument("--headless")
            self.chrome_options.add_argument(f"user-agent={UserAgent().random}")
        # Initialize the WebDriver
        self.driver = self.get_webdriver()

    def get_webdriver(self):
        return webdriver.Chrome(options=self.chrome_options)

    def scrape_page(self, url):
        self.driver.get(url)
        html_code = self.driver.page_source
        return html_code
