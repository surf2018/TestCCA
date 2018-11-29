'''
Created on Jun 22, 2016

@author: Soffee
'''
#-*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import time

test_dir='../testcase'
testlist=unittest.defaultTestLoader.discover(test_dir, pattern='test_01*.py', top_level_dir=None)

if __name__=='__main__':
#     for i in testlist:
#         print (i)
#     runner=unittest.TextTestRunner()
#     runner.run(testlist)
    print ('''
        1.running test_01PCSystem.py
        '''
     )
    print ("Starting running TestCase")
    now=time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time())) 
    filename='E:\\test_report\\ccaTestResult_'+now+'.html'
#     filename='c:\\result'+now+'.html'
    fp=open(filename, 'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='CCA_Test_Result',description='Test Result:')
    runner.run(testlist)
    fp.close()
    print("End")