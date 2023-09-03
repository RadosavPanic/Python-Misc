import smtplib
import base64

filename = "test.txt"

# read file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)

sender = "me@fromdomain.net"
receiver = "amrood.admin@gmail.com"
marker = "AUNIQUEMARKER"
body = """This is a test email to send an attachment"""

part1 = """From: From Person <me@fromdomain.net>
To: To Person <amrood.admin@gmail.com>
Subject: Sending Attachment
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s""" % (marker, marker)

part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s""" % (body, marker)

part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s
%s
--%s""" % (filename, filename, encodedcontent, marker)

message = part1 + part2 + part3

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receiver, message)
    print("E-mail successfully sent")
except smtplib.SMTPException:
    print("Error: unable to send e-mail")

