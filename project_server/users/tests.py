from django.test import TestCase
import requests
import json
import datetime
import time
#user_info = {'login': 'kenki', 'password': 'kenki'}
#r = requests.get('http://localhost:8000/user/login/', json=user_info).json()
#print(r['success'])
#array = [{'login': 'kenki'}, {'login': 'kenki'}]
#login = 'kenki'
#if login in array:
#    print(array)
#else:
#    print('bad')
#b = array[0].values()
#print([i for i in array[0].values()])
a = datetime.datetime.now()
print(a)
c = 0
for i in range(0,10000000000):
    c += 1
b = datetime.datetime.now()
print(b)
print(b-a)