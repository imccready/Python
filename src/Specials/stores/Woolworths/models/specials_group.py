from src import constants

class Specials_Group(object):
    def __init__(self, category_id, description, product_count, is_special, is_bundle, url_friendly_name):
        self.category_id = category_id
        self.description = description
        self.product_count = product_count
        self.is_special = is_special
        self.is_bundle = is_bundle
        self.url_friendly_name = url_friendly_name


    def json(self):
        return {
            'categoryId' : self.category_id,
            'pageNumber': 0,
            'pageSize': 0,
            'sortType': 'AvailableDate',
            'url': "{}/{}".format(constants.WOOLWORTHS_SPECIALS_URL, self.url_friendly_name),
            'location': "{}/{}".format(constants.WOOLWORTHS_SPECIALS_URL, self.url_friendly_name),
            'formatObject': "{\"name\":\"" + self.description + " \"}",
            'isSpecial': str(self.is_special).lower(),
            'isBundle': str(self.is_bundle).lower(),
            'isMobile': 'false',

            'filters': []
        }
