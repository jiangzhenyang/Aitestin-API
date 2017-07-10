import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

iplist = ['101.28.174.138:80', '116.62.10.152:80', '175.155.24.22:808']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)



'''
代理
步骤：
1.参数是一个字典{'类型':'代理的IP：端口号'}
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

2.定制、创建一个opener
opener = urllib.request.build_opener(proxy_support)

3a.安装opener
urllib.request.install_opener(opener)

3b.调用opener
opener.open(url)

'''
