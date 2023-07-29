import requests
from bs4 import BeautifulSoup
def navigable():
  url="https://webscraper.io/test-sites/e-commerce/allinone/computers"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"html.parser")
  tag=soup.header.div.a.button.span
  return (tag.string)

#GETTING THE FIRST ELEMENT OF THE DIV TAGS OPR 
def finding():
  url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"html.parser")
  return soup.find("h4",{"class":"pull-right price"})
  price=soup.find("h4",{"class":"pull-right price"})
  return (price.string)
print(finding())
