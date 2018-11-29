'''
Created on May 24, 2016

@author: Soffee
'''
#-*- coding: utf-8 -*-

from .Base import BasePage
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import threading
class BaiduP(BasePage):
    searchText_loc=(By.ID,"kw")
    searchButton_loc=(By.ID,"su")
    def input_text(self,workds):
        self.find_element(*self.searchText_loc).clear()
        time.sleep(1)
        self.find_element(*self.searchText_loc).send_keys(workds)
        time.sleep(1)
    def click_search(self):
        self.find_element(*self.searchButton_loc).click()
        time.sleep(1)
    def closePage(self):
        self.quit_page()
# if __name__=="__main__":
# def open_threading():
#     baseurl="http://cc.tvunetworks.com/tvucc"
#     driver=webdriver.Chrome()
# #    driver = webdriver.PhantomJS()
#     testb = LoginP(driver, baseurl)
#     testb.open()
#     time.sleep(1)
#     testb.input_username('soffeeshu@1.com')
#     testb.input_password('123456')
#     testb.input_validate()
#     testb.click_sigin()
# if __name__ == "__main__":
#     th = []
#     for i in range(1,1000):
#         t = threading.Thread(target=open_threading)
#         th.append(t)
#     print ('======================')
#     for i in th:
#         i.start()
#         time.sleep(5)  # 设置开启的时间间隔
#         print('==========='+str(i)+'===========')
#     for i in th:
#         i.join()
# for i in range(1,50):
#     driver=webdriver.Chrome()
#     baseurl="http://cc.tvunetworks.com/tvucc"
#     testb=LoginP(driver,baseurl)
#     testb.open()
#     time.sleep(1)
#     testb.input_username('soffeeshu@1.com')
#     testb.input_password('123456')
#     testb.input_validate()
#     testb.click_sigin()
#