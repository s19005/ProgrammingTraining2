li = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()

li1 = [li[0], li[4], li[5], li[6], li[7], li[8], li[14], li[15], li[18]]
ele1 = []
li2 = [li[1], li[2], li[3], li[9], li[10], li[11], li[12], li[13], li[16], li[17], li[19]]
ele2 = []

for i in li1:
    st = i[:1]
    ele1 += [st]

for i in li2:
    st = i[:2]
    ele2 += [st]

li3 = li1 + li2
ele = ele1 + ele2
dic = {}

for i in range(len(ele)):
    dic[ele[i]] = li.index(li3[i]) + 1

print(dic)
