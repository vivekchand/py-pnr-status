py-pnr-status [![Stories in Ready](https://badge.waffle.io/vivekchand/py-pnr-status.png?label=ready)](http://waffle.io/vivekchand/py-pnr-status)
==============

Usage:
------
```
python pnr_status.py <pnr-no> [retry interval in minutes] [-email=yourname@gmail.com]

Example:
--------
python pnr_status.py 4159198222 10

Sample Output:
--------------
Checking PNR Status ...
CONFIRMED! PNR Status:
PNR No.:4159198222
Passenger 1 
Current Status: CNF
Seat Number:S2 , 48,GN
Passenger 2 
Current Status: CNF
Seat Number:S2 , 44,GN
```

Todo:
-----
1. Send notification via email / sms when confirmed
2. Web App of py-pnr-status ( https://github.com/vivekchand/pypnrstatus.in )
3. Make py-pnr-status easier to use (Installable)


More feature suggestions can go here: https://github.com/vivekchand/py-pnr-status/issues/1

Thanks to:
----------
```
@sjs7007 ( sjs7007@gmail.com ) for email integration
@manojmj92 ( manojmj92@gmail.com ) for ongoing sms integration
```
