#Both num1 and num2 contains only digits(0-9).
#BOth num1 and num2 does not contain any leading zero.
#Approach1
def add_strings(num1, num2):
    eval(num1) + eval(num2)
    return str(eval(num1)+eval(num2))


#Given a string of length one, the ord function returns an integer representing the unicode point of
#Characher when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string

#Approach2
def add_strings2(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1-1)), 10**(len(num2-1))
    
    for i in num1:
        n1 += (ord(i)-ord("0")) * m1
        m1 = m1//10

    for i in num2:
        n2 += (ord(i)-od("0")) * m2
        m2 = m2//10

    return str(n1 + n2)


print(add_strings("str1"+ "str2"))
