import base64
import re

f = open('secenc.txt').read().encode('utf-8')

while True:
    if re.match('^[2-7A-Z=]+$', f.decode('utf-8')):
        f = base64.b32decode(f)
    elif re.match('^[0-9a-zA-Z+/=]+$', f.decode('utf-8')):
        f = base64.b64decode(f)
    else:
        print(f.decode('utf-8'))
        break
