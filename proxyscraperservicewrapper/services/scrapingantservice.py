import json
from typing import Optional

import requests

from proxyscraperservicewrapper.services.abstractservice import AbstractService


class ScrapingAntService(AbstractService):
    __api_base_url = "https://api.scrapingant.com/v2"
    __query_template = "{}/general?url={}&browser={}"
    __credit_usage_template = "{}/usage?x-api-key={}"

    @classmethod
    def fetch_html(cls, token: str, url: str, js_rendering: Optional[bool] = False) -> str:
        try:
            headers = {
                'x-api-key': token
            }

            if js_rendering is True:
                query = cls.__query_template.format(cls.__api_base_url, url, "true")
            else:
                query = cls.__query_template.format(cls.__api_base_url, url, "false")

            page = requests.get(query, headers=headers)
            html = page.content.decode("utf-8")
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

            return content_dict["remained_credits"]

        except Exception as e:
            raise e