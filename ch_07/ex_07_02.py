# 7.2 Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
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
