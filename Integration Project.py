from typing import \
    Any

import time

##Created by Fady Mikhail
##The Programmed Supermarket
##This program will illustrate paying for groceries at a supermarket
#Received help by Andrew Krupp, on 02/22/2022

def cost_of_items(item_name, num_items, item_cost):

    total_cost = num_items * item_cost
    print("Item name: ", item_name)
    print("Cost of one item: ", item_cost)
    print("Number of items purchased: ", num_items)
    print("Total cost: $", format(total_cost, "0.2f"))

    print("Here are a couple examples demonstrating my knowledge of math operators in python: ")
    print(total_cost **2)  #this is the exponentiation operator. It raises the number to the power of the exponent.
    print(total_cost / 2)    #this is the division operator. It divides the left number by the right number and returns a float point value.
    print(total_cost // 2)  #this is the floor division operator. It divides the left number by the right, rounding down the answer and returns a whole number.
    print(total_cost % 2)  #this is the modulus operator. It computes the remainder after division has been performed.
    print(total_cost + 2)   #this is the addition operator. It sums up two numbers
    print(total_cost * 2)   #this is the multiplication operator. it multiplies things by values
    print(total_cost - 2)    #this is the subtraction operator. It provides the difference of two numbers.

    print("Here a couple examples demonstrating my knowledge of Boolean operators in Python: ")

    print("First, we have the and operator, which is used to combine conditional statements: ")
    print("Note. The inputs must match, otherwise an error will occur. ")
    a = input("Enter a number: ")
    c = input("Enter a number: ")

    if (a == c) and (c == a):
        print("Boolean operator complete.")
    else:
        print("Error.")

    print("Next, we have the not operator: ")
    print("The not operator is used to invert the truth value of the Boolean expressions and objects.")
    print("If the input does not fall within the parameters of the statement, \nthe statement is false.")
    a = input("Enter a number: ")
    print(not(a >= '10') and (a <= '5'))

    print("Here are a couple examples demonstrating my knowledge of loops and iterative structures in Python: ")

    print("The for operator will repeat any given sequence in a list.")
    item_name = ["apple", "pear", "banana"]
    for z in item_name:
        print(z)

    print("The while operator will continue the loop indefinitely, so as long as the condition holds true.")
    item_cost = int(input("Enter a number: "))
    while item_cost < 20:
        print(item_cost)
        item_cost += 1

    print("The in and range functions are used when a user needs ")
    print("an action to be performed a specific number of times. ")
    item_cost = range(1,30)
    for item_cost in item_cost:
        print(item_cost)

    #Shortcut Operators
    print("Here is a demonstration of shortcut operators. ")

    item_cost = 10
    item_cost += 5
    print(item_cost)

    item_cost = 10
    item_cost -= 5
    print(item_cost)

    item_cost = 10
    item_cost *= 5
    print(item_cost)

    item_cost = 10
    item_cost /= 5
    print(item_cost)

    item_cost = 10
    item_cost %= 5
    print(item_cost)

    item_cost = 10
    item_cost //= 5
    print(item_cost)

    item_cost = 10
    item_cost **= 5
    print(item_cost)

    print('Thank you!', name)
    print("Have a great day " * 2)  #When used in a string, the * operator will repeat a string for a number of times
    print("The " + "end") #When used in a string, the + signs will concatenate.


def main():
    print("Hello!")
    print("Welcome to the Programmed Supermarket \nwhere all your items are digitized.")
    print("Today's date : 04","07","2022", sep = "/")
    print("Please enter your name and an associate will be with you shortly")
    #user must enter their name
    name = input("Enter your name: ")
    time.sleep(2)
    print("Hi", name)
    print("I'm Janet and I will be taking care of you today")
    print("Did you find everything you were looking for today?", end = ' ')
    loop = input("Enter 'yes' or 'no' to continue. ")
    #requires user input to proceed.
    if loop.lower() == "yes" or loop.lower() == "y":
        print("Great!")
    elif loop.lower() == "no" or loop.lower() == "n":
        print("Sorry to hear that."*2)
    else:
        print("invalid input, Please enter yes or no")    ##if user inputs a value that is neither 'yes' or 'no'
    item_name = input("Name of the item: ")
    num_items = int(input("What is the number of items bought?: "))
    item_cost = float(input("How much does this item cost?: "))
    cost_of_items(item_name, num_items, item_cost)

main()
##As items are ringing up on the register,
##the items and their prices are displayed for the customer to see


