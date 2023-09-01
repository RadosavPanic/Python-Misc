import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue('maths'):
    math_flag = "ON"
else:
    math_flag = "OFF"

if form.getvalue('physics'):
    physics_flag = "ON"
else:
    physics_flag = "OFF"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Checkbox Form CGI val</title>")
print("</head>")
print("<body>")
print("<h2>CheckBox maths is: %s</h2>" % math_flag)
print("<h2>CheckBox physics is: %s" % physics_flag)
print("</body>")
print("</html>")

