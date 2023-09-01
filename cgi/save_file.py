import cgi
import cgitb
import os

cgitb.enable()
form = cgi.FieldStorage()

fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    fp = open(fn, 'wb')
    fp.write(fileitem.file.read())
    fp.close()
    message = f"The file {fn} was uploaded successfully"
else:
    message = "No file was uploaded"

print("Content-Type: text/html\r\n\r\n <html> <body> <p>%s</p> </body></html> " % message)

