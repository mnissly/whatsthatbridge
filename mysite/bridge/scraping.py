import requests
from bs4 import BeautifulSoup


class Bridge:
    county = "howard"

    """
    Builds a Bridge class from the Website using the county. Raises exception if the county does not exist.
    :param county: name of the county in MD
    """

    # this calls the html file from the internet
    url = f'https://bridgehunter.com/md/{county}/'
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")
    x_elements = soup.select('.x a', class_="name")
    bridge_name = x_elements[1].text


if __name__ == '__main__':
    bridge_trial = Bridge.bridge_name

    print(bridge_trial)
