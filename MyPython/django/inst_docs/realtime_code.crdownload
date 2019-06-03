#Bottle is a fast, simple and lightweight WSGI(Web Server Gateway Interface) micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the Python Standard Library.

from bottle import route, run, HTTPResponse, request

emp_det = {'ename':'KUMAR', 'eid':343}

@route('/get_emp_details', method="GET")
def get_emp_det():
    return HTTPResponse(body=emp_det)

@route('/create_emp', method="POST")
def create_emp():
    d = request.json
    emp_det.update(d)
    return HTTPResponse(emp_det)

@route('/update_emp', method="PUT")
def update_emp():
    d = request.json
    emp_det.update(d)
    return HTTPResponse(' {0} RECORD UPDATED SUCCESSFULLY'.format(d))

@route('/delete_emp', method="DELETE")
def delete_emp():
    d = request.json
    k = list(d.keys())
    k = k[0]
    del emp_det[k]
    return HTTPResponse(' Deleted {0} record SUCCESSFULLY'.format(k))

run(host='localhost', port=8822, debug=False, reloader=True)


'''
## To get all emp table details with HTTP method GET
http://localhost:8822/get_emp_details


## json req data and url for create emp with HTTP method POST
http://localhost:8822/create_emp
req_data = {"sal":"50000"}

## json req data and url for update emp with HTTP method PUT
http://localhost:8822/update_emp
{"ename":"RAMU"}

## json req data and url for delete emp with HTTP method DELETE
http://localhost:8822/delete_emp
{"ename":"RAMU"}
'''

