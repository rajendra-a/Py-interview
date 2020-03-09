def largest_sum(array):
    if len(array) == 0:
        return print("Too small")

    max_sum = current_sum = array[0]

    for num in array:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
        
    return max_sum

print(largest_sum([1, -2, -3, 4, 5, -2, -6]))