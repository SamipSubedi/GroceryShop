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
    new_dict = {item['id']:item for item in t}
    
    for item in new_dict:
        rating = new_dict.get(item).get('rating').get('rate')
        count = new_dict.get(item).get('rating').get('count')
        new_dict.get(item)['rate'] = rating
        new_dict.get(item)['count'] = count
        del new_dict.get(item)['rating']
    
    print(new_dict)
    
    conn = sqlite3.connect('store.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE Product (
            id INT,
            Title TEXT,
            Price INT,
            Description TEXT,
            Category TEXT,
            IMAGE BLOB,
            RATE REAL,
            COUNT INT
            )""")
    
    product_values = (new_dict)
        
    
    with sqlite3.connect("store.db") as connection:
        cursor = connection.cursor()
        cursor.executemany("INSERT INTO Product VALUES(?,?,?,?,?,?,?,?)", (product_values))
        print(cursor.execute("SELECT * from Product;").fetchall())
        cursor.execute("SELECT * from Product;")
        for row in cursor.fetchall():
            print(row)


        