import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP e-email test

This is a test e-mail message to be sent in HTML format.
<b>This is HTML message</b>
<h1>This is headline.</h1>
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("E-mail successfully sent")
except smtplib.SMTPException:
    print("Error: unable to send e-mail")



