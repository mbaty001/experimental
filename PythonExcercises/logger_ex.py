import logging

LOG_FILE = './hc.log'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#
# All DEBUG messages will go to the rotated log file only.
#
#handler = logging.handlers.RotatingFileHandler(LOG_FILE, mode = 'a', backupCount = 2, maxBytes = 100000000)

#
# All DEBUG messages will go to the fresh new log file only.
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