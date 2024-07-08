'''
Author: 吕 锐中 1286565437@qq.com
Date: 2024-01-02 22:29:00
LastEditors: 吕 锐中 1286565437@qq.com
LastEditTime: 2024-01-07 13:31:49
FilePath: \kechengsheji\vue01\public\sql.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!/usr/bin/python3

import pymysql
import json
import os

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='testdb')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# SQL 查询语句
sql = "SELECT * FROM course"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 执行查询
query = ('SELECT * FROM useraccounts')
cursor.execute(query)

# 将查询结果转换为 JSON 格式
rows = [x for x in cursor]
result = []
for row in rows:
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    result.append(d)

filename = "useraccounts.json"
path = os.getcwd() + "\\" + "hello-world"+"\\"+"public"+"\\"+"json"+"\\"+filename

# 将 JSON 数据保存到文件中
with open(path, 'w') as f:
    json.dump(result, f)

# 执行查询
query = ('SELECT * FROM productdetails')
cursor.execute(query)

# 将查询结果转换为 JSON 格式
rows = [x for x in cursor]
result2 = []
for row in rows:
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    result2.append(d)

filename = "productdetails.json"
path = os.getcwd() + "\\" + "hello-world"+"\\"+"public"+"\\"+"json"+"\\"+filename

# 将 JSON 数据保存到文件中
with open(path, 'w') as f:
    json.dump(result2, f)


# 关闭数据库连接

db.close()