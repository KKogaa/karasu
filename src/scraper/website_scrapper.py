from bs4 import BeautifulSoup
import requests
import pandas as pd
from .website import Website


class WebsiteScraper:
    def __init__(self, website: Website):
        self.website = website

    def get_all_manhwas(self, url: str):
        URL = "https://www.webtoons.com/en/"
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, "html.parser")
        print(soup)

    def get_all_manhwa(self, url: str):
        URL = "https://www.webtoons.com/en/"
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, "html.parser")
        print(soup)
