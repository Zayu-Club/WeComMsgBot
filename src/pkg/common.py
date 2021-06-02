import sys
import json
import logging
import logging.config
#import globalvar
from . import globalvar

logging.config.fileConfig(globalvar.DICT_GOLVAR['LOG_CONF_PATH'])
logger = logging.getLogger('common')


def getConfig(configPath, rwopt):
    config = ''
    try:
        with open(configPath, rwopt, encoding='utf-8') as jsonFile:
            config = json.load(jsonFile)
        jsonFile.close()
    except Exception as e:
        logger.error(f"Loading configuration:{configPath} failed")
        logger.exception(e)
        sys.exit()
    logger.info(f"Loading configuration:{configPath} successfully")
    return config
