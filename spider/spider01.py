from urllib import request
from urllib import parse
from urllib.request import urlopen
import urllib
response=request.urlopen('http://www.zhihu.com')
html=response.read()
print(html)