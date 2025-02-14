import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart

import monitorfile
import checklog
import zipfile
import os
 
def zip_dir(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标文件夹路径前缀
        fpath = path.replace(dirpath,'')
 
        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()

def send_email(name,export_time,zipfile):
    # 邮件内容
    subject = 'export-finished'
    #正文为export_time
    body = str(export_time)
    
    # 构建邮件
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
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
    else:
        msg['To'] = name + '@insta360.com'

    att1 = open(zipfile, 'rb')
    part = MIMEBase('application', 'zip')
    part.set_payload(att1.read())
    att1.close()
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=zipfile)
    msg.attach(part)

    
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
        print('邮件发送成功')
    os.remove(zipfile)

def export_send(name,expecttimes):
    path = r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log"
    if monitorfile.monitorfile(path,expecttimes):
        export_time = checklog.check(path)
        dir_list = os.listdir(path)
        dir_time = [os.path.getmtime(os.path.join(path, dir)) for dir in dir_list]
        newest_dir = dir_list[dir_time.index(max(dir_time))]
        zip_dir(os.path.join(path, newest_dir),os.path.join(path, newest_dir)+'.zip')
        send_email(name,export_time,os.path.join(path, newest_dir)+'.zip')

if __name__ == '__main__':
    # send_email('oyj',1)
    name = str(input('输入姓名：'))
    expecttimes = int(input('输入预期导出次数：'))
    export_send(name,expecttimes)