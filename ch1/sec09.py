import random

sentence = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
li1 = sentence.split()
li2 = []

for word in li1:
    if len(word) <= 4:
        li2 += [word]
    else:
        li3 = list(word[1:len(word) - 1])
        random.shuffle(li3)
        li2 += [word[0] + ''.join(li3) + word[len(word) - 1]]

print(' '.join(li2))
