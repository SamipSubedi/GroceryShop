from Main import make_get_request
import sqlite3

response = make_get_request('https://fakestoreapi.com/products')
t = response.json()
new_dict = t
def extract():
    for item in new_dict:
        item['rate'] = item['rating']['rate']
        item['count'] = item['rating']['count']


extract()

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
    print("Product Id: " + str(i["id"]), "\nProduct Name: " +
          i["title"], "\nPrice: " + str(i["price"]))


productslist = int(input('Enter the Id of Product you want to buy: '))
quantity = int(input("Enter the quantity of the product you want to buy: "))
c = next((i for i in items if i['id'] == productslist))
total = c['price'] * quantity
print(f"Your Total price is : {str(total)}")

trial = 'name: ' + name,  "id: " + str(c['id']), 'title: ' + c['title'],  \
    'total: ' + str(total), 'Quantity: ' + str(quantity)


def write_bill():
    with open('bill.txt', 'w') as f:
        for line in trial:
            f.write(str(line)+'\n')


write_bill()

print("\n ------------------------------------------------------------------ \n")


def read_bill():
    with open('bill.txt', 'r') as f2:
        print(f2.read())


read_bill()
