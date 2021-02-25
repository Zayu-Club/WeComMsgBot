from globalvarHelper import globalvarHelper
from common import *

def main():
    APP_CONF_PATH = globalvarHelper().getGlobalVar('APP_CONF_PATH')
    CONFIG_FILE = getConfig(APP_CONF_PATH, 'r')
    print(CONFIG_FILE)
   
   

if __name__ == "__main__":
    main()
