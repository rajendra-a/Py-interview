#Given string, are all characters unique?
#Should give a True or False Return

#Uses Python Built in structures

def unique(string):
    string = string.replace(" ", "")
    return len(set(string)) == len(string)


print(unique("codingraj"))