# Exercise 2: Write another program that prompts for a list of numbers as above
#  and at the end prints out both the maximum and minimum of the numbers instead
#  of the average.

user_input = input("Enter a number: ")
current_num = 0
total = 0
count = 0
# average = 0
valid_input = False
min_value = None
max_value = None

#checks that the user put in a valid int or float

while user_input != "done" :
    try :
        current_num = int(user_input)
        valid_input = True
    except :
        print("Invalid input")
        valid_input = False

    if valid_input :
        total = total + current_num
        count = count + 1
        if min_value is None :
            min_value = current_num
            max_value = current_num
        elif current_num < min_value :
            min_value = current_num
        elif current_num > max_value :
            max_value = current_num

    user_input = input("Enter a number: ")

# average = total / count

print("Maximum is", max_value)
print("Minimum is",min_value)

# test cases should match below expected outputs
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 4 7
