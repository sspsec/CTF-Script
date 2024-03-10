with open(file='edu_doamin.txt', mode='r') as f:
    res_list = []
    lines = f.readlines()
    for i in lines:
        if i not in res_list:
            res_list.append(i)

with open(file='edu_domain.txt', mode='w') as f:
    for i in res_list:
        f.write(i)
