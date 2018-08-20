from google.cloud import logging


class GoogleLogger(object):
    logging_client = logging.Client()
    log = logging_client.logger("Items")

    def log_text(self, value):
        self.log.log_text("( ITEMS ) - {}".format(value))

    def log_error(self, value):
        self.log.log_text("( ITEMS ) ERROR - {}".format(value))
