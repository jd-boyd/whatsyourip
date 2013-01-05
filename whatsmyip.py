import json

def application(environ, start_response):
    #print environ.keys()
    #for k,v in environ.iteritems():
    #    print k, ":", v
    #print environ['REMOTE_ADDR']
    #print environ['PATH_INFO']

    if environ['PATH_INFO'] == "/":
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return "Your IP is: %s\n" % environ['REMOTE_ADDR']

    if environ['PATH_INFO'].startswith("/json"):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return json.dumps({"ip": environ['REMOTE_ADDR']})

    if environ['PATH_INFO'].startswith("/text"):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return environ['REMOTE_ADDR']

