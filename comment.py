# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
url = "https://www.digikala.com/ajax/product/comments/790118/?page=1&mode=buyers"
page = requests.get(url)
print(page.status_code)   # This should print 200
soup = BeautifulSoup(page.content, 'html.parser')
comments = soup.find_all('div', class_="article")
for comment in comments:
    #get header text
        header = comment.find("div", class_="header")
        _headerText = header.find("div")
        _headerTextAuthor = _headerText.find("span")
        header_text = str(_headerText).replace(
            "<span>{}</span>".format(_headerTextAuthor.string), "")
        header_text = str(header_text).replace("<div>","")
        header_text = str(header_text).replace("</div>", "")
        headerTextAuthor = _headerTextAuthor.string
    #get comment
        description = comment.find("p")
        print(header_text)
        print(description.text)
