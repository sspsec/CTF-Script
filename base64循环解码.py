import base64


def base64decode():
    f = open('flag.txt', 'rb')
    flag = f.read()
    while b'flag' not in flag:
        flag = base64.b64decode(flag)
    print(flag)


if __name__ == '__main__':
    print('Start...')
    base64decode()
    print('Done!')
