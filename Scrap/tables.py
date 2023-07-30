import requests
from bs4 import BeautifulSoup
import pandas as pd

#GETTING ALL THE HEADERS OF TABLE WITH TH TAGS
def first():
  url="https://ticker.finology.in/"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"html.parser")
  table=soup.find("table",class_="table table-sm table-hover screenertable")
  headers=table.find_all("th")
  return headers

#GEETING ALL THE HEADERS OF TABLE WITH TH TAGS IN TEXT FORMAT
def second():
  url="https://ticker.finology.in/"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"html.parser")
  table=soup.find("table",class_="table table-sm table-hover screenertable")
  headers=table.find_all("th")
  headers_text=[]
  for i in headers:
    headersitr=i.text
    headers_text.append(headersitr)
  return headers_text
#GETTING ALL THE HEADERS OF TABLE WITH TH TAGS IN TEXT FORMAT BUT IN DATAFRAMES
def third():
    url = "https://ticker.finology.in/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table", class_="table table-sm table-hover screenertable")
    headers = table.find_all("th")
    headers_text = []
    for i in headers:
        headersitr = i.text
        headers_text.append(headersitr)
    df = pd.DataFrame(columns=headers_text)  # Corrected here
    return df
#GETING ALL THE TABLE DATA 
def fourth():
  url="https://ticker.finology.in/"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"html.parser")
  table=soup.find("table",class_="table table-sm table-hover screenertable")
  rows=table.find_all("tr")
  check=[]
  for hello in rows[1:]:
    dank=hello.text
    check.append(dank)
 #return check
  check1=[]
  for newli in check:
    newli2=newli.replace("\n","  ")
    check1.append(newli2)
  for item in check1:
        print(item)
  '''
  for i in rows[1:]:
    data=i.find_all("td")
    row=[tr.text for tr in data]
    return row
  ''' 
 # df=pd.DataFrame()
  df = pd.DataFrame(check1, columns=['Data'])
    
    # Save DataFrame to csv
  df.to_csv('data.csv', index=False)
print(fourth())
