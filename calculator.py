message="""welcome to the simple calculator application:
1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Exit the application
"""


def Addition():
    num1=int(input("number 1:"))
    num2=int(input("number 2:"))
    print(f"the result of {num1} + {num2} is {num1+num2}")
    
def Subtraction():
    num1=int(input("number 1:"))
    num2=int(input("number 2:"))
    print(f"the result of {num1} - {num2} is {num1-num2}")

    
def Multiplication():
    num1=int(input("number 1:"))
    num2=int(input("number 2:"))
    print(f"the result of {num1} x {num2} is {num1*num2}")

    
def Division():
    num1=int(input("number 1:"))
    num2=int(input("number 2:"))
    print(f"the result of {num1} / {num2} is {num1/num2}")

    
    
while True:
    choice_user=int(input(message))
    
    
    if choice_user==1:
        Addition()
    
    elif choice_user==2:
        Subtraction()
    
    elif choice_user==3:
        Multiplication()
    
    elif choice_user==4:
        Division()
    elif choice_user==5:
        print("thank you for using our application")
        break
    else:
        print("sorry this choice didn't exist")


    
    
    