import urllib2
import sys
import json
import re
import sqlite3

reload(sys)
sys.setdefaultencoding('utf-8')

skill = []          #技能
skilldes =[]        #技能说明
skillQ = []
skillQdes =[]
skillW = []
skillWdes =[]
skillE = []
skillEdes =[]
skillR = []
skillRdes =[]


def getContext(url):    #获取技能介绍
    try:
        response = urllib2.urlopen(url)
    except Exception,e:
        print "open url error"
    context = response.read()

    return context

def getHero():      #获取英雄信息
    with open("hero.json",'r') as f:
        text = f.read()
    jsonstr = json.loads(text)
    #print jsonstr["keys"]
    hero = jsonstr["data"].keys()
    name = []
    title = []
    id = []

    for h in hero:
        ahero = jsonstr["data"][h]
        name.append(ahero['name'])
        title.append(ahero['title'])
        id.append(ahero['id'])

    #print name[0],title[0],id[0]
    return name,title,id

def getHeroSkill(context,i):
    pattern = re.compile(r'{\"data.*}')
    search = pattern.search(context)
    str = search.group(0)
    jsonstr = json.loads(str)

    skill.append(jsonstr["data"]["passive"]["name"])
    skilldes.append(jsonstr["data"]["passive"]["description"])
    skillQ.append(jsonstr["data"]["spells"][0]["name"])
    skillQdes.append(jsonstr["data"]["spells"][0]["description"])
    skillW.append(jsonstr["data"]["spells"][1]["name"])
    skillWdes.append(jsonstr["data"]["spells"][1]["description"])
    skillE.append(jsonstr["data"]["spells"][2]["name"])
    skillEdes.append(jsonstr["data"]["spells"][2]["description"])
    skillR.append(jsonstr["data"]["spells"][3]["name"])
    skillRdes.append(jsonstr["data"]["spells"][3]["description"])



if __name__=='__main__':

    name,title,id = getHero()
    defaultUrl = "http://lol.qq.com/biz/hero/"
    j = 0
    for i in id:
        context = getContext(defaultUrl+i+'.js')
        #print name[j]
        getHeroSkill(context,j)
        j = j + 1

    try:
        con = sqlite3.connect("hero.db")
    except:
        print "connection error!"

    try:        #创建表
        con.execute('''CREATE TABLE heros
       (id TEXT PRIMARY KEY     NOT NULL,
        name       TEXT    NOT NULL,
        title      TEXT    NOT NULL,
        skill          TEXT    NOT NULL,
        skilldes          TEXT    NOT NULL,
         skillQ          TEXT    NOT NULL,
        skillQdes          TEXT    NOT NULL,
         skillW          TEXT    NOT NULL,
        skillWdes          TEXT    NOT NULL,
         skillE          TEXT    NOT NULL,
        skillEdes          TEXT    NOT NULL,
         skillR          TEXT    NOT NULL,
        skillRdes          TEXT    NOT NULL
       )''')
        print "create table successful"
    except:
        print "create table error! "
    t = 0
    for i in id:
        sid = id[t]
        print sid
        sname = name[t]
        stitle = title[t]
        sskill = skill[t]
        sskilldes = skilldes[t]
        sskillQ = skillQ[t]
        sskillQdes = skillQdes[t]
        sskillW = skillW[t]
        sskillWdes = skillWdes[t]
        sskillE = skillE[t]
        sskillEdes = skillEdes[t]
        sskillR = skillR[t]
        sskillRdes = skillRdes[t]
        con.execute("INSERT INTO heros (id,name,title,skill,skilldes,skillQ,skillQdes,skillW,skillWdes,skillE,skillEdes,skillR,skillRdes) \
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
                  ,(sid,sname,stitle,sskill,sskilldes,sskillQ,sskillQdes,sskillW,sskillWdes,sskillE,sskillEdes,sskillR,sskillRdes))
        t = t + 1
        con.commit()
    con.close()




