import sys
import json
import requests
import time

def get_status(pnr_no):
    resp = requests.get('http://pnrapi.alagu.net/api/v1.0/pnr/%s'%pnr_no)
    resp = json.loads(resp.content)
    status = resp['status']
    data = resp['data']
    if data == {} or status == "INVALID":
        print 'Invalid PNR Number!'
        return

    def check_if_passengers_cnf(passengers):
        for passenger in passengers:
            if passenger['status'] == 'CNF':
                return True
        return False

    def print_current_status(passengers):
        i = 1
        for passenger in passengers:
            print 'Passenger %s ' % i
            print 'Current Status: ' + passenger['status']
            i+=1

    while not data['chart_prepared']:
        if status == 'OK':
            time.sleep(1)
        resp = requests.get('http://pnrapi.alagu.net/api/v1.0/pnr/%s'%pnr_no)
        resp = json.loads(resp.content)
        status = resp['status']
        data = resp['data']
        passengers = data['passenger']
        if check_if_passengers_cnf(passengers):
            break
        print 'Not confirmed yet ..'
        print 'Current status: '
        print_current_status(passengers)

    print 'CONFIRMED!!!'
    print 'PNR No.:' +data['pnr_number']

    passengers = data['passenger']
    print_current_status(passengers)


pnr_no = sys.argv[1]
get_status(pnr_no)
