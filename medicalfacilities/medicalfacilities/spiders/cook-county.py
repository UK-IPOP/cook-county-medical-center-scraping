import scrapy
import json

with open("data/county-urls.json", "r") as f:
    urls = json.load(f)


class CookCounty(scrapy.Spider):
    name = "cookcounty"

    start_urls = [u["url"] for u in urls]

    def parse(self, response):
        name = response.css(".col-md-3 h2::text").get()
        address = " ".join(
            (x.strip() for x in response.css(".col-md-3 h6::text")[:2].getall())
        )
        yield {
            "name": name,
            "address": address,
        }
