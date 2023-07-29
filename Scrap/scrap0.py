from re import I
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
#print(finding())
#GEEING THE DESCRIPTION OF THE FIRST ELEMENT OF THE DIV TAGS 
def findingdescription():
  url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"html.parser")
  desc=soup.find("p",{"class","description"})
  return desc.string
#  return soup.find("p",{"class","description"})

#print(findingdescription())

def findingAllDescription():
  url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"html.parser")
  prices=soup.find_all("h4",class_="pull-right price")
  #return prices
  #return len(prices)
  for i in prices:
    return i
#print(findingAllDescription())
#  printing all the prices
def findingAllDescription1():
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    prices = soup.find_all("h4", {"class":"pull-right price"})
    return len(prices)
    return prices
    for price1 in prices:
      return price1
    for price in prices:
        print(price.text)  # print the text inside the HTML tag
    return prices[3]
#print(findingAllDescription1())
def findingAllDescription2():
  url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"html.parser")
  description=soup.find_all("p",class_="description")
  #return len(description)
  #return description
  for descriptiononly in description:
    print(descriptiononly.text)
#print(findingAllDescription2())
#
