import json
from unicodedata import name
import requests
from requests.exceptions import HTTPError
import sqlite3

class Main:
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
    
    #Creating Table
    conn = sqlite3.connect('store.db')
    c = conn.cursor()
    c.executescript(
        """DROP TABLE IF EXISTS Product;
            CREATE TABLE Product (
            id INT,
            title TEXT,
            price INT,
            description TEXT,
            category TEXT,
            image TEXT,
            rate INT,
            count INT
            );
        """)
    
    #ADDING VALUE TO TABLE   
    product_values = new_dict  
    c.executemany("INSERT INTO Product VALUES(:id,:title,:price,:description,:category,:image,:rate,:count)", product_values)
    conn.commit()
    c.execute("SELECT * from Product;").fetchall()
    c.execute("SELECT * from Product;")
    
    print("WELCOME TO GROCERY SHOP")
    name = input("Enter your name: ")
    print("___________________________________________________________________________________________")
    print("\n Hello " +name+ " HERE IS THE ITEM WE HAVE AVAILABLE ON THE SHOP")
    print("\n ___________________________________________________________________________________________")
    for row in c.fetchall():
        t_id, t_title, t_price, t_description, t_category, t_image, t_rate, t_count = row 
        print(f" id : {t_id} || title:  {t_title } || price: {t_price} || \n desc:  {t_description} \
            || \n category: {t_category} || \n imagelink: {t_image} || \n rate: {t_rate} || quantity: {t_count}")
    
    pid = int(input("Enter product id: "))
    quantity = int(input("Enter product quantity you want to buy"))
    
       
    

   





        