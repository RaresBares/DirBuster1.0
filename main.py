import sys, requests, time

url = ""
list = ""


def test(fullurl):
    if requests.get(fullurl).status_code == 200:
        return bool(1)
    else:
        return bool(0)


if len(sys.argv) == 2:
    print()
    url = sys.argv[0]
    list = sys.argv[1]
    f = open(list)
    for line in f:
        if test(url+line):
            print("/" + line + " : 200")

else:
    print("python DirBuster.py [URL] [LIST]")
