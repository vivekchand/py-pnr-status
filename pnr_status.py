import sys
import json
import requests
import time
default_retry_interval = 10*60 #10 min

def get_pnr_status(argv):
    if len(argv) < 2:
        print 'Usage: python pnr_status.py <pnr-no> [retry interval in min]'
        return

    if len(argv) == 3:
        retry_interval = int(argv[2])*60
    else:
        retry_interval = default_retry_interval

    pnr_no = argv[1]
    resp = requests.get('http://pnrapi.alagu.net/api/v1.0/pnr/%s'%pnr_no)
    resp = json.loads(resp.content)
    status = resp['status']
    data = resp['data']
    if data == {} or status == "INVALID":
        print 'Invalid PNR Number!'
        return

    def check_if_passengers_cnf(passengers):
        for passenger in passengers:
            if passenger['status'] != 'CNF':
                return False
        return True

    def print_current_status(passengers):
        i = 1
        for passenger in passengers:
            print 'Passenger %s ' % i
            print 'Current Status: ' + passenger['status']
            i+=1
    
    while not data['chart_prepared']:
        resp = requests.get('http://pnrapi.alagu.net/api/v1.0/pnr/%s'%pnr_no)
        resp = json.loads(resp.content)
        status = resp['status']
        if status != 'OK':
            continue
        data = resp['data']
        passengers = data['passenger']
        if check_if_passengers_cnf(passengers):
            break
        print 'Not confirmed yet ..'
        print 'Current status: '
        print_current_status(passengers)
        print 'Trying again after time interval of %s sec' % retry_interval
        time.sleep(retry_interval)

    print 'CONFIRMED!!!'
    print 'PNR No.:' +data['pnr_number']

    passengers = data['passenger']
    print_current_status(passengers)

get_pnr_status(sys.argv)
