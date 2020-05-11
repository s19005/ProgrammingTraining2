st = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".replace(
    ",", ""
).replace(
    ".", ""
)
li = list(st.split())
pi = []

for i in li:
    num = len(i)
    pi += [num]

print(pi)
