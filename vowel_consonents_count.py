def count(string):
    vowel_count = 0
    consonent_count = 0
    vowels = "aeiou"
    for char in string:
        if char not in vowels:
            consonent_count += 1
        else:
            vowel_count += 1
    return vowel_count, consonent_count

print(count('rajendra'))
