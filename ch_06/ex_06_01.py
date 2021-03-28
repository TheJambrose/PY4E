# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

fruit = 'banana'
indexes = len(fruit) - 1

while indexes >= 0:
    letter = fruit[indexes]
    print(letter)
    indexes = indexes - 1
