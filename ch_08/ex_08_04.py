# 8.4 Open the file romeo.txt and read it line by line. For each line, split
# the line into a list of words using the split() method. The program should
# build a list of words. For each word on each line check to see if the word
# is already in the list and if not append it to the list. When the program
# completes, sort and print the resulting words in alphabetical order.
fname = input("Enter file name: ")

file_handle = open(fname)
word_list = []

# go through each line of the file
for line in file_handle :
    # split each line into a list of words by whitespace
    words = line.split()

    for word in words:
        # If the word list already contains a word skip it, otherwise append it
        # to the list
        if word_list.count(word) != 0:
            continue
        word_list.append(word)

#sort the list direclty
word_list.sort()
print(word_list)
