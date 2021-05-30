# Exercise 4


# import module
import requests
# import pandas as pd
from bs4 import BeautifulSoup


# link for extract html data
def get_data(url):
    r = requests.get(url)
    return r.text


html_data = get_data("https://www.pcmag.com/news/silicon-usa-technology-made-in-america")
soup = BeautifulSoup(html_data, 'html.parser')

with open('paragraph.txt', 'w') as file:
    for data in soup.find_all("p"):
        file.write(f"\n{data.get_text()}")

