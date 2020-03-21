from bs4 import BeautifulSoup
import requests

# access request from the url
response = requests.get("https://coreyms.com/category/development/terminal")
# get html data using text attribute - str type
html_info = response.text
# parse the data using html.parser
parse_data = BeautifulSoup(html_info, "html.parser")

# parsing means converting from one type -> other

firstList = []
dateList = []

# get the data form of list using find_all() method.
getLink = parse_data.find_all("a", attrs={"class": "entry-title-link"})
for eachLink in getLink:
    # get each text data from list using text attribute
    firstList.append(eachLink.text)
print(firstList)

# get Date from page
getTime = parse_data.find_all("time", attrs={"class": "entry-time"})
for eachTime in getTime:
    dateList.append(eachTime.text)
print(dateList)
