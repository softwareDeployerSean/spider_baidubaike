
import re
import urllib
from urllib.parse import urlparse

from bs4 import BeautifulSoup


class SpiderParser(object):
    def parser_html(self, p_url, downhtml):
        if p_url is None or downhtml is None:
            return
        soup = BeautifulSoup(downhtml, "html.parser")
        urls = self.get_urls(p_url, soup)
        data = self.get_data(p_url, soup)
        return (urls, data)

    def get_urls(self, p_url, soup):
        # <a target="_blank" href="/item/%E9%9D%92%E8%8B%94%E8%B5%8B">青苔赋</a>
        urls = set()
        links = soup.find_all("a", href=re.compile(r"/item/"))
        for link in links:
            url = link['href']
            full_url = urllib.parse.urljoin(p_url, url)
            urls.add(full_url)
        return urls

    def get_data(self, p_url, soup):
        # < title > 美女_百度百科 < / title >
        # <meta name="description" content="美女是一个汉语词汇，拼音是měi nǚ，指容貌姣好、仪态优雅的女子。中国古代关于美女的形容词和诗词歌赋众多，形成了丰富的美学资料。《墨子·公孟》：“譬若美女，处而不出，人争求之。”...">
        data = {}
        data['url'] = p_url
        data['title'] = soup.title.string
        data['description'] =soup.find(attrs={"name":"description"})['content']
        return data
