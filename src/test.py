from logging import config
from globalvarHelper import globalvarHelper
from common import *
from wecombasic import *
from sendMsgHelper import *

def main():
    app_config = getConfig(globalvarHelper().getGlobalVar('APP_CONF_PATH'), 'r')
    corpid = app_config['corpid']
    corpsecret = app_config['corpsecret']
    agentid = app_config['agentid']

    #Get access_token
    access_token = getAccessToken(corpid,corpsecret)

    #Send message
    msgContent = "一个测试消息。\n测试链接：<a href=\"https://azure0.xxy233.xyz\">点一下这个链接</a>"
    receivers_userid = app_config['remind_Users']['receivers_userid']
    msgjson = getSimpleMessageJson(agentid,msgContent,receivers_userid)
    sendMessage(access_token,msgjson)
   
if __name__ == "__main__":
    main()