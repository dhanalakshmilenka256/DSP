import urllib.request
url='http://www.rguktsklm.ac.in'
resp=urllib.request.urlopen(url)
page1=resp.read()
page=str(page1)
def geturl(page):
    a=page.find('<a href')
    b=page.find("'",a)
    c=page.find("'",b+1)
    url=page[b+1:c]
    return url
while True:
    url,n=geturl(page)
    page=page[n: ]
    if url:
        print(url)
    else:
        break
