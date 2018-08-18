import requests

class RequestHelper(object):

    @staticmethod
    def getPage(url):
        request = requests.get(url)
        return request.content

    #
    @staticmethod
    def get_json(url):
        request = requests.get(url)
        return request.json() if request is not None else None

    @staticmethod
    def post_json(url, data):
        request = requests.post(url, data=data)
        return request.json() if request is not None else None
