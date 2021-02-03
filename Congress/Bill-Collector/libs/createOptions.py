# get the names of the options
# store them
# output them to a json or text file
from bs4 import BeautifulSoup
from requests import Response
import requests


def createFile(text):
    optionsFile = open("optionsText.txt", "w+")
    optionsFile.write(text)


def scrapeOptions():
    response = requests.get(
        "https://www.congress.gov/search?searchResultViewType=expanded"
    )
    soup = BeautifulSoup(markup=response.content, features="lxml")
    return soup


def parseData(soup):
    categoryBox = soup.find(id="nav")
    for link in categoryBox.find_all("a"):
        print(link.get_text())


resp = scrapeOptions()
parseData(resp)
