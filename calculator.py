def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    else:
        return x / y

def main():
    print("Simple Calculator\n")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("select your operator\n")
    print("1.addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide\n")

    choice = input("Enter your choice (1/2/3/4)\n")
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
