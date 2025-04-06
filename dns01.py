import sys
import os
import requests
import urllib

def getpostdata(mode):
	post_data = {}
	target_names = [
		'CERTBOT_DOMAIN',
		'CERTBOT_VALIDATION',
		'CERTBOT_TOKEN',
		'CERTBOT_CERT_PATH',
		'CERTBOT_KEY_PATH',
		'CERTBOT_SNI_DOMAIN',
		'CERTBOT_AUTH_OUTPUT'
	]
	for name in target_names:
		if os.environ.get(name) != None:
			post_data[name] = os.environ[name]
	post_data['EDIT_CMD'] = mode
	# print(post_data)
	return post_data

if __name__ == '__main__':
	mode = sys.argv[1]
	id = sys.argv[2]
	pwd = sys.argv[3]

	url = 'https://www.mydns.jp/directedit.html'
	params = urllib.parse.urlencode(getpostdata(mode))
	headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
	auth = (id, pwd)

	for i in range(5):
		res = requests.post(url=url, data=params, headers=headers, auth=auth)
		loc = res.headers.get('Location')
		if loc == None:
			break
		url = loc
	print(res.status_code)
	# print(res.text)
