import math
while True:
    con=input("calculate(1) or stop(0)?")
    if con=="1":
        num1=float(input("print first number: "))
        num2=float(input("print second number: "))
        act=input("+ and - and * and / and sin and cos and tan and cot and factorial and radical : ")
        if act=="+":
            print(num1+num2)
        elif act=="-":
            print(num1-num2)
        elif act=="*":
            print(num1*num2)
        elif act=="/":
            if num2==0:
                while num2==0:
                    num2=float(input("Enter a non-zero number: "))
            print(num1/num2)
        elif act=="sin":
            choice=input("sin of which number you want to calculate?num1 or num2?")
            if choice=="num1":
                print(math.sin(num1*math.pi/180))
            elif choice=="num2":
                print(math.sin(num2*math.pi/180))
        elif act=="cos":
            choice=input("cos of which number you want to calculate?num1 or num2?")
            if choice=="num1":
                print(math.cos(num1*math.pi/180))
            elif choice=="num2":
                print(math.cos(num2*math.pi/180))
        elif act=="tan":
            choice=input("tan of which number you want to calculate?num1 or num2?")
            if choice=="num1":
                print(math.tan(num1*math.pi/180))
            elif choice=="num2":
                print(math.tan(num2*math.pi/180))
        elif act=="cot":
            choice=input("cot of which number you want to calculate?num1 or num2?")
            if choice=="num1":
                print((math.tan(num1*math.pi/180))**(-1))
            elif choice=="num2":
                print((math.tan(num2*math.pi/180))**(-1))
        elif act=="factorial":
            choice=input("factorial of which number you want to calculate?num1 or num2?")
            if choice=="num1":
                print(math.factorial(num1))
            elif choice=="num2":
                print(math.factorial(num2))
        elif act=="radical":
            choice=input("radical of which number you want to calculate?num1 or num2?")
            if choice=="num1":
                print(math.sqrt(num1))
            elif choice=="num2":
                print(math.sqrt(num2))
    elif con=="0":
        break