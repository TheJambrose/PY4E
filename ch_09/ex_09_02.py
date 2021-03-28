# Exercise 2: Write a program that categorizes each mail message by which day
# of the week the commit was done. To do this look for lines that start with
# “From”, then look for the third word and keep a running count of each of the
# days of the week. At the end of the program print out the contents of your
# dictionary (order does not matter).

file_name = input("Enter file name: ")
fhand = open(file_name)

days_dict = {}

for line in fhand :
    words = line.split()
    if len(words) < 3 or words[0] != "From" :
        continue
    day = words[2]
    # if day not in days_dict :
    #     days_dict[day] = 1
    # else :
    #     days_dict[day] += 1
    days_dict[day] = days_dict.get(day, 0) +1
print(days_dict)
