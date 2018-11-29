'''
Created on Aug 26, 2016

@author: Soffee
'''

import requests
import json
import time
class DestinationInterfack():
    def __init__(self):
        # self.sid=sid
        self.path="http://10.12.23.124:8081/cc/receiver/queryRlist"
        self.datas={"pageSize":"15","pageNum":"1","scope":"1","condition":"","favorite":"0","deviceSearchStatus":{"offline":"true","online":"true","live":"true","sort":"false"}}
        # self.headers={'Cookie':'SID='+self.sid}
        self.headers = {"Content-Type": "application/json"}

    def queryRlist(self):
        response = requests.post(self.path, data=json.dumps(self.datas), headers=self.headers)
        Rlist={}
        RInfoList=json.loads(response.text)
        RinfoArray=RInfoList['data']['resultList']
        print(RinfoArray)
        count=len(RinfoArray)
        for Rinfo in RinfoArray:
            rpid=Rinfo['peerId']
            rname=Rinfo['name']
            rip=Rinfo['ip']
            fav=Rinfo['favorite']
            livedpid=Rinfo['livePeerId']
            livePname=Rinfo['livePeerName']
        Rlist[rpid]=[rname,rip,fav,livedpid,livePname]
        return Rlist

if __name__=="__main__":
    RInfo=DestinationInterfack()
    # AllRinfo,num=RInfo.getAllR()
    # setBitrate=5120
    # setDelay=2000
    # rpid='013da140f80b9a14'
    result=RInfo.queryRlist()
    # result=RInfo.getFeatureList(rpid,"soffeeshu@1.com")
    print ("result:"+str(result))

#{'013da140f80b9a14': ['R_4', '013da140f80b9a140012fcc9832a3801', ''], 'f16ff006b4cbf191': ['R_f191', '9f1eb1e9a8f36007', '6007'], '2fe7d7ac8b02bb6d': ['R_BB6D', '6e0922a5b8dc66ad', 'TVU_T66AD'], '71d376f34919cd8f': ['TVU_RCD8F', 'ef479062099e56bf0000000000000002', 'TVU_R56BF_SDI'], '137ab0df62633b45': ['TVU_R3B45', '7e2b6269c1d97866', '7866']}
