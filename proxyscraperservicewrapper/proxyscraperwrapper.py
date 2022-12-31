from typing import Optional
from proxyscraperservicewrapper.services.scraperboxservice import ScraperBoxService
from proxyscraperservicewrapper.services.scrapingantservice import ScrapingAntService
from proxyscraperservicewrapper.services.webscrapingaiservice import WebScrapingAIService
from proxyscraperservicewrapper.services.zenscrapeservice import ZenScrapeService


class ProxyScraperWrapper:
    @classmethod
    def fetch_html_scraperbox(cls, token: str, scrape_url: str, js_rendering: Optional[bool] = False):
        try:
            return ScraperBoxService.fetch_html(url=scrape_url,
                                                token=token,
                                                js_rendering=js_rendering)
        except Exception as e:
            raise e

    @classmethod
    def fetch_remaining_credits_scraperbox(cls, token: str):
        try:
            return ScraperBoxService.fetch_credit_usage_info(token)
        except Exception as e:
            raise e

    @classmethod
    def fetch_html_scrapingant(cls, token: str, scrape_url: str, js_rendering: Optional[bool] = False):
        try:
            return ScrapingAntService.fetch_html(url=scrape_url,
                                                 token=token,
                                                 js_rendering=js_rendering)
        except Exception as e:
            raise e

    @classmethod
    def fetch_remaining_credits_scrapingant(cls, token: str):
        try:
            return ScrapingAntService.fetch_credit_usage_info(token)
        except Exception as e:
            raise e

    @classmethod
    def fetch_html_webscrapingai(cls, token: str, scrape_url: str, js_rendering: Optional[bool] = False):
        try:
            return WebScrapingAIService.fetch_html(url=scrape_url,
                                                   token=token,
                                                   js_rendering=js_rendering)
        except Exception as e:
            raise e

    @classmethod
    def fetch_remaining_credits_webscrapingai(cls, token: str):
        try:
            return WebScrapingAIService.fetch_credit_usage_info(token)
        except Exception as e:
            raise e

    @classmethod
    def fetch_html_zenscrape(cls, token: str, scrape_url: str, js_rendering: Optional[bool] = False):
        try:
            return ZenScrapeService.fetch_html(url=scrape_url,
                                               token=token,
                                               js_rendering=js_rendering)
        except Exception as e:
            raise e

    @classmethod
    def fetch_remaining_credits_zenscrape(cls, token: str):
        try:
            return ZenScrapeService.fetch_credit_usage_info(token)
        except Exception as e:
            raise e
