
class Airbnb:

  def __init__(self):
    self.names = []
    self.prices = []
    self.descriptions = []
    self.reviews = []

  def check(self, url):
    r = requests.get(url)
    self.soup = BeautifulSoup(r.text, "html.parser")

  def name(self):
    name1 = self.soup.find_all("div", class_="t1jojoys dir dir-ltr")
    for namecheck in name1:
      namecheck1 = namecheck.text
      self.names.append(namecheck1)

  def price(self):
    price1 = self.soup.find_all("span", class_="a8jt5op dir dir-ltr")
    for pricecheck in price1:
      if(len(self.prices)<len(self.names)):
        pricecheck1 = pricecheck.text
        pricecheck2 = pricecheck1.replace("$", "$.")
        self.prices.append(pricecheck2)

  def description(self):
    description1 = self.soup.find_all("span", class_="dir dir-ltr")
    for descriptioncheck in description1:
      if len(self.descriptions) < len(self.names):
        descriptioncheck1 = descriptioncheck.text
        self.descriptions.append(descriptioncheck1)

  def review(self):
    review1 = self.soup.find_all("span", class_="r1dxllyb dir dir-ltr")
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
    df.to_csv("Airbnbpart1.csv", index=False)

object = Airbnb()
for i in range(1, 20):  # Change the range accordingly
  url ="https://www.airbnb.com/s/New-Delhi--India/homes?adults=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes"
  object.check(url)
  object.name()
  object.price()
  object.description()
  object.review()
object.dataframe()
