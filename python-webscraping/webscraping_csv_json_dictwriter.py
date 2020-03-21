from bs4 import BeautifulSoup
import requests
from csv import DictWriter
import json

# access request from the url
response = requests.get("https://coreyms.com/category/development/terminal")
# get html data using text attribute - str type
html_info = response.text
# parse the data using html.parser
# parsing means converting from one type -> other
parse_data = BeautifulSoup(html_info, "html.parser")

# get the data form of list using find_all() method.
getMain = parse_data.find_all("main", attrs={"class": "content"})
# create an empty list
all_info = []
i = 0
for get_each_main in getMain:
    # get list of article elements
    get_article = get_each_main.find_all("article")
    j = len(get_article)
    while j > 0:
        # get article is a ResultSet object, so we cant call find_all on that.
        # get the title
        get_title_text = get_article[i].find("h2").get_text()
        # get the date
        get_date = get_article[i].find("time").get_text()
        # get author name
        get_author = get_article[i].find("span", attrs={"class": "entry-author-name"}).get_text()
        # get description
        content_text = get_article[i].find("div", attrs={"class": "entry-content"}).get_text()
        description = content_text.split(".")[0]
        # get youtube link
        get_youtube_link = get_article[i].find("iframe")["src"].split("?")[0]

        # get files under
        category_list = []
        # get list of data with attribute rel
        get_category = get_article[i].find_all("a", attrs={"rel": "category tag"})
        for each_category in get_category:
            category_list.append(each_category.text)
        # join each item in the list with a comma
        category_list = ", ".join(category_list)

        tag_list = []
        # get list of data with attribute rel
        get_tags = get_article[i].find_all("a", attrs={"rel": "tag"})
        for each_tag in get_tags:
            tag_list.append(each_tag.text)
        # join each item in the list with a comma
        tag_list = ", ".join(tag_list)
        # append all result to a list
        all_info.append({
            "title": get_title_text,
            "date": get_date,
            "author": get_author,
            "description": description,
            "youtube url": get_youtube_link,
            "categories": category_list,
            "tag": tag_list,
        })
        # increment j and decrement i
        j -= 1
        i += 1
    print(all_info)

    # writing to a csv file
with open("./pageData.csv", "w") as my_csv:
    # make a list of headers
    headers = ["title", "date", "author", "description",
               "youtube url", "categories", "tag"]
    # use DictWriter() to write each dict item to csv
    write_to_csv = DictWriter(my_csv, fieldnames=headers)
    # first write header
    write_to_csv.writeheader()
    for each_info in all_info:
        # write each row
        write_to_csv.writerow(each_info)


# write this data to json file
with open("./all.json", "w") as jw:
    json.dump(all_info, jw)
