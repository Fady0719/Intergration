##Created by Fady Mikhail
##The Programmed Supermarket
##This program will illustrate paying for groceries at a supermarket
#Received help by Andrew Krupp, on 02/22/2022

print("Hello!")
print("Welcome to the Programmed Supermarket \nwhere all your items are digitlized.")
print("Today's date : 02","22","2022", sep = "/")
print("Please enter your name and an associate will be with you shortly")
#user must enter their name
name = input("Enter your name")          
print("Hi", name)
print("I'm Janet and I will be taking care of you today")
print("Did you find everything you were looking for today?",end = ' ')
loop = input("Enter 'yes' or 'no' to continue.")
    
#requires user input to proceed. 
if (loop == 'Yes') or (loop == 'yes'):
    print("Great!")
elif (loop == 'No') or (loop == 'no'):
    print("sorry to hear that"*2)
else:
    print("invalid input, Please enter yes or no")    ##if user inputs a value that is neither 'yes' nor 'no'

##As items are ringing up on the register,
##the items and their prices are displayed for the customer to see

item_name = input("Name of the item: ") 
num_items = int(input("What is the number of items bought?: "))
item_cost = float(input("How much does this item cost?: "))

total_cost = num_items * item_cost

print("Item name: ", item_name)
print("Cost of one item: ", item_cost)
print("Number of items purchased: ", num_items)
print("Total cost: $", format(total_cost, "0.2f"))

print("Here are a couple examples demonstrating my knowledge of math operators in python: ")
print(total_cost ** 2)  #this is the exponentation operator. It raises the number to the power of the exponent.
print(total_cost / 2)    #this is the divison operator. It dividies the left number by the right number and returns a float point value. 
print(total_cost // 2)  #this is the floor division operator. It divides the left number by the right, rounding down the answer and returns a whole number.
print(total_cost % 2)  #this is the modulus operator. It computes the remainder after division has been performed.
print(total_cost + 2)   #this is the additon operator. It sums up two numbers
print(total_cost * 2)   #this is the multiplication operator. it multiplies things by values
print(total_cost - 2)    #this is the subtration operator. It provides the difference of two numbers.

print("Thank you!", name)
print("Have a great day " * 2)  #When used in a string, the * operator will repeat a string for a number of times 
print("The " + "end") #When used in a string, the + signs will concatenate.



