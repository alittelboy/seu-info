#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''''
爬取全部的srtp学分，需要先获取学号列表
需要连接seu
18.5.12
辣鸡土豆
'''

import urllib.request

def gethtml(num):
    url = "http://10.1.30.98:8080/srtp2/USerPages/SRTP/Report3.aspx"
    values = {
        "Code":str(num)
    }
    data = urllib.parse.urlencode(values).encode(encoding='UTF8')
    request = urllib.request.Request(url,data)
    response = urllib.request.urlopen(request)
    data = response.read()
    data = data.decode('utf-8')
    #print(data)
    return data

def getsrtp(num):
    try:
        a = num
        html = gethtml(a)
        heji = '''<td align="center" nowrap>合计</td>\r\n'''
        a = html.find(heji)
        #print(a)
        import re
        zongfen = '''<td align=\"center\" nowrap(.*?)>(\\d+.\\d)</td>'''
        t = html[a:len(html)]
        ans = re.search(zongfen, t, re.M | re.I)
        return ans.groups()[1]
    except:
        return "0.0"

def getnumber():
    import pymysql
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "密码", "库名")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT number FROM mypcqq.srtp2 where number > '19315111' order by number;")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    '''
        for ele in data:
        print(ele[0])
    '''

    # 关闭数据库连接
    db.close()
    return data

def save(num,point):
    import pymysql
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "密码", "库名")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SET SQL_SAFE_UPDATES = 0;")
    sql="update srtp2 set srtppoint="+point+" where number='"+num+"';"
    print(sql)
    cursor.execute(sql)
    db.commit()
    # 关闭数据库连接
    db.close()



numbers=getnumber()
for ele in numbers:
    num=ele[0]
    point=getsrtp(num)
    save(num,point)



'''
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
'''