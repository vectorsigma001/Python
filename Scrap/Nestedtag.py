import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
##GETTING ALL THE BOXES
def namesAndDescription():
  soup=BeautifulSoup(r.text,"html.parser")
  boxes=soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
  return boxes
#GETTING ELEMENT OF A SPECIFIC BOX
def namesAndDescription1():
  soup=BeautifulSoup(r.text,"html.parser")
  boxes=soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")[2]
  #return boxes
  #GETTING NAMES OF FROM THE BOXES
  name=boxes.find("a").text
  #return name
  desc=boxes.find("p").text
  #return desc
  navbar=soup.find_all("ul",class_="nav",id="side-menu")
  name=(soup.find("li",class_="active"))
  #return navbar
  #return name.text
   #priting all thbe names , desc and the navbars
  return(
    
    name.text
  )
print(namesAndDescription1())
