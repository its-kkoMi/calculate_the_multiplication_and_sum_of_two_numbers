# Assignment 5 - Exercise 1
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. 
# Otherwise, return their sum.

# Ask user for two inputs

first_number = int(input("1st Number: "))
second_number = int(input("2nd Number: "))

# Use def function for product or sum

def product_or_sum(first_number, second_number) :
    product = first_number * second_number
    
    if product <= 1000:
        return product
    else:
        return first_number + second_number

# Print product or sum

print(product_or_sum(first_number, second_number))