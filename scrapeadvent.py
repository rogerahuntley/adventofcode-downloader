import requests
import os
from bs4 import BeautifulSoup

# script created by rogerahuntley to be used for good
# please do not spam adventofcode server
# use case: to download descriptions at once and avoiding pinging server


def scrape_and_save_day(year, day):
    # scrape
    html = download_day(year, day)
    # save
    save_day(year, day, html)


def download_day(year, day):
    url = f'https://adventofcode.com/{year}/day/{day}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.select_one(".day-desc")
    return str(soup)


def save_day(year, day, html):
    filename = f'descriptions/{year}/{day}/description.html'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(html)


# run loop to generate and run all dates
for year in range(2015, 2021):
    for day in range(1, 26):
        scrape_and_save_day(year, day)
