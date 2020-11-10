def check_angram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    #check if same number of letters
    if len(s1) != len(s2):
        return False

    #count frequency of each letter 
    count = { }

    for letter in s1:   # for every letter in first string
        if letter in count:  # if letter is already in dictionary, then
            count[letter] += 1 #  add 1 to the letter
        else:
            count[letter] = 1

    # do reverse for the second string

    for letter in s2:
        if letter in s1:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            return False
         
    return True


x = check_angram("public relations", "crap built on lies")
print(x)
