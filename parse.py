from html.parser import HTMLParser

import requests as requests


class HtmlParser(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            print('Title: ', tag)

    def handle_endtag(self, tag):
        pass
        # print("Encountered an end tag :", tag)

    def handle_data(self, data):
        pass
        # print("Encountered some data  :", data)


parser = HtmlParser()
page = requests.get('http://www.ninjacuba.com/freelancers/fabian-ruiz-estevez')
parser.feed(str(page.content))
