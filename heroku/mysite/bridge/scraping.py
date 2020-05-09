import requests
from bs4 import BeautifulSoup

from .models import Bridge


def get_bridgehunters_page(county):
    """
    this function will open the page and throw out the entire contents of the page
    :param county: the name of the county of interest
    :return: the content of the website
    """
    url = f'https://bridgehunter.com/md/{county}/'
    page = requests.get(url)
    return page.content


def parse_page(page):
    """

    :param page: the html file that is read to be parsed
    :return:
    """
    soup = BeautifulSoup(page, 'html.parser')
    result = soup.select('.x') #this looks for all of the divs with class = x
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

            q = Bridge(name=bridge_name, description=bridge_description, year_built=bridge_history)
            q.save()

"""if __name__ == '__main__':
    for county in ['howard']:
        bh_page = get_bridgehunters_page(county)
        parse_page(bh_page)
"""