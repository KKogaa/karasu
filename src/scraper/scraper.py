from .website_scrapper import WebsiteScraper
from .website import Website


class Scraper:
    def __init__(self, website: Website = None):
        self.website = website

    def initialize(self):
        """Finds all the available manhwa titles with their corresponding url for the set website

        :return: _description_
        """
        # hmm maybe only run initialization when told to do so

        if self.website == Website.WEBTOON:
            return self._initialize_webtoon()
        return None

    def _initialize_webtoon(self):
        """_summary_

        :return: _description_
        """

        return None

    def show_available(self, page: int, size: int):
        """Lists all the manhwas that are available for scrapping for the set website."""

        # TODO: return paginated list
        return None

    def scrape(self, manhwa_title: str):
        if self.website == Website.ASURASCANS:
            return self._scrape_asura(manhwa_title=manhwa_title)
        elif self.website == Website.WEBTOON:
            return self._scrape_webtoon(manhwa_title=manhwa_title)
        return None

    def _scrape_webtoon(self, manhwa_title: str):
        pass

        # https://www.webtoons.com/en/romance/go-away-romeo/episode-1/viewer?title_no=5066&episode_no=1
        # set cookie session some flags for auth

    def _scrape_asura(self, manhwa_title: str):
        pass
