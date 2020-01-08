from common.readExcel import ReadExcel
import os
import unittest,requests
from ruamel import yaml
from ddt import ddt,data
from common.readRequests import SendRequests

path = os.path.join(os.path.dirname(os.getcwd()),'resource','test_api1.xlsx')
testcast = ReadExcel.readExcel(path,'login')

#获取根目录
rootpath = os.path.abspath(os.path.dirname(__file__)).split('')[0]
print('根目录为:%s'%rootpath)
ypath = os.path.join(rootpath,'common','token.yaml')

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
        if re.status_code == 200:
            if true_status == 1:
                #获取token 并放在yaml上
                login_token = re['data']['token']
                print('login_token:%s'%login_token)
                with open(ypath,'w',encoding='utf-8') as f:
                    yaml.dump(login_token,f,Dumper=yaml.RoundTripDumper)

        print('ddt中数据为:%s'%true_status)
        expect_result = data['expect_result'].split(':')[1]
        self.assertEqual(true_status,int(expect_result),'实际返回数据为:%s'%re)


# if __name__ == '__main__':
#     unittest.main()