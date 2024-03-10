import zlib
import struct

filename = "misc35.jpg"
with open(filename, 'rb') as f:
    all_b = f.read()
# w = all_b[159:161]
# h = all_b[157:159]
for i in range(901, 1200):
    name = str(i) + ".jpg"
    f1 = open(name, "wb")
    im = all_b[:159] + struct.pack('>h', i) + all_b[161:]
    f1.write(im)
    f1.close()
