# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.



class Countdown():
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < 0:
            raise StopIteration
        num = self.n
        self.n -=1
        return num
    
num = int(input("Enter number: "))
for i in Countdown(num):
    print(i)