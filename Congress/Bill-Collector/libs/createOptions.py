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
        #"https://www.congress.gov/search?searchResultViewType=expanded"
        'https://www.congress.gov/search'
    )
    soup = BeautifulSoup(markup=response.content, features="lxml")
    return soup


def parseData(soup) -> list:
    
    shownOptions = soup.select(".facetbox-shownrow > a", strip=True)
    hiddenOptions = soup.select(".facetbox-hiddenrow > a", strip=True)
    words = []

    for links in shownOptions:
        print(links.text)
    print('HIDDEN')
    for links in hiddenOptions:
        print(links.text)

    print(hiddenOptions)
    
    return words
    # print(shownOptions[0].contents)


resp = scrapeOptions()
print(parseData(resp))

# full options specific wording
# everytime you click option need specific url
# human readable
# every congress section have list of what options are
# committees change
# what works for each congress session
# maybe different
# do congress manually

# programmically
# click on 73rd and look at url
# send request in python
# get html response back put into beutiful soup
# find all for html element of span class
# repeatable code


# categoryBox = soup.find(id="nav")
    # for link in categoryBox.find_all("a"):
    # print(link.get_text())

    # the two css classes that they are in

# look at stripped strings
    # for child in shownOptions:
    #     for grandchild in child.children:
    #         # try:
    #         print("in try")
    #         # strip
    #         # if it contains < or [] or no lettersthen don't append
    #         cleanedString = grandchild
    #         if isinstance(cleanedString, BeautifulSoup.NavigableString):
    #             print(type(cleanedString))
    #         else:
    #             print("nah")

    # if not cleanedString.isspace() and cleanedString.isalpha():
    #     if not cleanedString.index("<") and not cleanedString.index("["):
    #         words.append(cleanedString)
    # except:
    # do nothin
    # print("error ")
    # i
