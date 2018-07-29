import re

from bs4 import BeautifulSoup

from src.models.item import Item


class Page(object):
    def __init__(self, store):
        self.domain = "https://www.woolworths.com.au"
        self.store = store
        self.next_page = None


    def get_items(self, webdriver):
        content = webdriver.get_page()
        soup = BeautifulSoup(content, "html.parser")
        elements = soup.find_all("div", {"class": "shelfProductTile-content"})
        items = []
        for element in elements:
            try:
                # Get Name
                name = element.find("a", {"class": "shelfProductTile-descriptionLink"}).text.strip()

                #Get Url
                urlPath = element.find("a", {"class": "shelfProductTile-descriptionLink"})['href']
                url = "{}{}".format(self.domain, urlPath)

                #Get Price
                dollars = element.find("span", {"class": "price-dollars"})
                dollars = dollars.text.strip() if dollars is not None else None
                cents = element.find("span", {"class": "price-cents"})
                cents = cents.text.strip()  if cents is not None else None
                price = float("{}.{}".format(dollars, cents)) if dollars is not None and cents is not None else None

                #Get Image
                image_url = element.find("img", {"class": "shelfProductTile-image"})['src'].strip()

                #Get Id
                match = re.search("\/\d*(?=.jpg$)", image_url)
                matchGroup = match.group() if match is not None else None
                id = matchGroup[1:] if matchGroup is not None else None

                if id is not None:
                    item = Item(self.store, name, price, url, image_url, id)
                    item.save_to_mongo()
                else:
                    print("Invalid ID: {}".format(image_url))
            except Exception as e:
                print(e)
                print("Error - getting item: {}".format(element))



# get item details
    #   https://www.woolworths.com.au/apis/ui/product/detail/503678?isMobile=false
    #   https://www.woolworths.com.au/apis/ui/product/detail/384247?isMobile=false

    def is_next_page(self, webdriver):
        content = webdriver.get_page()
        soup = BeautifulSoup(content, "html.parser")
        next_page = soup.find("a", {"class": "paging-next"})

        if (next_page is not None):
            webdriver.next_page("paging-next")
            return True
        else:
            return False


