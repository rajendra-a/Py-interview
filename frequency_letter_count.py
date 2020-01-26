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