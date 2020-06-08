sentence = "I am an NLPer"
sentencelist = sentence.split()
sentence2 = ''.join(sentencelist)

n = 2
word_bi_gram = []
cha_bi_gram = []

for i in range(len(sentencelist) - 1):
    word_bi_gram += [''.join(sentencelist[i:i + n])]

for i in range(len(sentence2) - 1):
    cha_bi_gram += [sentence2[i:i + n]]

print('単語bi-gram: ', word_bi_gram)
print('文字bi-gram: ', cha_bi_gram)
