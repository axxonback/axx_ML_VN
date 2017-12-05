# encoding: UTF-8
#Copy To vnpy\vn.trader\
import sys
import ctypes
import time
from vtEngine import MainEngine
from eventEngine import *
#----------------------------------------------------------------------
class LogPrint(object):
    def __init__(self, mainEngine):
        self.eventEngine = mainEngine.eventEngine
        # 注册事件监听
        self.registerEvent()
    def onEventLog(self, event):
        log = event.dict_['data']
        print ':'.join(['Get EventLog__',log.logTime, log.logContent])
    def registerEvent(self):
        """注册事件监听"""
        self.eventEngine.register(EVENT_LOG, self.onEventLog)
        self.eventEngine.register(EVENT_CTA_LOG, self.onEventLog)
        
        
    
def run(gateway,strategyName):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    """主程序入口"""
    mainEngine = MainEngine()
    logPrint=LogPrint(mainEngine)
    print "connect MongoDB.........."
    mainEngine.dbConnect()
    time.sleep(5)
    
    print "connet %s.........."%gateway
    mainEngine.connect(gateway)
    time.sleep(5)
    
    print "start strategy %s......."%strategyName
    mainEngine.ctaEngine.loadSetting()
    mainEngine.ctaEngine.initStrategy(strategyName)
    mainEngine.ctaEngine.startStrategy(strategyName)


    
if __name__ == '__main__':
    
     run("CTP","double ema")
    
