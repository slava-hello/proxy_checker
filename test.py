import urllib.request , socket

socket.setdefaulttimeout(180)

# read the list of proxy IPs in proxyList
with open('text.txt', 'r') as file:

    proxyList = file.readlines()[1:]# there are two sample proxy ip
print(proxyList)
def is_bad_proxy(pip, type):
    try:
        proxy_handler = urllib.request.ProxyHandler({type: pip})
        print(1)
        opener = urllib.request.build_opener(proxy_handler)
        print(2)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        print(3)
        urllib.request.install_opener(opener)
        print(4)
        sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
        #sock=urllib.urlopen(req)
        print(5)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print( "ERROR:", detail)
        return 1
    return 0
good = []
print(5)
for item in proxyList:
    if len(good) >= 5:
        quit()
    a = item.split(', ')
    if is_bad_proxy(a[0], a[1][:-2]):
        print ("Bad Proxy", item)
    else:
        print (item, "is working")
        good.append(item)

