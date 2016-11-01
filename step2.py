import json
import requests

def reverseString(word):
    return word[::-1] #just slice it

myToken = '7c9de6a9cba356ae4bbe6e86226cbbdf'
request = requests.post('http://challenge.code2040.org/api/reverse',json={'token':myToken})
reverse = reverseString(request.text)
request1 = requests.post('http://challenge.code2040.org/api/reverse/validate',json={'token':myToken,'string':reverse})

print(request1.text)