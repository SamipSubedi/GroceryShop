from FetchingData import *
from FetchingData import FetchingData
import sqlite3


def FetchItems():
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


    s = FetchingData()
    response = s.make_get_request('https://fakestoreapi.com/products')
    t = response.json()
    new_dict = s.extract(t)
   

    # ADDING VALUE TO TABLE
    product_values = new_dict
    c.executemany(
        "INSERT INTO Product VALUES(:id,:title,:price,:description,:category,:image,:rate,:count)", 
        product_values)
    conn.commit()


    c.execute("SELECT * from Product;")
    values = c.fetchall()
    items = [{k: item[k] for k in item.keys()}for item in values]
    return items


