import json
from typing import Optional

import requests

from proxyscraperservicewrapper.services.abstractservice import AbstractService


class ZenRowsService(AbstractService):
    __api_base_url = "https://api.zenrows.com/v1"
    __query_template = "{}/?apikey={}&url={}&js_render={}"
    __credit_usage_template = "{}/usage?apikey={}"

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

            return content_dict["api_credit_limit"] - content_dict["api_credit_usage"]

        except Exception as e:
            raise e