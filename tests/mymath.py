#Add two numbers
def add(a,b):
    return a+b

#Subtract two numbers
def subtract(a,b):
    return a-b

#Multiply two numbers
def multiply(a,b):
    return a*b

#Divide two numbers
def divide(a,b):
    return a/b

def main():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    #Take input from the user
    choice = input("Enter choice(1/2/3/4):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    #use switch case to perform the operation
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))
    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
