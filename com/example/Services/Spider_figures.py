import pymysql
from matplotlib import pyplot
import matplotlib
import numpy
matplotlib.rc("font", family='Microsoft YaHei')

class Figures:
    # db_sql = pymysql.connect(host='localhost',database='mysql1',user='root',password='123456')
    # cursor = db_sql.cursor(pymysql.cursors.DictCursor)
    def __init__(self):
        print('可视化工具启动')

    def drawDist(self,list,legend):
        xlist = []
        ylist = []
        for item in list:
            # print(item['time'])
            xlist.append(item['time'])
            ylist.append(float(item['price']))
            # print('类型',type(float(item['price'])))
        pyplot.figure(dpi=300,figsize=(20,10))
        pyplot.title(list[0]['legend'])
        pyplot.xlabel('time',fontsize=20)
        pyplot.ylabel('price',fontsize=20)
        x = xlist
        y = ylist
        pyplot.plot(x,y,'b',lw=2)
        pyplot.plot(x,y,'ro')
        pyplot.xticks(rotation=90)
        pyplot.tick_params(labelsize=12)
        # pyplot.yticks(numpy.arange(418.5,461.25,10))
        pyplot.grid(True)

        # pyplot.show()
        pyplot.savefig('C:/Users/Lenovo/Desktop/statistics/pic-{}.png'.format(legend))
        print(legend+'分析完成')
        pyplot.close()
