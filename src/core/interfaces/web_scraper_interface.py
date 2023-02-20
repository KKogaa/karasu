from abc import ABC, abstractmethod

def WebScraperInterface(ABC):
    @abstractmethod
    def scrape(self, url: str) -> dict :
        raise NotImplementedError
