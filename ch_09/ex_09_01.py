# Write a program that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn’t matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.

file_name = input("Enter file name:")

file_handle = open(file_name)

file_as_dict = dict()

for line in file_handle :
    words = line.split()

    # if len(words) <1 :
    #     continue

    for word in words :
        file_as_dict[word] = "This word was in the text"

print("Dictionary made successfullly")

check_word = input("What word did you want to check for? ")

is_in_dict = check_word in file_as_dict

if is_in_dict :
    print(f"The word '{check_word}' is in {file_name}.")
else :
    print(f"Sorry, the word '{check_word}' cannot be found in {file_name}.")
