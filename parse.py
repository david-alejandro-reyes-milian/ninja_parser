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
