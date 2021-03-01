from globalvarHelper import MaterialType, globalvarHelper
import json
import logging
import logging.config

logging.config.fileConfig(globalvarHelper().getGlobalVar('LOG_CONF_PATH'))
logger = logging.getLogger('sendMsgHelper')

def getTextMessageJson(agentid,content,touser=None,toparty=None,totag=None,safe=0,\
    enable_id_trans=0,enable_duplicate_check=0,duplicate_check_interval=1800):
    message_dic = {\
        'touser':touser,\
        'toparty':toparty,\
        'totag':totag,\
        'msgtype':'text',\
        'agentid':agentid,\
        'text':{\
            'content':content\
        },\
        'safe':safe,\
        'enable_id_trans':enable_id_trans,\
        'enable_duplicate_check':enable_duplicate_check,\
        'duplicate_check_interval':duplicate_check_interval,\
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json

def getImageMessageJson(agentid,media_id,touser=None,toparty=None,totag=None,safe=0,\
    enable_duplicate_check=0,duplicate_check_interval=1800):
    message_dic = {\
        'touser':touser,\
        'toparty':toparty,\
        'totag':totag,\
        'msgtype':MaterialType.image,\
        'agentid':agentid,\
        'image':{\
            'media_id':media_id\
        },\
        'safe':safe,\
        'enable_duplicate_check':enable_duplicate_check,\
        'duplicate_check_interval':duplicate_check_interval,\
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json