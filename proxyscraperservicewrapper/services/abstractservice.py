from abc import ABC, abstractmethod

class AbstractService(ABC):
    @classmethod
    @abstractmethod
    def fetch_html(cls, token: str, url: str, js_rendering: bool) -> dict:
        pass

    @classmethod
    @abstractmethod
    def fetch_credit_usage_info(cls, token: str) -> dict:
        pass
