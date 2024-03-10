# -*- coding:utf-8 -*-
import string

ciphertext = 'PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}'
secretkey = 'lovekfcabdghijmnpqrstuwxyz'
plaintext = ''

for letter in ciphertext:
    if letter in string.ascii_lowercase:
        index = secretkey.lower().index(letter)
        plaintext += string.ascii_lowercase[index]
        continue
    if letter in string.ascii_uppercase:
        index = secretkey.upper().index(letter)
        plaintext += string.ascii_uppercase[index]
        continue
    plaintext += letter

print(plaintext)