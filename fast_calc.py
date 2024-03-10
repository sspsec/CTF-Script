import requests
from lxml import etree
import re

url = 'http://114.67.246.176:15618/'
s = requests.Session()
response = s.get(url)

# html = response.text.encode('ISO-8859-1').decode('utf-8')
# html = etree.HTML(html)
# x = html.xpath('//form/text()')
# y = x[1].strip().replace('=', '')
# print(y)
#
# i = s.post(url, data={'v': eval(y)})
#
# print(i.content)

html = response.text.encode('ISO-8859-1').decode('utf-8')
html = etree.HTML(html)
x = html.xpath('//div')[0].text[:-3]
res = eval(x)
data = {
    'value': res
}
i = s.post(data=data, url=url)

print(i.text)
