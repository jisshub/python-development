from scrapy import Spider, Request

import json


class PostSpider(Spider):
    name = "posts"
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        # get selector list post items
        post_item = response.css(".post-item")
        # iterate thru each post_item
        for each_post_data in post_item:
            # each_post_date is a selector type , thus we can apply css selector
            # here v will yield the result in a dictionary
            yield {
                # get title of each post
                "title": each_post_data.css('.post-header a::text').get(),
                # get date on each post
                "date": each_post_data.css('.post-header a::text')[1].get(),
                # get author of each post
                "author": each_post_data.css('.post-header a::text')[2].get()
            }
            # get url of next page
        next_page = response.css("a.next-posts-link::attr(href)").get()
        if next_page:
            # if url exists join url with response object
            next_page = response.urljoin(next_page)
            # call Request() which accepts a url and a callback function parse().
            # later, yield the result
            yield Request(next_page, callback=self.parse)
            # thus this url will processed and crawled by parse() again.
