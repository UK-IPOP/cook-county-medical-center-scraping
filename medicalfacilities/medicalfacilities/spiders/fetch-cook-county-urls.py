import scrapy


class CookCountyUrls(scrapy.Spider):
    name = "cookcountyurls"

    start_urls = [
        "https://cookcountyhealth.org/our-locations/",
    ]

    def parse(self, response):
        urls = response.css("a.elementor-post__thumbnail__link")
        for url in urls:
            yield {"url": url.attrib["href"]}
