# sums two numbers
def addition(num1, num2):
    return num1 + num2


# subs the second number from the first
def subtraction(num1, num2):
    return num1 - num2


# returns num1 the power of num2
def power(num1, num2):
    return num1 ** num2


# returns num1 divides ny num2
def division(num1, num2):
    return num1 / num2


# returns the multiplication of num1 and num2
def multiply(num1, num2):
    return num1 * num2


# checks if the given number is positive
def check_positive(num):
    return num.isnumeric() or check_float(num)


# checks if the given num is negative
def check_negative(num):
    if num[0] == "-":
        return num[1:].isnumeric() or check_float(num[1:])
    return False


# checks if the given num is float
def check_float(num):
    return num.replace(".", "").isnumeric()


# dict of operators
OPERATORS = {1: "+",
             2: "-",
             3: "^",
             4: "/",
             5: "*", }

# dict of operators and functions
FUNCTIONS = {"+": addition,
             "-": subtraction,
             "^": power,
             "/": division,
             "*": multiply}


def main():
    while True:
        operator = input("Please enter the operator: + - ^ * /\n")
        # checks if the operator is valid or not
        while operator not in OPERATORS.values():
            print("The operator isn't valid")
            operator = input("Please enter the operator: + - ^ * /\n")

        num1 = input("Please enter first operand\n")
        # checks if the numbers are valid or not
        while not (check_negative(num1) or check_positive(num1)):
            print("The number isn't valid")
            num1 = input("Please enter first operand\n")

        num2 = input("Please enter second operand\n")
        while not (check_negative(num2) or check_positive(num2)):
            print("The number isn't valid")
            num2 = input("Please enter first operand\n")

        # casting to float because int can be float but float can't be int
        num1 = float(num1)
        num2 = float(num2)

        # prints the result
        result = FUNCTIONS[operator](num1, num2)
        print("The result of", num1, operator, num2, "is", result)

        print("------------------------------")
        exit_while = input("If you want to quit press q, else press any other key and then enter\n")
        if exit_while == 'q':
            break


if __name__ == "__main__":
    main()
