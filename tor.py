import requests
import re
proxies={
    'http':'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}
url='http://api.ipify.org/?format=json'

print('Check ip address*********************************************')
print('Before tor proxies:')
r=requests.get(url)
print('My ip is:',r.text)

print('After tor proxies:')
r=requests.get(url,proxies=proxies)
print('The tor ip is:',r.text)
