from User import User
from Order import Order
from Database import FetchItems

class Shops:
    def __init__(self, name, product_list):
        self._name = name
        self.order_list = []
        self.product_list = product_list
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    
       
    def show_product(self):
        print(f"{'id':10s} {'title':100s} {'price':10s}")
        for i in self.product_list:
            id =  str(i['id'])
            title = i['title']
            price = str(i['price'])
            print(f"{id:10s} {title:100s} {price:10s}")
    
    def order(self):
        self.show_product()
        check = False
        while check == False:
            while True:
                try:
                    product_id = int(
                        input('Enter the Id of Product you want to buy: '))
                    if product_id <= 0 or product_id > len(items):
                        print("Enter product id available")
                    else:
                        check = True
                        quantity = int(
                            input("Enter the quantity of the product you want to buy: "))       
                        self.order_list.append(Order(quantity= quantity, product = product_id))
                        print("\n")
                        more_items = input("Enter yes to buy more product: ")
                        if more_items == "yes":
                            continue
                        break 
                except ValueError:
                    print("Enter Apropriate value")
    
    def total_amount(self, user_name):
        self.order()
        cart = []
        for item in self.order_list:
            cart.append ((item.quantity, self.product_list[item.product-1]))  
        total = 0
        
        for item in cart:
            total += item[0] * item[1].get('price')
        print (total)  
        tax = total * 0.1
        print(f"Your Total price is : {str(total + tax)}")
        
        final_text = ""
        for index, item in enumerate(cart):
            final_text = final_text + "\n" +str(index+1) + "\nitem: " + item[1].get('title') + "\nquantity: " +  str(item[0]) + "\nprice: " + str(item[1].get('price'))
        
        
        final_bill = 'Name: ' + user_name,  '\nDetails:' + final_text + \
            '\n\nTotal: ' + str(total), 'After Tax: ' + \
            str(round(total + tax))
        return final_bill

    def write_bill(self, final_bill):
        with open('bill.txt', 'w') as f:
            for line in final_bill:
                f.write(str(line)+'\n')

    def read_bill(self):
        with open('bill.txt', 'r') as f2:
            print(f2.read())
        
    
        
        

items = FetchItems()

s1 = Shops('Grocery', items)
user_name = input("Enter your name: ")
user = User(user_name)
print("___________________________________________________________________________________________")
print("\n Hello " + user.user_name +
    " HERE IS THE ITEM WE HAVE AVAILABLE ON THE SHOP")
print(" ___________________________________________________________________________________________")

final_bill = s1.total_amount(user_name)

s1.write_bill(final_bill)

print("------------------------------------------------------------------")

s1.read_bill()
