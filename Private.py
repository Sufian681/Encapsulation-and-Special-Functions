class MyClass:
    __privateVar = 27
    
    
    def __init__(self, name):
        self.name = name
        
    def __privateMeth(self):
        print("I'm inside class MyClass")
        
    def hello(self):
        print(f"Private Variable value: {MyClass.__privateVar}")
        
        
xyz = MyClass("Nahian")
xyz2 = MyClass("SUFI")

print(xyz.name)
print(xyz2.name)

# print(xyz.__privateVar)
# print(xyz2.__privateVar)

# xyz.__privateMeth()

xyz.hello()
