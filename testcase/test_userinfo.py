from common.readExcel import ReadExcel
import os
import unittest,requests

from ddt import ddt,data
from common.readRequests import SendRequests

path = os.path.join(os.path.dirname(os.getcwd()),'resource','test_api1.xlsx')
testcast = ReadExcel.readExcel(path,'userinfo')

@ddt
class DdtTest(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
    def tearDown(self):
        pass

    @data(*testcast)
    def test_api(self,data):

        re = SendRequests().sendRequests(self.s,data)
        true_status = int(re['status'])
        print('ddt中数据为:%s'%true_status)
        expect_result = data['expect_result'].split(':')[1]
        self.assertEqual(true_status,int(expect_result),'实际返回数据为:%s'%re)
