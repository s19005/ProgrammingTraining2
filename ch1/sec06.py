sentence1 = 'paraparaparadise'
sentence2 = 'paragraph'

X = []
Y = []

for i in range(len(sentence1) - 1):
    X += [sentence1[i:i + 2]]

for i in range(len(sentence2) - 1):
    Y += [sentence2[i:i + 2]]

setX = set(X)
print('X:' + str(setX))
setY = set(Y)
print('Y:' + str(setY))

union = setX | setY
print('和集合: ', union)

intersection = setX & setY
print('積集合: ', intersection)

difference = setX - setY
print('差集合: ', difference)

def in_se(li):
    if 'se' in li:
        return '含まれます'
    else:
        return '含まれません'

print('seはXに' + in_se(X))
print('seはYに' + in_se(Y))
