class Bank():
    
    bank_name = "State Bank of Pakistan"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
customer1 = Bank()
customer2 = Bank()

print("Original Bank Name")
print("Customer 1 Bank:", customer1.bank_name)
print("Customer 2 Bank:", customer2.bank_name)

Bank.change_bank_name("National Bank of Pakistan")

print("\nChanged Bank Name")
print("Customer 1 Bank:", customer1.bank_name)
print("Customer 2 Bank:", customer2.bank_name)

