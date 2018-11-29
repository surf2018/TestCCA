'''
Created on May 24, 2016

@author: Soffee
'''
#-*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
class BasePage(object):
    #åˆ�å§‹åŒ–driver,url,titleç­‰
    def __init__(self,selenium_driver,base_url):
        self.driver = selenium_driver
        self.base_url=base_url
    def _open(self,url,length,width):
        self.driver.get(url)
        time.sleep(1)
        if(length=='' and width==''):
            self.driver.maximize_window()
        elif(length!=0 and width!=0):
            self.driver.set_window_size(length, width)
        # self.driver.maximize_window()
        time.sleep(0.5)
#         assert self.on_page(pagetitle),"open page fail %s" %url
#     def on_page(self,pagetitle):
#         return pagetitle in self.driver.title
    def find_element(self,*loc):
        try:
            # WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print ("Can't find",loc," element in page")
    def find_elements(self,*loc):
        try:
            return self.driver.find_elements(*loc)
        except:
            print ("Can't find",loc," element in page")      
    def switch_frame(self,loc):
        self.driver.switch_to_frame(loc)
    def switch_back(self):
        self.driver.switch_to_default_content()
    def open(self,length,width):
        self._open(self.base_url,length,width)
    def changeZoom(self,zoom):
        if(zoom!=''):
            js="document.body.style.zoom="+str(zoom)+"%"
            self.execute_script(js)
    def execute_script(self,src):
        self.driver.execute_script(src)
    def send_keys(self,loc,value,clear_first=True, click_first=True):
        try:
            loc=getattr(self,"_%s" % loc)
            print (loc)
            self.find_element(*loc).click()
            time.sleep(0.5)
            self.find_element(*loc).clear()
            time.sleep(0.5)
            self.find_element(*loc).send_keys(value)
            time.sleep(0.5)
        except:
            print("Can't find %s element in page" % (self,loc))
    def switch_alert(self):
        a=self.driver.switch_to_alert()
        prompt=a.text
        a.accept()
        return prompt
    
    def switch_alert_JS(self):
        self.driver.execute_script("window.confirm = function(msg) { return true; }")
        
    def quit_page(self):
        self.driver.quit()
    def getCurUrl(self):
        return self.driver.current_url()
    def moveover(self,*loc):
        chain=ActionChains(self.driver)
        implement=self.driver.find_element(*loc)
        chain.move_to_element(implement).perform()
    def click_ENTER(self):
        chain=ActionChains(self.driver)
        chain.key_down(Keys.ENTER).perform()
    def getTitle(self):
        Title=self.driver.title
        return Title
    def saveScreenToFile(self,path,fileName):
        filepath=path+fileName+'.png'
        self.driver.save_screenshot(filepath)
        time.sleep(0.5)