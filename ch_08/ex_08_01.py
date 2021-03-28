# Exercise 1: Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None. Then write a function
# called middle that takes a list and returns a new list that contains all but
# the first and last elements.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print(f"List1 before chop() is: {list1}")

print(f"List2 before middle() is: {list2}")


# take off first and last list item.
def chop(list) :
    #no error handling, assumes at least 2 items in list
    #deletes the first item in list. directly alters the list provided!
    del list[0]
    #deletes the last item in list
    del list[len(list) - 1]

    return None

# return a new list that is the middle of a list. Does not actually alter
# the list provided
def middle(list) :
    #copies the list provided, because "new_list = list" would create an alias.
    new_list = list.copy()
    #uses chop on the new list since we are already with this being altered
    chop(new_list)
    return new_list


chop(list1)

list3 = middle(list2)

print(list1)
print(list3)
#confirms the list used in middle() provided is not altered
print(list2)
