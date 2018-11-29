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
class LoginP(BasePage):
    username_loc=(By.ID,"username")
    password_loc=(By.ID,"password")
    signin_loc=(By.ID,"sign-in")
    # logfail_loc=(By.ID,"LoginFailText")
    # emailAlert_loc=(By.ID,"emailAlert")
    # validateCode_loc=(By.CSS_SELECTOR,"input#validationCode")
    def input_username(self,username):
        self.find_element(*self.username_loc).clear()
        time.sleep(0.5)
        self.find_element(*self.username_loc).send_keys(username)
        time.sleep(0.5)
    def input_password(self,password):
        self.find_element(*self.password_loc).clear()
        time.sleep(0.5)
        self.find_element(*self.password_loc).send_keys(password)
        time.sleep(0.5)
    def input_validate(self):
#         self.find_element(*self.validateCode_loc).click()
#         time.sleep(0.5)
        validcode='tvuq'
        self.find_element(*self.validateCode_loc).send_keys(validcode)
        time.sleep(0.5)
    def click_sigin(self):
        self.find_element(*self.signin_loc).click()
        time.sleep(1)
    def getLogFailText(self):
        return self.find_element(*self.logfail_loc).text
    def getemailAlert(self):
        return self.find_element(*self.emailAlert_loc).text
    def closePage(self):
        self.quit_page()
    def login(self,username,password):
        self.input_username(username)
        time.sleep(0.5)
        self.input_password(password)
        time.sleep(0.5)
        # self.input_validate()
        # time.sleep(0.5)
        self.click_sigin()
        time.sleep(1)
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