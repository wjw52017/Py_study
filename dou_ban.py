#coding=utf-8
import urllib2
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def getTag(url):
    try:
         response = urllib2.urlopen(url)
    except Exception,e:
        print "open error"
    context = response.read()

    soup = BeautifulSoup(context,"html.parser")
    for tag in soup.find_all('table','tagCol'):
        d = tag.get_text()
        with open("E:\\douban.txt","a") as f:
            f.write(d)

        #for h in tag.find_all("a"):
            #print h.get("href")


if __name__ == '__main__':
    url = "https://book.douban.com/tag/?icn=index-nav"
    getTag(url)

