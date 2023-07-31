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

#SCRAPING FLIPKART MILTIPAGE WHEN PAGE HAVE THNE SAME PATTERN IN THE URL LIKE NUMBERS AND THE NUMBERS IN THE COMING URL CHANGES WITH IN SOME SEQUENCE 
class Multiweb:

  def __init__(self):
    self.names = []
    self.prices = []
    self.descriptions = []
    self.reviews = []

  def check(self, url):
    r = requests.get(url)
    self.soup = BeautifulSoup(r.text, "html.parser")

  def name(self):
    name1 = self.soup.find_all("div", class_="_4rR01T")
    for namecheck in name1:
      namecheck1 = namecheck.text
      self.names.append(namecheck1)

  def price(self):
    price1 = self.soup.find_all("div", class_="_30jeq3 _1_WHN1")
    for pricecheck in price1:
      if(len(self.prices)<len(self.names)):
        pricecheck1 = pricecheck.text
        pricecheck2 = pricecheck1.replace("₹", "Rs.")
        self.prices.append(pricecheck2)

  def description(self):
    description1 = self.soup.find_all("ul", class_="_1xgFaf")
    for descriptioncheck in description1:
      if len(self.descriptions) < len(self.names):
        descriptioncheck1 = descriptioncheck.text
        self.descriptions.append(descriptioncheck1)

  def review(self):
    review1 = self.soup.find_all("div", class_="_3LWZlK")
    for reviewcheck in review1:
      if len(self.reviews) < len(self.names):
        reviewcheck1 = reviewcheck.text
        self.reviews.append(reviewcheck1)

  def dataframe(self):
    df = pd.DataFrame({
        "Name": self.names,
        "Price": self.prices,
        "Description": self.descriptions,
        "Reviews": self.reviews
    })
    df.to_csv("MobileUnder5k.csv", index=False)


object = Multiweb()
for i in range(1, 20):  # Change the range accordingly
  url = f"https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page={i}"
  object.check(url)
  object.name()
  object.price()
  object.description()
  object.review()
object.dataframe()
