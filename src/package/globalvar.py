from enum import Enum

DICT_GOLVAR = {
    'APP_CONF_PATH': './/conf//appconf.json',
    'LOG_CONF_PATH': './/conf//log.conf',
    'LOG_CONF_DIR': './/conf//log'
}


class MaterialType(Enum):
    image = 'image'
    voice = 'voice'
    video = 'video'
    file = 'file'
