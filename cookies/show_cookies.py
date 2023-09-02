import os
import cgitb

cgitb.enable()

print('Content-type: text/plain\r\n\r\n')

if "HTTP-COOKIE" in os.environ:
    print(os.environ["HTTP-COOKIE"].split(";"))
    for cookie in os.environ["HTTP-COOKIE"].split(";"):
        (key, value) = str(cookie).split("=")
        print(key.lstrip(), "-->", value)
else:
    print("HTTP_COOKIE not set!")

