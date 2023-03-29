from Chef import Chef

class ChineseChef(Chef):
   def __init__(self, name , rating, location):
      super().__init__(name, rating)
      self.location = location
   
   def details(self):
      return ("This restro name is " +self.name+ " And rating is " +str(self.rating)+ "and located on " +self.location )
   
   def make_special_dish(self):
      return ("Chinese chef makes special choupsey")
   
   def make_fish(self):
      return ("Chinese chef cooks fish")