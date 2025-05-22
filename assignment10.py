class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

d = Dog("Bruno", "Labrador")
d.bark()
