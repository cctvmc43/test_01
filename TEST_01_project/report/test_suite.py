import unittest
from login.test_case.test_001 import login_test
from common import HTMLTestRunnerCN

if __name__ == '__main__':
    #定义一个单元测试容器
    testunit = unittest.TestSuite()
    #将测试用例导入至容器中
    testunit.addTest(login_test("test_001A"))
    testunit.addTest(login_test("test_002A"))
    reportPath = "E:\\TEST_01_project\\report\\"+"Report.html"
    #open 目录下的文件，并进行写入
    fp = open(reportPath,"wb")
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='V端测试报告',
        description='用例执行情况：',
        # tester="Findyou"
    )
    runner.run(testunit)
    fp.close()