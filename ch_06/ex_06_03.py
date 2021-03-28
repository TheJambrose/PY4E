# Exercise 3: Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)


def count(string_to_search: str, letter_to_find: str) :
    count = 0
    for char in string_to_search :

        if char == letter_to_find :
            count = count + 1

    print(count)

count("banana", "a")
