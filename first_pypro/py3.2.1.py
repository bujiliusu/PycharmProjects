# import urllib2
# response = urllib2.urlopen('http://www.zhihu.com')
# html = response.read()
# print html

# import urllib2
# import urllib
# url = 'http://58.240.54.194:1688/users/login/?next=/'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# referer = 'http://58.240.54.194:1688/users/'
# postdata = {'username' : 'admin',
#             'password' : 'eMic_NEt_1106-1!'}
# headers = {'User-Agent': user_agent, 'Referer' : referer}
# data = urllib.urlencode(postdata)
# req = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(req)
# html = response.read()

# import urllib2
# import cookielib
#
# cookie = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open('http://www.zhihu.com')
# for item in cookie:
#     print item.name+':'+item.value

# import urllib2
# opener = urllib2.build_opener()
# opener.addheaders.append(('cookie', 'email='+"bujilisu@163.com"))
# req = urllib2.Request("http://www.zhihu.com")
# response = opener.open(req)
# print response.headers
# retdata = response.read()

# import urllib2
# import socket
# socket.setdefaulttimeout(10)
# urllib2.socket.setdefaulttimeout(10)
# import urllib2
# request = urllib2.Request("http://www.zhihu.com")
# response = urllib2.urlopen(request, timeout=10)
# html = response.read()
# print html

# import urllib2
# try:
#     response = urllib2.urlopen("http://www.google.com")
#     print response
# except urllib2.HTTPError as e:
#     if hasattr(e, 'code'):
#         print 'Error code:', e.code

# import urllib2
# response = urllib2.urlopen('http://www.zhihu.com')
# isRedirected = response.geturl() == 'http://www.zhihu.com'

# import urllib2
# class RedirectHandler(urllib2.HTTPRedirectHandler):
#     def http_error_301(self, req, fp, code, msg, headers):
#         pass
#     def http_error_302(self, req, fp, code, msg, headers):
#         result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
#         result.status = code
#         result.newurl = result.geturl()
#         return result
# opener = urllib2.build_opener(RedirectHandler)
# opener.open('http://www.zhihu.cn')

import urllib2
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener([proxy,])
urllib2.install_opener(opener)
response = urllib2.urlopen("http://www.zhihu.com")
print response.read()


