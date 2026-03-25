# Ex 1: Print numbers from 1 to 10

def print_numbers(*args):
    """
    Print numbers from 1 to 10
    Args:
        *args: Numbers to print
    """
    for num in args:
        print(num)

def print_numbers2(num1: int, num2: int) -> int:
    """
    Print numbers from 1 to 10
    args:
        num1 - int
        num2 - int
    """
    for num in range(num1, num2 + 1):
        print(num)


if __name__ == "__main__":
    print_numbers(1,2,3,4,5,6,7,8,9,10)
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        print_numbers2(x, y)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

