#!/usr/bin/python
# -*- coding: UTF-8 -*-


'''
获取在校生信息，05-17
jwc.seu.edu.cn
18.5.12
辣鸡土豆
'''
def getstu(num):
    import urllib
    import urllib.request
    url="http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action?queryAcademicYear=18-19-1&queryStudentId=" + str(num)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    data=data.decode("utf8")
    #print(data)

    import re
    pat=r'''<td width="20." align="left">(.*?)</td>'''
    ans=re.findall(pat,data)
    #print(type(ans))
    ans[0]=ans[0][3:len(ans[0])]
    ans[1] = ans[1][3:len(ans[1])]
    ans[2] = ans[2][3:len(ans[2])]
    ans[3] = ans[3][5:len(ans[3])]
    ans[4] = ans[4][3:len(ans[4])]
    print(ans[0],ans[1],ans[2],ans[3],ans[4])
    return ans

def savestudent(ans):
    import pymysql

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "密码", "库名",charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    #sql="insert into seustudents2 value('%s','%s','%s','%s');" % (ans[4],ans[0],ans[2],ans[3])
    sql="update seustudents2 set studentname='%s',college='%s',number='%s' where card='%s';" % (ans[4],ans[0],ans[2],ans[3])
    print(sql)
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)

    db.commit()
    # 关闭数据库连接
    db.close()

#下面的范围根据需要写
for num in range(213170636,213174500):
    try:
        ans=getstu(num)
        savestudent(ans)
    except:
        pass
