class Utilities(object):

    @staticmethod
    def generate_paging_array(total_size, page_size):
        for x in range(0, total_size, page_size):
            size = page_size if (x + page_size) < total_size else  total_size - x
            yield size

    @staticmethod
    def page_array(items, page_size):
        for i in range(0, len(items), page_size):
            yield items[i:i + page_size]