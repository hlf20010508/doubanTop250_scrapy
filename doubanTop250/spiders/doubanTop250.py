import scrapy
from doubanTop250.items import Doubantop250Item

class Doubantop250Spider(scrapy.Spider):
    name = 'doubanTop250'
    allowed_domains = ['movie.douban.com']
    start_urls = []
    for i in range(10):
        start_urls.append('https://movie.douban.com/top250?start={}&filter='.format(25*i))

    file=open('top250.txt', 'w', encoding='utf8')
    file.close()
    def parse(self, response):
        item=Doubantop250Item()
        movies=response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['name']=movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['director']=movie.xpath('.//div[@class="bd"]/p[1]/text()[1]').extract()[0]
            item['brief']=movie.xpath('.//div[@class="bd"]/p[1]/text()[2]').extract()[0]
            item['score']=movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['comment']=movie.xpath('.//div[@class="star"]/span[4]/text()').extract()[0]
            item['quote']=movie.xpath('.//span[@class="inq"]/text()').extract()
            yield item