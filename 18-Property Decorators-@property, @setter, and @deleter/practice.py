# # normal process

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
    
#     def calculatePercentage(self):
#         return str((self.phy+self.chem+self.math)/3) + "%"
    

# s1 = Student(98,97,99)
# print(s1.calculatePercentage())
# s1.phy = 86 
# print(s1.phy)
# print(s1.calculatePercentage())


# # property process

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     @property
#     def calculatePercentage(self):
#         return str((self.phy+self.chem+self.math)/3) + "%"
    

# s1 = Student(98,97,99)
# print(s1.calculatePercentage)
# s1.phy = 86 
# print(s1.phy)
# print(s1.calculatePercentage)




class Product:
    def __init__(self,price):
        self._price = price  # private variable

    @property
    def pricing(self):
        return self._price  # getter
    
    @pricing.setter
    def pricing(self,value):
        if value >=0:
            self._price = value
        else:
            print("price cannot be negative")
    @pricing.deleter
    def pricing(self):
        print("price is being deleted...")
        del self._price
    


p1 = Product(100)
print(p1.pricing) #100 (calls the @property, pricing)
p1.pricing =50

print(p1.pricing)


del p1.pricing

