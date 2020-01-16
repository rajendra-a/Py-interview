string = input("enter a string: ")
s1 = string
s2 = string[::-1]
if s1 == s2:
    print(string ,"is a palindrome")
else:
    print(string, "is not a palindrome")