#Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e., the
# whole email address). At the end of the program, print out the contents of
# your dictionary.

file_name = input("Enter a file name: ")

fhand = open(file_name)

domain_dict = {}

for line in fhand :
    words = line.split()

    #standard guard statement for emails
    if len(words) < 2 or words[0] != "From" :
        continue

    emails_and_domain = words[1].split(sep = "@")
    # print(emails_and_domain)
    domain_dict[emails_and_domain[1]] = domain_dict.get(emails_and_domain[1], 0) +1

print(domain_dict)
print(list(domain_dict))

thing = domain_dict.keys()

print(thing)

thing2 = domain_dict.items()
print(thing2)
