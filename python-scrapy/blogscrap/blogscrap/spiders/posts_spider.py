# import scrapy package
import scrapy


# later define a class that inherits from Spider class
class PostsSpider(scrapy.Spider):
    # define a name for spider
    name = "first_scrap"
    # urls to scrap from
    start_urls = ["https://blog.scrapinghub.com/page/1/",
                  "https://blog.scrapinghub.com/page/2/", ]

    # use parse() to process the response object we get
    # and return the scraped data
    def parse(self, response):
        # get page of each url in the start_urls list,
        page_no = response.url.split("/")[-1]
        # a filename for both pages
        filename = f"page-{page_no}.html"
        # write scraped data to these files
        with open(filename, mode="wb") as f:
            # write the body of the page to files
            f.write(response.body)

