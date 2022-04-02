import requests
from bs4 import BeautifulSoup
import pandas

wiki_url="https://en.wikipedia.org/wiki/Main_Page"
req = requests.get(wiki_url)
content = req.content
#print(content)

soup=BeautifulSoup(content,"html.parser")
body = soup.find_all("div",{"class":"me-body"})
desc = soup.find_all("td",{"class":"MainPageBG"})
pic=soup.find_all("img",{"alt":"Northern rosella"})
pic_1 = soup.find_all("a",{"href":"northern rosella"})
banner = soup.find_all("div",{"id":"mp-topbanner"})
portals = soup.find_all("ul",{"id":"mp-portals"})
bottom_content = soup.find_all("div",{"id":"mp-sister-content"})

print(body,desc,pic,pic_1,banner,portals,bottom_content)



