import base64
import re
import base91


def baseDec(text, type):
    if type == 1:
        return base64.b16decode(text)
    elif type == 2:
        return base64.b32decode(text)
    elif type == 3:
        return base64.b64decode(text)
    elif type == 4:
        return base64.b85decode(text)
    elif type == 5:
        return base91.decode(text.decode())
    else:
        pass


def detect(text):
    try:
        if re.match("^[0-9A-F=]+$", text.decode()) is not None:
            return 1
    except:
        pass

    try:
        if re.match("^[A-Z2-7=]+$", text.decode()) is not None:
            return 2
    except:
        pass

    try:
        if re.match("^[A-Za-z0-9+/=]+$", text.decode()) is not None:
            return 3
    except:
        pass

    try:
        if re.match("^[A-Za-z0-9$%()*+,-./:;?@[\]^_`{|}~]+$", text.decode()) is not None:
            return 4
    except:
        pass

    try:
        if re.match("^[^-\']+$", text.decode()) is not None:
            return 5
    except:
        pass

    return 5


def autoDec(text):
    floor = 0
    while True:
        try:
            code = detect(text)
            text = baseDec(text, code)
            floor += 1
            print("第{0}层：\n".format(floor), text)
            if not text: break
        except:
            break


if __name__ == "__main__":
    # with open("Autopy/crypto/doc/form",'rb') as f:
    #     content = f.read()
    content = "@iH<,{*;oUp/im\"QPl`yR*ie}NK;.D!Xu)b:J[Rj+6KKM7P@iH<,{*;oUp/im\"QPl`yR".encode()
    autoDec(content)


