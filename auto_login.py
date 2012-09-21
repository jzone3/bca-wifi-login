#!/usr/bin/python

import urllib
import urllib2
import socket

username = 'USERNAME'
password = 'PASSWORD'

def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("google.com",80))
	return (s.getsockname()[0])

url = 'https://ccahack.bergen.org/auth/perfigo_validate.jsp'
values = {
	'reqFrom' : 'perfigo_simple_login.jsp',
	'uri' : 'https://ccahack.bergen.org/',
	'cm' : 'ws32vklm',
	'userip' : get_ip(),
	'os' : 'MAC_OSX',
	'index' : '4',
	'username' : username,
	'password' : password,
	'provider' : 'BCA',
	'login_submit' : 'Continue'
}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
