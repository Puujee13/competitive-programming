text = input()
word = text.count(' ') + 1
count = len(text)
print(word)
print(count-word-1)
print(round(count-word / word))