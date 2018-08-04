from src import constants
from src.Specials.stores.Woolworths.models.specials_group import Specials_Group
from src.common.request import Request
from src.common.utilities import Utilities
from src.models.item import Item
from typing import List

class Woolworths(object):
    def __init__(self):
        self.specials_categories = "Specials"
        self.specials_categories_children = [
            "Half Price"
        ]

    @property
    def get_specials(self):
        categories = self.get_categories_with_specials()
        all_items =[]
        for category in categories:
            items = self.get_items_from_category(category)
            all_items.extend(items if not None else [])
        return all_items

    def get_categories_with_specials(self):
        all_categories = Request.get_json(constants.WOOLWORTHS_CATEGORIES_WITH_SPECIALS_URL)
        specials_groups = []
        for category in all_categories['Categories']:

            if category['Description'] == self.specials_categories:
                for specials in category['Children']:

                    if specials['Description'] in self.specials_categories_children:
                        group = Specials_Group(description= specials['Description'],
                                               category_id= specials['NodeId'],
                                               product_count= specials['ProductCount'],
                                               is_special= specials['IsSpecial'],
                                               is_bundle= specials['IsBundle'],
                                               url_friendly_name= specials['UrlFriendlyName'])
                        specials_groups.append(group)
                break

        return specials_groups

    def get_items_from_category(self, specials_group):
        items = []
        product_count = specials_group.product_count

        #get rid of
        #product_count = 2

        call_pages = Utilities.generate_paging_array(product_count, constants.WOOLWORTHS_ITEMS_PER_PAGE)

        for page_num, page_size in enumerate(call_pages):
            request_data = specials_group.json()
            request_data['pageNumber'] = page_num + 1
            request_data['pageSize'] = page_size

            json_response = Request.post_json(constants.WOOLWORTH_ITEM_URL, request_data)
            items.extend( self.get_items(json_response) )

        return items

    def get_items(self, json_response):
        items: List(Item) = []
        if json_response is not None and json_response['Success'] == True:
            for product in json_response['Bundles']:
                product = product['Products'][0]

                item: Item = Item( product_code= product['Stockcode'],
                             barcode=product['Barcode'],
                             store=constants.WOOLWORTHS,
                             name=product['Name'],
                             price=product['Price'],
                             product_url="https://www.woolworths.com.au/shop/productdetails/{}/{}".format(product['Stockcode'], product['UrlFriendlyName']),
                             image_url=product['MediumImageFile'],
                             category=product['AdditionalAttributes']['piesdepartmentnamesjson'],
                             sub_category=product['AdditionalAttributes']['piessubcategorynamesjson'])
                items.append( item )

        return items

    def get_item_call_pages(self, total_products):
        pages = []
        total = 0
        items_per_page = constants.WOOLWORTHS_ITEMS_PER_PAGE
        for x in range(items_per_page, total_products, items_per_page):
            pages.append(items_per_page)
            total = total + items_per_page
        pages.append( total_products - total )
        return pages
