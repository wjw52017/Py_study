#coding=utf-8
import urllib2
import sys
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from colorama import init,Fore,Style

reload(sys)
sys.setdefaultencoding('utf-8')

def getTag(url):
    try:
         response = urllib2.urlopen(url)
    except Exception,e:
        print "open error"
    context = response.read()

    soup = BeautifulSoup(context,"html.parser")
    text = []
    for tag in soup.find_all('table','tagCol'):
        d = tag.get_text()
        text.append(d)
    return text
        #with open("E:\\douban.txt","a") as f:
            #f.write(d)

        #for h in tag.find_all("a"):
            #print h.get("href")


if __name__ == '__main__':
    url = "https://book.douban.com/tag/?icn=index-nav"
    text = getTag(url)

    #处理中文乱码
    #rigth_text = str(text).replace('u\'', '\'')
   # result =  rigth_text.decode("unicode-escape")
    #print result[]

    x = PrettyTable(['name'])   #输出格式处理
    x.align["name"] = "l"
    x.padding_width = 1
    for r in text:
        x.add_row([r])
    init(autoreset=True)
    print Fore.RED + Style.BRIGHT + '书籍种类 and 数量 '
    print x

