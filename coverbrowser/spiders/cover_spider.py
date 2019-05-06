import scrapy
from coverbrowser.items import CoverItem


class CoversScraper(scrapy.Spider):
    name = "covers"

    start_urls = ["http://www.coverbrowser.com/covers/XXX",
                  "http://www.coverbrowser.com/covers/XXXXX"]

    def parse(self, response):
        nextpageurl = response.xpath(
            '//p[@class="issuesNavigationTop"]/strong/a[contains(., "Next")]/@href').get()
        print('next page url: ', nextpageurl)
        for item in self.scrape(response):
            yield item

        if nextpageurl:
            nextpage = response.urljoin(nextpageurl)
            print("Found url: {}".format(nextpage))
            yield scrapy.Request(nextpage, callback=self.parse)

    def scrape(self, response):
        images = []
        for image in response.xpath('//p[@class="cover"]/a/img/@src'):
            imageURL = response.urljoin(image.get())
            print('image url: ', imageURL)
            images.append(imageURL)

        yield CoverItem(image_urls=images)
