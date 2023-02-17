def find_second_largest(lst):
  lst.sort()  # Ascending order 1......100
  return lst[-2]


print(find_second_largest([3, 4, 5, 6, 9, 7, 12, 8]))