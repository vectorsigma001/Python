import requests
from bs4 import BeautifulSoup
import pandas as pd
#Creating a dataframes with pandas
def dataframes():
  url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"lxml")
  #putting productname in a list
  names=soup.find_all("a",class_="title")
  product_name=[]
  for i in names:
    name=i.text
    product_name.append(name)
  #extracting and putting product prices in a list
  prices=soup.find_all("h4",class_="pull-right price")
  prices_list=[]
  for i in prices:
    price=i.text
    prices_list.append(price)
  #extracing and putting description in a list
  desc=soup.find_all("p",class_="description")
  desc_list=[]
  for i in desc:
    desc=i.text
    desc_list.append(desc)
  #extracing and putting reviews in a list
  reviews=soup.find_all("p",class_="pull-right")
  reviews_list=[]
  for i in reviews:
    rew=i.text
    reviews_list.append(rew)

  #creating a dataframe with pandas
  df=pd.DataFrame({"Product Name":product_name,"Prices":prices_list,"Description":desc_list,"Number of reviews":reviews_list})
  df.to_csv("hello.csv")

#check hello.csv files to check all the datas 
