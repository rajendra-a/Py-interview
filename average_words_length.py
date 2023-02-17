sentence1 = "Hi, all, my name is Rajendra...I am from india."
sentence2 = "I need to work very hard to learn more about algorithms in python."

# first remove all punctuations
def average_len_words(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p,'')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)

print(average_len_words(sentence1))




