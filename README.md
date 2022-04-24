## Wrapper for Scraper Proxy Service (Private)
<hr>

### Setup
```
pip install git+https://github.com/AlexQ0807/proxyscraperservicewrapper.git
```


### Example

```
from proxyscraperservicewrapper.proxyscraperwrapper import ProxyScraperWrapper

ps = ProxyScraperWrapper(scraper_proxy_service_url=SCRAPER_PROXY_SERVICE_URL,
                          basic_auth_username=AUTH_USERNAME,
                          basic_auth_password=AUTH_PASSWORD,
                          crypto_password=CRYPTO_PASSWORD,
                          scraperbox_token=SCRAPEBOX_TOKEN,
                          scrapingant_token=SCRAPINGANT_TOKEN)

remaining_credits = ps.fetch_remaining_credits_scraperbox()

ps.fetch_html_scraperbox(url)
```