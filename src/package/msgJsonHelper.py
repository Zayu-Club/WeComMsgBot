import json
import logging
import logging.config
import globalvar

logging.config.fileConfig(globalvar.DICT_GOLVAR['LOG_CONF_PATH'])
logger = logging.getLogger('sendMsgHelper')


def setTextMessageJson(agent_id, content, touser=None, toparty=None, totag=None, safe=0,
                       enable_id_trans=0, enable_duplicate_check=0, duplicate_check_interval=1800):
    message_dic = {
        'touser': touser,
        'toparty': toparty,
        'totag': totag,
        'msgtype': 'text',
        'agentid': agent_id,
        'text': {
            'content': content
        },
        'safe': safe,
        'enable_id_trans': enable_id_trans,
        'enable_duplicate_check': enable_duplicate_check,
        'duplicate_check_interval': duplicate_check_interval,
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json


def setImageMessageJson(agent_id, media_id, touser=None, toparty=None, totag=None, safe=0,
                        enable_duplicate_check=0, duplicate_check_interval=1800):
    message_dic = {
        'touser': touser,
        'toparty': toparty,
        'totag': totag,
        'msgtype': globalvar.MaterialType.image.name,
        'agentid': agent_id,
        'image': {
            'media_id': media_id
        },
        'safe': safe,
        'enable_duplicate_check': enable_duplicate_check,
        'duplicate_check_interval': duplicate_check_interval,
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json


def setVoiceMessageJson(agent_id, media_id, touser=None, toparty=None, totag=None,
                        enable_duplicate_check=0, duplicate_check_interval=1800):
    message_dic = {
        'touser': touser,
        'toparty': toparty,
        'totag': totag,
        'msgtype': globalvar.MaterialType.voice.name,
        'agentid': agent_id,
        'voice': {
            'media_id': media_id
        },
        'enable_duplicate_check': enable_duplicate_check,
        'duplicate_check_interval': duplicate_check_interval,
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json


def setVideoMessageJson(agent_id, media_id, video_title, video_description, touser=None,
                        toparty=None, totag=None, safe=0, enable_duplicate_check=0, duplicate_check_interval=1800):
    message_dic = {
        'touser': touser,
        'toparty': toparty,
        'totag': totag,
        'msgtype': globalvar.MaterialType.video.name,
        'agentid': agent_id,
        'video': {
            'media_id': media_id,
            'title': video_title,
            'description': video_description
        },
        'safe': safe,
        'enable_duplicate_check': enable_duplicate_check,
        'duplicate_check_interval': duplicate_check_interval,
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json


def getFileMessageJson(agent_id, media_id, touser=None, toparty=None, totag=None, safe=0,
                       enable_duplicate_check=0, duplicate_check_interval=1800):
    message_dic = {
        'touser': touser,
        'toparty': toparty,
        'totag': totag,
        'msgtype': globalvar.MaterialType.file.name,
        'agentid': agent_id,
        'file': {
            'media_id': media_id
        },
        'safe': safe,
        'enable_duplicate_check': enable_duplicate_check,
        'duplicate_check_interval': duplicate_check_interval,
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json


def getTextCardMessageJson(agent_id, textcard_title, textcard_description, textcard_url,
                           textcard_btntxt='More', touser=None, toparty=None, totag=None, enable_id_trans=0,
                           enable_duplicate_check=0, duplicate_check_interval=1800):
    message_dic = {
        'touser': touser,
        'toparty': toparty,
        'totag': totag,
        'msgtype': 'textcard',
        'agentid': agent_id,
        'textcard': {
            'title': textcard_title,
            'description': textcard_description,
            'url': textcard_url,
            'btntxt': textcard_btntxt
        },
        'enable_id_trans': enable_id_trans,
        'enable_duplicate_check': enable_duplicate_check,
        'duplicate_check_interval': duplicate_check_interval,
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json


def getMpnewsMessageJson(agent_id, mpnews_title, media_id, mpnews_content, url=None,
                         mpnews_author=None,
                         mpnews_digest=None, touser=None, toparty=None, totag=None,
                         safe=0, enable_id_trans=0, enable_duplicate_check=0, duplicate_check_interval=1800):
    message_dic = {
        'touser': touser,
        'toparty': toparty,
        'totag': totag,
        'msgtype': 'mpnews',
        'agentid': agent_id,
        'mpnews': {
            "articles": [
                {
                    "title": mpnews_title,
                    "thumb_media_id": media_id,
                    "author": mpnews_author,
                    "content_source_url": url,
                    "content": mpnews_content,
                    "digest": mpnews_digest
                }
            ]
        },
        'safe': safe,
        'enable_id_trans': enable_id_trans,
        'enable_duplicate_check': enable_duplicate_check,
        'duplicate_check_interval': duplicate_check_interval,
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json


def getMarkdownMessageJson(agent_id, content, touser=None, toparty=None, totag=None,
                           enable_duplicate_check=0, duplicate_check_interval=1800):
    message_dic = {
        'touser': touser,
        'toparty': toparty,
        'totag': totag,
        'msgtype': 'markdown',
        'agentid': agent_id,
        'text': {
            'content': content
        },
        'enable_duplicate_check': enable_duplicate_check,
        'duplicate_check_interval': duplicate_check_interval,
    }
    message_json = json.dumps(message_dic)
    logger.debug(message_json)
    return message_json
