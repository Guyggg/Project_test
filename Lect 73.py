systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []


def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
    print(price)
while True:
    menuName = input("Plese Enter Menu :")

    if(menuName.lower() == "exit"):
        break
    else:
        price = systemMenu[menuName]
        menuList.append([menuName, systemMenu[menuName]])
        price = price + systemMenu[menuName]

showBill()