import requests

## To get all emp table details
res = requests.get('http://localhost:8822/get_emp_details')
print('\n response code is :', res.status_code)
print('\n EMP details are :', res.json())


## To create new emp record
# r = requests.post('http://localhost:8822/create_emp', json={"EID":555})
# r_data = r.json()
# eid = r_data['EID']
# assert eid == 55 , ' HTTP POST methos is not working'
#if eid != 555 : raise AssertionError(' HTTP POST methos is not working')
# print('\n POST is :', type(r_data))


## To Update emp 
#r = requests.put('http://localhost:8822/update_emp', json={"EID":999})
#print('\n update is :', r.text)


## To Delete emp 
# r = requests.delete('http://localhost:8822/delete_emp', json={"EID":"SRIRAM"})
# print('\n response code is :', r.status_code)
# assert r.status_code == 200 , ' Not able to process request'
# print('\n Deleted is :', r)
