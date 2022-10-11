import re

line = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200'

# a regular expression using named groups to pull out the IP address from a line
re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
m = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
print('IP:', m.group('IP'))

# a regular expression to get the time from log file
r = r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
m = re.search(r, line)
print('Time:', m.group('Time'))

# grab multiple elements, as has been done here: the IP, user,time, and request:
r = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
r += r' - (?P<User>\w+) '
r += r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
r += r' (?P<Request>".+")'
m = re.search(r, line)
print('IP:', m.group('IP'))
print('User:', m.group('User'))
print('Time:',  m.group('Time'))
print('Request:', m.group('Request'))
