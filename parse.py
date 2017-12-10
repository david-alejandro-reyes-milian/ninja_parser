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


def get_name_from_page():
    name = soup.h1.contents[0]
    return str(name).strip()


def get_image_url_from_page():
    all_photos = soup.find_all("img", class_="img-responsive")
    url_image = all_photos[0].get('src')
    return url_image


def get_job_title_from_page():
    job_title = soup.h3
    return job_title.string


def get_job_location_from_page():
    job_details = soup.find_all("div", {"class": "job-detail-description"})
    job_location = job_details[0].contents[1]
    return str(job_location).strip()


def get_job_time_from_page():
    job_details = soup.find_all("div", {"class": "job-detail-description"})
    try:
        job_time = job_details[0].contents[4]
        job_time = job_time.contents[0]
        return str(job_time).strip()
    except:
        return


def get_about_from_page():
    column_whit_about = soup.find("div", {"class": "col-lg-8"})
    about = column_whit_about.contents[3].string
    about = str(about).strip()
    return about
