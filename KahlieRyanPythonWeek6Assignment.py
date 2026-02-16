#1
def main(x):


    """Asks user for number input then counts down

    Args: Number
    Returns: Countdown
    """
    while x > 0:
        print(x)
        x = x - 1
    print ("Blastoff!!!")


main(int(input("Enter a number and watch as your mind is blown: ")))


#2
def count_down_odd_even(x):


    """Asks user for number input then counts down
    #adds odd or even specification

    Args: Number
    Returns: Countdown
    """
    while x > 0:
        if x % 2 == 0:
            print(f"{x} is even")
        else:
            print(f"{x} is odd")
        x = x - 1
    print ("Blastoff!!!")


count_down_odd_even(int(input("Enter a number and watch as your mind is blown: ")))


#3
def count_down_integers(x, y):


    """Asks user for number input then counts down
     #adds a decrease integer as an input

    Args: Number, decrease integer
    Returns: Countdown
    """
    while x > 0:
        if x % 2 == 0:
            print(f"{x} is even")
        else:
            print(f"{x} is odd")
        x = x - y
    print ("Blastoff!!!")
x = int(input("Enter the number we should start with: "))
y = int(input("Enter the number for a rate of decrease: "))


count_down_integers(x, y)


#4.1
def count_string():


    """Asks user for word input and counts the string if its <= 5 letters
    Args: None
    Returns: String and letter count"""

    word = input("Enter a word: ")

    while len(word) >= 5:
        print(f"The word {word} is {len(word)} letters long.")
        return word
    else:
        print("goodbye")
        exit()



count_string()

#4.2
def count_string_for():


    """Asks user for word input and counts the string if its <= 5 letters
    Args: None
    Returns: String and letter count
    stops after  5 loops exits if string is under 5 letters"""

    for i in range(4):
        word = input("Enter a word: ")
        if len(word) >= 5:
            print(f"The word {word} is {len(word)} letters long.")
        elif len(word) < 5:
            print("goodbye")
            exit()

    else:
        print("get a life this game isn't that fun man :3")
        return None


count_string_for()


#5
def count_dec_bin_hex():
    """Counts to 10 in decimal binary and hex
    Args: None
    Returns: 1-10 in decimal binary and hex
    """

    number = 1
    while number <= 10:
        output = f"Decimal: {number:d}, Binary: {number:b}, Hexadecimal: {number:x}"
        print(output)
        number = number + 1
    else:
        return None

count_dec_bin_hex()


#6.1 iterative
def stars():
    """Asks user for number and prints that amount of asteriks
        then prints one less star until none remain to print
        Args: star number
        Returns: stars one less each time
        """

    star = int(input("Enter a number of stars: "))
    while star > 0:
        print("*" * star)
        star = star - 1
    else:
        return None

stars()

#6.2 recursion
def recursion_stars(r_stars):
    """Asks user for number and prints that amount of asteriks
        then prints one less star until none remain to print
        Args: star number
        Returns: stars one less each time
        """

    if r_stars <= 0:
        return
    print("*" * r_stars)
    recursion_stars(r_stars - 1)


num = int(input("Enter a number of stars: "))
recursion_stars(num)


if __name__ == "__main__":
    main(x)