# Exercise 3: Write a program to read through a mail (ie. log mbox-short.txt)
# build a histogram using a dictionary to count how many messages have come
# from each email address, and print the dictionary.

file_name = input("Enter a file name: ")

fhand = open(file_name)

email_dict = {}


for line in fhand :
    words = line.split()

    if len(words) < 2 or words[0] != "From" :
        continue

    # since email is always the 2nd and we always now have
    # word lists at least 2 words long we can use the get default
    # method for dictionaries to add and add to specific emails
    email_dict[words[1]] = email_dict.get(words[1], 0) + 1

print(email_dict)
