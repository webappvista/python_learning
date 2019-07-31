# temperature = 80
# if temperature > 40:
#     print("it's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("it's nice")
# else:
#     print("it's cold")
# print("Done")

# age = 2
# message = "Eligible" if age >= 18 else "Not elibible"
# print(message)

# high_income = True
# good_credit = False
# studen = False

# if (high_income or good_credit) and not studen:
#     print("Eligible")
# else:
#     print("Not eligible")

# age should be between 18 and 65

# age = 65
# if 18 <= age <= 65:
#     print("Eligible")
# else:
#     print("Not eligible")

# for i in range(1, 11, 2):
#     print("Attempt", i, i * ".")

# high_income = False
# good_credit = True
# student = True

# if high_income and good_credit and student:
#     print("You are Approved and You get very low interest")
# elif high_income or good_credit and student:
#     print("Eligible but, high interest")
# else:
#     print("You are NOT approved")

# age = 66
# if 18 <= age <= 65:
#     print('Eligible')
# else:
#     print('Not Eligible')


# For Loops section

# for i in range(1, 11):
#     print('Attempting ', i, i * '.')

# for Else loop

# succesful = False

# for i in range(3):
#     print('Attempting')
#     if succesful:
#         print('Successful')
#         break
# else:
#     print('Attempted 3 time and failed')

# Nested loops

# for x in range(1, 6):
#     for y in range(1, 6):
#         print(f"({x}),({y})")

# iterables
# comments = ['hello', 'hi', 'hola', 'bien']

# for a in comments:
#     print(f"This is thi first iteration " + a)

# While loops

# number = 10000

# while number > 0:
#     print(number)
#     number //= 2

# command = ""

# while command.lower() != "quite":
#     command = input(">")
#     print("Echoing", command)

# Functions
# defining a function

# def greet(first_name, last_name):
#     print(f" Hi {first_name} {last_name}")
#     print(f" welcome aboard {first_name} {last_name}. ")


# greet('mike', 'smith')

# def get_greeting(name, last):
#     return f" hello {name} {last}."


# message = get_greeting('Miky', 'hi')
# print(message)

# Keyword arguments in functions

# def increment(number, by):
#     return number + by


# print(increment(2, 1))

# default arguments in function

# def increment(number, by=1):
#     return number + by


# print(increment(5))

# Functions with extra arguments that returns a tuple

# def multipy(*numbers):
#     total = 1
#     for i in numbers:
#         total *= i
#     return total


# print(multipy(2, 3, 4, 5, 10, 38, 2))
