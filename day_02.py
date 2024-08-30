"""Lets see Built in functions, variables, data types and numbers"""

#First, let's defined some variables
FIRST_NAME = 'Astrid'
LAST_NAME = 'Meza'
FULL_NAME = 'Astrid Meza'
COUNTRY = 'Germany'
CITY = 'Hamburg'
AGE = 45
SKILLS = ['HTML','CSS','JS','React','Python']
YEAR = 2024
CANDY_BAR_PRICE = 5.36
# I can declared multiple variables in one line
name,school,last_year = 'Astrid','High school', 2023

'''
Lets use some built in functions.
Print function will take multiple arguments.
An argument is a value which we put inside the funtion parenthesis.
'''

print('Hello World!')
print('Hello',',','World!')
print('Country:',COUNTRY)

# DATA TYPES

print(type(FIRST_NAME))
print(type(LAST_NAME))
print(type(FULL_NAME))
print(type(COUNTRY))
print(type(CITY))
print(type(AGE))
print(type(SKILLS))
print(type(YEAR))
print(type(CANDY_BAR_PRICE))
print(type(last_year))

# Compare the length of your first name and your last name

print('First name lenght:',len(FIRST_NAME))
print('Last name lenght:',len(LAST_NAME))
FIRST_ONE = len(FIRST_NAME)
SECOND_ONE = len(LAST_NAME)
print('The greatest lenght is:',max(FIRST_ONE,SECOND_ONE))

NUM_ONE = 5
NUM_TWO = 4

TOTAL = NUM_ONE + NUM_TWO
print (TOTAL)
DIFF = NUM_TWO - NUM_ONE
print(DIFF)
PRODUCT = NUM_TWO * NUM_ONE
print (PRODUCT)
DIVISION = NUM_ONE / NUM_TWO
print(DIVISION)
REMINDER = NUM_ONE % NUM_TWO
print (REMINDER)
