number = int(input("Number: "))
for i in range(number):
    print((" "*(number-i-1))+"*"*i+"*"+"*"*i+(" "*(number-i-1)))
