
# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

#initilize the instance    
b1 = Bank()
#before change
print(Bank.bank_name)
print(b1.bank_name)
#change class variable name
Bank.change_bank_name("nation bank")
#after change
print(Bank.bank_name)
print(b1.bank_name)
