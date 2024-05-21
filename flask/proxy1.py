#proxy1.py

import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

class SourceScraper:
    def __init__(self, start_urls):
        self.start_urls = start_urls
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.driver = self.get_webdriver()

    def get_webdriver(self):
        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={UserAgent().random}")
        return webdriver.Chrome(options=chrome_options)

    def scrape_page(self, url):
        self.driver.get(url)
        html_code = self.driver.page_source
        return html_code

    def scrape(self):
        result_data = []

        for url in self.start_urls:
            print(f"Scraping {url}")
            html_content = self.scrape_page(url)
            result_data.append({
                'url': url,
                'html_content': html_content,
                # Add more fields as needed
            })

        self.driver.quit()
        return result_data

    def save_to_json(self, data, filename='output.json'):
        if filename != 'output.json':
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=2)

