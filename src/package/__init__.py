import logging
import logging.config
import os
import sys

__all__ = ['common', 'globalvar', 'msgJsonHelper', 'wecombasic']
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)19s] [%(levelname)-s] [%(filename)-s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if(not os.path.exists(".//log")):
    logging.warning("The log directory does not exist.")
    try:
        os.mkdir(".//log")
        logging.info("The log directory has been created.")
    except Exception as e:
        logging.error("The log directory creation failed.")
        sys.exit()
else:
    logging.info("The log directory already exists.")

logger = logging.getLogger('Kernel')
logger.info("The kernel is loaded.")
