class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to ", self.name, self.lastname, "'s cart")

customer1 = Customer() #สร้างobject ใช้งานจริงไม่งั้นมันจะใช้งานไม่ได้
customer1.name = "Krittin"
customer1.lastname = "Au-jean"
customer1.addCart()
