

def rotation(array, s):

    s %= len(array) # to shift more than 5 times 

    #s *= -1  # to reverse the direction 

    shifted_array = array[s: ] + array[ :s]

    return shifted_array

print(rotation([1, 2, 3, 4, 5], 4))