import logging

LOG_FILE = './war.log'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#
# All DEBUG messages will go to the log file only.
#
handler = logging.FileHandler(LOG_FILE, mode = 'w')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#
# All INFO messages go the file and to the screen
#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

log = logger