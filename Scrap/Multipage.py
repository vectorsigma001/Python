# EXTRACTING HREF FROM MULTUPLE PAGES
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

#WHEN YOU HAVE A CERTAIN CHANGES IN DIFFERENT PAGE YOU CAN MANIPULATE IT IN THIS WAY
#SCRAPING MOBILE PHONES UNDER 500000
def scrapingMobilePhones():
  for i in range(1,11):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page="+str(i)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    np=soup.find("a",class_="_1LKTO3").get("href")
    cnp="https://www.flipkart.com"+np
    print(url)
      #url=cnp
      #r=requests.get(url)
      #soup=BeautifulSoup(r.text,"html.parser")
  

scrapingMobilePhones()
