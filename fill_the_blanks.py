# Given array containing None values fill in the None values with most recent not None value
nums = [1, None, 2, 3, None, None, 5, None]
def fill_the_blanks(array):
    valid = 0
    result = []
    for i in array:
        if i is not None:
            result.append(i)
            valid = i
        else:
            result.append(valid)
    return result

print(fill_the_blanks(nums))