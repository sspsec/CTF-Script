import binascii

with open('flag.txt', 'r') as s:
    s = s.read()
    out = open('2.docx', 'wb')
    out.write(binascii.a2b_hex(s))
    out.close()
