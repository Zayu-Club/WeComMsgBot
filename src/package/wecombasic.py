import json
import logging
import logging.config
import requests
import globalvar

logging.config.fileConfig(globalvar.DICT_GOLVAR['LOG_CONF_PATH'])
logger = logging.getLogger('wecombasic')


def getAccessToken(corpid, corpsecret):
    try:
        reponse = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                               params={'corpid': corpid, 'corpsecret': corpsecret})
        logger.debug(reponse.json())
        access_token = reponse.json()['access_token']
        logger.info(f"Get Access_Token successful : {access_token}")
        return access_token
    except Exception as e:
        logger.error('Request access token failed.')
        logger.exception(e)


def getMaterialMediaId(access_token, materialType: globalvar.MaterialType, fileName):
    try:
        files = {'media': open(fileName, 'rb')}
    except Exception as e:
        logger.error("Failed to open material.")
    try:
        reponse = requests.post('https://qyapi.weixin.qq.com/cgi-bin/media/upload',
                                params={'access_token': access_token,
                                        'type': materialType.name},
                                files=files,
                                )
        logger.debug(reponse.text)
        return json.loads(reponse.text).get('media_id')
    except Exception as e:
        logger.exception('Failed to get media_id.')


def sendMessage(access_token, msg_json):
    try:
        reponse = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send',
                                params={'access_token': access_token},
                                data=msg_json)
        logger.debug(reponse.text)
        logger.info("Message sent successfully.")
    except Exception as e:
        logger.error('Failed to send message.')
