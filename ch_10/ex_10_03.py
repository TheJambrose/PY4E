# Exercise 3: Write a program that reads a file and prints the letters in
# decreasing order of frequency. Your program should convert all the input to
# lower case and only count the letters a-z. Your program should not count
# spaces, digits, punctuation, or anything other than the letters a-z. Find text
# samples from several different languages and see how letter frequency varies
# between languages. Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.
import string
# import digits

name = input("Enter file:")
if len(name) < 1 : name = "romeo.txt"
handle = open(name)

letter_dict = {}

for line in handle :
    #remove punctuation
    line = line.translate(line.maketrans("","", string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words :
        for char in word :
            #check if is a letter and skips if it isn't
            if char.isalpha() :
            #adds the character to the dict or increments the value
                letter_dict[char] = letter_dict.get(char, 0) + 1
    # remove digits

# print(letter_dict)

ordered_letter_dict = []
# make a sortable list of key value pairs
for k,v in letter_dict.items() :
    ordered_letter_dict.append((v, k))
#sort and then print the value pairs
for letters in sorted(ordered_letter_dict):
    print(letters[1], letters[0])
