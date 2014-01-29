py-pnr-status [![Stories in Ready](https://badge.waffle.io/vivekchand/py-pnr-status.png?label=ready)](http://waffle.io/vivekchand/py-pnr-status)
==============

Usage:
------
```
python pnr_status.py <pnr-no> [-retry_interval=60] [-email=yourname@gmail.com]

Arguments:
----------
-retry_interval => retry interval in minutes
-email => email address you want to get notified, 
          You will have to give your email password in next step.

Example:
--------
python pnr_status.py 4813108954 -retry_interval=90 -email=vivekchand19@gmail.com 
Password: 

Checking PNR Status ...
Not confirmed yet ..
Current status: 
Passenger 1 
Current Status: W/L  53
Seat Number:W/L  78,GNWL
Passenger 2 
Current Status: W/L  54
Seat Number:W/L  79,GNWL
Passenger 3 
Current Status: W/L  55
Seat Number:W/L  80,GNWL
Trying again after time interval of 90.0 min
sending mail ...
sent :)
```

Todo:
-----
1. Send notification via sms when confirmed
2. Web App of py-pnr-status ( https://github.com/vivekchand/pypnrstatus.in )
3. Make py-pnr-status easier to use (Installable)


More feature suggestions can go here: https://github.com/vivekchand/py-pnr-status/issues/1

Thanks to:
----------
```
@sjs7007 ( sjs7007@gmail.com ) for email integration
@manojmj92 ( manojmj92@gmail.com ) for ongoing sms integration
```
