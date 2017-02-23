import requests

r = requests.get('http://www.python.org')
print type(r)
print r.status_code
# print r.text
print r.cookies.items()

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text

s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print r.text

