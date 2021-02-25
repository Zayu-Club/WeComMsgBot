from globalvarHelper import globalvarHelper
import json
import os
import logging
import logging.config

if(not os.path.exists(".\\log")):
    try:
        os.mkdir(".\\log")
    except Exception as e:
        print(e)

logging.config.fileConfig(globalvarHelper().getGlobalVar('LOG_CONF_PATH'))
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