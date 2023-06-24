print("welcome to oksx's 2 number -basic- calculator")
print("240623")

while True:
    sign = int(input("pls select what do u want to do 1 for +, 2 for -, 3 for *, 4 for /, 5 for **, 0 for exit: "))
    
    
    if sign == 1 : 
        num1 = int(input("pls type number 1 here: "))
        num2 = int(input("pls type number 2 here: "))
        print(num1 + num2)
    
    elif sign == 2:
        num1 = int(input("pls type number 1 here: "))
        num2 = int(input("pls type number 2 here: "))
        print(num1 - num2)
    
    elif sign == 3:
        num1 = int(input("pls type number 1 here: "))
        num2 = int(input("pls type number 2 here: "))
        print(num1 * num2)
 
    elif sign == 4:
        num1 = int(input("pls type number 1 here: "))
        num2 = int(input("pls type number 2 here: "))
        print(num1 / num2)
    
    elif sign == 5:
        num1 = int(input("pls type number 1 here: "))
        num2 = int(input("pls type number 2 here: "))
        print(num1 ** num2)

    elif sign == 0:
        print("see ya")
        break

    else:
        print("invalid command")
        continue
