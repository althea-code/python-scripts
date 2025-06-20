import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1') #GET request to API endpoint

if response.status_code == 200:
    print('Request Successful :) ')
    print(response.text)
else:
    print(f'Unfortunately, request has failed. Status Code: {response.status_code}')