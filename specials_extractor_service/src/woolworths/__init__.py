from typing import List

from src.requesthelpers import RequestHelper
from src import constants
from src.utilities import Utilities
from src.woolworths.model.specialsgroup import SpecialsGroup



class Woolworths(object):
    def __init__(self):

        #todo this will be removed
        self.specials_categories_children = [
            "Half Price"
        ]

    def get_categories_with_specials(self) -> List[SpecialsGroup]:
        response_data = RequestHelper.get_json(constants.WOOLWORTHS_CATEGORIES_WITH_SPECIALS_URL)

        specials_categories = []
        for top_level_category in response_data['Categories']:
            if top_level_category['Description'] == constants.WOOLWORTHS_SPECIALS_CATEGORIES:
                specials_categories = top_level_category['Children']
                break


        specials_groups: List[SpecialsGroup] = []
        for category in specials_categories:
            #TODO this probably will move to the database to check
            if category['Description'] in self.specials_categories_children:
                specials_groups.extend( self.get_paged_category_groups(category) )
        return specials_groups

    # break each call to api into smaller chunks
    def get_paged_category_groups(self, category) -> List[SpecialsGroup]:
        specials_groups: List[SpecialsGroup] = []
        product_count = category['ProductCount']
        call_pages = Utilities.generate_paging_array(product_count, constants.WOOLWORTHS_ITEMS_PER_PAGE)

        for page_num, page_size in enumerate(call_pages):

            specials_group = SpecialsGroup(description=category['Description'],
                                           category_id=category['NodeId'],
                                           product_count=category['ProductCount'],
                                           is_special=category['IsSpecial'],
                                           is_bundle=category['IsBundle'],
                                           url_friendly_name=category['UrlFriendlyName'],
                                           page_number=page_num + 1,
                                           page_size=page_size)

            specials_groups.append( specials_group )
        return specials_groups


