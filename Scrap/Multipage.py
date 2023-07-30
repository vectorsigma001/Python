# EXTRACTING HREF FROM THE CLASS
def scrapingMobilePhones():
  url="https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
  r=requests.get(url)
  soup=BeautifulSoup(r.text,"html.parser")
  while True:
    np=soup.find("a",class_="_1LKTO3").get("href")
    cnp="https://www.flipkart.com"+np
    print(cnp)
    url=cnp
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
  

scrapingMobilePhones()
  1
