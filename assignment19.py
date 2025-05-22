class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

m = Multiplier(3)
print("Is m callable?", callable(m))
print("m(5) =", m(5))
