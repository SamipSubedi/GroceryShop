class Chef:
    def __init__(self , name, rating):
        self.name = name
        self.rating = rating
    
    def details(self):
        return("The name of reatro is " +self.name+ "and rating is " +str(self.rating))
    
    def make_food(self):
        return("Chef makes food")
    
    def make_special_dish(self):
        return("This Chef makes special dish")