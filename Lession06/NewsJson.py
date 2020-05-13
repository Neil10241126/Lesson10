import json
import requests

news_list = []   # 將資料整理至list中
url = 'http://oldpaper.g0v.ronny.tw/index/json?fbclid=IwAR1zip-1_wLBrsZ2p9RfiAjm-WeFaxb8UyI4nA-uXOhK6Q3Wkgn7D_Zukow'
data = json.loads(requests.get(url).text)

for d in data.get('data'):
    dict = {'title':d.get('title'), 'headlines':d.get('headlines')}
    news_list.append(dict)
#1.
# print(news_list)

#2.
#for news in news_list:
    #for head in news['headlines']:
        #if '譚德塞' in head[1]:
            #print(head)
#3.
#file = open('news3.txt', 'a')
#for news in news_list:
    #for head in news['headlines']:
        #if '譚德塞' in head[1]:
            #print(head)
            #file.writelines(head)
            #file.write("\n")

#4.
file = open('news4.txt', 'a', encoding='UTF-8')
for news in news_list:
    for head in news['headlines']:
        if '譚德塞' in head[1]:
            print(head)
            file.writelines(head)
            file.write("\n")

# 上課筆記新增
# 口罩 json
# https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json

#各大報頭條 OpenData (json)
#http://oldpaper.g0v.ronny.tw/index/json?fbclid=IwAR1zip-1_wLBrsZ2p9RfiAjm-WeFaxb8UyI4nA-uXOhK6Q3Wkgn7D_Zukow

#桃園 youbike json
#https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json

#口罩
#json
#https: // raw.githubusercontent.com / kiang / pharmacies / master / json / points.json




