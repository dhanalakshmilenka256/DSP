page="welcome to <a href='www.yahoo.com'>hello"
print(page)
def geturl(page):
    a=page.find('<a href')
    b=page.find("'",a)
    c=page.find("'",b+1)
    url=page[b+1:c]
    return url
url=geturl(page)
print(url)
