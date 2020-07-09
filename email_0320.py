# -*-coding:utf-8-*-

def email(p,text,subject):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText(text,'plain','utf-8')
    msg['From'] = formataddr(['胡杨','jyhu9303@163.com'])
    msg['To'] = formataddr('胡杨','jyhu9303@163.com')
    msg['Subject'] = subject

    server = smtplib.SMTP('smtp.163.com',25)
    server.login('jyhu9303@163.com','xiaohubishen1991')
    server.sendmail('jyhu9303@163.com',[p, ],msg.as_string())
    server.quit()

email('jyhu9303@163.com','i love python')