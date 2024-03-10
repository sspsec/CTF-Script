# -*- coding: utf-8 -*-
import hashlib

k = 'TASC?O3RJMV?WDJKX?ZM'
for i in range(26):
    temp1 = k.replace('?', str(chr(65 + i)), 1)
    for j in range(26):
        temp2 = temp1.replace('?', chr(65 + j), 1)
        for n in range(26):
            temp3 = temp2.replace('?', chr(65 + n), 1)
            s = hashlib.md5(temp3.encode('utf8')).hexdigest().upper()
            if s[:4] == 'E903':
                print('flag{' + s + '}')
