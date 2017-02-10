from uuid import uuid4
import MySQLdb,random, string
chars = string.digits + string.letters
def uuidkey(num):# 使用uuid方法得到随机值
    id_list = [str(uuid4()) for i in range(num)]
    return id_list
def randomkey(num):# 使用random随机取数据值
    id_list = ["".join(random.sample(chars, 20)) for i in range(num)]
    return id_list
    
def create_table_put_keys(id_list,table):#将获得的随机值存入mysql
    conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='lyyc12345',
        db ='test',
        )
    cur = conn.cursor()
    cur.execute("drop table if exists %s" % table)    #若存在table表则删除
    cur.execute("create table %s(id int, coupon char(40))" % table)    #创建数据表
    temp = 1
    for i in id_list:    #将id_list里边的数据插入到mysql中
        cur.execute("insert into %s values('%d','%s')" %(table,temp,i))
        temp=temp+1
    cur.close()    #关闭游标
    conn.commit()    #提交数据
    conn.close()    #关闭数据库连接
def main():
    create_table_put_keys(uuidkey(200),'uuidtable')
    create_table_put_keys(randomkey(200),'randomtable')
if __name__ == '__main__':
    main()
