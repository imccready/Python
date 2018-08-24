from google.cloud import logging


class GoogleLogger(object):
    logging_client = logging.Client()
    log = logging_client.logger("Item-History")

    def log_text(self, value):
        self.log.log_text("( Item History ) - {}".format(value))


    def log_error(self, error):
        self.log.log_text("( Item History ) ERROR - {}".format(error))