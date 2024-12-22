def calculator():
    """
    A simple calculator that performs basic arithmetic operations.
    """

    while True:
        print("Select The operation.")
        print("1.Add")
        print("2.Sub")
        print("3.Mul")
        print("4.Div")
        print("5.Exit")

        select = input("Enter choice(1/2/3/4/5): ")

        if select in ('1', '2', '3', '4'):
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if select == '1':
                result = num1 + num2
                print(num1, "+", num2, "=", result)

            elif select == '2':
                result = num1 - num2
                print(num1, "-", num2, "=", result)

            elif select == '3':
                result = num1 * num2
                print(num1, "*", num2, "=", result)

            elif select == '4':
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(num1, "/", num2, "=", result)

        elif select == '5':
            print("Exiting calculator.")
            break
        else:
            print("Invalid Input")

 
calculator()
