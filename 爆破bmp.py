import struct
import zlib

f = open('misc31.bmp', 'rb')
c = f.read()
width = c[18:22]
height = c[22:26]
# 爆破bmp宽度
for i in range(900, 1100):
    f1 = open(str(i) + '.bmp', 'wb')
    # print(struct.pack('>i',i)[::-1])
    img = c[:18] + struct.pack('>i', i)[::-1] + c[22:]
    f1.write(img)
    f1.close()
