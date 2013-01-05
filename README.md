whatsyourip
===========

Simplest possible WSGI app for whats my IP type service.

I got sick of picking a service then having it disappear from under me, 
so I took an hour and wrote one as a WSGI app.  To make it as easy 
as possible to use, it doesn't require anything beyond Python 2.6 (for JSON
support) and a WSGI server, such as the wsgiref server that also comes with 
Python.  It uses no external libraries or frameworks.

To run the wsgiref example:

    python ./wsgiref_test.py

To run in gunicorn:

    gunicorn -b 0.0.0.0:8000 -w 4 whatsmyip:application