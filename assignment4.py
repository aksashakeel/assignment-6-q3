class Bank:
    bank_name = "Old Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

a = Bank()
b = Bank()

print(a.bank_name)
Bank.change_bank_name("New Bank")
print(a.bank_name)
print(b.bank_name)