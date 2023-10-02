import os
import unittest
from dotenv import load_dotenv
from proxyscraperservicewrapper.proxyscraperwrapper import ProxyScraperWrapper

load_dotenv()

class TestProxyScraperServiceWrapper(unittest.TestCase):

    SCRAPE_URL = "https://docs.scrapingant.com/api-credits-usage"
    JS_RENDERING = False
    TOKEN_SCRAPINGANT = os.getenv("TEST_TOKEN_SCRAPINGANT")
    TOKEN_WEBSCRAPINGAI = os.getenv("TEST_TOKEN_WEBSCRAPINGAI")
    TOKEN_ZENSCRAPE = os.getenv("TEST_TOKEN_ZENSCRAPE")
    TOKEN_ZENROWS = os.getenv("TEST_TOKEN_ZENROWS")

    def test_scrapingant(self):
        res = ProxyScraperWrapper.fetch_html_scrapingant(
            token=self.TOKEN_SCRAPINGANT,
            scrape_url=self.SCRAPE_URL,
            js_rendering=self.JS_RENDERING
        )
        print(res)
        self.assertTrue(isinstance(res, str))

    def test_scrapingant_credits(self):
        remaining_credits = ProxyScraperWrapper.fetch_remaining_credits_scrapingant(token=self.TOKEN_SCRAPINGANT)
        print("Credits: {}".format(remaining_credits))
        self.assertTrue(isinstance(remaining_credits, int))


    def test_webscrapingai(self):
        res = ProxyScraperWrapper.fetch_html_webscrapingai(
            token=self.TOKEN_WEBSCRAPINGAI,
            scrape_url=self.SCRAPE_URL,
            js_rendering=self.JS_RENDERING
        )
        print(res)
        self.assertTrue(isinstance(res, str))

    def test_webscrapingai_credits(self):
        remaining_credits = ProxyScraperWrapper.fetch_remaining_credits_webscrapingai(token=self.TOKEN_WEBSCRAPINGAI)
        print("Credits: {}".format(remaining_credits))
        self.assertTrue(isinstance(remaining_credits, int))


    def test_zenscrape(self):
        res = ProxyScraperWrapper.fetch_html_zenscrape(
            token=self.TOKEN_ZENSCRAPE,
            scrape_url=self.SCRAPE_URL,
            js_rendering=self.JS_RENDERING
        )
        print(res)
        self.assertTrue(isinstance(res, str))

    def test_zenscrape_credits(self):
        remaining_credits = ProxyScraperWrapper.fetch_remaining_credits_zenscrape(token=self.TOKEN_ZENSCRAPE)
        print("Credits: {}".format(remaining_credits))
        self.assertTrue(isinstance(remaining_credits, int))


    def test_zenrows(self):
        res = ProxyScraperWrapper.fetch_html_zenrows(
            token=self.TOKEN_ZENROWS,
            scrape_url=self.SCRAPE_URL,
            js_rendering=self.JS_RENDERING
        )
        print(res)
        self.assertTrue(isinstance(res, str))

    def test_zenrows_credits(self):
        remaining_credits = ProxyScraperWrapper.fetch_remaining_credits_zenrows(token=self.TOKEN_ZENROWS)
        print("Credits: {}".format(remaining_credits))
        self.assertTrue(isinstance(remaining_credits, int))

if __name__ == '__main__':
    unittest.main()