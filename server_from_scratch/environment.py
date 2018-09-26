# Python's bundled WSGI server
from wsgiref.simple_server import make_server
from wsgiref.util import guess_scheme
import json
import inventory

# set the encoding
encoding = 'utf-8'
# set port
port = 8000
#create object of MyApp
my_obj = inventory.MyApp()

def application_(environ, start_response):

    try:
        response_text = my_obj.dispatch(environ)
    except Exception as exc:
        print(exc)
        status = "500 Internal Server Error"
        response_text = ''
    status = '200 OK' # HTTP Status
    headers = [('Content-type', 'text/plain; charset=' + encoding)] # HTTP Headers
    start_response(status, headers)

    return [response_text.encode('utf-8')]


httpd = make_server('', port, application_)
print(f"Serving on port {port}...")

# Serve until process is killed
httpd.serve_forever()


'''
# To kill process server running
> lsof -i tcp:8000
pyhon   pid#...null=

>kill -9 9037


1- Make server and run it ( whihch we made above)




2- Create your API
We will cerate simple API for inventory
 {"socks": 1: "shirt": 2}


 Goal:          ->  Http method used

 Check Inventory --> get all items or get specific item
 Add to invent. - > Post or patch
Delete from inventory -> delete
'''
