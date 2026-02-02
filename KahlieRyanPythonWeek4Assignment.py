#Using numbers to show which part of the homework I'm working on
#1
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


"""adds three numbers, divides by 3
    
Args: int(num1, num2, num3)
    
Returns: int(average of num1, num2, num3)
"""

print(average(7, 5, 9))
print(average(6, 6, 7))

#2
#Will run because the docstring acts
#as a comment without affecting the code
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(average(7, 5, 9))
print(average(6, 6, 7))


"""adds three numbers, divides by 3

Args: int(num1, num2, num3)

Returns: int(average of num1, num2, num3)
"""

#3
#I don't believe this will work because "num1" is not a variable
#just the functions parameters that need to be called in an argument
#they are undefined variables

#print(num1) #and I was correct

#4 and #6
def dogs_age_human_years(age):
    return 24 + (age - 2) * 4
age = int(input("What is your dogs age?: "))


"""finds a dogs age in human years
    
Args: int(age)

Returns: int(dogs age in human years)
"""
print(f"{age} dogs years is equivalent to {dogs_age_human_years(age)} human years, "
      f"if only they aged like humans :(" )

#5
def car_value(price, years, rate):
    value = price - (price * (years * rate)) #calculates value
    return int(value)


"""calculates value of a car after so many years

Args: (price, years, type)

Returns: int(car value)
"""
#depreciation rate
germany = 0.05 #5%
japan = 0.07 #7%
italy = -0.05 #5% appreciation

#prompt user for input on price, years owned, and the country of origin
price = int(input("Initial car price: "))
years = int(input("Years owned: "))
country = input("Choose country of origin (Germany, Japan, Italy): ").lower()

#defines rates as floats for each country respectively
if country == "italy":
    rate: float = italy
elif country == "germany":
    rate: float = germany
elif country == "japan":
    rate: float = japan
else :
    rate: float = 0.06 #if other country is chosen default rate

final_value = car_value(price, years, rate)

#calls function
print(f"the final value of your car is {final_value}")

def ice_cream_calculator(number_of_scoops):
    ice_cream = float(number_of_scoops * 1.15 + 2.25)
    return int(ice_cream)

ice_price = ice_cream_calculator(number_of_scoops)

number_of_scoops = int(input("Enter the number of scoops you want: "))

print(f"The price of your ice cream is {ice_price}")







