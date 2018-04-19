import urllib
from urllib import parse
from urllib.parse import quote


class SpiderData(object):
    def __init__(self):
        self.datas = []

    def add_data(self, content):
        if content is None:
            return
        self.datas.append(content)

    def print_data(self):
        if self.datas.__len__() == 0:
            return
        with open('spider_data.html', 'w', encoding="utf-8") as sd:
            sd.write('<html>')
            sd.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
            sd.write('<body>')
            sd.write('<table>')
            for data in self.datas:
                url = data['url']
                print(parse.unquote(url))
                url=parse.unquote(url)
                sd.write('<tr>')
                sd.write('<td>%s</td>' % url)
                sd.write('<td>%s</td>' % data['title'])
                sd.write('<td>%s</td>' % data['description'])
                sd.write('</tr>')
            sd.write('</table>')
            sd.write('</body>')
            sd.write('</html>')
