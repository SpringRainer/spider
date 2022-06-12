import requests
import re

class SpiderData:
    def __init__(self):
        print("开始爬取数据")

    # 获取币种表
    def getTTy(self):
        json_01 = requests.post("http://price.mofcom.gov.cn/datamofcom/front/financial/dynamic/optionList")
        print(json_01.text)
        return json_01.text

    # 获取到价格变化表
    def getPriceList(self):
        json_01 = requests.post("http://price.mofcom.gov.cn/datamofcom/front/index/echart/data/query")
        # print(json_01.text)
        return json_01.text

    def getStockCertificate(self):
        json_01 = requests.get("http://quotes.money.163.com/trade/lsjysj_zhishu_000001.html?year=2021&season=3")
        return json_01.text