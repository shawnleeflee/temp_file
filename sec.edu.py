import urllib2
def unzip(data):
        import gzip
        import StringIO
        data = StringIO.StringIO(data)
        gz = gzip.GzipFile(fileobj=data)
        data = gz.read()
        gz.close()
        return data
header = {
"Host": "202.120.7.201:8002",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
"Accept": "*/*",
"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"X-Requested-With": "XMLHttpRequest",
"Referer": "http://202.120.7.201:8002/",
"Connection": "keep-alive",
}
url = "http://202.120.7.201:8002/query.php"

f = file('sec.edu.port.txt','w')
for i in range(256*256):   
    data = '{"port":"'+str(i)+'"}'
    req = urllib2.Request(url,data,headers=header)
    try:
        res = urllib2.urlopen(req)
    except:
        pass
    content = res.read()
    if content != '[]':
        try:
            temp =  unzip(content)
            f.write(temp)
            print temp
        except:
            f.write(content)
            print content
            
f.close()