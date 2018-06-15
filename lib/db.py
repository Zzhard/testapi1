import pymysql
import logging
from config import config

def get_db_conn():
    db=pymysql.connect(host=config.host,user=config.user,passwd=config.passwd,db=config.db,port=config.port)

    return db

#查询数据方法
def query_db(sql):
    con=get_db_conn()
    cursor=con.cursor()
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
    except:
        print("can not find data")
    cursor.close()
    con.close()
    return data

#增删改数据方法
def change_db(sql):
    con=get_db_conn()
    cursor=con.cursor()
    try:
        cursor.execute(sql)
        logging.info(sql)
        con.commit()
    except Exception as e:
        con.rollback()
        logging.error(e.message)
if __name__ == '__main__':
    sql="show tables"
    print(query_db(sql))
