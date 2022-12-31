## Wrapper for Scraper Proxy Service (Private)
<hr>

### Setup
```
pip install git+https://github.com/AlexQ0807/proxyscraperservicewrapper.git
```


### Example

```
from proxyscraperservicewrapper.proxyscraperwrapper import ProxyScraperWrapper

scrape_url = "google.com"
scraperbox_token = "XXXXXXXXX"

# Fetch remaining credits
remaining_credits = ProxyScraperWrapper.fetch_remaining_credits_scraperbox(token=scraperbox_token)

# Fetch scraped html content
ProxyScraperWrapper.fetch_html_scraperbox(token=scraperbox_token, url=scrape_url, js_rendering=True)
```