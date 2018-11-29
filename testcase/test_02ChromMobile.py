'''
Created on May 25, 2016

@author: Soffee
'''
# from src.Login import LoginP
from selenium import webdriver
from src.testbaidu import BaiduP
from src.Base import BasePage
from src.Destination import DestinationP
from src.Login import LoginP
import time
import csv
from ddt import ddt,data,unpack
from src.model.Logger import Logger
from appium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import selenium.remote.DesiredCapabilities
# base_url="http://cc.tvunetworks.com/tvucc"
# pagetitle="TVU User Service"
# username="admin@tvunetworks.com"
# password="123456"
import unittest
#测试数据
def get_data(file_name):
    # print("file_name"+str(file_name))
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    print(rows)
    return rows

@ddt
class login(unittest.TestCase):
    def setUp(self):
        self.url="http://10.12.23.124:8081/#/"
        self.path = 'd:\\TVUCC\\ChromMobile\\'
        self.username = "soffeeshu@tvu.com"
        self.password = "123456"
        # 浏览器数组
        self.lists = ['chrome', 'safari']
        # video预期结果
        self.expected_vsize = {'height': 292, 'width': 364}
        # rTinfo的框的大小
        self.expect_rTinfoSize = {'height': 162, 'width': 154}
        self.expect_setBitDelaySize = {'height': 171, 'width': 240}
        self.logger = Logger('test_02ChromMobile')
        self.length=''
        self.width=''
        #浏览器数组
        # self.lists=['chrome','safari']
    # '''chrom模拟不同分辨率'''
    @data(*get_data("test_mobile_data.csv"))
    @unpack
    def test_01checkVideoSize(self,deviceName):
        filename = 'test_01checkVideoSize'+deviceName+".jpg"
        # self.logger.printlog("test_01mobile")
        mobile_emulation = {"deviceName": deviceName}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(executable_path="D:\\Python36\\chromedriver_win32\\chromedriver.exe",
                                       desired_capabilities=chrome_options.to_capabilities())
        dp=DestinationP(driver,self.url)
        dp.open(self.length,self.width)
        time.sleep(1)
        #用户登录
        login=LoginP(driver,self.url)
        login.login(self.username,self.password)
        #勾选All
        dp.checkAll("check")
        self.logger.printlog("check All")
        time.sleep(3)
        dp.saveScreenToFile(self.path,filename)
        time.sleep(1)
        #check video size
        result = dp.checkVideoSize(self.expected_vsize)
        if(result==1):
            self.logger.printlog("视频和预期结果匹配")
            print("视频和语气结果匹配")
        dp.quit_page()
        self.assertEqual(result, 1),"test_01checkVideoSize fail"

    @data(*get_data("test_mobile_data.csv"))
    @unpack
    def test_02checkPagination(self,deviceName):
        result = 0
        filename = "test_02checkPagination_" + deviceName + ".png"
        mobile_emulation = {"deviceName": deviceName}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(executable_path="D:\\Python36\\chromedriver_win32\\chromedriver.exe",
                                  desired_capabilities=chrome_options.to_capabilities())
        # print("browersName:"+str(browserName)+" version:"+self.driver.capabilities['version'])

        dp = DestinationP(driver, self.url)
        dp.open(self.length, self.width)
        time.sleep(1)
        # 用户登录
        login = LoginP(driver, self.url)
        login.login(self.username, self.password)
        # 勾选All
        dp.checkAll("check")
        self.logger.printlog("check All")
        time.sleep(1)
        # 翻页
        flag = dp.pagiation()
        if (flag == 0):
            result = 0
        time.sleep(2)
        dp.saveScreenToFile(self.path, filename)
        time.sleep(1)
        # check video size
        result = dp.checkVideoSize(self.expected_vsize)
        self.logger.printlog("视频和语气结果匹配")
        print("视频和语气结果匹配")
        dp.quit_page()
        self.assertEqual(result, 1), "test_02checkPagination fail"

    @data(*get_data("test_mobile_data.csv"))
    @unpack
    def test_03lastPageCheck(self, deviceName):
        filename = "test_03lastPageCheck" + deviceName + ".png"
        mobile_emulation = {"deviceName": deviceName}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(executable_path="D:\\Python36\\chromedriver_win32\\chromedriver.exe",
                                  desired_capabilities=chrome_options.to_capabilities())
        dp = DestinationP(driver, self.url)
        dp.open(self.length, self.width)
        time.sleep(1)
        # 用户登录
        login = LoginP(driver, self.url)
        login.login(self.username, self.password)
        # 勾选All
        dp.checkAll("check")
        self.logger.printlog("check All")
        time.sleep(1)
        # 翻到最后一页
        dp.jumpToLastPage()
        time.sleep(2)
        dp.saveScreenToFile(self.path, filename)
        time.sleep(1)
        # check video size
        result = dp.checkVideoSize(self.expected_vsize)
        if (result == 1):
            self.logger.printlog("视频和预期结果匹配")
            print("视频和预期结果匹配")
        dp.quit_page()
        self.assertEqual(result, 1), "test_03lastPage fail"

    @data(*get_data("test_mobile_data.csv"))
    @unpack
    def test_04checkDynamicSorting(self,deviceName):
        filename = "test_04checkDynamicSorting" + deviceName + ".png"
        mobile_emulation = {"deviceName": deviceName}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(executable_path="D:\\Python36\\chromedriver_win32\\chromedriver.exe",
                                  desired_capabilities=chrome_options.to_capabilities())
        dp = DestinationP(driver, self.url)
        dp.open(self.length, self.width)
        time.sleep(1)
        # 用户登录
        login = LoginP(driver, self.url)
        login.login(self.username, self.password)
        # 勾选All
        dp.checkAll("check")
        self.logger.printlog("check All")
        time.sleep(1)
        # 点击dynamicSorting
        dp.checkDynamicSorting("check")
        time.sleep(2)
        dp.saveScreenToFile(self.path, filename)
        time.sleep(1)
        # check video size
        result = dp.checkVideoSize(self.expected_vsize)
        if (result == 1):
            self.logger.printlog("视频和预期结果匹配")
            print("视频和预期结果匹配")
        result_sort = dp.checkVideoSort()
        dp.saveScreenToFile(self.path, filename + "_sort")
        if (result_sort == 1):
            self.logger.printlog("视频排序和预期结果匹配")
            print("视频排序和预期结果匹配")
        dp.quit_page()
        self.assertEqual(result, 1), "test_04checkDynamicSorting check videosize fail"
        self.assertEqual(result_sort, 1), "test_04checkDynamicSorting check videosort fail"

    @data(*get_data("test_mobile_data.csv"))
    @unpack
    def test_05searchReceiverName(self,deviceName):
        searchText = "Ari"
        filename = "test_05searchReceiverName" + deviceName + ".png"
        mobile_emulation = {"deviceName": deviceName}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(executable_path="D:\\Python36\\chromedriver_win32\\chromedriver.exe",
                                  desired_capabilities=chrome_options.to_capabilities())
        dp = DestinationP(driver, self.url)
        dp.open(self.length, self.width)
        time.sleep(1)
        # 用户登录
        login = LoginP(driver, self.url)
        login.login(self.username, self.password)
        # 勾选All
        dp.checkAll("check")
        self.logger.printlog("check All")
        time.sleep(1)
        # 点击search,search
        dp.searchText(searchText)
        time.sleep(1)
        dp.saveScreenToFile(self.path, filename)
        time.sleep(1)
        # check video size
        result = dp.checkVideoSize(self.expected_vsize)
        if (result == 1):
            self.logger.printlog("视频大小和预期结果匹配")
            print("视频大小和预期结果匹配")
        # check searchresult
        RNames = dp.getReceiverName()
        for rname in RNames:
            if (searchText not in rname):
                results = 0
                break
        if (results == 1):
            self.logger.printlog("搜索结果匹配")
            print("搜索结果匹配")
        dp.quit_page()
        self.assertEqual(result, 1), "test_05searchReceiverName check videosize fail"
        self.assertEqual(results, 1), "test_05searchReceiverName search fail"

    @data(*get_data("test_mobile_data.csv"))
    @unpack
    def test_06checkFavorite(self,deviceName):
        results = 1
        opera = "check"
        filename = "test_06checkFavorite" + deviceName + ".png"
        mobile_emulation = {"deviceName": deviceName}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(executable_path="D:\\Python36\\chromedriver_win32\\chromedriver.exe",
                                  desired_capabilities=chrome_options.to_capabilities())
        dp = DestinationP(driver, self.url)
        dp.open(self.length, self.width)
        time.sleep(1)
        # 用户登录
        login = LoginP(driver, self.url)
        login.login(self.username, self.password)
        # 勾选All
        dp.checkAll("check")
        self.logger.printlog("check All")
        time.sleep(1)
        # 勾选favorite
        dp.checkFavorite(opera)
        time.sleep(2)
        dp.saveScreenToFile(self.path, filename)
        time.sleep(1)
        #check favorite
        result_fa=dp.checkFavoriteVideo()
        if(result_fa==1):
            self.logger.printlog("视频都为favorite和预期结果匹配")
            print("视频都为favorite和预期结果匹配")
        #check video size
        result = dp.checkVideoSize(self.expected_vsize)
        if (result == 1):
            self.logger.printlog("视频大小和预期结果匹配")
            print("视频大小和预期结果匹配")
        dp.quit_page()
        self.assertEqual(result_fa,1),"test_06checkFavorite check vidoe isfavorite fail"
        self.assertEqual(result, 1), "test_06checkFavorite check videosize fail"

    @data(*get_data("test_mobile_data.csv"))
    @unpack
    def test_07checkRinfoSize(self, deviceName):
        filename = "test_07checkRinfoSize" + deviceName + ".png"
        mobile_emulation = {"deviceName": deviceName}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(executable_path="D:\\Python36\\chromedriver_win32\\chromedriver.exe",
                                  desired_capabilities=chrome_options.to_capabilities())
        dp = DestinationP(driver, self.url)
        dp.open(self.length, self.width)
        time.sleep(1)
        # 用户登录
        login = LoginP(driver, self.url)
        login.login(self.username,self.password)
        # 勾选All
        dp.checkAll("check")
        self.logger.printlog("check All")
        time.sleep(1)
        # 点击 trinfo and check size
        result_rTinfoSize=dp.checkrTInfoSize(self.expect_rTinfoSize,self.path,filename)
        if (result_rTinfoSize == 1):
            self.logger.printlog("视频大小和预期结果匹配")
            print("视频大小和预期结果匹配")
        dp.quit_page()
        self.assertEqual(result_rTinfoSize, 1), "test_07checkRinfoSize check videosize fail"
    @data(*get_data("test_mobile_data.csv"))
    @unpack
    def test_08checkControlBoard(self,deviceName):
        filename = "test_07checkRinfoSize" + deviceName + ".png"
        mobile_emulation = {"deviceName": deviceName}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(executable_path="D:\\Python36\\chromedriver_win32\\chromedriver.exe",
                                  desired_capabilities=chrome_options.to_capabilities())
        dp = DestinationP(driver, self.url)
        dp.open(self.length, self.width)
        time.sleep(1)
        # 用户登录
        login = LoginP(driver, self.url)
        login.login(self.username, self.password)
        # 勾选All
        dp.checkAll("check")
        self.logger.printlog("check All")
        time.sleep(1)
        # 点击 controldelayBitraty and check size
        result_setBitDelaySize= dp.checkBitDelaySize(self.expect_setBitDelaySize, self.path, filename)
        if (result_setBitDelaySize == 1):
            self.logger.printlog("视频大小和预期结果匹配")
            print("视频大小和预期结果匹配")
        dp.quit_page()
        self.assertEqual(result_setBitDelaySize, 1), "test_08checkControlBoard check videosize fail"
    def tearDown(self):
        print("test end")
if __name__=="__main__":
    unittest.main()