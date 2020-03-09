string = "Rajendra"
count = { }
for letter in string: # for every letter in string
    if letter in count: # if letter is already in count
        count[letter] += 1  # add 1 to that letter key
    else:
        count[letter] = 1
print(count)


def printRLEs(s):

    i=0
    while(i < len(s)-1):

        # counting occurences
        count = 1

        while s[i] == s[i+1]:

            i += 1
            count += 1

            if i + 1 == len(s):
                break
        
        print(str(s[i])+ str(count), end=" ")

        i += 1

    print()


printRLEs('success')