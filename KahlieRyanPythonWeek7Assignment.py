#1
def all_even_numbers():
    """ Prints out all even numbers between 2 user input integers
    Args: none
    Returns: list of even numbers between 2 user input integers
    """
    #asks input for a number to start/end on
    start = int(input(f"Enter the starting number: "))
    end = int(input(f"Enter the number to end on: "))

    print(f"The even numbers between {start} and {end} are: ")

    #checks to see if the numbers in range are divisible by 2
    #determining if they're even
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)


all_even_numbers()

#2
def all_factors(number):
    """ Prints out all factors of a given positive integer
    Args: Number
    Returns: list of factors of positive integer
    """
number = int(input(f"Enter the positive number: "))

print(f"The factors of {number} are: ")
i = 1
#if number is divided by the i and leaves a remainder of 0 that means it
#is a factor
while i <= number:
    if number % i == 0:
        print(i)
    i += 1


all_factors(number)


#3
def name_value():
    """ Gives an integer value of your name with each letter
    having a corresponding number
    Args: name
    Returns: integer value of your name"""
    name = input("Enter your name: ")
    total_sum = 0

    #iterates through each character in the name and lowers caps
    for char in name.lower():
        if char.isalpha():
            #calculates position of letter
            letter_score = ord(char) - 97
            total_sum += letter_score

    print(f"Your name is {name} with a sum of {total_sum}")

name_value()


#4
def print_squares(n):
    """
    Prints out the squares of n
    """
    #stops function otherwise recursion working backwards will
    #repeat too many times
    if n < 1:
        return

    #works backwards to reverse the recursion
    print_squares(n - 1)

    #squares the input number
    print(n ** 2)

num = int(input(f"Enter a number: "))
print(f"Squares from 1 to {num} are: ")
print_squares(num)


#5
def teepee_sort(num_list):
    """
    Sorts a list of numbers into a teepee shape with the
    smallest on the outside largest on the inside and
    odd numbers on the left and even numbers on the right.
    """
    evens = []
    odds = []

    #sorting the numbers into even or odd
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    #sort lists smallest to largest
    odds.sort()
    evens.sort()

    #
    print(f"The odds of {num} are: ")
    if odds[-1] > evens[-1]:
        peak = odds.pop()
    else:
        peak = evens.pop()

    #reverses the right even side so it goes down instead of up
    evens.reverse()

    #concatonates the final list
    sorted_list = odds + [peak] + evens

    return sorted_list

numbers = [12, 23, 4, 10, 11, 15, 65, 90, 6, 2]
result = teepee_sort(numbers)

print(f"The teepee sorted list from {numbers} is {result}")


