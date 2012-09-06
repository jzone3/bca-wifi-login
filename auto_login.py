import urllib
import urllib2

def bca_wifi():
    try:
        response=urllib2.urlopen('http://168.229.108.58',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

if bca_wifi():
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
