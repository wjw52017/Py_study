import time

def climb(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb(n-1)+climb(n-2)

if __name__=='__main__':
    start = time.time()

    result = climb(33)

    end = time.time()
    print end - start

    print result