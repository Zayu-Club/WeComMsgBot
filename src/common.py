import json
import logging
import logging.config

LOG_CONF_PATH = ".\\conf\\log.conf"

logging.config.fileConfig(LOG_CONF_PATH)
logger = logging.getLogger('common')


def getConfig(configPath, rwopt):
    config = ''
    try:
        with open(configPath, rwopt, encoding='utf-8') as jsonFile:
            config = json.load(jsonFile)
        jsonFile.close()
    except Exception as e:
        logger.exception(e)
    logger.info(f"Loading configuration:{configPath} successfully")
    return config
