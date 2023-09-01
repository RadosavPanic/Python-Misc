import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "Not entered"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Textarea Form CGI val</title>")
print("</head>")
print("<body>")
print("<h2>Entered text content is: %s</h2>" % text_content)
print("</body>")
print("</html>")