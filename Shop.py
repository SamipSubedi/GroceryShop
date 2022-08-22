from Database import FetchItems
from User import User


class Shop:
    def __init__(self, name, items):
        self._name = name
        self.items = items

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def show_product(self):
        for i in self.items:
            print("Product Id: " + str(i["id"]), "\nProduct Name: " +
                  i["title"], "\nPrice: " + str(i["price"]))

    def total_amount(self, user_name):
        c = next((i for i in items if i['id'] == productslist))
        total = c['price'] * quantity
        tax = total * 0.1
        print(f"Your Total price is : {str(total + tax)}")
        final_bill = 'Name: ' + user_name,  "id: " + str(c['id']), 'Title: ' + c['title'],  \
            'Total: ' + str(total), 'After Tax: ' + \
            str(total + tax), 'Quantity: ' + str(quantity)
        return final_bill

    def write_bill(self, final_bill):
        with open('bill.txt', 'w') as f:
            for line in final_bill:
                f.write(str(line)+'\n')

    def read_bill(self):
        with open('bill.txt', 'r') as f2:
            print(f2.read())


items = FetchItems()

s1 = Shop('Grocery', items)
print('WELCOME TO ' + s1.name + ' Store')

user_name = input("Enter your name: ")
user = User(user_name)

print("___________________________________________________________________________________________")
print("\n Hello " + user.user_name +
      " HERE IS THE ITEM WE HAVE AVAILABLE ON THE SHOP")
print(" ___________________________________________________________________________________________")

s1.show_product()


check = False
while check == False:
    try:
        productslist = int(input('Enter the Id of Product you want to buy: '))
        if productslist <= 0 or productslist > len(items):
            print("Enter product id available")
        else:
            check = True  
            quantity = int(
                input("Enter the quantity of the product you want to buy: "))       
    except ValueError:
        print("Enter Apropriate value")
    

final_bill = s1.total_amount(user_name)

s1.write_bill(final_bill)

print("------------------------------------------------------------------")

s1.read_bill()
