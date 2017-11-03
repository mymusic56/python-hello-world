import requests
import json

"""
http://mp.weixin.qq.com/s/rhXCVituAvgymV8X28i5Lw
"""
url = "http://xcy.qm.com/HeadPortrait/index";
res = requests.post(
    url,
    data={
        "key": "combo",
        "action": "sysInfo",
        "platform": "android",
        "version": "1.0",
        "channel": "test"
    }
)

response = {}
response["status_code"] = res.status_code
response["reason"] = res.reason
response["url"] = res.url
response["headers"] = res.headers
content = res.content
#print(response)
print(content)
print("--------------------------------------")

#打印headers
# for name,value in res.headers.items():
#     print("%s:%s" % (name,value))
# print("--------------------------------------")


#以json格式传输
payload = {"key": "combo", "action": "sysInfo", "platform": "android", "version": "1.0", "channel": "test" }
json_res = requests.post(url, json=payload)
print(json_res.content)
requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
requests.put(url)
requests.delete(url)
requests.options(url)
requests.head(url)