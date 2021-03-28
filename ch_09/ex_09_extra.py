import string

fname = input("Enter file name: ")

if len(fname) < 1 :
    fname = 'clown.txt'

hand = open(fname)

di = dict()

for line in hand :
    line = line.rstrip()
    # print(line)
    #remove formatting and punctuation
    line = line.translate(line.maketrans("","", string.punctuation))
    line = line.lower()
    wds = line.split()
    # print(wds)
    for word in wds:
        di[word] = di.get(word, 0) + 1


# print(di)

#now find the most common word
big_count = None
big_word = None
for word,count in di.items() :
    if big_count is None or count > big_count :
        big_count = count
        big_word = word
    else :
        continue
print(f"The most common word is '{big_word}'' used {big_count} time(s).")

sorted_keys = sorted(di.keys())

# print(sorted_keys)
