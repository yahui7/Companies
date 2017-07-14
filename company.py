import re
import urllib.request

url = "http://money.cnn.com/data/dow30/"
html = urllib.request.urlopen(url).read()
html = str(html)
pat_name = '<td class="wsod_firstCol">.*?<\/td>'
htm_names = re.compile(pat_name).findall(html)
htm_names = str(htm_names)
pat_name1 = '<span title=.*?<'
com_names = re.compile(pat_name1).findall(htm_names)
names = list()
for item in com_names:
    name1 = item.split('>')
    name = name1[1].split('<')
    names.append(name[0])
print(names)

pat_price = '<td class="wsod_aRight">.*?<\/span>'
data = re.compile(pat_price).findall(html)
pat_price1 = '<span stream="last_.*?" class=".*?">[0-9].*?<\/span>'
data = str(data)
data1 = re.compile(pat_price1).findall(data)
prices = list()
for item in data1:
    price1 = item.split('>')
    price = price1[1].split('<')
    prices.append(price[0])
print(prices)
