import smtplib
from email.mime.text import MIMEText
from email.header import Header

import monitorfile
 
def send_email(name):
    # 邮件内容
    subject = 'export-finished'
    body = 'export-finished'
    
    # 构建邮件
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '2785089588@qq.com'
    if name == 'oyj':
        msg['To'] = 'ouyujie@insta360.com'
    elif name == 'lxx':
        msg['To'] = 'liuxiaoxue@insta360.com'
    elif name == 'zhj':
        msg['To'] = 'zhaohanjie@insta360.com'
    elif name == 'hxj':
        msg['To'] = 'hexiaojuan@insta360.com'
    elif name == 'wgy':
        msg['To'] = 'weiguye@insta360.com'
    elif name == 'zzc':
        msg['To'] = 'zhangzechao@insta360.com'
    elif name == 'cyx':
        msg['To'] = 'caiyunxuan@insta360.com'
    
    # 发送邮件
    smtp_server = 'smtp.qq.com'
    smtp_port = 587
    sender_email = '2785089588@qq.com'
    password = 'uueyqlthaqumdgge' #在QQ邮箱设置里拿到的码
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, [msg['To']], msg.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败:', str(e))

def export_send(name):
    if monitorfile.monitor_file(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log"):
        send_email(name)

if __name__ == '__main__':
    # send_email('oyj')
    export_send('oyj')