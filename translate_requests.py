import json
from urllib.parse import urlencode
import requests
content=0
while True:
    content=input("请输入需要翻译的内容:")
    if content!='quit':
        data={
            'from':'zh',
            'to':'en',
            'query':content,
            'transtype':'translang',
            'simple_means_flag':3
        }
        url="http://fanyi.baidu.com/v2transapi"
        data=urlencode(data)
        response=requests.get(url,data)
        html=response.text
        target=json.loads(html)
        tgt=target['trans_result']['data'][0]['dst']
        print("翻译的结果是：%s"% tgt)
    else:
        break
