#Non repeat element 
# 
def non_repeat(string):
    string = string.replace(" ", "")

    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1

        else:
            char_count[char] = 1

    for char in string:
       if char_count[char] == 1:
           return char
    
    return None

print(non_repeat("rajendra"))


    


