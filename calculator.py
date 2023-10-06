def add(a,b):
    answer= a+b
    print(str(a) + "+" +str(b) + "=" +str(answer)+ "\n")

def sub(a, b):
    answer = a - b
    print(str(a)+"-"+str(b)+ "="+ str(answer)+ "\n")

def mul(a, b):
    answer=a*b
    print(str(a) + "*"+str(b)+"="+str(answer)+ "\n")

def div(a, b):
    answer=a/b
    print(str(a) + "/"+str(b)+"="+str(answer)+ "\n")

def mod(a,b):
    answer=a%b
    print(str(a)+"%"+str(b)+"="+str(answer)+ "\n")

while True:
    print("A. Addition")
    print("B. subtraction")
    print("C. Multiply")
    print("D. Divide")
    print("E. Modulus")
    print("F. Exit")

    choice=input("input you choise: ")

    if choice=="a" or choice =="A":
        print("Addition")
        a=int(input("Enter your first number: "))
        b=int(input("enter your second number: "))
        add(a,b)

    elif choice=="b" or choice =="B":
        print("Substraction")
        a=int(input("Enter your first number: "))
        b=int(input("enter your second number: "))
        sub(a,b)

    elif choice=="c" or choice =="C":
        print("Multiply")
        a=int(input("Enter your first number: "))
        b=int(input("enter your second number: "))
        mul(a,b)

    elif choice=="d" or choice =="D":
        print("Division")
        a=int(input("Enter your first number: "))
        b=int(input("enter your second number: "))
        div(a,b)

    elif choice=="e" or choice =="E":
        print("Modulo")
        a=int(input("Enter your first number: "))
        b=int(input("enter your second number: "))
        mod(a,b)

    elif choice=="f" or choice =="f":
        print("Program ended")
        quit ()
