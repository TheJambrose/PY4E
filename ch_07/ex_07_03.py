# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun,
# they add a harmless Easter Egg to their program. Modify the program that
# prompts the user for the file name so that it prints a funny message when
# the user types in the exact file name “na na boo boo”. The program should
# behave normally for all other files which exist and don’t exist.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try:
    fh = open(fname)
except :
    print("File cannot be opened.")
    quit()

count = 0
current_index = 0
total_spam_conf = 0
spam_confidence_as_float = 0
average_spam_conf = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    #found some spam confidence, now count it
    count = count + 1
    # print(count)

    #grab the index of the colon and find the remaing text on the line ie. the
    # spam confidence values
    current_index = line.find(":")
    spam_conf_as_str = line[ current_index + 1 : ]

    #clean the whitespace and convert to a float
    spam_confidence_as_float = float(spam_conf_as_str.strip())

    #add spam_confidence_as_float to total
    total_spam_conf = total_spam_conf + spam_confidence_as_float
    # print(type(spam_confidence_as_float))
    # print(total_spam_conf)
    # print(line)
#compute average confidence
average_spam_conf = total_spam_conf / count

print("Average spam confidence:", average_spam_conf)
