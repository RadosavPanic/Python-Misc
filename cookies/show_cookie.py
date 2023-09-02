import http.cookies
import os

print("Content-type: text/plain\n")

try:
    cookie = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print("John = " + cookie["Elvis"].value)
except(http.cookies.CookieError, KeyError):
    print("John cookie not set!")
