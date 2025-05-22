class counter:
    count = 0

    def __init__(self, name):
        self.name = name
        counter.count += 1

    @classmethod
    def show_count(cls): 
        print("Total objects created:", cls.count) 

        
obj1 = counter("Aqsa")
obj2 = counter("Esha")
obj3 = counter("Fiza")

counter.show_count()
print(obj1.name, obj2.name, obj3.name)       