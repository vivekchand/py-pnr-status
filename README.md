py-pnr-status Usage:
====================

```
python pnr_status.py <pnr-no> [retry interval in minutes]

Example:
--------
python pnr_status.py 4159198222 10

Sample Output:
--------------
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
=====
1. Send notification via email / sms when confirmed
2. Make py-pnr-status easier to use (Installable)


More feature suggestions can go here: https://github.com/vivekchand/py-pnr-status/issues/1
If you encounter any bug please create an issue for it :)
