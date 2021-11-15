import scrapy


class UniversitySpider(scrapy.Spider):
    name = "university"

    start_urls = [
        "https://www.uchicagomedicine.org/find-a-location?page=6&sortby=default",
    ]

    def parse(self, response):
        block_content = response.css(".locations-content")
        for block in block_content:
            name = block.css("h3 a::text").get()
            address = " ".join(block.css("p::text").getall()[:2])
            data = {"name": name, "address": address}
            yield data
