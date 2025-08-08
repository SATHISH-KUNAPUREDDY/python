# class vehicle():
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
    
#     def display(self):
#             print(f"Brand:{self.brand}, Model:{self.model}, Year:{self.year}")
            
# class car(vehicle):
#     def __init__(self, brand, model, year,doors):
#          super().__init__(brand, model, year)
#          self.doors = doors
         
#     def display(self):
#        super().display() 
#        print(f"Doors:{self.doors}")
       
# class bike(vehicle):
#     def __init__(self, brand, model, year,bike_type):
#          super().__init__(brand, model, year)
#          self.bike_type= bike_type
         
#     def display(self):
#        super().display()  
#        print(f"Type: {self.bike_type}")  
       
# class truck(vehicle):
#     def __init__(self, brand, model, year,capacity):
#         super().__init__(brand, model, year)
#         self.capacity = capacity

        
#     def display(self):
#         super().display() 
#         print(f"Capacity:{self.capacity} tons") 
        
# car=car("Toyata","camry",2022,4)
# bike=bike("Yamaha","r15",2020,1)
# truck=truck("Volvo","FH16",2021,25)

# print("car Details: ")
# car.display()

# print("\nBike Detalis: ")
# bike.display()

# print("\nTruck Detalis: ")
# truck.display()

# print("\nLoory Detalis: ")
# loory.display()
         