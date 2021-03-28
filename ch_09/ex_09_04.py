# Exercise 4: Add code to the Exercise 3 program to figure out who has the most
# messages in the file. After all the data has been read and the dictionary has
# been created, look through the dictionary using a maximum loop (see
# Chapter 5: Maximum and minimum loops) to find who has the most messages and
# print how many messages the person has

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

#from ex 3
# print(email_dict)


# check for max sender
max_send_email = None
for email in email_dict :
    if max_send_email is None or email_dict[email] > email_dict[max_send_email] :
        max_send_email = email
print(max_send_email, email_dict[max_send_email])
