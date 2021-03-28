# Exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages
# from each person using a dictionary.
#
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the
# list in reverse order and print out the person who has the most commits.

file_name = input("Enter a file name: ")

if len(file_name) < 1 :
    file_name = "mbox-short.txt"

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

# print(email_dict)

email_count = []

for k,v in email_dict.items() :
    email_count.append((v, k))
email_count = sorted((email_count), reverse = True)

print(email_count[0][1], email_count[0][0])
