
def dow(y,m,d):
    list = [0,3,2,5,0,3,5,1,4,6,2,4]
    y -= m < 3
    return (y+y/4-y/100+y/400+list[m-1]+d)%7

if __name__ == '__main__':
    year = input("please input year:")
    month = input("please input month:")
    day = input("please input day:")
    print "this day is week"
    print dow(year,month,day)