# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

timestamp_list = []
hour_count_dict = {}


for line in handle :
    words = line.split()

    if len(words) < 6 or words[0] != "From":
        continue
        #the hours are always the 6th item and always have two digits so we
        #can grab the hours and then splice the result into the list
    timestamp_list.append(words[5][:2])
# print(timestamp_list)

# now, count the values in the list as a dict
for stamp in timestamp_list :
    hour_count_dict[stamp] = hour_count_dict.get(stamp, 0) + 1

# Grab the dict pairs and sort by the hours key and print pairs
for (k, v) in sorted(hour_count_dict.items()) :
    print(k, v)
