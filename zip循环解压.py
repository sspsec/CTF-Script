import zipfile

filename = '0573'

while True:
    file = zipfile.ZipFile(filename + '.zip', 'r')
    file.extractall(pwd=bytes(filename, encoding='utf-8'))
    for i in file.namelist():
        print(i[:-3:1])
        filename = i[:-4:1]
