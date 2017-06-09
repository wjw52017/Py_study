import time

def getway(n,dict):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if dict.has_key(n):
        return dict.get(n)
    else:
        value = getway(n-1,dict)+getway(n-2,dict)
        dict[n] = value
        return value

if __name__ == '__main__':
    start = time.time()
    dict = {}
    result = getway(33,dict)
    end = time.time()
    print end -start
    print result