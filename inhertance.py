class Animal :
    def __init__(self,name):
        self.name = name
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "woof"
    
    
class Cat(Animal) :
    def sound(self):
        return 'meou'  
    def is_cute(self) :
       return 'is cute'  
    
dog = Dog("jesi")    
cat = Cat('moki')

print(f"{dog.name} says {dog.sound()}")
print(f"{cat.name} that is {cat.is_cute()} says {cat.sound()}")

