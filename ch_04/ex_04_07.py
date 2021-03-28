# Exercise 7:
# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.

user_score = input("Enter Score: ")
response = str()

#Error Test check for float
try:
    score = float(user_score)
except:
    print("Bad score")
    quit()

def computegrade(score: str) -> str :
    if score < 0.0 :
        grade = "Bad score"
    elif score < 0.6 :
        grade = "F"
    elif score < 0.7 :
        grade = "D"
    elif score < 0.8 :
        grade = "C"
    elif score < 0.9 :
        grade = "B"
    elif score <= 1.0 :
        grade = "A"
    else :
        grade = "Bad Score"

    return grade


grade = computegrade(score)

print(grade)
