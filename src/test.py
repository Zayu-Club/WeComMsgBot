from pkg import common,globalvar,wecombasic,msgJsonHelper

def main():
    app_config = common.getConfig(globalvar.DICT_GOLVAR['APP_CONF_PATH'],'r')
    corpid = app_config['corpid']
    corpsecret = app_config['corpsecret']
    agentid = app_config['agentid']

    # Get access_token
    access_token = wecombasic.getAccessToken(corpid, corpsecret)

    # Send message
    msgContent = "一个测试消息。\n测试链接：<a href=\"https://azure.xxy-yeah.xyz\">点一下这个链接</a>"
    receivers_userid = app_config['remind_Users']['receivers_userid']
    msgjson = msgJsonHelper.setTextMessageJson(
        agentid, msgContent, receivers_userid)
    wecombasic.sendMessage(access_token, msgjson)

if __name__ == "__main__":
    main()