# The basic outline of this problem is to read the file, look for integers
#using the re.findall(), looking for a regular expression of '[0-9]+' and then
#converting the extracted strings to integers and summing up the integers.
import re

fhand = open("regex_sum_1194587.txt")
line_num = []
running_total = int()
for line in fhand :
    line = line.rstrip()
    line_num = re.findall('[0-9]+', line)
    if len(line_num) < 0 : continue

    for num in line_num :
        running_total += int(num)
        print(running_total)
