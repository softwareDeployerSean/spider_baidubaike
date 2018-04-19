class SpiderUrl(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_newurl(self, target_url):
        if target_url == None:
            return
        elif target_url not in self.new_urls and target_url not in self.old_urls:
            self.new_urls.add(target_url)

    def has_newurl(self):
        return self.new_urls.__len__() != 0

    def get_newurl(self):
        return self.new_urls.pop()

    def add_newurls(self, newurls):
        if newurls == None:
            return
        for url in newurls:
            self.add_newurl(url)
