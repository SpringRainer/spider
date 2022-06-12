from com.example.Services.Spider_data import SpiderData
import pymysql
import json
import pandas
import re

from com.example.Services.Spider_figures import Figures

db_mysql = pymysql.connect(host='localhost',database='mysql1',user='root',password='123456')
cursor = db_mysql.cursor(pymysql.cursors.DictCursor)

#建表
def newTableByProperties(tablename,properties):
    try:
        sql_start = 'create table '+tablename+'('
        sql_inner = ''
        sql_end = ')'
        cursor.execute('drop table if exists '+tablename)

        for index in range(len(properties)):
            if(index < len(properties)-1):
                sql_inner += properties[index]+' varchar(20),'
            else:
                sql_inner += properties[index]+' varchar(20)'
        print(sql_start+sql_inner+sql_end)
        cursor.execute(sql_start+sql_inner+sql_end)
        print('建表成功')
    except:
        print('建表失败')

# 持久化
def durableDataToMysql(dictList,tablename,price_type):
    try:
        sql_start = 'insert into '+tablename+' values '
        value = ''
        sql_end = ''

        if (price_type == 'xjb_3'):
            for item in dictList['list']:
                value += '(\''+dictList['legend'][0]+'\',\''+item[price_type]+'\',\''+item['time']+'\'),'
            # print('新加坡三号')

        if (price_type == 'rb_3'):
            for item in dictList['list']:
                value += '(\''+dictList['legend'][1]+'\',\''+item[price_type]+'\',\''+item['time']+'\'),'
            # print('日本三号')

        if (price_type == 'tb_3'):
            for item in dictList['list']:
                value += '(\''+dictList['legend'][2]+'\',\''+item[price_type]+'\',\''+item['time']+'\'),'
            # print('泰国三号')

        if (price_type == 'qian'):
            for item in dictList['list']:
                value += '(\''+dictList['legend'][0]+'\',\''+item[price_type]+'\',\''+item['time']+'\'),'
            # print('铅')

        if (price_type == 'niu'):
            for item in dictList['list']:
                value += '(\''+dictList['legend'][1]+'\',\''+item[price_type]+'\',\''+item['time']+'\'),'
            # print('铝')

        if (price_type == 'xin'):
            for item in dictList['list']:
                value += '(\''+dictList['legend'][2]+'\',\''+item[price_type]+'\',\''+item['time']+'\'),'
            # print('锌')

        if (price_type == 'zz_price'):
            for item in dictList['list']:
                value += '(\''+dictList['legend'][0]+'\',\''+item[price_type]+'\',\''+item['time']+'\'),'
            # print('郑州')

        if (price_type == 'ny_price'):
            for item in dictList['list']:
                value += '(\''+dictList['legend'][1]+'\',\''+item[price_type]+'\',\''+item['time']+'\'),'
            # print('纽约')

        if (price_type == 'price'):
            for item in dictList['list']:
                value += '(\''+dictList['legend'][0]+'\',\''+item[price_type]+'\',\''+item['time']+'\'),'
            # print(dictList['legend'][0])

        value = value.strip(',')
        cursor.execute(sql_start+value+sql_end)
        db_mysql.commit()
        print('持久化完成')
        print(sql_start+value+sql_end)
    except:
        db_mysql.rollback()
        print('持久化失败')

def queryDataResult(tablename,legend):
    sql_start = 'select t.* from '+tablename+' t where t.legend = '+'\''+legend+'\''
    print(sql_start)
    cursor.execute(sql_start)
    result = cursor.fetchall()
    # print(result)
    return result

def queryLegend():
    sqlstart = 'select distinct legend from pricelist'
    cursor.execute(sqlstart)
    result = cursor.fetchall()
    return result

# 启动方法
if __name__ == '__main__':
    # spiderData = SpiderData()
    # json_01 = spiderData.getPriceList()
    # dictList = json.loads(json_01)
    # print(dictList)
    #
    # # properties = ['legend','price','time']
    # # newTableByProperties(tablename='pricelist',properties=properties)
    # #
    # #
    # for item in dictList:
    #     # print(dictList[item])
    #     print(type(item))
    #     if (item == 'trxj'):
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='xjb_3')
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='rb_3')
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='tb_3')
    #
    #     if (item == 'jsjg'):
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='qian')
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='niu')
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='xin')
    #
    #     if (item == 'mh'):
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='zz_price')
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='ny_price')
    #
    #     if (item == 'zjgxm'):
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='price')
    #
    #     if (item == 'bltyy'):
    #         durableDataToMysql(dictList=dictList[item],tablename='pricelist',price_type='price')

    # figure = Figures()
    # result = queryLegend()
    # print(result)
    # for item in result:
    #     print(item['legend'])
    #     pricelist = queryDataResult(tablename='pricelist',legend=item['legend'])
    #     print(pricelist)
    #     figure.drawDist(pricelist,legend=item['legend'])
    spider = SpiderData()
    result = spider.getStockCertificate()
    print(result)


