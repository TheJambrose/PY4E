user_score = input("Enter Score: ")
response = str()

#Error Test check for float
try:
    score = float(user_score)
except:
    print("Bad score")
    quit()

if score < 0.0 :
    print("Bad score")
elif score < 0.6 :
    print("F")
elif score < 0.7 :
    print("D")
elif score < 0.8 :
    print("C")
elif score < 0.9 :
    print("B")
elif score <= 1.0 :
    print ("A")
else :
    print("Bad Score")
