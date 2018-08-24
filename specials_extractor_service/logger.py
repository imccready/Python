from google.cloud import logging


class GoogleLogger(object):
    logging_client = logging.Client()
    log = logging_client.logger("Specials-Extractor")

    def log_text(self, value):
        self.log.log_text("( SPECIALS SERVICE ) - {}".format(value))


    def log_error(self, error):
        self.log.log_text("( SPECIALS SERVICE ) ERROR - {}".format(error))