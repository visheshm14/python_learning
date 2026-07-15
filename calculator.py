def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y 

def div(x,y):
    if(y!=0):
        return x/y
    print("Not divisible")

while True:
    print(" simple calculator")

    print("1 for addition")
    print("2 for subtraction ")
    print("3 for multiplication")
    print("4 for divide")
    print("5 for exit")

    choice = int(input("enter your choice"))

    if(choice == 5):
        print("calculator closed!!")
        break
     
    num1 = int(input("enter your number 1"))
    num2 = int(input("enter your number 2"))

    if(choice == 1):
       print("Addition =",add(num1,num2))

    elif(choice == 2):
        print("Subtraction = ",sub(num1,num2)) 

    elif(choice == 3):
        print("Multiplication = ",mul(num1,num2))        

    elif(choice == 4):
        print("Divide = ",div(num1,num2))  
