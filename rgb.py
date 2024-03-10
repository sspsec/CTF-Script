from PIL import Image

step = 8
Byte = ""
flag = ""

for i in range(1, 1168, 2):
    path = f"Traffic_Light_wps图片\\Traffic_Light_wps图片_{i}.png"
    image = Image.open(path)
    R = image.getpixel((110, 50))[1]
    Y = image.getpixel((110, 100))[1]
    G = image.getpixel((110, 130))[1]

    if R != 172:
        Byte += "1"
    if Y != 172:
        continue
    if G != 172:
        Byte += "0"

for i in range(0, len(Byte), step):
    flag += chr(int((Byte[i:i + step]), 2))

print(flag)
