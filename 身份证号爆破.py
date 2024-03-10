a = '621022'
b = '5237'


def youxiao(sfz):
    sum = 0
    xym = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    for i in range(0, 17):
        sum = xym[i] * int(sfz[i])
    if sum % 11 == 5:
        return True
    else:
        return False


for i in range(1990, 2001):
    for j in range(1, 13):
        if j < 10:
            j = '0' + str(j)
        for x in range(1, 32):
            if x < 10:
                x = "0" + str(x)
            birth = str(i) + str(j) + str(x)
            sfz = a + str(birth) + b
            if youxiao(sfz):
                print(sfz + "\n")
