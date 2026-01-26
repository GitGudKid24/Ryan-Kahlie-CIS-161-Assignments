name = input("What is your name? : ")
print(f"Hello, {name}!")

#//// does not work unless you convert strings to integers
age = int(input("What is your age? : "))
years = int(input("Select a number of years to add to your age : "))
print(f"{name}, in {years} years, you will be {age + years} years old. Live in the moment ;)")

#converting to floats to include decimals
work_hours = float(input("How many hours do you work per week? : "))
hourly = float(input("What is your hourly wage? : $"))
#multiplying hourly times hours worked and weeks in a year to get annual salary
print(f"Your gross pay this week is ${hourly*work_hours} "
      f"and your estimated annual gross pay will be ${hourly*work_hours*52} ")