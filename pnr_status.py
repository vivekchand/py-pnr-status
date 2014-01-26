import json
import requests
import time

pnr_no = sys.argv[1]
resp = requests.get('http://pnrapi.alagu.net/api/v1.0/pnr/%s'%pnr_no)
resp = json.loads(resp.content)
status = resp['status']
data = resp['data']
if status == "INVALID":
    print 'Invalid PNR Number!'

while not data['chart_prepared']:
    if status == 'OK':
        time.sleep(1)
    resp = requests.get('http://pnrapi.alagu.net/api/v1.0/pnr/%s'%pnr_no)
    resp = json.loads(resp.content)
    status = resp['status']
    data = resp['data']

print 'PNR No.:' +data['pnr_number']

passengers = data['passenger']
i = 1
for passenger in passengers:
    print 'Passenger %s' % i
    print 'Current Status:' + passenger['status']
    i+=1

