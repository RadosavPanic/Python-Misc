import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue('dropdown'):
    subject = form.getvalue('dropdown')
else:
    subject = "Not entered"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Dropdown Form CGI val</title>")
print("</head>")
print("<body>")
print("<h2>Selected subject is: %s</h2>" % subject)
print("</body>")
print("</html>")