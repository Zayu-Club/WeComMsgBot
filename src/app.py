from logging import config
from os import pipe
from common import getConfig

def main():
    app_config = getConfig(globalvarHelper().getGlobalVar('APP_CONF_PATH'), 'r')
    corpid = app_config['corpid']
    corpsecret = app_config['corpsecret']
    agentid = app_config['agentid']

    #Get access_token
    access_token = getAccessToken(corpid,corpsecret)

    #Send message
    #msgContent = "一个测试消息。\n测试链接：<a href=\"azure.xxy-yeah.xyz\">点一下这个链接</a>"
    #receivers_userid = app_config['remind_Users']['receivers_userid']
    #msgjson = getTextMessageJson(agentid,msgContent,receivers_userid)
    #sendMessage(access_token,msgjson)

    #Upload Tempfile
    receivers_userid = app_config['remind_Users']['receivers_userid']
    media_id = getMaterialMediaId(access_token,MaterialType.image,'.\\source\\test_Image0.png')
    #Send message
    msgjson = getMpnewsMessageJson(agentid,'这是标题',media_id,'哈哈哈哈快来点我鸭','https://azure.xxy-yeah.xyz','作者咕咕咕','描述信息',\
        touser=receivers_userid)
    sendMessage(access_token,msgjson)
   
if __name__ == "__main__":
    main()