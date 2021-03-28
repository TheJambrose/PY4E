# Ex4.6 Exercise 6: Rewrite your pay computation with time-and-a-half for
# overtime and create a function called computepay which takes two parameters
# (hours and rate).

user_hours = input("Enter Hours: ")
user_rate = input("Enter Rate: ")

def computepay(hours: int, rate: int) -> int:
    # check if eligible for overtime
    if hours <= 40.0:
        pay = round(rate * hours, 2)

    else:
        overtime_hours = hours - 40
        overtime_pay = round((overtime_hours * rate) * 1.5, 2)
        hours = hours - overtime_hours
        pay = round((hours * rate) + overtime_pay, 2)

    return pay

# Check that the user entered numbers
try:
    hours = float(user_hours)
    rate = float(user_rate)
except:
    print("Error, please enter numeric input")
    quit()

pay = computepay(hours, rate)


print("Pay", pay)
