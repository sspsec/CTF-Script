import os.path

flag = ""
for i in range(1, 87):
    path = str(i) + ".jpg"
    num = os.path.getsize(path)
    with open(path, "rb") as f:
        f.seek(int(num) - 100)  # 移动文件光标到倒数第一百个字节
        s = f.read(100)
        flag += bytes.decode(s)

print(flag)
