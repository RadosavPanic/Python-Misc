import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue('subject'):
    subject = form.getvalue('subject')
else:
    subject = "Not set"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Radio Form CGI val</title>")
print("</head>")
print("<body>")
print("<h2>Selected subject is: %s</h2>" % subject)
print("</body>")
print("</html>")


