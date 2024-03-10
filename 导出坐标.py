import re

str_ = ""
str_list = []
with open('flag.txt') as f:
    for i in f.readline():
        str_ += i
        if str_[-1] == ")":
            str_ = "".join(re.findall("\(.*\)", str_))
            str_list.append(str_.strip('(').strip(')'))
            str_ = ""

with open('rgb.txt', 'w') as f:
    for i in str_list:
        f.write(i + '\n')
