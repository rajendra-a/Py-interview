k = open('demofile4.txt', 'r', encoding='utf-8')
count = 0
text = k.read()
for char in text:
    if char.isupper():
        count += 1
