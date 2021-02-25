#use:globalvarHelper().getGlobalVar('KEY')

class globalvarHelper:
    __DICT_GOLVAR = {
        'APP_CONF_PATH' : '.\\conf\\appconf.json',
        'LOG_CONF_PATH' : '.\\conf\\log.conf',
        'LOG_CONF_DIR' : '.\\log'
    }
  
    def getGlobalVar(self,key):
        return self.__DICT_GOLVAR[key]