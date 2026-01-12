#setting variables for use with f-strings
from calendar import monthcalendar, firstweekday

sibling = "sister"
sibling_name = "Christina"
#calling variables in a string
print(f"I have a {sibling} and her name is {sibling_name}")

#setting up more variables
name = input("Enter your first name: ")
age = input("Enter your current age: ")
savings = input("Enter your yearly savings: $ ")

#using integers in the called variables to modify them without using a function
print(f"Hello {name}! You are currently {age} years old. In 10 years you will be {int(age) + 10} years old.")
print(f" If you save ${savings} each year, in 5 years you will have saved {int(savings)*5}.")
print(f"Your average monthly savings is {int(savings)/12} dollars per month.")

#importing calendar to calculate how many days in a month
import calendar

def seconds_in_month():
    # Prompt the user for input on the month
    mth = input("Enter the month by number: ")
    #converts to integer
    month_number = int(mth)
    _, number_of_days = calendar.monthrange(2026, month_number)
    #calculating the number of seconds per day
    total_seconds = number_of_days * 86400
    print(f"There are {total_seconds} seconds in month {month_number} (which has {number_of_days} days).")
#even after looking up all of this it took me forever to figure out especially to use the underscore for a throwaway variable
    return total_seconds

# Calls the function
seconds_in_month()

def full_cartons_of_eggs():
    eggs = input("How many eggs do you have? :")
    eggs_number = int(eggs)
    cartons = eggs_number // 12
    remainder = eggs_number % 12
    print(f"There are {cartons} cartons of eggs with {remainder} remaining.")

full_cartons_of_eggs()


