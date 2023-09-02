import http.cookies
import datetime
import random
import cgitb

cgitb.enable()

expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = http.cookies.SimpleCookie()

cookie["session"] = str(random.randint(1, 1000000000))
cookie["session"]["domain"] = ".localhost"
cookie["session"]["path"] = "/cgi-bin/"
cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S GMT")

print("Set-Cookie: John=Connor; expires=Wednesday, 06-Aug-2023 23:50:30 GMT;")
print("Set-Cookie: Peter=Garrison; expires=Wednesday, 06-Aug-2023 23:50:30 GMT;")
print(cookie.output())
print("Content-type: text/plain\r\n\r\n")
print("Cookie of http.cookies.SimpleCookie:\n" + cookie.output())
