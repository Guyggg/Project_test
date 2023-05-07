def login():
    usernameInput = input("Username: ")
    passwordInput = input("Password: ")
    if usernameInput == "Admin" and passwordInput =="1234":
        return True
    else:
        return False
def showMenu():
    print("-----iShop-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>>"))
    return userSelected
def vatCal(totalPrice):
    vat = 7
    result = totalPrice * (1 + vat / 100)
    return result
def priceCal():
    price1 = int(input("First Product Price: "))
    price2 = int(input("Second Product Price: "))
    return vatCal(price2 + price1)

print(priceCal())