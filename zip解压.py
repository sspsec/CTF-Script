import zipfile

for i in range(1, 87):
    zFile = zipfile.ZipFile(str(i) + '.zip', 'r')
    zFile.extractall(path="D:\\work")