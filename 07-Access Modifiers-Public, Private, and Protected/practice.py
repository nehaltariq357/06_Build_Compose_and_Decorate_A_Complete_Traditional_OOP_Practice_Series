
class Test:
    def __init__(self):
        self.name = "public"
        self._salry = "protected"
        self.__ssn = "private"

    def inside(self):
        print(self.name) 
        print(self._salry)
        print(self.__ssn)


t = Test()

print(t.name) # punlic
print(t._salry) # protected (should not, but can)
#print(t.__ssn)  # error(private)
print(t._Test__ssn) # hack (not recommended)