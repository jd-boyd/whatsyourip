from wsgiref.simple_server import make_server

from whatsyourip import application

httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."

# Respond to requests until process is killed
httpd.serve_forever()
