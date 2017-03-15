from raven import Client
from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging

import logging


client = Client('http://89dd6d7f4a8e4c07b21dc8f38a8b39c6:063921ba4690414aa911ae939ac56b22@fefinance1-5810:8080/2')
handler = SentryHandler(client, level=logging.DEBUG)
setup_logging(handler)

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


log.debug('This is a debug message')
log.info('This is an info message')
log.warning('This is a warning message')
log.error('This is an error message')
log.critical('This is a critical message')
