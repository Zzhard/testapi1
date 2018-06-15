import  os
import  logging
#数据库配置
host="192.168.59.128"
user="root1"
passwd="123456"
port=3306
db="test"
#邮件配置
sender="1178145190@qq.com" #发送邮件方
receiver="1178145190@qq.com"#接收方，多个收件人就以逗号隔开
emailusername="1178145190@qq.com" #登录邮箱的用户名
emailpassword="zxuhgazkykxwiedj"
server="smtp.qq.com"#smtp服务

#获取项目目录
basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(basedir)

#数据目录
datapath=os.path.join(basedir,"data")
#print(datapath)

#报告目录
reportpath=os.path.join(basedir,"report")
#print(reportpath)

#日志配置
#获取日志存放地址
logdir=os.path.join(basedir,'log')
logpath=os.path.join(logdir,'log.txt')
print(logpath)

logger = logging.getLogger('接口自动化测试')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(logpath, encoding='utf-8')
datafmt = "%Y-%m-%d %H:%M:%S"
fm = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt=datafmt)
fh.setFormatter(fm)
logger.addHandler(fh)

logging.getLogger("requests").setLevel(logging.WARNING)

if __name__ == '__main__':
    logger.info("this is test")