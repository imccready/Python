from src import constants

class SpecialsGroup(object):
    def __init__(self, category_id, description, product_count, is_special, is_bundle, url_friendly_name, page_number, page_size):
        self.category_id = category_id
        self.description = description
        self.product_count = product_count
        self.is_special = is_special
        self.is_bundle = is_bundle
        self.url_friendly_name = url_friendly_name
        self.page_number = page_number
        self.page_size = page_size


    def json(self):
        return {
            'categoryId' : self.category_id,
            'pageNumber': self.page_number,
            'pageSize': self.page_size,
            'sortType': 'AvailableDate',
            'url': "{}/{}".format(constants.WOOLWORTHS_SPECIALS_URL, self.url_friendly_name),
            'location': "{}/{}".format(constants.WOOLWORTHS_SPECIALS_URL, self.url_friendly_name),
            'formatObject': 'FIX THIS!!', # "{\"name\":\"" + self.description + " \"}",
            'isSpecial': str(self.is_special).lower(),
            'isBundle': str(self.is_bundle).lower(),
            'isMobile': 'false',

            'filters': []
        }
