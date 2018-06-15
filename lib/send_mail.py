import  smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import  MIMEMultipart
from config import config

def send_mail(title,msg):
    #发件人
    sender=config.sender
    receiver=config.receiver
    server=config.server
    title=title
    message=msg
    username=config.emailusername
    password=config.emailpassword
    msg=MIMEText(message)
    msg["Subject"]=title
    msg["From"]=sender
    msg["To"]=receiver
    #建立连接
    s=smtplib.SMTP_SSL(server)
    #r认证
    s.login(username,password)
    #发送邮件
    s.sendmail(sender,receiver.split(','),msg.as_string())
    s.quit()
#发送测试报告
def send_mail_testreport(title):
    sender=config.sender
    receiver=config.receiver
    server=config.server
    username=config.emailusername
    password=config.emailpassword
    bodyfp=open(config.basedir+'\\report\\'+'Report.html',encoding='utf-8')
    body=bodyfp.read()
    msy_root=MIMEMultipart()
    msg_root = MIMEMultipart()
    msg_root["subject"] = title
    msg_root["from"] = config.sender
    msg_root["to"] = config.receiver
    msg_html = MIMEText(body, "html", 'utf-8')
    msg_root.attach(msg_html)

    att1 = MIMEText(body, 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="Report.html"'
    msg_root.attach(att1)
    # msg_root.attach()

    s = smtplib.SMTP_SSL(server)
    # 认证
    s.login(username, password)
    # 发送邮件
    s.sendmail(sender, receiver.split(','), msg_root.as_string())
    s.quit()
if __name__ == '__main__':
    send_mail_testreport('test')

