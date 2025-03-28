# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            # Collaborator1: Sun Haoxiang/202483890020/2025-03-28
            
            result = add(num1, num2)
            print(f"{num1:.1f} + {num2:.1f} = {result:.1f}")
        elif choice == '2':
            # Collaborator2: Sun Haoxiang/202483890020/2025-03-28
            
            result = subtract(num1, num2)
            sign = "-" if result < 0 else ""
            print(f"{num1:.1f} - {num2:.1f} = {sign}{abs(result):.1f}")
        elif choice == '3':
            # Collaborator3: Sun Haoxiang/202483890020/2025-03-28
            
            result = multiply(num1, num2)
            print(f"{num1:.1f} × {num2:.1f} = "
                  f"{int(result) if result.is_integer() else result:.1f}")
        elif choice == '4':
            # Collaborator4: Sun Haoxiang/202483890020/2025-03-28
            
            if num2 == 0:
                print("Error: Division by zero!")
                continue
            result = divide(num1, num2)
            print(f"{num1:.1f} ÷ {num2:.1f} = {result:.1f}")

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
