cipher = '5555555595555A65556AA696AA6666666955'


def iee(cipher):
    tmp = ''
    for i in range(len(cipher)):
        a = bin(eval('0x' + cipher[i]))[2:].zfill(4)
        tmp = tmp + a[1] + a[3]
        print(tmp)
    plain = [hex(int(tmp[i:i + 8][::-1], 2))[2:] for i in range(0, len(tmp), 8)]
    print(''.join(plain).upper())


iee(cipher)
