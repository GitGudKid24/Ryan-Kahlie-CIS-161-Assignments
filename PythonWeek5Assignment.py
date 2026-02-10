#1
from state_capitals import capitals_dict #used for function on question 2

#finds remainded if a number is divided by 5 to determine if its divisible
num = int(input("Enter a number to see if it is divisible by 5: "))
if num % 5 == 0:
    print(f"The number {num} is divisible by 5")
else:
    print (f"The number {num} is not divisible by 5")

#2 #uses if and elif statements to find a limited number of states
#slower than using a func with a dictionary
state = input("Enter the name of your state to find the capital: ")
if state == "Oregon":
    print(f"The capital of Oregon is Salem")
elif state == "Idaho":
    print(f"The capital of Idaho is Boise")
elif state == "Wyoming":
    print(f"The capital of Wyoming is Cheyenne")
elif state == "Colorado":
    print(f"The capital of Colorado is Denver")
elif state == "Kansas":
    print(f"The capital of Kansas is Topeka")
else:
    print("I'm still learning some of the capitals, sorry!")

#2.2
def capitals():


    """Finds your states capital from a limited library
    Args: State

    Returns: Capital

    """
    your_state = input("Enter the name of your state to find the capital: ")
    capital = capitals_dict[your_state]
    print(f"The capital of {your_state} is {capital}")

#Calling the function
capitals()

#2.3 match case
#def state_capitals2():


   # """ uses match case to find state capital
    #args: state

   # returns: Capital"""

    #state2 = input("Enter the name of your state to find the capital: ")
    #match state2:
        #case "Oregon":
           # capital2 = "salem"
       # case "Idaho":
           # capital2 = "boise"
        #case "Wyoming":
           # capital2 = "Cheyenne"
        #case "Colorado":
           # capital2 = "Denver"
        #case "Kansas":
            #capital2 = "Topeka"
       # case _:
           # capital2 = "No capital found"
    #print(f"The capital of {state2} is {capital2}")

#did all of this ^^^^ to realize the version of python I'm on doesn't support
#match statements, gotta update lol

#3
def pool_prices():


    """ Finds pool price per age
    Args: age
    Returns: Pool price"""

    age = int(input("What is your age? : "))
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 60:
        return 6
    else:
        return 4

print(f"The pool price for you is ${pool_prices()}")

#4

import requests

def count_hugo_string(url, word):


    """
    Gets the contents of a URL and finds the times a word occurs

    Args: the url, the word to search for

    Returns: the number of times a word occurs
    """
    response = requests.get(url)
    return response.text.count(word)


hugo = count_hugo_string('https://gohugo.io/', "hugo")
print(f"The word Hugo appears {hugo} times in the given URL")

#5
import psutil

def running_processes():
    """Finds running processes on my system"""
    pids = psutil.pids()
    return len(pids)

if __name__=="__main__":
    process_count = running_processes()
    print(f"There are {process_count} running processes on my system")