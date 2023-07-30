import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.iplt20.com/auction"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
overview=soup.find_all("div",class_="auction-grid-view mt-3")

#STORING NAME OF THE TEAM IN A LIST
teamname=soup.find_all("div",class_="agv-team-name")
teamnamelist=[]
for check in teamname:
   check1=check.text
   teamnamelist.append(check1)
#STORING FUND REMANING OF THE TEAM IN A LIST
info=soup.find_all("span",class_="fr-fund")
fundremainlist=[]
for check in info:
  check1=check.text
  fundremainlist.append(check1)
newfundremainlist=[]
#GENERATING INDICES FOR SKIPING SOME ELEMENTS
indices=[]
for i in range(0,len(fundremainlist),3):
  indices.append(i)
newfundremainlist=[fundremainlist[i] for i in indices]
newfundremainlist1=[]
storageforfundremain=[]
for newfundremainlist1 in newfundremainlist:
  storageforfundremain.append(newfundremainlist1)
#GENERATING OVERSEAS PLAYERS
overseaslist=[]
storageforoverseasplayers=[]
for check in info:
  check1=check.text
  overseaslist.append(check1)
newoverseaslist=[]
indices=[]
for i in range(1,len(overseaslist),3):
  indices.append(i)
newoverseaslist=[overseaslist[i] for i in indices]
newoverseaslist1=[]
for newoverseaslist1 in newoverseaslist:
  storageforoverseasplayers.append(newoverseaslist1)
#GENERATING TOTAL PLAYERS
totalplayerlist=[]
storagefortotalplayer=[]
for check in info:
  check1=check.text
  totalplayerlist.append(check1)
newtotalplayerlist=[]
indices=[]
for i in range(2,len(totalplayerlist),3):
  indices.append(i)
newtotalplayerlist=[totalplayerlist[i] for i in indices]
newtotalplayerlist1=[]
for newtotalplayerlist1 in newtotalplayerlist:
  storagefortotalplayer.append(newtotalplayerlist1)

#Creating a dataframe with pandas
df=pd.DataFrame({"Team Name":teamnamelist,"Fund Remained":storageforfundremain,"Overseas Players":storageforoverseasplayers,"Total Players":storagefortotalplayer})
df.to_csv("iplauction.csv", index=False)
