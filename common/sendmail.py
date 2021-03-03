#!/usr/bin/python3
# Author:Maweiqing
# -*- coding: utf-8 -*-
# @Time     :2021/2/22 10:30
# @Software: PyCharm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from common.conf import read_conf
from common.logger import logger
def sendmail():
    # 设置smtplib所需的参数
    # 下面的发件人，收件人是用于邮件传输的。
    logger("准备发送邮件","info")
    date_lits = read_conf(sec="Email",config_path="../common/config_test.conf")
    print(date_lits)
    smtpserver = 'smtp.qq.com'
    username = date_lits[0][1]
    password = date_lits[1][1]
    sender = date_lits[2][1]
    #设置收件人
    receiver = date_lits[3][1].split("\n")
    subject = date_lits[4][1]

    # 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
    # subject = '中文标题'
    # subject=Header(subject, 'utf-8').encode()

    # 构造邮件对象MIMEMultipart对象
    # 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = date_lits[6][1]
    # msg['To'] = 'XXX@126.com'
    # 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
    msg['To'] = ";".join(receiver)
    # msg['Date']='2012-3-16'

    # 构造文字内容
    text =  date_lits[5][1]
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    # 构造图片链接
    # sendimagefile = open(r'D:\pythontest\testimage.png', 'rb').read()
    # image = MIMEImage(sendimagefile)
    # image.add_header('Content-ID', '<image1>')
    # image["Content-Disposition"] = 'attachment; filename="testimage.png"'
    # msg.attach(image)

    # 构造html
    # 发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
    # html = """
    # <html>
    #   <head></head>
    #   <body>
    #     <p>Hi!<br>
    #        How are you?<br>
    #        Here is the <a href="http://www.baidu.com">link</a> you wanted.<br>
    #     </p>
    #   </body>
    # </html>
    # """
    # text_html = MIMEText(html, 'html', 'utf-8')
    # text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
    # msg.attach(text_html)

    # 构造附件
    sendfile = open(r'../logs/2021-02-22.log', 'rb').read()
    text_att = MIMEText(sendfile, 'base64', 'utf-8')
    text_att["Content-Type"] = 'application/octet-stream'
    # 以下附件可以重命名成aaa.txt
    text_att["Content-Disposition"] = 'attachment; filename="2021-02-22.log"'
    # 另一种实现方式
    # text_att.add_header('Content-Disposition', 'attachment', filename='2021-02-22.log')
    # 以下中文测试不ok
    # text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
    msg.attach(text_att)

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    # set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    # smtp.set_debuglevel(1)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    logger("发送邮件完成发送人员为："+str(receiver),"info")
if __name__ == "__main__":
    sendmail()