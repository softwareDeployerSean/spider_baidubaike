from spider_baidu_baike import spider_down, spider_parser, spider_data, spider_url


class SpiderBaike(object):
    def __init__(self):
        self.dowm = spider_down.SpiderDowm()
        self.parser = spider_parser.SpiderParser()
        self.urls = spider_url.SpiderUrl()
        self.data = spider_data.SpiderData()

    def run(self):
        global target_url
        count = 1
        self.urls.add_newurl(target_url)
        while self.urls.has_newurl():
            if count > 100:
                break
            try:
                newurl = self.urls.get_newurl()
                downhtml = self.dowm.down_html(newurl)
                (newurls, content) = self.parser.parser_html(newurl, downhtml)
                self.urls.add_newurls(newurls)
                self.data.add_data(content)
                count += 1
            except Exception as e:
                print("spider error", e)
        self.data.print_data()


if __name__ == "__main__":
    target_url = "https://baike.baidu.com/item/%E7%BE%8E%E5%A5%B3"
    sd = SpiderBaike()
    sd.run()
