import urllib
import urllib2


url = 'https://ccahack.bergen.org/auth/perfigo_validate.jsp'
values = {
	'reqFrom' : 'perfigo_simple_login.jsp',
	'uri' : 'https://ccahack.bergen.org/',
	'cm' : 'ws32vklm',
	'userip' : '168.229.108.58',
	'os' : 'MAC_OSX',
	'index' : '4',
	'username' : 'USERNAME_HERE',
	'password' : 'PASSWORD_HERE',
	'provider' : 'BCA',
	'login_submit' : 'Continue'
}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
