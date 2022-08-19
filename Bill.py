from User import *


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
