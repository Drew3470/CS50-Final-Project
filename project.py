import sys

def store():
    print("\n Calculator\n")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

    answer = input("select a option (1/2/3/4/5/): ")

    if answer == "1":
        print(add())
    elif answer=="2":
        print(subtract())
    elif answer == "3":
        print(multiply())
    elif answer == "4":
        divide()
    elif answer == "5":
        sys.exit("Thank you")
    else:
        print("Invalid , Try again")

    store()


def add(n_1=None,n_2=None):
    if n_1 is None or n_2 is None:
        n_1= float(input("First number: "))
        n_2= float(input("second number: "))

    result = n_1 + n_2
    print(f"{n_1} + {n_2} = {result}")
    return result

def subtract(n_1=None,n_2=None):
    if n_1 is None or n_2 is None:
        n_1= float(input("First number: "))
        n_2= float(input("second number: "))
    result= n_1 - n_2
    print(f"{n_1} - {n_2} = {result} ")
    return result

def multiply(n_1=None,n_2=None):
    if n_1 is None or n_2 is None:
        n_1= float(input("First number: "))
        n_2= float(input("second number: "))
    result = n_1 * n_2
    print(f"{n_1} * {n_2} = {result} ")
    return result

def divide(n_1=None,n_2=None):
    if n_1 is None or n_2 is None:
        n_1= float(input("First number: "))
        n_2= float(input("second number: "))

    try:
        result = n_1 / n_2
        print(f"{n_1} / {n_2} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None



def main():
    store()

if __name__ == "__main__":
    main()


