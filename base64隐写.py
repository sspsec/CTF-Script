import base64

base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'  # Base64编码表 按顺序的
flag = ''
bin_str = ''
res = ''
with open('come.txt', 'rb') as f:
    for line in f.readlines():
        print(line)
        initial_b64 = str(line, 'utf-8').strip('\r\n')
        standard_b64 = str(base64.b64encode(base64.b64decode(initial_b64)), 'utf-8').strip('\r\n')  # 转换成标准的base64编码
        offset = abs(
            base64chars.index(initial_b64.replace('=', '')[-1]) - base64chars.index(standard_b64.replace('=', '')[-1]))
        # 计算偏移量 用已经base64隐写后的字符串最后一位字符对应的编码值 减去 标准base64加密后的字符串最后移位的编码值 并取绝对值
        equalnum = initial_b64.count('=')  # 计算等于号有几个

        if equalnum:
            bin_str += bin(offset)[2:].zfill(equalnum * 2)  # 将偏移量转换为二进制并累加 最高为4位二进制位（两个等于号）

        for i in range(0, len(bin_str), 8):
            res += chr(int(bin_str[i:i + 8], 2))  # 以8位为一个字符遍历出来

        print(res, end='')
