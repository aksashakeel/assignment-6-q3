class car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is started....")
        
my_car = car("Honda")
print(my_car.brand)        

my_car.start()
        