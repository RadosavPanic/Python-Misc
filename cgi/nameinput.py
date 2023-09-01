# CGI (Common Gateway Interface)

# !/usr/bin/python
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

print("Content-type:text/html\r\n\r\n")  # MIME string
print("<html>")
print("<head>")
print("<title>Form CGI val</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body>")
print("</html>")


