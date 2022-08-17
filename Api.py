import json
import requests
from requests.exceptions import HTTPError
import sqlite3

class API:
    requests.get('https://fakestoreapi.com/products')
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
    #new_dict = {item['id']:item for item in t}
    new_dict = t 

    for item in new_dict:
        item['rate'] = item['rating']['rate']
        item['count']= item['rating']['count']
    #print(new_dict)
    
    conn = sqlite3.connect('store.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE Product (
            id INT,
            title TEXT,
            price INT,
            description TEXT,
            category TEXT,
            image TEXT,
            rate INT,
            count INT
            )""")
    
    product_values = new_dict
        
    
        
    c.executemany("INSERT INTO Product VALUES(:id,:title,:price,:description,:category,:image,:rate,:count)", product_values)
    conn.commit()
    print(c.execute("SELECT * from Product;").fetchall())
    c.execute("SELECT * from Product;")
    for row in c.fetchall():
        print(row)


        