from globalvarHelper import globalvarHelper
import common
import logging
import logging.config

logging.config.fileConfig(globalvarHelper().getGlobalVar('LOG_CONF_PATH'))
logger = logging.getLogger('common')

