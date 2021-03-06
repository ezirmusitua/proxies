# -*- coding: utf-8 -*-
import scrapy

from proxy_crawler.items import ProxyItemLoader, Proxy


class Ip181Spider(scrapy.Spider):
    name = 'ip181'
    allowed_domains = ['ip181.com']
    start_urls = ['http://ip181.com/']

    def parse(self, response):
        rows = response.css('.panel-body tbody tr:not(:first-child)')
        proxies = []
        for row in rows:
            loader = ProxyItemLoader(item=Proxy(), selector=row)
            loader.add_css('ip_address', 'td:nth-child(1)::text')
            loader.add_css('port', 'td:nth-child(2)::text')
            proxy_type = row.css('td:nth-child(4)::text').extract()
            loader.add_value('proxy_type', proxy_type)
            proxies.append(loader.load_item())
        return proxies
