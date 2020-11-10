#Given an array what is the most frequently occuring element
#You can given list or array as input.
def most_frequent(lst):
    count = { }
    max_count = 0
    max_item = None

    for i in lst:
        if i not in count: # item from the list not in dictionary
            count[i] = 1    # dictionary key value "1"

        else:
            count[i] += 1  # else it increament the value of key by 1

        if count[i] > max_count: # if the key value is greater than 0(max_count)
            max_count = count[i] # max_count = key value
            max_item = i         # after iterations we will get greatest value in from the dictionry key

    return max_item


print(most_frequent("rajendra reddy"))
