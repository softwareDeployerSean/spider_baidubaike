from urllib import request



class SpiderDowm(object):
    def down_html(self, url):
        content = None
        if url == None:
            return content

        response = request.urlopen(url)
        if response.getcode() == 200:
            content = response.read()
        return content
