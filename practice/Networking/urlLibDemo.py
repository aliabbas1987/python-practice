import urllib.request
try:
    ur = urllib.request.urlopen("http://nitb.ddns.net:10030/")
    content=ur.read()
except urllib.error.HTTPError:
    print("url not avialable")
    exit()

f = open("ministrywebsite.html",'wb')
f.write(content)
f.close()

try:
    urllib.request.urlretrieve("https://www.raileurope.com/white-label/overseas/img/re_logo.png", "test.png")
except urllib.error.HTTPError:
    print("url not avialable")
    exit()