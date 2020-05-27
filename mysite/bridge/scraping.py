import requests
from bs4 import BeautifulSoup

from .models import Bridge


def get_bridgehunters_page(url, county):
    """
    this function will open the page and return the entire contents of the page
    :param county: the name of the county of interest
    :param url: the url for the state of interest
    :return: the content of the website
    """
    url = url+county
    page = requests.get(url)
    return page.content


def parse_page(page):
    """
    This will parse through the given page, and put all the bridges in the database
    :param page: the html file that is read to be parsed
    :return: list of bridge elements
    """

    bridge_data = []
    soup = BeautifulSoup(page, 'html.parser')
    result = soup.select('.x')  # this looks for all of the divs with class = x
    for div_element in result:
        bridge_exists = div_element.find('span', class_='slost')
        if bridge_exists is None:
            bridge_name = div_element.find('a', class_='name')
            if bridge_name is not None:
                bridge_name = bridge_name.text
            bridge_description = div_element.find('span', class_='overview')
            if bridge_description is not None:
                bridge_description = bridge_description.text
            bridge_history = div_element.find('span', class_='history')
            if bridge_history is not None:
                bridge_history = bridge_history.text
            elif bridge_history is None:
                bridge_history = "There is no history for this bridge yet!"
            map_url = div_element.find('span', class_='i')
            if map_url is not None:
                map_url = map_url.find('a')
                if map_url is not None:
                    map_url = (map_url['href'])
                    map_url = "https://bridgehunter.com/" + map_url
                    print(">> ", map_url)
                    latitude, longitude = get_coordinates(map_url)


            #q = Bridge(name=bridge_name, description=bridge_description, year_built=bridge_history, lat=latitude, long = longitude)
            #q.save()
                    print(f'{bridge_name=}, {bridge_description=}, {bridge_history=}, {latitude=}, {longitude=}')

def get_coordinates(map_url):
    """

    :param map_url: This is the url of the bridge of interest
    :return: the latitude and longitude in a tuple
    """
    map_page = requests.get(map_url).content
    soup = BeautifulSoup(map_page, 'html.parser')
    result = soup.find_all('div', class_='section')
    for facts_exist in result:
        facts_section = facts_exist.find('a', {'name': 'Facts'})
        if facts_section is not None:
            facts = facts_exist.find('dl')
            if facts is not None:
                coordinates = facts.find('span', class_='geo')
                latitude = coordinates.find('span', class_='latitude')
                if latitude is not None:
                    latitude = latitude.text
                longitude = coordinates.find('span', class_='longitude')
                if longitude is not None:
                    longitude = longitude.text
                return latitude, longitude


def county_list(url):
    """
    this function will get all of the county links in a state
    :param url: the url of the state of interest
    :return: a list of counties in a given state
    """
    counties = []

    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    result = soup.find(id='widepagecontent')
    result = result.find('ul')
    result = result.find_all('li')
    for county_name in result:
        if county_name is not None:
            county_name = county_name.find('a')
            counties.append(county_name['href'])

    return counties


if __name__ == '__main__':

    page = get_bridgehunters_page('https://bridgehunter.com/md/', 'howard')
    parse_page(page)
