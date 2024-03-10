import binascii

with open(file='1.txt', mode='r') as f:
    with open(file='hex2strings.txt', mode='wb') as j:
        for i in f.readlines():
            j.write(binascii.unhexlify(i[:-1]))

