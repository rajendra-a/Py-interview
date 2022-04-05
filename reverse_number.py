def reverse_number(number):
    string_num = str(number)

    if string_num[0] == '-':
        return int('-'+string_num[:0:-1])
    else:
        return int(string_num[::-1])

def reverse_str(number):
    string = str(number)
    return "".join(reversed(number.split()))


print(reverse_number(3434))