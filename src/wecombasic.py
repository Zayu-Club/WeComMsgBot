from globalvarHelper import globalvarHelper,MaterialType
from requests_toolbelt import MultipartEncoder
import json
import logging
import logging.config
import requests

logging.config.fileConfig(globalvarHelper().getGlobalVar('LOG_CONF_PATH'))
logger = logging.getLogger('wecombasic')

def getAccessToken(corpid,corpsecret):
    try:
        reponse = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',\
            params={'corpid': corpid,'corpsecret': corpsecret})
        #logger.debug(reponse.json())
        access_token = reponse.json()['access_token']
        logger.info(f"Get Access_Token successful : {access_token}")
        return access_token
    except Exception as e:
        logger.error('Request access token failed.')

#未完成的方法！
def getMaterialMediaId(access_token,materialType:MaterialType,fileName):
    #materialFile = {'file' : open(filePath, 'r')}
    materialFile = MultipartEncoder(
        fields={'materialFile0': ('file', open(fileName, 'rb'), 'multipart/form-data')},
    )
    reponse = requests.post('https://qyapi.weixin.qq.com/cgi-bin/media/upload',\
        params = {'access_token': access_token,\
            'type': 'image'},\
        data = materialFile,\
        headers = {'Content-Type': 'image; multipart/form-data; boundary=-------------------------acebdf13572468',\
            'Content-Disposition':'form-data; name="image";filename="aaaaaaa"; filelength=10',\
            'Content-Type': 'application/octet-stream'
            }
        )
    logger.debug(reponse.text)
    return reponse.text
    
def sendMessage(access_token,msg_json):
    try:
        reponse = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send',\
            params={'access_token': access_token},\
            data=msg_json)
        logger.info("Message sent successfully.")
    except Exception as e:
        logger.error('Failed to send message.')