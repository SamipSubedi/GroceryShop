from Shop import *
from Shop import Shop

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
