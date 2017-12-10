from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests as requests

web_url = 'http://www.ninjacuba.com/freelancers/fabian-ruiz-estevez'
local_url = r"c:\profile2.html"


def instantiate_soup_with_url(url):
    page = requests.get(url)
    new_soup = BeautifulSoup(page, "html.parser")
    return new_soup


def instantiate_soup_with_local_page(url):
    new_soup = BeautifulSoup(open(url).read(), "html.parser")
    return new_soup


soup = instantiate_soup_with_local_page(local_url)


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
page = requests.get(web_url)
parser.feed(str(page.content))
