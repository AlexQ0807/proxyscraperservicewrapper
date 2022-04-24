import json
import requests
import cryptocode
from requests.auth import HTTPBasicAuth
from compressortoolbox.compressor import Compressor


class ProxyScraperWrapper:
    def __init__(self, scraper_proxy_service_url: str, basic_auth_username: str, basic_auth_password: str,
                 crypto_password: str, scraperbox_token: str = None, scrapingant_token: str = None):
        """
        :param scraper_proxy_service_url:
        :param basic_auth_username:
        :param basic_auth_password:
        :param crypto_password:
        :param scraperbox_token:
        :param scrapingant_token:
        """
        self.scraper_proxy_service_url = scraper_proxy_service_url
        self.auth = HTTPBasicAuth(basic_auth_username, basic_auth_password)
        self.crypto_password = crypto_password
        self.scraperbox_token = scraperbox_token
        self.scrapingant_token = scrapingant_token

    def __fetch_html(self, scrape_url, api_name, api_token):
        proxy_url = "{}/{}".format(self.scraper_proxy_service_url, api_name)
        encrypted_token = cryptocode.encrypt(api_token, self.crypto_password)

        payload = {
            "token": encrypted_token,
            "url": scrape_url,
            "compress": True
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        try:
            req = requests.request("POST", proxy_url, json=payload, auth=self.auth, headers=headers)

            if req.status_code == 200:
                content = json.loads(req.content)
                if 'compressed' in content:
                    content = Compressor.decompress_dict(content['compressed'])

                return content['html']
            else:
                raise Exception(req.text)
        except Exception as e:
            raise e

    def fetch_html_scraperbox(self, scrape_url):
        try:
            return self.__fetch_html(scrape_url=scrape_url, api_name="scraperbox", api_token=self.scraperbox_token)
        except Exception as e:
            raise e

    def fetch_html_scrapingant(self, scrape_url):
        try:
            return self.__fetch_html(scrape_url=scrape_url, api_name="scrappingant", api_token=self.scrapingant_token)
        except Exception as e:
            raise e

    def __fetch_remaining_credits(self, api_name, api_token):
        proxy_url = "{}/{}".format(self.scraper_proxy_service_url, api_name)
        encrypted_token = cryptocode.encrypt(api_token, self.crypto_password)

        payload = {
            "token": encrypted_token,
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        try:
            req = requests.request("POST", proxy_url, json=payload, auth=self.auth, headers=headers)
            content = json.loads(req.content)
            if req.status_code == 200:
                return int(content["remaining_credits"])
            else:
                raise Exception(req.text)
        except Exception as e:
            raise e

    def fetch_remaining_credits_scraperbox(self):
        try:
            return self.__fetch_remaining_credits("scraperbox/usage", self.scraperbox_token)
        except Exception as e:
            raise e

    def fetch_remaining_credits_scrapingant(self):
        try:
            return self.__fetch_remaining_credits("scrappingant/usage", self.scrapingant_token)
        except Exception as e:
            raise e
