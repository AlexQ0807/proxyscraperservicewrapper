import json
from typing import Optional

import requests

from proxyscraperservicewrapper.services.abstractservice import AbstractService


class WebScrapingAIService(AbstractService):
    __api_base_url = "https://api.webscraping.ai"
    __query_template = "{}/html?api_key={}&url={}&js={}"
    __credit_usage_template = "{}/account?api_key={}"

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
            content_str = res.content.decode("utf-8")
            content_dict = json.loads(content_str)

            return content_dict['remaining_api_calls']

        except Exception as e:
            raise e
