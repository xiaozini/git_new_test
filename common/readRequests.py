from common.readExcel import ReadExcel
import requests
from common.read_token import get_token
import json

class SendRequests():

    def sendRequests(self,s,apiData):
        url = apiData['url']
        method = apiData['method']
        header = apiData['header']
        body = apiData['body']
        if "token" in body:
            #替换Token值
            # 获取token 并放在yaml上
            body['token']=get_token()


        res = s.request(url = url,json = json.loads(body),headers=json.loads(header),method = method,verify=False)
        resultJson = res.json()
        print('返回数据为111:%s' % resultJson)
        return resultJson