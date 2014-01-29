import sys
import json
import requests
import time
import smtplib
import getpass
default_retry_interval = 10*60 #10 min

def sendEmail(pnr,Message,emailId,passw):
    subject = 'PNR Status %s' % pnr
    msg = 'Subject: %s\n\n%s' % (subject, Message)
    fromaddr=emailId
    toaddrs=emailId
    try:
        print 'sending mail ...'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(emailId,passw)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        print 'sent :)'
    except smtplib.SMTPAuthenticationError, e:
        server.quit()
        print 'Invalid email or password'
        emailId = ''
        passw = ''

def get_pnr_status(argv):
    if len(argv) < 2:
        print 'Usage: python pnr_status.py <pnr-no> [-retry_interval=60] [-email=yourname@gmail.com]'
        return

    emailId = ''
    passw = ''
    retry_interval = default_retry_interval

    if len(argv) >= 3:
        for arg in argv[2:]:
            extarg = arg.split('=')
            if extarg[0] == '-email':
                emailId = extarg[1]
                passw = getpass.getpass()
            elif extarg[0] == '-retry_interval':
                retry_interval = int(extarg[1])*60

    pnr_no = argv[1]
    print '\nChecking PNR Status ...'
    resp = requests.get('http://pnrapi.alagu.net/api/v1.0/pnr/%s'%pnr_no)
    resp = json.loads(resp.content)
    status = resp['status']
    data = resp['data']
    if data == {} and status == 'OK':
        print 'Something went wrong real bad! Try again Later :)'
        return

    if status == "INVALID":
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
            print 'Seat Number:' + passenger['seat_number']
            i+=1

    def get_current_status(passengers):
        temp=''
        i = 1
        for passenger in passengers:
            temp = temp+ 'Passenger %s ' % i +'\n' + 'Current Status: ' + passenger['status']
            temp = temp +'\n'+ 'Seat Number:' + passenger['seat_number']+'\n\n'
            i+=1
        return temp

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
        print 'Trying again after time interval of %s min' % (int(retry_interval)/60.0)
        if(emailId!=''):
            emailMsg = get_current_status(passengers)
            pnr = data['pnr_number']
            sendEmail(pnr,emailMsg,emailId,passw)
        time.sleep(retry_interval)

    if data['chart_prepared']:
        print 'Chart Prepared! PNR Status:'
    else:
        print 'CONFIRMED! PNR Status:'
    print 'PNR No.:' +data['pnr_number']

    passengers = data['passenger']
    print_current_status(passengers)

    if(emailId!=''):
        emailMsg = get_current_status(passengers)
        pnr = data['pnr_number']
        sendEmail(pnr,emailMsg,emailId,passw)


get_pnr_status(sys.argv)

