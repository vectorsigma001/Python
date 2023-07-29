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

print(third())
