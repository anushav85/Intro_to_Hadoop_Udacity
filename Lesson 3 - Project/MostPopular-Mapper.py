#!/usr/bin/python

# Format of each line is:
# %h %l %u %t \"%r\" %>s %b
# example: 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

# Where:
#    %h is the IP address of the client
#    %l is identity of the client, or "-" if it's unavailable
#    %u is username of the client, or "-" if it's unavailable
#    %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
#    %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol o$
#    %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request ha$
#    %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.# date\ttime\tstore n$

import sys
from urlparse import urlparse

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        ip, identity, username, datetime, timezone, method, path_, proto, status, size = data
        temp1 = urlparse(path_).path.split("/")[-1]
        print "{0}".format(temp1)
