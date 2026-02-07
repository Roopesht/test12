import requests

response = requests.get('https://api.github.com/users/octocat')

print (response.json())

from math import sqrt
