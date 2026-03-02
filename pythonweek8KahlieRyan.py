from operator import truediv
from symbol import return_stmt

import alphabet


#1
def stop_shouting():
    """
    Prompts user for one phrase as input
    matches phrase to second input in caps
    prints (stop shouting!)
    """
    phrase1 = input("Enter a phrase: ")
    phrase2 = input("Enter the same phrase in UPpercase: ")

    #checks first if the strings match then if the second input is uppercase
    if phrase1 == phrase2:
        return
    if phrase2.isupper():
        print("Stop shouting please!")
    else:
        print("I can't hear you speak up")


stop_shouting()

#2
def vowels_check(x):
    """
    Checks to see how many vowels in a string
    """
    #starts vowel counter
    vowels = 0
    #vowel list
    vowels_list = ['a','e','i','o','u']
    #iterates through user input lowering any letters to match list
    #and checks for vowels in list
    for letter in x.lower():
        if letter in vowels_list:
            vowels += 1
    print(f"There are {vowels} vowels in this string")


x = input("Give me a sentence and I can count how many vowels there are!: ")

vowels_check(x)

#3
def alpha_order():
    """
    Asks for 2 inputs, returns which input is first
    in alphabetical order
    """
    #checks alphabetical order
    if string_1 < string_2:
        print(f"{string_1} comes before {string_2}")
    else:
        print(f"{string_2} comes before {string_1}")


string_1 = input("Give me a string: ")
string_2 = input("Give me a different string: ")

alpha_order()


#4
def email_test():
    """
    checks to see if email matches
    """
    email_1 = input("Enter an email: ")
    email_2 = input("Enter your email again: ")

    while email_1 != email_2:
        print("The emails you entered do not match please try again")
        email_1 = input("Enter an email: ")
        email_2 = input("Enter your email again: ")
    else:
        print("The emails you entered match!")


email_test()


#5
def iter_factorial(n):
    """
    Iterates through every number below n and multiplies
    by n to find a factiorial
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input("Give me an integer: "))
iter_factorial(n)


def recursive_factorial(n):
    """
    Recursively calculates factorial
    """
    #stops when n is less than 1 or it will go too long
    if n <= 1:
        return 1
    r = recursive_factorial(n - 1)
    return r * n

n = int(input("Give me an integer: "))
recursive_factorial(n)

print(f"Iterative: {iter_factorial(n)}")
print(f"Recursive: {recursive_factorial(n)}")
