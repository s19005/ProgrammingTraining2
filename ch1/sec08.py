def cipher(s):
    result = ''
    for c in s:
        result += chr(219 -ord(c)) if c.islower() else c
    return result

s = input('メッセージを入力して下さい: ')
print(cipher(s))
