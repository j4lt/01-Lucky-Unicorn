

# Functions go here...

# checks for yes / no answers
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please say yes / no")


def instructions():
    print ("****How to Play****")
    print()
    print("The rules of the game go here")
    print()
    return""

# Main Routine goes here...
played_before = yes_no ("Have you played the game before?")

if played_before == "no":
    instructions()

print("Program continues")