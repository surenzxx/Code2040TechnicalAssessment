import json
import requests

myToken = '7c9de6a9cba356ae4bbe6e86226cbbdf'
myGithub= 'https://github.com/surenzxx/Code2040TechnicalAssessment'
request = requests.post('http://challenge.code2040.org/api/register', json={'token':myToken,'github':myGit})

print(request.text)