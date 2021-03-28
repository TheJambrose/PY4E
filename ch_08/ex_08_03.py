# Exercise 3: Rewrite the guardian code in example two without two if
# statements. Instead, use a compound logical expression using the or logical
# operator with a single if statement.

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    #guards for upt to potentially 2 word lists instead of just empty
    if len(words) < 3 or words[0] != 'From' :
        continue
    print(words[2])
