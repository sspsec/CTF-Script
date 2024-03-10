import base64

with open(file='1.txt', mode='r') as f:
    bincode = base64.b64decode(f.read())

    filename = open('flag.rar', 'wb')
    filename.write(bincode)
    filename.close()
    print('succeed！！！')
