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

#SCRAPING FLIPKART SIGNLE PAGE 
class Multiweb:
  url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page=1"
  names=[]
  prices=[]
  descriptions=[]
  reviews=[]
  def check(self):   
    r=requests.get(self.url)
    self.soup=BeautifulSoup(r.text,"html.parser")
    
  def name(self):
    name1=self.soup.find_all("div",class_="_4rR01T")
    for namecheck in name1:
      namecheck1=namecheck.text
      self.names.append(namecheck1)
      
  def price(self):
    price1=self.soup.find_all("div",class_="_30jeq3 _1_WHN1")
    for pricecheck in price1:
      pricecheck1=pricecheck.text
      self.prices.append(pricecheck1)
      
  def description(self):
    description1=self.soup.find_all("ul",class_="_1xgFaf")
    for descriptioncheck in description1:
      descriptioncheck1=descriptioncheck.text
      self.descriptions.append(descriptioncheck1)
     
  def review(self):
    review1=self.soup.find_all("div",class_="fMghEO")
    for reviewcheck in review1:
      reviewcheck1=reviewcheck.text
      self.reviews.append(reviewcheck1)
    
    
  def dataframe(self):
    df=pd.DataFrame({"Name":self.names,"Price":self.prices,"Description":self.descriptions,"Reviews":self.reviews})
    df.to_csv("MobileUnder5k.csv",index=False)
     
object=Multiweb()
object.check()
object.name()
object.price()
object.description()
object.review()
object.dataframe()
