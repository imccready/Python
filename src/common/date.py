import datetime


class Date(object):

    @staticmethod
    def get_today():
        return datetime.datetime.today().strftime('%d/%m/%Y')

    @staticmethod
    def get_month():
        return datetime.datetime.today().strftime('%b %y')
