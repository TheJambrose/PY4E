# Exercise 1: Write a program which repeatedly reads numbers until the user
#  enters “done”. Once “done” is entered, print out the total, count, and
#  average of the numbers. If the user enters anything other than a number,
#  detect their mistake using try and except and print an error message and
#  skip to the next number.
user_input = input("Enter a number: ")
current_num = 0
total = 0
count = 0
average = 0
valid_input = False

#checks that the user put in a valid int or float

while user_input != "done" :
    try :
        current_num = float(user_input)
        valid_input = True
    except :
        print("Invalid input")
        valid_input = False

    if valid_input:
        total = total + current_num
        count = count + 1
    user_input = input("Enter a number: ")
average = total / count

print(total, count, average)

# test cases should match below expected outputs
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333
