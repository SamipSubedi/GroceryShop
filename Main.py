import json
import requests
from requests.exceptions import HTTPError
import sqlite3


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
for item in new_dict:
    item['rate'] = item['rating']['rate']
    item['count'] = item['rating']['count']
# Creating Table
conn = sqlite3.connect('store.db')
conn.row_factory = sqlite3.Row
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

# ADDING VALUE TO TABLE
product_values = new_dict
c.executemany(
    "INSERT INTO Product VALUES(:id,:title,:price,:description,:category,:image,:rate,:count)", product_values)
conn.commit()

c.execute("SELECT * from Product;")
values = c.fetchall()
items = [{k: item[k] for k in item.keys()}for item in values]

print("WELCOME TO GROCERY SHOP")
name = input("Enter your name: ")
print("___________________________________________________________________________________________")
print("\n Hello " + name + " HERE IS THE ITEM WE HAVE AVAILABLE ON THE SHOP")
print(" ___________________________________________________________________________________________")

for i in items:
    print(i["id"], i["title"], i["price"])

a = 5

productslist = int(input('Enter the Id of Product you want to buy: '))
quantity = int(input("Enter the quantity of the product you want to buy: "))
c = next((i for i in items if i['id'] == productslist))
total = c['price'] * quantity
print(f"Your Total price is : {str(total)}")

trial = c['id'], c['title'],  total, quantity

with open('my_file_2.txt', 'w') as f:
    f.write(str(trial))