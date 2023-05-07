"""""
inputRound = int(input("Please Enter Number: "))
sum = 0
for x in range(inputRound):
    inputNumber = int(input("X = "))
    sum = inputNumber+sum
print(sum)
"""""
"""
inputRound = int(input("Please Enter Number : "))
sum = 0
for x in range(inputRound):
    inputNumber = int(input("x" + str(x + 1) + ":"))
"""

start = int(input("Start: "))
step = int(input("Step: "))
result = ""
for i in range(5):
    print(start + step *i)

