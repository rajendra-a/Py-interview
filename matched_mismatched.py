# Given two sentences,return an array that has the words that appear in one sentence 
# and not the other and an array with the words in common.
sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def matched_mismatched(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
    return sorted(list(set1^set2)), sorted(list(set1&set2))

print(matched_mismatched(sentence1, sentence2))