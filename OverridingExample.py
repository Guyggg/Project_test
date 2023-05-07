class Animal():
    def eat(self):
        print("Eating Eating !!!")

class Cat(Animal):
    name= ""
    def setName(self, text):
        self.name = text
    def eat(self):
        print("Meowwwwww", self.name)

cat1 = Cat()
cat1.name= "Nueangoen"
cat1.eat()