from PIL import Image

x = 200  # x坐标  通过对txt里的行数进行整数分
y = 200  # y坐标  x * y = 行数
im = Image.new('RGB', (x, y))
file = open('qr.txt')

for i in range(0, x):
    for j in range(0, y):
        line = file.readline()  # 获取一行的rgb值
        line = line[:-2]
        line = line[1:]
        # print(line)
        rgb = line.split(', ')  # 分离rgb，文本中逗号后面有空格
        im.putpixel((i, j), (int(rgb[0]), int(rgb[1]), int(rgb[2])))
im.save('flag.png')
