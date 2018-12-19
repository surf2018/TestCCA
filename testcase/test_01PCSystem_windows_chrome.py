'''
Created on May 25, 2016

@author: Soffee
'''
# from src.Login import LoginP
from selenium import webdriver
from src.Destination import DestinationP
from src.model import Logger
from src.Login import LoginP
from src.Base import BasePage
import time
import csv
from ddt import ddt,data,unpack
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
class ccaSystem(unittest.TestCase):
    def setUp(self):
        self.url="http://10.12.128.228/tvudc/"
        # self.url = "http://10.12.22.98/tvudcc/"
        self.path = 'd:\\TVUCC\\PCSystem\\'
        # self.username="3333"
        self.username = "soffeeshu@1.com"
        self.password="123456"
        #浏览器数组
        self.lists=['chrome','safari']
        #video预期结果
        self.expected_vsize = {'height': 292, 'width': 364}
        #rTinfo的框的大小
        self.expect_rTinfoSize = {'height': 168, 'width': 154}
        self.expect_setBitDelaySize = {'height': 171, 'width': 240}
        self.logger = Logger.Logger('test_01System')
    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack
    def test_01checkVideoSize(self,platform,browserName,version,length,width):
        #P匹配所有平台的chrome
        # chromeOpitons = webdriver.ChromeOptions()
        # if(browserName!='safari'):
        filename="test_01checkVideoSize_"+platform+browserName+length+width+".png"
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                           desired_capabilities=desired_capabilities)
            # print("browersName:"+str(browserName)+" version:"+self.driver.capabilities['version'])

            dp=DestinationP(driver,self.url)
            dp.open(length,width)
            time.sleep(1)
            #用户登录
            login=LoginP(driver,self.url)
            login.login(self.username,self.password)
            #勾选All
            dp.checkAll("check")
            print("check All")
            self.logger.printlog("check All")
            time.sleep(1)
            #去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            dp.saveScreenToFile(self.path,filename)
            time.sleep(1)
            # #check video size
            # result = dp.checkVideoSize(self.expected_vsize)
            # if(result==1):
            #     self.logger.printlog("视频和预期结果匹配")
            #     print("视频和预期结果匹配")
            result=1
        except Exception  as e:
            print("Raeason",e)
        finally:
            dp.quit_page()
        self.assertEqual(result, 1),"test_01checkVideoSize fail"
    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack
    def test_02checkPagination(self,platform,browserName,version,length,width):
        result_pag=0
        filename = "test_02checkPagination_" + platform + browserName + length + width + ".png"
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                      desired_capabilities=desired_capabilities)
            # print("browersName:"+str(browserName)+" version:"+self.driver.capabilities['version'])

            dp = DestinationP(driver, self.url)
            dp.open(length, width)
            time.sleep(1)
            # 用户登录
            login = LoginP(driver, self.url)
            login.login(self.username,self.password)
            #勾选All
            dp.checkAll("check")
            print("check All")
            self.logger.printlog("check All")
            time.sleep(1)
            # 去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            #翻页
            flag=dp.pagiation()
            if(flag==0):
                result_pag=0
            else:
                result_pag=1
            time.sleep(3)
            dp.saveScreenToFile(self.path, filename)
            time.sleep(1)
            # check video size
            # result = dp.checkVideoSize(self.expected_vsize)
            # if(result==1):
            #     self.logger.printlog("视频和预期结果匹配")
            #     print("视频和预期结果匹配")
        except Exception as e:
            print("Reason:",e)
        finally:
            dp.quit_page()
        self.assertEqual(result_pag, 1), "test_02checkPagination fail"
    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack
    def test_03lastPageCheck(self,platform,browserName,version,length,width):
        filename = "test_03lastPage" + platform + browserName + length + width + ".png"
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                      desired_capabilities=desired_capabilities)
            dp = DestinationP(driver, self.url)
            dp.open(length, width)
            time.sleep(1)
            # 用户登录
            login = LoginP(driver, self.url)
            login.login(self.username,self.password)
            #勾选All
            dp.checkAll("check")
            print("check All")
            self.logger.printlog("check All")
            time.sleep(1)
            # 去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            #翻到最后一页
            result_lastp=dp.jumpToLastPage()
            time.sleep(3)
            dp.saveScreenToFile(self.path, filename)
            time.sleep(1)
            # # check video size
            # result = dp.checkVideoSize(self.expected_vsize)
            # if(result==1):
            #     self.logger.printlog("视频和预期结果匹配")
            #     print("视频和预期结果匹配")
        except Exception as e:
            print("Reason:",e)
        finally:
            dp.quit_page()
        self.assertEqual(result_lastp, 1), "test_03lastPage fail"
    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack

    def test_04checkDynamicSorting(self,platform,browserName,version,length,width):
        filename = "test_04checkDynamicSorting" + platform + browserName + length + width
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                      desired_capabilities=desired_capabilities)
            dp = DestinationP(driver, self.url)
            dp.open(length, width)
            time.sleep(1)
            # 用户登录
            login = LoginP(driver, self.url)
            login.login(self.username,self.password)
            # 勾选All
            dp.checkAll("check")
            print("check All")
            self.logger.printlog("check All")
            time.sleep(1)
            # 去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            # 点击dynamicSorting
            dp.checkDynamicSorting("check")
            time.sleep(2)
            # check video 的排序
            result_sort = dp.checkVideoSort()
            if (result_sort == 1):
                self.logger.printlog("视频排序和预期结果匹配")
                print("视频排序和预期结果匹配")
            #截图
            dp.saveScreenToFile(self.path, filename + "_sortTop.png")
            time.sleep(3)
            #下拉到底部截图
            js="$(window).scrollTop(100000000);"
            dp.execute_script(js)
            time.sleep(3)
            #video sort排序截图
            dp.saveScreenToFile(self.path, filename+"_sortBottom.png")
            time.sleep(1)
            # # check video size
            # result = dp.checkVideoSize(self.expected_vsize)
            # if(result==1):
            #     self.logger.printlog("所有视频和预期结果匹配")
            #     print("所有视频和预期结果匹配")
        except Exception as e:
            print("Reason:",e)
        finally:
            dp.quit_page()
        # self.assertEqual(result, 1), "test_04checkDynamicSorting check videosize fail"
        self.assertEqual(result_sort,1),"test_04checkDynamicSorting check videosort fail"
    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack
    def test_05searchReceiverName(self, platform, browserName, version, length, width):
        searchText="9a14"
        results=1
        filename = "test_06search" + platform + browserName + length + width + ".png"
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                      desired_capabilities=desired_capabilities)
            dp = DestinationP(driver, self.url)
            dp.open(length, width)
            time.sleep(1)
            # 用户登录
            login = LoginP(driver, self.url)
            login.login(self.username,self.password)
            # 勾选All
            dp.checkAll("check")
            print("check All")
            self.logger.printlog("check All")
            time.sleep(1)
            # 去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            # 点击search,search
            dp.searchText(searchText)
            time.sleep(3)
            dp.saveScreenToFile(self.path, filename)
            time.sleep(1)
            # #check video size
            # result = dp.checkVideoSize(self.expected_vsize)
            # if (result == 1):
            #     self.logger.printlog("视频大小和预期结果匹配")
            #     print("视频大小和预期结果匹配")
            #check searchresult
            results=dp.checkReceiverName(searchText)
            if(results==1):
                self.logger.printlog("搜索结果匹配")
                print("搜索结果匹配")
        except Exception as e:
            print("Reason:",e)
        finally:
            dp.quit_page()
        # self.assertEqual(result, 1), "test_05searchReceiverName check videosize fail"
        self.assertEqual(results,1),"test_05searchReceiverName search fail"
    #
    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack
    def test_06checkFavorite(self, platform, browserName, version, length, width):
        opera="check"
        filename = "test_06checkFavorite" + platform + browserName + length + width + ".png"
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                      desired_capabilities=desired_capabilities)
            dp = DestinationP(driver, self.url)
            dp.open(length, width)
            time.sleep(1)
            # 用户登录
            login = LoginP(driver, self.url)
            login.login(self.username,self.password)
            # 勾选All
            dp.checkAll("check")
            print("check All")
            self.logger.printlog("check All")
            time.sleep(1)
            # 去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            # 勾选favorite
            dp.checkFavorite(opera)
            time.sleep(3)
            dp.saveScreenToFile(self.path, filename)
            time.sleep(1)
            #check favorite
            result_fa=dp.checkFavoriteVideo()
            if(result_fa==1):
                self.logger.printlog("视频都为favorite和预期结果匹配")
                print("视频都为favorite和预期结果匹配")
            # #check video size
            # result = dp.checkVideoSize(self.expected_vsize)
            # if (result == 1):
            #     self.logger.printlog("视频大小和预期结果匹配")
            #     print("视频大小和预期结果匹配")
        except Exception as e:
            print("Reason:",e)
        finally:
            dp.quit_page()
        self.assertEqual(result_fa,1),"test_06checkFavorite check vidoe isfavorite fail"
        # self.assertEqual(result, 1), "test_06checkFavorite check videosize fail"

    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack
    def test_07checkRinfoSize(self, platform, browserName, version, length, width):
        filename = "test_07checkRinfoSize" + platform + browserName + length + width + ".png"
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                      desired_capabilities=desired_capabilities)
            dp = DestinationP(driver, self.url)
            dp.open(length, width)
            time.sleep(1)
            # 用户登录
            login = LoginP(driver, self.url)
            login.login(self.username,self.password)
            # 取消勾选All
            dp.checkAll("uncheck")
            self.logger.printlog("uncheck All")
            time.sleep(1)
            # 去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            #勾选live
            result_live=dp.checkLiveReceivers('check')
            print("check liveReceivers")
            # trinfo 框自动弹出and check size
            result_rTinfoSize=dp.checkrTInfoSize(self.expect_rTinfoSize,self.path,filename)
            if (result_rTinfoSize == 1):
                self.logger.printlog("rTinfo大小和预期结果匹配")
                print("rTinfo大小和预期结果匹配")
            # # check video size
            # result = dp.checkVideoSize(self.expected_vsize)
            # if (result == 1):
            #     self.logger.printlog("所有视频大小和预期结果匹配")
            #     print("所有视频大小和预期结果匹配")
        except Exception as e:
            print("Reason:",e)
        finally:
            dp.quit_page()
        self.assertEqual(result_rTinfoSize, 1), "test_07checkRinfoSize check rinfoSIZE fail"
        self.assertEqual(result_live, 1), "test_07checkRinfoSize 不显示live的视频 fail"
        # self.assertEqual(result, 1), "test_07checkRinfoSize check videosize fail"

    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack
    def test_08unfoldRinfo(self, platform, browserName, version, length, width):
        result_unfolderrTinfo=0
        filename = "test_08unfoldRinfo" + platform + browserName + length + width + ".png"
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                      desired_capabilities=desired_capabilities)
            dp = DestinationP(driver, self.url)
            dp.open(length, width)
            time.sleep(1)
            # 用户登录
            login = LoginP(driver, self.url)
            login.login(self.username, self.password)
            # 取消勾选All
            dp.checkAll("uncheck")
            self.logger.printlog("uncheck All")
            time.sleep(1)
            # 去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            # 勾选live
            result_live=dp.checkLiveReceivers('check')
            print("check liveReceivers")
            # trinfo 框自动弹出and check size
            expect_rTinfoSize_unfolder = {'height': 0, 'width': 0}
            result_unfolderrTinfo = dp.unfolderrTInfo(expect_rTinfoSize_unfolder, self.path, filename)
            if (result_unfolderrTinfo == 1):
                self.logger.printlog("收起rTinfo下拉框成功")
                print("收起rTinfo下拉框成功")
            # # check video size
            # result = dp.checkVideoSize(self.expected_vsize)
            # if (result == 1):
            #     self.logger.printlog("所有视频大小和预期结果匹配")
            #     print("所有视频大小和预期结果匹配")
        except Exception as e:
            print("Reason:",e)
        finally:
            dp.quit_page()
        self.assertEqual(result_unfolderrTinfo, 1), "test_08unfoldRinfo unfolder Rinfo fail"
        self.assertEqual(result_live, 1), "test_08unfoldRinfo 勾选live,不显示Liveh视频 fail"
        # self.assertEqual(result, 1), "test_08unfoldRinfo check videosize fail"

    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack
    def test_09checkControlBoard(self,platform, browserName, version, length, width):
        filename = "test_09checkControlBoard" + platform + browserName + length + width + ".png"
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                      desired_capabilities=desired_capabilities)
            dp = DestinationP(driver, self.url)
            dp.open(length, width)
            time.sleep(1)
            # 用户登录
            login = LoginP(driver, self.url)
            login.login(self.username, self.password)
            # 取消勾选All
            dp.checkAll("uncheck")
            self.logger.printlog("uncheck All")
            time.sleep(1)
            # 去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            # 勾选live
            result_live=dp.checkLiveReceivers('check')
            print("check liveReceivers"+str(result_live))
            time.sleep(1)
            # 点击 controldelayBitraty and check size
            result_setBitDelaySize= dp.checkBitDelaySize(self.expect_setBitDelaySize, self.path, filename)
            if (result_setBitDelaySize == 1):
                self.logger.printlog("BitDelaySize大小和预期结果匹配")
                print("BitDelaySize大小和预期结果匹配")
            # # check video size
            # result = dp.checkVideoSize(self.expected_vsize)
            # if (result == 1):
            #     self.logger.printlog("所有视频大小和预期结果匹配")
            #     print("所有视频大小和预期结果匹配")
        except Exception as e:
            print("Reason:",e)
        finally:
            dp.quit_page()
        self.assertEqual(result_setBitDelaySize, 1), "test_09checkControlBoard check videosize fail"
        self.assertEqual(result_live,1),"test_09checkControlBoard 勾选live不显示live的视频 fail"
        # self.assertEqual(result, 1),"test_08checkControlBoard checkvideosize fail"

    @data(*get_data("test_data_windows_chrome.csv"))
    @unpack
    def test_10checkLiveVideo(self, platform, browserName, version, length, width):
        filename = "test_10checkLiveVideo" + platform + browserName + length + width + ".png"
        result=1
        desired_capabilities = {"platform": platform,
                                "browserName": browserName,
                                "version": version,
                                "javascriptEnabled": True
                                }
        try:
            driver = webdriver.Remote(command_executor='http://10.12.128.233:4444/wd/hub',
                                      desired_capabilities=desired_capabilities)
            dp = DestinationP(driver, self.url)
            dp.open(length, width)
            time.sleep(1)
            # 用户登录
            login = LoginP(driver, self.url)
            login.login(self.username, self.password)
            # 取消勾选All
            dp.checkAll("uncheck")
            self.logger.printlog("uncheck All")
            time.sleep(1)
            # 去掉勾选Sort and Favorite
            dp.checkDynamicSorting("uncheck")
            time.sleep(1)
            dp.checkFavorite('uncheck')
            time.sleep(1)
            # 勾选live
            result_live=dp.checkLiveReceivers('check')
            if(result_live==1):
                print("check liveReceivers")
                time.sleep(1)
                #点击所有视频的个eys图标
                result_eye=dp.clickEyeIcon(self.path,filename)
                time.sleep(1)
                if(result_eye==1):
                    print("点击所有的视频都能打开")
                else:
                    print("点击所有的视频都不能打开")
        except Exception as e:
            print(e)
            result=0
        finally:
            dp.quit_page()
        self.assertEqual(result, 1), "test_10checkLiveVideo fail"
        self.assertEqual(result_live,1),"test_10checkLiveVideo 勾选live不显示live的视频 fail"
        self.assertEqual(result_eye, 1), "test_10checkLiveVideo 点击eye,不能显示所视频"


    def tearDown(self):
        print("test end")
if __name__=="__main__":
    unittest.main()