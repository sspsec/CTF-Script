from collections import Counter

filename = '11.txt'
result = {}
with open(file=filename, mode='r') as f:
    text = f.read()
    dic = Counter(text).most_common()
    for i in dic:
        print(i[0], end='')
