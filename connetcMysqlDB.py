import pymysql

# 连接数据库

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "database": "91dapin"
}

# db = pymysql.Connect('127.0.0.1', 'root', 'root', '91dapin')
##当*和**符号出现在函数定义的参数中时，表示任意数目参数收集。
# *arg表示任意多个无名参数，类型为tuple;**kwargs表示关键字参数，为dict，使用时需将*arg放在**kwargs之前
db = pymysql.Connect(**config)

# 使用cursor()方法创建一个游标对象
# cursor = db.cursor() # 数据以元组方式返回
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 数据以字段形式返回

# 使用execute()方法执行SQL语句
cursor.execute("SELECT * FROM invoic_admins")

# cursor.execute("DELETE FROM invoic_admins WHERE ID =26")
# db.commit()  #insert delete update时必须要提交数据

# fetchone():获取下一行数据，第一次为首行；fetchall():获取所有行数据源 fetchmany(4):获取下4行数据
data = cursor.fetchone()

# 打印获取到的数据
print(data)

# 关闭游标和数据库的连接
cursor.close()
db.close()
