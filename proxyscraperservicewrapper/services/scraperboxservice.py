from typing import Optional

import requests

from proxyscraperservicewrapper.services.abstractservice import AbstractService


class ScraperBoxService(AbstractService):
    __api_base_url = "https://api.scraperbox.com/scrape"
    __query_template = "{}?token={}&url={}&javascript_enabled={}"
    __credit_usage_template = "{}?token={}&url=0"

    @classmethod
    def fetch_html(cls, token: str, url: str, js_rendering: Optional[bool] = False) -> str:
        try:
            if js_rendering is True:
                query = cls.__query_template.format(cls.__api_base_url, token, url, "true")
            else:
                query = cls.__query_template.format(cls.__api_base_url, token, url, "false")

            page = requests.get(query)
            html = page.text
            return html

        except Exception as e:
            raise e

    @classmethod
    def fetch_credit_usage_info(cls, token: str):
        try:
            url = cls.__credit_usage_template.format(cls.__api_base_url, token)
            res = requests.get(url)
            headers = res.headers

            return headers['X-Credits-Remaining']

        except Exception as e:
            raise e
