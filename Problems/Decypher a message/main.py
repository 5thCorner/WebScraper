s = bytes(input(), encoding='utf-8')
n = (int(input())).to_bytes(2, byteorder='little')
key = sum(n)
for i in range(len(s)):
    print(chr(key + s[i]), end='')
