flag = ['灩', '捯', '䍔', '䙻', 'ㄶ', '形', "楴", '獟', '楮', '獴', '㌴', '摟', '潦', '弸', '彤', '㔲', '挶', '戹', '㍽']

result = ''

for i in range(len(flag)):
    for j in range(126):
        if 0 < ord(flag[i]) - (j << 8) <= 126:
            result += chr(j) + chr(ord(flag[i]) - (j << 8))

print(result)
