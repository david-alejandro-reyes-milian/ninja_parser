from bs4 import BeautifulSoup
import requests as requests
import json
import os


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


def get_social_links_from_page():
    url_links = []
    social_links = soup.find_all("a", {"class": "link social website"})
    for link in social_links:
        url_link = link.get("href")
        if not url_links.__contains__(url_link):
            url_links.append(url_link)

    return url_links


def get_skills_from_page():
    skills = []
    skills_in_page = soup.find_all("div", {"class": "job clearfix"})
    for html_skill in skills_in_page:
        period = html_skill.contents[1].contents[1]
        year_from = period.contents[0].string
        year_to = period.contents[2].string
        period = '%s - %s' % (year_from, year_to)

        description = html_skill.contents[3]
        profession = description.contents[1]
        profession = str(profession.string).strip()

        where = description.contents[3]
        where = str(where.string).strip()

        description = description.contents[5]
        description = str(description.string).strip()

        skill = {
            "period": period,
            "profession": profession,
            "where": where,
            "description": description
        }
        skills.append(skill)
    return skills


new_contact = {
    "name": get_name_from_page(),
    "image_url": get_image_url_from_page(),
    "job_title": get_job_title_from_page(),
    "job_location": get_job_location_from_page(),
    "job_time": get_job_time_from_page(),
    "about": get_about_from_page(),
    "social_links": get_social_links_from_page(),
    "skills": get_skills_from_page()
}

file_name = "data.json"


def save_data_to_json_file(json_data):
    with open(file_name, 'w+') as f:
        json.dump(json_data, f, indent=4)

