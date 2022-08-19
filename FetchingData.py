import requests
from requests.exceptions import HTTPError

def make_get_request(url):
    try:
        response = requests.get(url)
        # if the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP Error occured: {http_err}')
    except Exception as err:
        print(f'Other error occured: {err}')
    else:
        print('Successful get request', response)
        return response
make_get_request('https://fakestoreapi.com/products')

response = make_get_request('https://fakestoreapi.com/products')
t = response.json()
new_dict = t

def extract():
    for item in new_dict:
        item['rate'] = item['rating']['rate']
        item['count'] = item['rating']['count']


extract()