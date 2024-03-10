f = open('1.txt')
temp = []
while True:
    k = f.read(3)
    if k:
        temp.append(k)
    else:
        break

f.close()
for i in temp:
    num = '0x' + i
    num = int(num, base=0)
    num = chr(num)
    print(num, end='')
