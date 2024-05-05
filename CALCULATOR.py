////////////////////////////TASK 1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#MAIN FILE

import Calculator.Basic as B1
import Calculator.Scientific as S1
import Calculator.Converter as C1

choice = int(input("Please enter 1 for basic, 2 for scientific and 3 for converter or 0 to end. "))

while choice !=0:
    if choice == 1:
        choice1 = int(input("select 1 for addition, 2 for subtract, 3 for multiply and 4 for divide. "))
        if choice1 == 1:
            ask1 = int(input("Enter 1 number. "))
            ask2 = int(input("Enter 2 number. "))
            print(B1.addition(ask1,ask2))
        elif choice1 == 2:
            ask1 = int(input("Enter 1 number. "))
            ask2 = int(input("Enter 2 number. "))
            print(B1.subtract(ask1,ask2))
        elif choice1 == 3:
            ask1 = int(input("Enter 1 number. "))
            ask2 = int(input("Enter 2 number. "))
            print(B1.multiply(ask1,ask2))
        elif choice1 == 4:
            ask1 = int(input("Enter 1 number. "))
            ask2 = int(input("Enter 2 number. "))
            print(B1.divide(ask1,ask2))
        elif choice1 == 0:
            print("Thanks for using calculator. ")
            break
    elif choice == 2:
        choice1 = int(input("select 1 for sqroot, 2 for exponential, 3 for cubeit. "))
        if choice1 == 1:
            ask1 = int(input("Enter 1 number. "))
            print(S1.sqroot(ask1))
        elif choice1 == 2:
            ask1 = int(input("Enter 1 number. "))
            ask2 = int(input("Enter 2 number. "))
            print(S1.exponential(ask1,ask2))
        elif choice1 == 3:
            ask1 = int(input("Enter 1 number. "))
            ask2 = int(input("Enter 2 number. "))
            print(S1.cubeit(ask1))
        elif choice1 == 0:
            print("Thanks for using calculator. ")
            break
    elif choice == 3:
        choice1 = int(input("select 1 for PKRtoDINAR, 2 for temperature, 3 for inch2centi. "))
        if choice1 == 1:
            ask1 = int(input("Enter 1 number. "))
            print(C1.pkrtodinar(ask1))
        elif choice1 == 2:
            ask1 = int(input("Enter 1 number. "))
            print(C1.celtofahren(ask1))
        elif choice1 == 3:
            ask1 = int(input("Enter 1 number. "))
            ask2 = int(input("Enter 2 number. "))
            print(C1.inch2centi(ask1))
        elif choice1 == 0:
            print("Thanks for using calculator. ")
            break
    
#Converter.py

def pkrtodinar(a):
    result = a*1000
    return result

def celtofahren(a):
    result = (a*(9/5))+32
    return result

def inch2centi(a):
    result = a*2.54
    return result

#Scientific.py

def sqroot(a):
    result = (x^1/2)
    return result
    
def exponential(a,b):
    result = a*b
    return result
    
def cubeit(a):
    result = a*a*a
    return result

#Basic.py

def addition(a,b):
    result = a+b
    return result

def subtract(a,b):
    result = a-b
    return result

def multiply(a,b):
    result = a*b
    return result

def division(a,b):
    result = a/b
    return result

-------------------------------------------------------------------        


                  
            
