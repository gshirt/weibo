import scrapy
from scrapy.http.request import Request
import logging
from weibo.items import WeiboItem

class weiboSpider(scrapy.Spider):
    name = 'weibo'
    start_urls = ['http://weibo.com/p/1005051918015782/home?from=page_100505&mod=TAB&is_all=1',]

    def start_requests(self):
        for url in self.start_urls:
            return [Request(url, method='get',  
                cookies={'ALF': '1523279791',
                'Apache': '9606121846193.572.1491639000402',
                'SCF':'AnIsTABvR8yw9ZO5-Mg3FADIsAvNWrRTrWvFHDhRzeYvDA55WmrVBjineHSt153DVL0YanLj7k5KWHD0kxGnVlE.',
                'SINAGLOBAL': '5380633808557.653.1491309482748',
                'SSOLoginState': '1491739308',
                'SUB': '_2A25177MuDeRhGeVH6FcZ8ifMzzqIHXVWnKPmrDV8PUJbmtBeLUX3kW9CI3_QRH49rYwEHHKk9-fYf-PuOQ..',
                'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0f4LhJ0xLhLjZP.f9J0ID5JpX5o2p5NHD95Q01Kef1hz4ehBcWs4Dqcjci--NiKnXi-2pi--ciKLhiKn4i--Ri-8siK.Ni--fiK.EiKyhi--Ri-isiKLhi--ciK.ci-z4',
                'SUHB': '0TPV8jqCgkE7Bi',
                'ULV': '1491639000406:4:4:4:9606121846193.572.1491639000402:1491575269257',
                'UM_distinctid': '15b393e9982449-0a5865634e62e78-3e6e4647-13c680-15b393e99836b9',
                'UOR': 'www.liaoxuefeng.com,widget.weibo.com,www.baidu.com',
                'USRANIME': 'usrmdinst_57',
                'WBStorage': '02e13baf68409715|undefined',
                'YF-Page-G0': '3d55e26bde550ac7b0d32a2ad7d6fa53',
                'YF-Ugrow-G0': '57484c7c1ded49566c905773d5d00f82',
                'YF-Ugrow-SEO-G0': '51e4c14680ad84d57e81dfa4eef90e15',
                'YF-V5-G0': 'fec5de0eebb24ef556f426c61e53833b',
                '_s_tentry': 'www.baidu.com',
                'login_sid_t': '71f883c4f1b41aeb76a1ed52cab32e19',
                'wb_h5video_3935829046': 'expand',
                'wvr': '6'}, 
                headers={ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',   
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',   
                    'Accept-Encoding': 'gzip, deflate', 
                    'DNT': '1', 
                    'Referer': '...',   
                    'Connection': 'keep-alive', 
                    'Cache-Control': 'max-age=0'})]
    
    def parse(self, response):
        uid = response.xpath('//h1[@class="username"]/text()').extract()
        followUrl = response.xpath('//span[text()=u"关注"]/parent::*/@href').extract()
        followerUrl = response.xpath('//span[text()=u"粉丝"]/parent::*/@href').extract()
        commentUrl = response.xpath('//span[text()=u"微博"]/parent::*/@href').extract()
        filename = response.url.split("/")[-2]  
        #logging.info(response.body)
        logging.info(uid)
        logging.info(followUrl)
        logging.info(followerUrl)
        logging.info(commentUrl)
        logging.info('response.body')
        with open(filename, 'wb') as f:  
            f.write(response.body)  
            f.close()

    def parseFollow(self, response):
        pass
