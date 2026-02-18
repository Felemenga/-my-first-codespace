# Program to check whether a given number is prime or not

def is_prime(number):
    """
    Returns True if the number is prime, otherwise False.
    """
    if number <= 1:
        return False

    # Check divisibility from 2 up to square root of the number
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


# Take input from user
user_input = int(input("Enter a number: "))

# Check and display result
if is_prime(user_input):
    print(f"{user_input} is a Prime number.")
else:
    print(f"{user_input} is NOT a Prime number.")
