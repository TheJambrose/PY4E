hours_worked = float(input("How many hours do you work each week:"))

pay_per_hour = float(input("Please input your hourly wage:"))

weekly_pay = round(hours_worked * pay_per_hour, 2)

monthly_pay = round(weekly_pay * 4, 2)

yearly_pay = round(weekly_pay * 52, 2)

print(f"Pay: {weekly_pay}")
