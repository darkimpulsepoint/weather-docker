import requests
from bs4 import BeautifulSoup


def get_places(name):
    url = 'https://www.accuweather.com/en/search-locations/?query=' + name
    agent = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=agent)
    soup = BeautifulSoup(response.text, 'lxml')
    locs = soup.find("div", class_="locations-list").find_all("a")
    d = {el.text.strip(): el["href"] for el in locs}
    # print(locs[0]["href"])
    # print(d)

    return d


def get_weather(url):
    agent = {"User-Agent": "Mozilla/5.0"}
    response = requests.get("https://"+url, headers=agent)
    soup = BeautifulSoup(response.text, 'lxml')
    temperature = soup.find("div", class_="forecast-container").find("div", class_="temp").text
    other_info = soup.find("div", class_="cur-con-weather-card__panel details-container").find_all("div", class_="spaced-content")
    other_info_dict = dict([(j.text for j in i.find_all("span")) for i in other_info])
    info = {"Temperature": temperature}
    info.update(other_info_dict)
    return info