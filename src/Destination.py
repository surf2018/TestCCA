'''
Created on Aug 24, 2016

@author: Soffee
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.model.Logger import Logger
# from smodule import getStatusFromMem
from selenium.webdriver.common.action_chains import *
from .Base import BasePage
import time
import json
class DestinationP(BasePage):
    log=Logger("DestinationLog")
    CheckBoxSelect_All_loc=(By.CSS_SELECTOR,"span.checkBoxSelect input")
    pageNumber_loc=(By.CSS_SELECTOR,"span#totalPageNum")
    paginationAllow_loc=(By.CSS_SELECTOR,"div.search_item.page span.iconfont.point")
    curpage_loc=(By.CSS_SELECTOR,"div.search_item.page input.cur_page")
    dynamicSort_loc=(By.CSS_SELECTOR,"div.search_item.dynamic input")
    favorite_loc=(By.CSS_SELECTOR,"div.search_item.favorite input")
    searchText_loc=(By.CSS_SELECTOR,"input.form-control.mr-sm-2.searchInput")
    videoBox_loc=(By.CSS_SELECTOR,"div.col-lg-1-5.col-md-1-5.col-xs-1.story-item.video_box")
    pageText_loc=(By.CSS_SELECTOR,"input.cur_page")
    videoStatus_loc=(By.TAG_NAME,"div")
    search_button_loc=(By.CSS_SELECTOR,"i.iconfont.search_icon")
    searchReceiverR_loc=(By.CSS_SELECTOR,"div.text-left.story-name span")
    favoriteVideos_loc=(By.CSS_SELECTOR,"div.story-favorite i")
    story_bg_loc=(By.CSS_SELECTOR,"div.story-bg>i")
    rTinfo_loc=(By.CSS_SELECTOR,"div.rTInfo")
    controlBoard_loc=(By.CSS_SELECTOR,"i.iconfont.control-board.point")
    setBitDelayBoard_loc=(By.CSS_SELECTOR,"div.setting_bit.bit_show")
    def checkBitDelaySize(self,expect_setBitDelaySize,path,filename):
        videoes=self.find_elements(*self.videoBox_loc)
        count=0
        result=1
        for video in videoes:
            video.find_element(*self.controlBoard_loc).click()
            time.sleep(2)
            #check size
            setBitDelayObject=video.find_element(*self.setBitDelayBoard_loc)
            size=setBitDelayObject.size
            if(size['height']==expect_setBitDelaySize['height'] and size['width']==expect_setBitDelaySize['width']):
                print("第" + str(count) + "个视频+setBitDelayBoard size:" + str(size)+"符合预期结果")
                self.log.printlog("第" + str(count) + "个视频+setBitDelayBoard size:" + str(size)+"符合预期结果")
            else:
                print("第" + str(count) + "个视频+setBitDelayBoard size:" + str(size)+"不符合预期结果")
                self.log.printlog("第" + str(count) + "个视频+setBitDelayBoard size:" + str(size)+"不符合预期结果")
                result=0
                break
        # save filename
        self.saveScreenToFile(path, filename)
        return result
    def clickStorybg(self):
        self.find_element(*self.story_bg_loc).click()
        time.sleep(1)
    def checkrTInfoSize(self,expect_rTinfoSize,path,filename):
        videoes=self.find_elements(*self.videoBox_loc)
        count=0
        result=1
        for video in videoes:
            video.find_element(*self.story_bg_loc).click()
            time.sleep(2)
            #check size
            rTinfoObject=video.find_element(*self.rTinfo_loc)
            size=rTinfoObject.size
            if(size['height']==expect_rTinfoSize['height'] and size['width']==expect_rTinfoSize['width']):
                print("第" + str(count) + "个视频+rTinfoSize size:" + str(size)+"符合预期结果")
                self.log.printlog("第" + str(count) + "个视频+rTinfoSize size:" + str(size)+"符合预期结果")
            else:
                print("第" + str(count) + "个视频+rTinfoSize size:" + str(size)+"不符合预期结果")
                self.log.printlog("第" + str(count) + "个视频+rTinfoSize size:" + str(size)+"不符合预期结果")
                result=0
                break
        # save filename
        self.saveScreenToFile(path, filename)
        return result
    def checkAll(self,oper):
        #check All是否被勾选
        attr=self.find_element(*self.CheckBoxSelect_All_loc).get_attribute('checkbox')
        if(oper=="check"):
            if(attr=='true'):
                self.log.printlog("All已被勾选,不做任何操作")
                print("All已被勾选,不做任何操作")
            else:
                # js="('span.checkBoxSelect input').prop(\"checked\",true)"
                # self.execute_script(js)
                self.find_element(*self.CheckBoxSelect_All_loc).click()
                time.sleep(1)
                print("All 被勾选")
                self.log.printlog("All 被勾选")
        elif(oper=="uncheck"):
            if(attr=='true'):
                print("All已被勾选,取消勾选")
                self.log.printlog("All已被勾选,取消勾选")
                self.find_element(*self.CheckBoxSelect_All_loc).click()
                time.sleep(1)
            else:
                # js="('span.checkBoxSelect input').prop(\"checked\",true)"
                # self.execute_script(js)
                print("All 没有被勾选，不做任何操作")
                self.log.printlog("ll 没有被勾选，不做任何操作")
    def checkVideoSize(self,expected_vsize):
        result=0
        videos=self.find_elements(*self.videoBox_loc)
        count=0
        for video in videos:
            vsize=video.size
            print(video.get_attribute("class"))
            print("video size:"+str(vsize)+" 预期结果:"+str(expected_vsize))
            self.log.printlog("video size:"+str(vsize)+"预期结果:"+str(expected_vsize))
            if(vsize['height']==expected_vsize['height'] and vsize['width']==expected_vsize['width']):
                result=1
                print("视频和预期一样")
                self.log.printlog("视频和预期一样")
            else:
                print("视频"+str(count)+"和预期结果不一样")
                self.log.printlog("视频"+str(count)+"和预期结果不一样")
                result=0
                break
            count=count+1
        return result

    def pagiation(self):
        try:
            numbers=self.find_element(*self.pageNumber_loc).text
            print("一共有"+numbers+"页")
            #获取当前页
            cur_num = self.find_element(*self.curpage_loc).get_attribute("value")
            print("现在是第" +cur_num + "页")
            if(cur_num<numbers):
                #点击往后翻页pagiation
                self.find_elements(*self.paginationAllow_loc)[1].click()
            elif(cur_num==numbers):
                #点击往前翻页
                self.find_elements(*self.paginationAllow_loc)[0].click()
            time.sleep(1)
            return 1
        except:
            print("pagination找不到页码")
            return 0

    def jumpToLastPage(self):
        numbers=self.find_element(*self.pageNumber_loc).text
        #获取当前页
        cur_num = self.find_element(*self.curpage_loc).text
        if(cur_num<numbers):
            #跳转到最后一页
            self.find_element(*self.pageText_loc).clear()
            self.find_element(*self.pageText_loc).send_keys(numbers)
            time.sleep(0.5)
            self.find_element(*self.pageText_loc).send_keys(Keys.ENTER)
            time.sleep(1)
        elif(cur_num==numbers):
            print("已经是最后一页,不跳转")
            self.log.printlog("已经是最后一页,不跳转")

    def checkDynamicSorting(self,oper):
        #check是否勾选Dynamic Sorting
        attr=self.find_element(*self.dynamicSort_loc).get_attribute('checkbox')
        if(oper=="check"):
            if(attr=='true'):
                print("已勾选dynamic sorting,不做任何操作")
                self.log.printlog("已勾选dynamic sorting,不做任何操作")
            else:
                self.find_element(*self.dynamicSort_loc).click()
                time.sleep(1)
                print("dynamic sorting被勾选")
                self.log.printlog("dynamic sorting被勾选")
        else:
            if(attr=='true'):
                print("已勾选dynamic sorting,取消勾选")
                self.log.printlog("已勾选dynamic sorting,取消勾选")

            else:
                self.find_element(*self.dynamicSort_loc).click()
                time.sleep(1)
                print("dynamic sorting被勾选")
                self.log.printlog("dynamic sorting被勾选")
    def checkVideoSort(self):
        result=0
        statusArray=[]
        videos=self.find_elements(*self.videoBox_loc)
        for video in videos:
            vstatus=video.find_elements(*self.videoStatus_loc)[-1].text
            statusArray.append(vstatus)
        onlineLast=str(statusArray).rfind('Online')
        liveFirst=str(statusArray).find('Live')
        liveLast=str(statusArray).rfind('Live')
        offlineFirst=str(statusArray).find('Offline')
        if(onlineLast<liveFirst and liveLast<offlineFirst):
            result=1
        else:
            result=0
        return result
    def checkFavorite(self,opera):
        #check Favorite是否被勾选
        if(opera=="check"):
            attr=self.find_element(*self.favorite_loc).get_attribute("checkbox")
            if(attr=="true"):
                print("favorite被勾选,不任何操作")
            else:
                self.find_element(*self.favorite_loc).click()
                time.sleep(1)
                print("favorite被勾选")
        elif(opera=="uncheck"):
            attr=self.find_element(*self.favorite_loc).get_attribute("checkbox")
            if(attr=="true"):
                print("favorite被勾选,取消勾选")
                self.find_element(*self.favorite_loc).click()
                time.sleep(1)
            else:
                print("favorite没被勾选，不做任何操作")
    #检查videobox是否都为favorite的
    def checkFavoriteVideo(self):
        result=1
        fvideos = self.find_elements(*self.favoriteVideos_loc)
        count = 0
        for video in fvideos:
            # check favorite是否被激活
            if("favorateActive" not in video.get_attribute('class')):
              print("视频："+str(count)+"不是favorite video,结果错误")
              self.log.printlog("视频：" + str(count) + "不是favorite video,结果错误")
              result=0
              break
            count = count + 1
        return result
    def searchText(self,searchText):
        self.find_element(*self.searchText_loc).clear()
        time.sleep(0.5)
        self.find_element(*self.searchText_loc).send_keys(searchText)
        time.sleep(1)
        self.find_element(*self.search_button_loc).click()
        time.sleep(2)

    def getReceiverName(self):
        RnameArray=self.find_elements(*self.searchReceiverR_loc).text
        return RnameArray
    # def getThumbnail(self,RpidArray):
    #     for rpid in RpidArray:


