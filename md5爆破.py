import hashlib

dic = '0123456789qazwsxedcrfvtgbyhnujmikolp'

for a in dic:
    for b in dic:
        t = (str(a) + str(b)).encode(encoding='UTF-8')
        md5 = hashlib.md5(t).hexdigest()
        if md5[1:2] == md5[14:15] and md5[14:15] == md5[17:18]:
            if (int(md5[1:2]) + int(md5[14:15]) + int(md5[17:18])) / int(md5[1:2]) == int(md5[31:32]):
                print(t)
