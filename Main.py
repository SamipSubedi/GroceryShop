from Chef import Chef
from ChineseChef import ChineseChef

c1 = Chef("Tamato", 3)
print(c1.make_food())
print(c1.make_special_dish())
print(c1.details())

c2 = ChineseChef("Tamato", 3, "China")
print(c2.make_food())
print(c2.make_special_dish())
print(c2.details())
print(c2.make_fish())