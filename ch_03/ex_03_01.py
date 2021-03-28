user_hours = input("Enter Hours: ")
user_rate = input("Enter Rate: ")
pay = float()

# Check that the user entered numbers
try:
    hours = float(user_hours)
    rate = float(user_rate)
except:
    print("Error, please enter numeric input")
    quit()

# check if eligible for overtime
if hours <= 40.0:
    # print("Regular.")
    pay = round(rate * hours, 2)
else:
    # print("Overtime.")
    overtime_hours = hours - 40
    overtime_pay = round((overtime_hours * rate) * 1.5, 2)
    hours = hours - overtime_hours
    pay = round((hours * rate) + overtime_pay, 2)



print(pay)
