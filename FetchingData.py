import requests
from requests.exceptions import HTTPError

class FetchingData:
    def make_get_request(self, url):
        try:
            response = requests.get(url, verify= False)
            # if the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP Error occured: {http_err}')
        except Exception as err:
            print(f'Other error occured: {err}')
        else:
            print('Successful get request', response)
            return response

    def extract(self, new_dict):
        for item in new_dict:
            item['rate'] = item['rating']['rate']
            item['count'] = item['rating']['count']
        return new_dict

   




