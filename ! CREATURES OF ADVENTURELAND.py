################################################################################# 
global pygame
global random
global attack
global allyno
global eneno
import random
global mychoice
testing_game = False #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! normalde FALSE
msgtim = []
objtim = []
played = False
progress = True
def date(zone):
        from time import gmtime, strftime
        #strftime("%Y-%m-%d %H:%M:%S", gmtime())
        if zone == "day":
                return int(strftime("%d", gmtime()))
        if zone == "hour":
                return float(strftime("%H.%M", gmtime()))
def cplay(name):
       # return
     #   name = "ost33"
        try:
            pygame.mixer.stop()
        except:
            pygame.mixer.init()
        #pygame.mixer.init()
        #pygame.init()
        filen = name + ".wav"
        try:
            a1Note = pygame.mixer.Sound(filen)
            pygame.mixer.set_num_channels(2)
            a1Note.play()
        except:
            filen = "ostn1" + ".wav"
            a1Note = pygame.mixer.Sound(filen)
            pygame.mixer.set_num_channels(2)
            a1Note.play()
def vplay(name):
        global pygame
        #return
       # pygame.mixer.init()
        filen = name + ".wav"
        try:
                a1Note = pygame.mixer.Sound(filen)
        except:
                return
       # a2Note = pg.mixer.Sound("sound1.wav")

        pygame.mixer.set_num_channels(20)
        a1Note.play()
        return
def wplay(name):
        global pygame
        #return
       # pygame.mixer.init()
        filen = name + ".wav"
        try:
                a2Note = pygame.mixer.Sound(filen)
        except:
                return
       # a2Note = pg.mixer.Sound("sound1.wav")

        pygame.mixer.set_num_channels(20)
        a2Note.play()
        return
def voplay(lst,i):
        #beg#skl#ski#ded#spc#mov
        global pygame
        import time
        name = lst[0].lower()
        pg.mixer.init()
        pg.init()
        filen = "w" + name + i + ".wav"
        try:
            a1Note = pg.mixer.Sound(filen)

            pg.mixer.set_num_channels(3)
            a1Note.play()
        except:
            return
        return
def text_objects1(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
def text_objects2(text, font):
    textSurface = font.render(text, True, (255,0,0))
    return textSurface, textSurface.get_rect()
def text_objects3(text, font):
    textSurface = font.render(text, True, (41,96,90))
    return textSurface, textSurface.get_rect()
def text_objects4(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()
def text_objects6(text, font):
    textSurface = font.render(text, True, (199,56,56))
    return textSurface, textSurface.get_rect()
def text_objects5(text, font):
    textSurface = font.render(text, True, (248,226,177))
    return textSurface, textSurface.get_rect()
def text_objects7(text, font):
    textSurface = font.render(text, True, (18,108,84))
    return textSurface, textSurface.get_rect()
def text_objects8(text, font):
    textSurface = font.render(text, True, (128,128,128))
    return textSurface, textSurface.get_rect()
def text_objects9(text, font):
    textSurface = font.render(text, True, (121,149,196))
    return textSurface, textSurface.get_rect()
def text_objects10(text, font):
    textSurface = font.render(text, True, (163,73,164))
    return textSurface, textSurface.get_rect()
def text_objects11(text, font):
    textSurface = font.render(text, True, (0,64,128))
    return textSurface, textSurface.get_rect()
def text_objects12(text, font):
    textSurface = font.render(text, True, (75,73,112))
    return textSurface, textSurface.get_rect()
def text_objects13(text, font):
    textSurface = font.render(text, True, (0,162,232))
    return textSurface, textSurface.get_rect()
def message(text,hero,size,colour,a,b):
    a = random.choice(range(10,40))
    b = random.choice(range(00,80))
    largeText = pygame.font.Font('freesansbold.ttf',size)
    if colour == "red":
        TextSurf, TextRect = text_objects2(text, largeText)
    elif colour == "s1":
        TextSurf, TextRect = text_objects3(text, largeText)
    elif colour == "white":
        TextSurf, TextRect = text_objects4(text, largeText)
    elif colour == "s3":
        TextSurf, TextRect = text_objects5(text, largeText)
    elif colour == "s4":
        TextSurf, TextRect = text_objects6(text, largeText)
    elif colour == "green":
        TextSurf, TextRect = text_objects7(text, largeText)
    elif colour == "gray":
        TextSurf, TextRect = text_objects8(text, largeText)
    elif colour == "s5":
        TextSurf, TextRect = text_objects9(text, largeText)
    elif colour == "purp":
        TextSurf, TextRect = text_objects10(text, largeText)
    elif colour == "blue":
        TextSurf, TextRect = text_objects11(text, largeText)
    elif colour == "blue2":
        TextSurf, TextRect = text_objects12(text, largeText)
    elif colour == "blue3":
        TextSurf, TextRect = text_objects13(text, largeText)
    else:
        TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (int(round((hero[2][2][3][0]+a-20))),int(round(hero[2][2][3][1]+b-40)))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    numb = False
    try:
        int(text)
        numb = True
    except:
        numb = False
    msgtim.append([TextSurf, TextRect,nowtime(),numb,0,0])
    return TextSurf, TextRect
def lmessage(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = ((x),(y))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    return
def printmessage(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects4(text, largeText)
    TextRect.center = ((x),(y))
    win.blit(TextSurf, TextRect)
    return
def printmessage2(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',10)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = ((x),(y))
    win.blit(TextSurf, TextRect)
    return
def printmessage3(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',10)
    TextSurf, TextRect = text_objects4(text, largeText)
    TextRect.center = ((x),(y))
    win.blit(TextSurf, TextRect)
    return
def printmessage4(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = ((x),(y))
    win.blit(TextSurf, TextRect)
    return
def printmessage5(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = ((x),(y))
    win.blit(TextSurf, TextRect)
    return
def objadd(teff,text,tim):
    if type(text) == str:
        text = text +".png"
        text = pygame.image.load(text)
    if teff[-2] == True:
            if teff[2][2][-1] == 1:
                         teff[2][2][3] = [500,350]
            if teff[2][2][-1] == 2:
                         teff[2][2][3] = [700,550]
            if teff[2][2][-1] == 3:
                         teff[2][2][3] = [500,750]
    if teff[-2] == False:
            if teff[2][2][-1] == 1:
                         teff[2][2][3] = [1400,350]
            if teff[2][2][-1] == 2:
                         teff[2][2][3] = [1200,550]
            if teff[2][2][-1] == 3:
                         teff[2][2][3] = [1400,750]
    obrect = teff[2][2][2].get_rect()
    we, he = obrect.width, obrect.height
    text = pygame.transform.rotozoom(text, 0, 0.6)
    objtim.append([text, tim ,nowtime(),-150,teff[2][2][3][1]-150,0])
    return
def objadd2(teff,text,text2,tim):
    if type(text) == str:
        text = text +".png"
        try:
                text = pygame.image.load(text)
        except:
                return
    if type(text2) == str:
        text2 = text2 +".png"
        try:
                text2 = pygame.image.load(text2)
        except:
                return
    if teff[-2] == True:
            if teff[2][2][-1] == 1:
                         teff[2][2][3] = [500,350]
            if teff[2][2][-1] == 2:
                         teff[2][2][3] = [700,550]
            if teff[2][2][-1] == 3:
                         teff[2][2][3] = [500,750]
    if teff[-2] == False:
            if teff[2][2][-1] == 1:
                         teff[2][2][3] = [1400,350]
            if teff[2][2][-1] == 2:
                         teff[2][2][3] = [1200,550]
            if teff[2][2][-1] == 3:
                         teff[2][2][3] = [1400,750]    
    text = pygame.transform.rotozoom(text, 0, 0.6)
    text2 = pygame.transform.rotozoom(text2, 0, 0.6)
    obrect = teff[2][2][2].get_rect()
    we, he = obrect.width, obrect.height
    #print(teff[2][2][3][0],teff[2][2][3][1])
    objtim.append([[text,text2], tim ,nowtime(),teff[2][2][3][0]-150,teff[2][2][3][1]-150,0])
    return
def acc(accuracy):
        import random
        ran = random.random()*100
        if ran < accuracy:
           return True
        else:
           return False
def fileop(filename):
    filename = str(filename) + ".txt"
    gamepoints = open(filename,"r")
    data11 = gamepoints.readlines()
    datax = []
    for qqq in range(len(data11)):
        line11 = data11[qqq].split()
        datax.append(line11)
    gamepoints.close()
    return datax
def save(xlist,filename):
        filename = str(filename) + ".txt"
        editpoints = open(filename, "w")
        for row in xlist:
                for rrow in row:
                        editpoints.write(str(rrow))
                        editpoints.write(" ")
                editpoints.write("\n")
        editpoints.close()
        return
def battleready(_hero,me,what):
    import random
    some = []
    for nd in _hero:
            some.append(nd)
    _hero = []
    for zzz in some:
            _hero.append(zzz)
    _hero[6] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    _hero[6][14] = random.choice(["MID","OFF"])
    if i == "z":
            _hero[6][14] = random.choice(["UP","MID","DOWN"])
    if i == "m":
            _hero[6][14] = "MID"
    if i == "z":
           if mychoice == "u" and me == True:
                    _hero[6][14] = "UP"
           elif mychoice == "m" and me == True:
                    _hero[6][14] = "MID"
           elif mychoice == "d" and me == True:
                    _hero[6][14] = "DOWN"
    else:
            if mychoice == "d" and me == True:
                    _hero[6][14] = "MID"
            elif mychoice == "a" and me == True:
                    _hero[6][14] = "OFF"   
    #[6][2] = turns
    _hero[6][2] = [0,0,0,0,0,0,0,0,0]
    _hero[6][8] = {} #effects
    atspeed = int(_hero[1][8] + _hero[1][9] + _hero[1][10])
    attack = int(_hero[1][0] + _hero[1][1] + _hero[1][2])
    magicattack = int(_hero[1][4] + _hero[1][5] + _hero[1][6])
    rnge = int(_hero[4])
    _hero[3] = int(_hero[3])
##    if league[-1] == "2" or league[-1] == "9":
##            if "MINION" not in _hero[0].upper():
##                    if _hero[6][5] <= 200:
##                            _hero[3] = int(_hero[3]) + 2000
##                    else:
##                            _hero[3] = int(_hero[3]) + 1000
    #stats
    _hero[6][3] = atspeed 
    _hero[6][4] = attack
    _hero[6][26] = magicattack
    _hero[6][5] = rnge
    _hero[6][6] = _hero[3] #maxheal
    _hero[6][27] = 100 #energy
    _hero[6][29] = 100 
    _hero[6][24] = _hero[3]
    _hero[6][23] = _hero[6][4]
    _hero[6][1] = random.choice(range(10000,1000000)) #code
    pr = "i"+_hero[0].lower()+"p.png"
    try:
        _hero[6][10] = pygame.image.load(pr)
    except:
        if _hero[5][1] == "p":
            pr = "ipr1.png"
            _hero[6][10] = pygame.image.load(pr)
        else:
            _hero[6][10] = 0
    if what == True and _hero[0].upper() == "MINION1":
            resm = "iminion1a.png"
            resm2 = resm
            _hero[6][14] = "OFF"
            if i == "z":
                    _hero[6][14] = random.choice(["UP","DOWN"])
    elif what == False and _hero[0].upper() == "MINION1":
            resm = "iminion1e.png"
            resm2 = resm
            _hero[6][14] = "OFF"
            if i == "z":
                    _hero[6][14] = random.choice(["UP","DOWN"])
    elif what == True and _hero[0].upper() == "MINION2":
            resm = "iminion2a.png"
            resm2 = resm
            _hero[6][14] = "MID"
    elif what == False and _hero[0].upper() == "MINION2":
            resm = "iminion2e.png"
            resm2 = resm
            _hero[6][14] = "MID"
    elif what == True and _hero[0].upper() == "MINION3":
            resm = "iminion3a.png"
            resm2 = resm
            _hero[6][14] = "MID"
    elif what == False and _hero[0].upper() == "MINION3":
            resm = "iminion3e.png"
            resm2 = resm
            _hero[6][14] = "MID"
    else:
            resm = "i"+_hero[0].lower()+".png"
            resm2 = "i"+_hero[0].lower()+"2.png"
            
    if i == "m":
            _hero[6][14] = "MID"
    #try:
    if i == "a":        
            resmr1 = "i"+_hero[0].lower()+"r1.png"
            resmr2 = "i"+_hero[0].lower()+"r2.png"
            resmr3 = "i"+_hero[0].lower()+"r3.png"
            resmra = "i"+_hero[0].lower()+"ra.png"
            resmra2 = "i"+_hero[0].lower()+"ra2.png"
            resmrb = "i"+_hero[0].lower()+"rb.png"
            resmr1 = pygame.image.load(resmr1)
            resmr2 = pygame.image.load(resmr2)
            resmr3 = pygame.image.load(resmr3)
            resmra = pygame.image.load(resmra)
            resmra2 = pygame.image.load(resmra2)
            resmrb =  pygame.image.load(resmrb)
##            resml1 = "i"+_hero[0].lower()+"l1.png"
##            resml2 = "i"+_hero[0].lower()+"l2.png"
##            resml3 = "i"+_hero[0].lower()+"l3.png"
##            resmla = "i"+_hero[0].lower()+"la.png"
##            resmla2 = "i"+_hero[0].lower()+"la2.png"
##            resmlb = "i"+_hero[0].lower()+"lb.png"
            resml1 = pygame.transform.flip(resmr1,True,False)
            resml2 = pygame.transform.flip(resmr2,True,False)
            resml3 = pygame.transform.flip(resmr3,True,False)
            resmlb = pygame.transform.flip(resmrb,True,False)
            resmla = pygame.transform.flip(resmra,True,False)
            resmla2 = pygame.transform.flip(resmra2,True,False)
            _hero[6][15] = [[resml1,resml2,resml3,resmla,resmla2,resmlb],[resmr1,resmr2,resmr3,resmra,resmra2,resmrb]]
            _hero[6][0] = resmr1
    #except:
    else:        
            _hero[6][0] = pygame.image.load(resm)
            _hero[6][15] = [pygame.image.load(resm),pygame.image.load(resm2)]
    if _hero[0].upper() == "STARCAKE":
            imirnarr3 = pygame.image.load("istarcake3.png")
            _hero[6][15].append(imirnarr3)
    if _hero[0].upper() == "COSMOWORM":
            isouldragonenergy = pygame.image.load("isouldragonenergy.png")
            _hero[6][15].append(isouldragonenergy)
    _hero[6][16] = 5 #bullet
    _hero[6][18] = 0
    _hero[7] = [0,0,15,15,int(_hero[2])]
            
##    if what == True:
##        _hero.append([100,500,5,5,int(_hero[2])])
##    if what == False:
##        _hero.append([900,50,5,5,int(_hero[2])])
##    if what == None:
##        _hero.append([400,200,5,5,int(_hero[2])])
    #x,y,w,h,vel _hero[7]
    #CD#RN
    _hero[8] = int(_hero[8])
    _hero[2] = int(_hero[2])
    _hero[9] = int(_hero[9])
    _hero[10] = int(_hero[10])
    _hero[11] = int(_hero[11])
    _hero[12] = int(_hero[12])
    _hero[13] = int(_hero[13])
    _hero[15] = int(_hero[15])#agility
    _hero[6][30],_hero[6][31],_hero[6][35] = [],[],[]
    #_hero[8] RNGE
    #_hero[9] CD
    #_hero[10] RNGE
    #_hero[11] CD
    #_hero[12] RNGE
    #_hero[13] CD
    #_hero[14] #TYPE
    if me == "Show":
            me = False
            eff(_hero,"show",1000)
    _hero.append(me)
    _hero.append(what)
    if _hero[0].upper() == "MINION1":
            _hero[0] = _hero[0] + str(random.choice(range(1000,10000)))
    allo.append(_hero)
    if _hero[0] == "CINDERS" and acc(50) == True:
            for b in heros:
                    if b[0] == "CINDERS":
                            battleready(b,False,_hero[-1])
    return
def levelup(hero):
        if "MINION" in hero[0].upper():
                return hero
        if hero[0] in ["MINION1","MINION2","MINION3"]:
                return hero
        #attack
        #life
        #level hero[6][22]/100 1
        hero[6][4] = hero[6][23] * (1 + (hero[6][22]/10000)) #attack
        hero[6][6] = hero[6][24] * (1 + (hero[6][22]/10000)) #maxheal
        hero[6][29] = 100 * (1 + (hero[6][22]/5000)) #energy
        return hero


def runesshow(ss):
        if ss[6][31] == [] or ss[6][31] == 0:
                return
        #x 350 y 250
        xd = 350
        yd = 250
        for item in ss[6][31]:
                resm = "ir"+item+".png"
                showtem = pygame.image.load(resm)
                showtem = pygame.transform.scale(showtem, (60,60))
                win.blit(showtem,(xd,yd))
                yd = yd + 75
        xd = 400
        yd = 250
        showtem = pygame.image.load("ika.png")
        win.blit(showtem,(xd,yd))
        yd = yd + 75
        showtem = pygame.image.load("iks.png")
        win.blit(showtem,(xd,yd))
        yd = yd + 75
        showtem = pygame.image.load("ikd.png")
        win.blit(showtem,(xd,yd))
        return
def runesselection(ss):
        if ss[6][31] == [] or ss[6][31] == 0:
                return
        if ss[-2] == True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                        selected = ss[6][31][0]
                        ss[6][30].append(selected)
                        ss[6][31] = []
                        wplay("vvchange")
                        ss[6][34] =ss[6][34] + 1
                        ss[6][35].append(selected)
                elif keys[pygame.K_s]:
                        selected = ss[6][31][1]
                        ss[6][30].append(selected)
                        ss[6][31] = []
                        wplay("vvchange")
                        ss[6][34] =ss[6][34] + 1
                        ss[6][35].append(selected)
                elif keys[pygame.K_d]:
                        selected = ss[6][31][2]
                        ss[6][30].append(selected)
                        ss[6][31] = []
                        wplay("vvchange")
                        ss[6][34] =ss[6][34] + 1
                        ss[6][35].append(selected)
        else:
                selected = random.choice(ss[6][31])
                ss[6][30].append(selected)
                ss[6][31] = []
                ss[6][34] =ss[6][34] + 1
                ss[6][35].append(selected)
        return ss
def runes(hero):
        if hero[6][30] == 0:
                hero[6][30] = []
        if hero[6][31] == 0:
                hero[6][31] = [] #choices set
        level = round(hero[6][22]/100)
        typ = hero[14]
        items = []
        if typ == "FIGHTER":
                set1 = ["wr1","wr2","re1","re2","re3"]
                set2 = ["wr3","re4","re5","ag3","ag4"]
                set3 = ["wr5","wr8","wr9","wr10","ag5"]
                set4 = ["wr11","wr13","wr14","re9","re10"]
                set5 = ["wr15","wr16","re11","re13","re14"]
                set6 = ["wrx","wrxx","rex","rexx","agx"]
        elif typ == "INTELLIGENCE":
                set1 = ["PR1","SO1","SO2","AG1","AG2"]
                set2 = ["PR2","SO3","SO4","AG3","AG4"]
                set3 = ["PR3","SO5","SO6","AG5","AG6"]
                set4 = ["PR4","SO7","SO8","AG7","AG8"]
                set5 = ["PR4","SO9","SO10","PR4","PR4"]
                set6 = ["prx","agx","agxx","sox","soxx"]
        elif typ == "MAGE":
                set1 = ["so1","so2","wr2","ag1","ag2"]
                set2 = ["so3","so4","wr4","re4","re5"]
                set3 = ["so5","so6","wr6","wr7","pr3"]
                set4 = ["so7","so8","wr12","re9","re10"]
                set5 = ["so9","so10","re12","re13","re14"]
                set6 = ["rexx","agx","agxx","sox","soxx"]
        elif typ == "SUPPORT":
                set1 = ["re1","re2","re3","ag1","ag2"]
                set2 = ["re4","re5","so3","so4","pr2"]
                set3 = ["re6","re7","re8","so5","so6"]
                set4 = ["re9","re10","so7","ag5","ag6"]
                set5 = ["re11","re12","re13","re14","so10"]
                set6 = ["rex","rexx","agx","sox","soxx"]
        elif typ == "TANK":
                set1 = ["wr1","wr2","re1","re2","re3"]
                set2 = ["wr3","re4","re5","so3","so4"]
                set3 = ["wr5","wr6","re6","re7","re8"]
                set4 = ["wr11","wr13","wr14","re9","re10"]
                set5 = ["wr15","wr16","re11","re13","re14"]
                set6 = ["wrx","wrxx","rex","rexx","soxx"]
        elif typ == "MARKSMAN":
                set1 = ["AG1","AG2","SO1","SO2","PR1"]
                set2 = ["WR3","WR4","SO3","SO4","PR2"]
                set3 = ["WR5","WR6","WR7","WR8","WR9"]
                set4 = ["AG5","AG6","SO7","SO8","WR12"]
                set5 = ["PR4","SO9","SO10","RE11","RE12"]
                set6 = ["wrx","agx","agxx","sox","soxx"]
        elif typ == "KILLER":
                set1 = ["wr1","wr2","ag1","ag2","so2"]
                set2 = ["wr3","re4","wr4","ag3","ag4"]
                set3 = ["wr5","wr7","wr8","wr9","wr10"]
                set4 = ["wr11","wr12","wr13","wr14","ag5"]
                set5 = ["wr15","wr16","ag5","ag6","wr14"]
                set6 = ["wrx","wrxx","rex","rexx","agx","agxx","sox","soxx"]
        else:
                return
        if hero[6][31] != []:
                return
        #hero[6][34]
        if hero[6][34] == 0 and level >= 5:
                set1.remove(random.choice(set1))
                set1.remove(random.choice(set1))
                choices = set1
                hero[6][31] = choices
        if hero[6][34] == 1 and level >= 10:
                set1.remove(random.choice(set1))
                set1.remove(random.choice(set1))
                choices = set1
                hero[6][31] = choices
        if hero[6][34] == 2 and level >= 15:
                set2.remove(random.choice(set2))
                set2.remove(random.choice(set2))
                choices = set2
                hero[6][31] = choices
        if hero[6][34] == 3 and level >= 20:
                set2.remove(random.choice(set2))
                set2.remove(random.choice(set2))
                choices = set2
                hero[6][31] = choices
        if hero[6][34] == 4 and level >= 25:
                set3.remove(random.choice(set3))
                set3.remove(random.choice(set3))
                choices = set3
                hero[6][31] = choices
        if hero[6][34] == 5 and level >= 30:
                set3.remove(random.choice(set3))
                set3.remove(random.choice(set3))
                choices = set3
                hero[6][31] = choices
        if hero[6][34] == 6 and level >= 35:
                set4.remove(random.choice(set4))
                set4.remove(random.choice(set4))
                choices = set4
                hero[6][31] = choices
        if hero[6][34] == 7 and level >= 40:
                set4.remove(random.choice(set4))
                set4.remove(random.choice(set4))
                choices = set4
                hero[6][31] = choices
        if hero[6][34] == 8 and level >= 50:
                set5.remove(random.choice(set5))
                set5.remove(random.choice(set5))
                choices = set5
                hero[6][31] = choices
        if hero[6][34] == 9 and level >= 60:
                set5.remove(random.choice(set5))
                set5.remove(random.choice(set5))
                choices = set5
                hero[6][31] = choices
        if hero[6][34] == 10 and level >= 75:
                set6.remove(random.choice(set6))
                set6.remove(random.choice(set6))
                choices = set6
                hero[6][31] = choices
        return hero
def runesapply(hero):
   #try:
        return
       
   #except:
   #        print(hero)
   #return hero 
        return hero
#nowturn = "unknown              
def turncalculator(ateam,eteam):
        global turntime
        global first
        global played
        pygame.event.clear()
        if len(eteam) <= 0 or len(ateam) <= 0:
                return
        for an in ateam:
                        if an[1][0] <= 0:
                                ateam.remove(an)
                                return
        for an in eteam:
                        if an[1][0] <= 0:
                                eteam.remove(an)
                                return
        windowdisp(ateam,eteam)
##        posp = []
##        for k in ateam:
##               posp.append(k[-1])
        #print(posp)
        allteams = []
        for zo in ateam:
                if zo[-1] in [False, "X"]:
                        allteams.append(zo)
        for zoz1 in eteam:
                if zoz1[-1] in [False, "X"]:
                        allteams.append(zoz1)
       
        if len(allteams) <= 0:
                for zo2 in ateam:
                                zo2[-1] = False  
                                allteams.append(zo2)
                for zo3 in eteam:
                                zo3[-1] = False
                                allteams.append(zo3)
        allteams.sort(key=lambda speedss: speedss[1][5])
        #code [6][1]
##        to = []
##        for aaa in allteams:
##                to.append([aaa[0],aaa[-1]])
##        print(to)
        attacker = allteams[0]
        
        
        if attacker[-2] == True:
                ev = pygame.event.get()
                nor = False
                #for event in ev:
                       # if event.type == pygame.MOUSEBUTTONUP:
                xv, yv = pygame.mouse.get_pos()
                for tew in eteam:
                                      if abs(xv - tew[2][2][3][0]) < 100 and abs(yv - tew[2][2][3][1]) < 100:
                                              hedef = tew
                                              if played == False:
                                                      played = True
                                                      vplay("vx4")
                                              nor = True
                if nor == False:
                        played = False
                        return
                        hedef = random.choice(eteam)
                for heros in ateam:
                        if  attacker[1][6] == heros[1][6]:
                                attacker = heros
                                attacker[-1] = False
                                break
        if attacker[-2] == False:
                hedef = random.choice(ateam)
                elt = hedef[2][1]
                elh = attacker[2][1]
                if critica(elh,elt) < 1:
                        hedef = random.choice(ateam)
                for biz in ateam:
                        elt = biz[2][1]
                        if critica(elh,elt) > 1 and acc(70) == True:
                                hedef = biz
                                break
                for heros in eteam:
                        if  attacker[1][6] == heros[1][6]:
                                attacker = heros
                                attacker[-1] = False
                                break
        
        if attacker[-1] != True: # and nowtime() -  target[2][2][11] >= 0:
                        
                        attacker[-1] = False
                        somevar = False
                        if attacker[2][2][6] == 0 and nowtime() - turntime > 1:
                                turntime = nowtime()
                                cont = applyeffects(attacker)
                                #if cont == False:
                                        #attacker[-1] = True
                                        #target[-1] = False
                                attacker[2][2][6] = 1
                                #hedef[2][2][6] = 0
                                        #return
                                attacker[2][2][6] = 1
                        if attacker[-2] == True and attacker[2][2][6] == 1:
                                somevar = attackcalculator(attacker, hedef)
                        elif attacker[-2] == False and attacker[2][2][6] == 1:
                                righttime = random.choice(range(1,7))
                                if (nowtime() - turntime) > righttime:
                                        somevar = attackcalculator(attacker, hedef)
                        if somevar == True:
                                #print("#####################################################")
                                #print(attacker[0],attacker[-2])
                                #print(hedef[0],hedef[-2])
                                turntime = nowtime()
                                attacker[-1] = True
                                attacker[2][2][10] = 1
                                attacker[2][2][6] = 0
                                hedef[2][2][11] = nowtime()
        return







                        






        
def attackcalculator(hero,target):
    #global attack
   # print(hero[0],target[0])
    if int(hero[1][0]) > int(hero[2][2][4]):
            hero[1][0] = int(hero[2][2][4])
    if int(target[1][0]) > int(target[2][2][4]):
            target[1][0] = int(target[2][2][4])    
    attack = 0
    ####################################
    keys = pygame.key.get_pressed()
    level = round((hero[2][2][5]/100))

    if "stun" in hero[2][2][1]:
            message("STUNNED",hero,30,"red",-20,-30)
            return True
    if "freeze" in hero[2][2][1]:
            message("FROZEN",hero,30,"blue",-20,-30)
            return True
    if hero[-2] == True:
        if keys[pygame.K_1]:
            attack = 1
        if keys[pygame.K_2]:
            attack = 2
        if keys[pygame.K_3]:
            attack = 3
        if keys[pygame.K_4]:
            attack = 4
##        if keys[pygame.K_5]:
##            attack = 5
##        if keys[pygame.K_6]:
##            attack = 6
##        if keys[pygame.K_7]:
##            attack = 7
##        if keys[pygame.K_8]:
##            attack = 8
        if keys[pygame.K_c]:
          if zone != "arena" and "elementum" not in zone:
            alife = round(target[1][0]*3.5)
            afullife = round(target[2][2][4]*3.5)
            if alife < afullife/5:
                u = 0
                v = random.choice(range(0,50))    
                message("CAPTURED",target,50,"black",u,v)
                target[1][0] = 0
        pygame.event.pump()
        if attack in hero[2][2][7]:
                return False
    elif hero[-2] == False:
##        if hero[2][2][7] != 8 and level >= 30:
##                attack = 8
##        elif hero[2][2][7] != 7 and acc(50) == True and level >= 25:
##                attack = 7
##        elif hero[2][2][7] != 6 and acc(50) == True and level >= 20:
##                attack = 6
##        elif hero[2][2][7] != 5 and acc(50) == True and level >= 15:
##                attack = 5
##        elif hero[2][2][7] != 5 and acc(50) == True and level >= 15:
##                attack = 5
##        elif hero[2][2][7] != 6 and acc(50) == True and level >= 20:
##                attack = 6
##        elif hero[2][2][7] != 7 and acc(50) == True and level >= 25:
##                attack = 7
        if 4 in hero[2][2][7] and acc(90) == True and level >= 10:
                attack = 4
        elif 3 in hero[2][2][7] and acc(50) == True and level >= 5:
                attack = 3
        elif 2 in hero[2][2][7] and acc(50) == True:
                attack = 2
        elif 1 in hero[2][2][7]:
                attack = 1
        else:
               attack = random.choice([1,2,3,4,3,4,3,4,3,4,3,4,3,4,3,4])
               while attack in hero[2][2][7]:
                       attack = random.choice([1,2,3,4,3,4,3,4,3,4,3,4,3,4,3,4])
        pygame.event.clear()
    if "confuse" in hero[2][2][1]:
            attack = random.choice([1,2,3,4])
            target = hero
    if "complete_confuse" in hero[2][2][1]:
            attack = random.choice([1,2,3,4])
            target = hero
    if attack == 0:
            return False
    if attack in [1]:
            if attack not in hero[2][2][7]:
                    hero[2][2][7].append(attack)
    if attack not in [2]:
            if 2 in hero[2][2][7]:
                    hero[2][2][7].remove(2)
    if attack in [2]:
            if attack not in hero[2][2][7]:
                    hero[2][2][7].append(attack)
    if attack not in [1]:
            if 1 in hero[2][2][7]:
                    hero[2][2][7].remove(1)  
    if attack in [3]:
            if attack not in hero[2][2][7]:
                    hero[2][2][7].append(attack)
                    eff(hero,"cooldown3")
    if attack in [4]:
            if attack not in hero[2][2][7]:
                    hero[2][2][7].append(attack)
                    eff(hero,"cooldown4")
    if "cooldown3" not in hero[2][2][1] and 3 in hero[2][2][7]:
                            hero[2][2][7].remove(3)
    if "cooldown4" not in hero[2][2][1] and 4 in hero[2][2][7]:
                            hero[2][2][7].remove(4)    
    level = round((hero[2][2][5]/100))
    if level >= 30:
            if attack not in [1,2,3,4]:
                    return attackcalculator(hero,target)
    elif level >= 25:
            if attack not in [1,2,3,4]:
                    return attackcalculator(hero,target)
    elif level >= 20:
            if attack not in [1,2,3,4]:
                    return attackcalculator(hero,target)
    elif level >= 15:
            if attack not in [1,2,3,4]:
                    return attackcalculator(hero,target)
    elif level >= 10:
            if attack not in [1,2,3,4]:
                    return attackcalculator(hero,target)
    elif level >= 5:
            if attack not in [1,2,3]:
                    return attackcalculator(hero,target)
    else:
            if attack not in [1,2]:
                    return attackcalculator(hero,target)
    if attack in [1,2,3,4]:
            skill = attack + 2
            onc = False
            for repeatt in range(int(hero[skill][2])):
                            u = 0
                            v = random.choice(range(0,50))
                            acu = int(hero[skill][3])
                            if "focus" in hero[2][2][1]:
                                    acu = acu * 2
                            if "bright" in hero[2][2][1]:
                                    acu = acu / 2
                            if "destruction" in hero[skill][0].lower():
                                            objadd2(target,"idestruction1","idestruction2",2)
                            elif "poison" in hero[skill][0].lower():
                                    objadd2(target,"ivenom","ivenom1",2)
                            elif "claw" in hero[skill][0].lower():
                                    objadd(target,"iclaw",1)    
                            elif "hard_jab" in hero[skill][0].lower():
                                    if hero[-2] == True:
                                            objadd(target,"ihardjaba",1)
                                    if hero[-2] == False:
                                            objadd(target,"ihardjabe",1)    
                            elif attack >= 3:
                                    if "p" != hero[skill][10]:
                                            nam1 = "i"+hero[2][1]+"11"
                                            nam2 = "i"+hero[2][1]+"12"
                                            objadd2(target,nam1,nam2,2)
                            elif attack >= 0:  #5  
                                    if "p" != hero[skill][10]:
                                            nam1 = "i"+hero[2][1]+"1"
                                            nam2 = "i"+hero[2][1]+"2"
                                            objadd2(target,nam1,nam2,2)
                            if attack == 4:
                                    if hero[-2] == True:
                                            targeteam = eteam
                                    if hero[-2] == False:
                                            targeteam = ateam
                            else:
                                    targeteam = [target]
                            for target in targeteam:
                                onc = False
                                if acc(acu) == True:
                                    damage_(hero,target,skill)
                                    if "sink_hole" in hero[skill][0].lower():
                                            objadd2(target,"isink_hole1","isink_hole2",2)     
                                    if hero[skill][6] != "no" and onc == False:
                                            if hero[skill][4] == "confuse":
                                                objadd2(target,"iconfuse","iconfuse2",2)
                                            if hero[skill][4] == "complete_confuse":
                                                objadd2(target,"iconfuse","iconfuse2",2)
                                            if hero[skill][4] == "stun":
                                                objadd2(target,"isleep","isleep2",2)
                                            if hero[skill][4] == "deepsleep":
                                                objadd2(target,"isleep","isleep2",2)
                                            if hero[skill][4] == "bright":
                                                objadd2(target,"ibright1","ibright2",2)
                                            if hero[skill][4] == "negate":
                                                objadd2(hero,"inegate1","inegate2",2)
                                            if acc(int(hero[skill][6])) == True:
                                                    if hero[skill][5] == "s":
                                                            peffect = "-"
                                                            peffect = hero[skill][4].lower()
                                                            if "area" in peffect:
                                                                    peffect = peffect.replace("area","")
                                                                    if hero[-2] == True:
                                                                            for do in ateam:
                                                                                    eff(do,peffect)
                                                                    if hero[-2] == False:
                                                                            for do in eteam:
                                                                                    eff(do,peffect)
                                                            else:
                                                                    eff(hero,hero[skill][4])
                                                    if hero[skill][5] == "e":
                                                            eff(target,hero[skill][4])
                                                    if hero[skill][4] == "extraturn":
                                                            message("EXTRA TURN",hero,25,"blue",u,v)
                                                            return False
                                            else:
                                                    if hero[skill][8] == "s":
                                                            message("miss",hero,25,"red",u,v)
                                                    if hero[skill][8] == "e":
                                                            message("miss",target,25,"red",u,v)
                                                    if hero[skill][8] == "extraturn":
                                                            message("EXTRA TURN",hero,25,"blue",u,v)
                                                            return False
                                                
                                    if hero[skill][9] != "no" and onc == False:
                                            if hero[skill][7] == "confuse":
                                                objadd2(target,"iconfuse","iconfuse2",2)
                                            if hero[skill][4] == "complete_confuse":
                                                objadd2(target,"iconfuse","iconfuse2",2)    
                                            if hero[skill][4] == "stun":
                                                objadd2(target,"isleep","isleep2",2)
                                            if hero[skill][4] == "bright":
                                                objadd2(target,"ibright1","ibright2",2)
                                            if hero[skill][4] == "deepsleep":
                                                objadd2(target,"isleep","isleep2",2)
                                            if hero[skill][4] == "negate":
                                                objadd2(hero,"inegate1","inegate2",2)
                                            if acc(int(hero[skill][9])) == True:
                                                    if hero[skill][8] == "s":
                                                            peffect = "-"
                                                            peffect = hero[skill][7]
                                                            if "area" in peffect:
                                                                    peffect = peffect.replace("area","")
                                                                    if hero[-2] == True:
                                                                            for do in ateam:
                                                                                    eff(do,peffect)
                                                                    if hero[-2] == False:
                                                                            for do in eteam:
                                                                                    eff(do,peffect)
                                                            else:
                                                                    eff(hero,hero[skill][7])
                                                    if hero[skill][8] == "e":
                                                            eff(target,hero[skill][7])
                                            else:
                                                    if hero[skill][8] == "s":
                                                            message("miss",hero,25,"red",u,v)
                                                    if hero[skill][8] == "e":
                                                            message("miss",target,25,"red",u,v)
                                    onc = True
                                else:
                                    message("MISS",target,35,"red",u,v)
            attack = 0    
            return True    
    return False
def areaeff(hero,target,effect,turn):    
    global attack
    showww = False
    if hero != target:
            showww = True
    if hero[0] == "MANTO":
            showww = False
    rangetars = []
    targets = []
    rnge = 0
    rnge = hero[6][5] + 0
    if "MIA" in hero[0] and attack == 1:
            rnge = 50
    if attack == 4:
            rnge = hero[12] + 0
    if attack == 3:
            rnge = hero[10] + 0
    if attack == 2:
            rnge = hero[8] + 0
    attack = 0
    if "EVANGELA" in hero[0]:
            rnge = 350
    if target[-1] == False:
        for n in allo:
            if n[-1] == False:
                targets.append(n)     
    elif target[-1] == True:
        for n in allo:
            if n[-1] == True:
                targets.append(n)
    for sets in targets:
        dis = (int(round(sets[7][1]+(sets[7][3]/2)-(hero[7][1]+(hero[7][3]/2))))**2+int(round(sets[7][0]+(sets[7][2]/2)-(hero[7][0]+(hero[7][2]/2))))**2)**(1/2)
        if dis <= rnge:
              rangetars.append(sets)
    for n in rangetars:
        if showww == True:
            if hero[5][0] == "p":
                ob = hero[6][10]
                if attack in [2,3,4]:
                        try:
                                pr =  "i"+hero[0].lower()+"p2.png"
                                ob = pygame.image.load(pr)
                        except:
                                ob = hero[6][10]
                z = 1
                while z <= int(hero[5][3]):
                    z = z + 1
                    projectiles.append([ob,hero[7][0]+hero[7][2],hero[7][1]+hero[7][3],target[6][1],hero[7][4],False])
            else:
                if hero[6][10] == 0:
                    ob = random.choice(["ip1","ip2","ip3"])
                    if attack in [2,3,4]:
                        try:
                                pr =  "i"+hero[0].lower()+"p2.png"
                                ob = pygame.image.load(pr)
                        except:
                                ob = ob
                    objadd(target,ob,2)
                else:
                    vplay("VD")
                    ob = hero[6][10]
                    if attack in [2,3,4]:
                        try:
                                pr =  "i"+hero[0].lower()+"p2.png"
                                ob = pygame.image.load(pr)
                        except:
                                ob = hero[6][10]
                    objadd(target,ob,2)
        if hero[0] == "MANTO":
                if n == hero:
                        continue
                elif "MINION" in n[0]:
                        continue
                else:
                        ob = hero[6][10]
                        try:
                             pr =  "i"+hero[0].lower()+"p2.png"
                             ob = pygame.image.load(pr)
                        except:
                             ob = hero[6][10]
                        objadd(n,ob,2)
                        eff(n,effect,turn)
                        return
        if hero[0] != "MANTO":
                eff(n,effect,turn)
        
    if hero[0] == "INFERIA":
            if len(rangetars) == 1:
                    eff(hero,"Attackrise2",5)
    if hero[0] == "EVANGELA":
            if len(rangetars) > 2:
                    eff(hero,"EVAPOWER",10)
                    eff(hero,"Attackrise2",10)
                    areadamage(hero,100)
                    if "EVAPOWER" in hero[6][8]:
                                hero[6][3] = 30 
                    
    return
def areadamage(hero,c):
    global attack
    z = 0
    rangetars = []
    rnge = hero[6][5] + 0
    if attack == 4:
            rnge = hero[12] + 0
    if attack == 3:
            rnge = hero[10] + 0
    if attack == 2:
            rnge = hero[8] + 0
    if "EVANGELA" in hero[0] and "EVAPOWER" in hero[6][8]:
            rnge = 350
    attack = 0
    targets = []
    if hero[-1] == False:
        for n in allo:
            if n[-1] == True or n[0] in ["ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                targets.append(n)     
    elif hero[-1] == True or hero[0]:
        for n in allo:
            if n[-1] == False or n[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"]:
                targets.append(n)
    for sets in targets:
        dis = (int(round(sets[7][1]+(sets[7][3]/2)-(hero[7][1]+(hero[7][3]/2))))**2+int(round(sets[7][0]+(sets[7][2]/2)-(hero[7][0]+(hero[7][2]/2))))**2)**(1/2)
        if dis <= rnge and z < c:
              z = z + 1
              rangetars.append(sets)
    if "AYLEY" in hero[0]:
            if len(targets) > 5:
                    eff(hero,"Heal",320)
    if "OZ" in hero[0]:
            if len(targets) < 3:
                    eff(hero,"Attackrise",5)
    rep = False
    for target in rangetars:
        if "PENGUITOX" in hero[0] and attack == 3:
                if "Poison" in target[6][8]:
                        damage_(hero,target)
                        damage_(hero,target)
        else: 
                damage_(hero,target)
                if "EVANGELA" in hero[0] and "EVAPOWER" in hero[6][8]:
                        chase(hero,target,30)
                        eff(hero,"Heal",50)
                if "PENGUITOX" in hero[0] and attack == 4:
                        if target[3] < 0:
                                rep = True
    if rep == True:
            areadamage(hero,100)   
    return
def critica(el,ele):
        elements = ["static","cloud","gem"]
        if el in elements and ele in elements:
                if el == elements[elements.index(ele) - 1]:
                        return 1.5
                elif  ele == elements[elements.index(el) - 1]:
                        return 0.5
        elements = ["sea","star","plant"]
        if el in elements and ele in elements:
                if el == elements[elements.index(ele) - 1]:
                        return 1.5
                elif  ele == elements[elements.index(el) - 1]:
                        return 0.5
        elements = ["balance","chaos"]
        if el in elements and ele in elements:
                if el != ele:
                        return 2
                elif el == ele and el == "balance":
                        return 0.25
                elif el == ele and el == "chaos":
                        return 2
        return 1
def damage_(hero,target,skill):
       # print(hero[0])
        at = 0
        at = int(hero[skill][1])
        if at == 0:
                return
        if hero[skill][10] == "p":
                powr = int(hero[1][2])
                defr = 70
                critic = 1
                vplay("VD")
        else:
                name = "v"+hero[2][1]
                try:
                        vplay(name)
                except:
                        vplay("VD")
                powr = int(hero[1][1])
                defr = 70
                critic = critica(hero[2][1],target[2][1])
        if "negate" in hero[2][2][1]:
                if critic == 0.5:
                        critic = 1
        if "negate" in target[2][2][1]:
                if critic == 1.5:
                        critic = 1
        ran = random.choice(range(0,4))
        if acc(50) == True:
                ran = -1*ran
        defn = 70 / (10+defr)
        powr = (10+powr) / 70
        damage = critic * ((at) * defn * powr) + ran
        if damage < 0:
                damage = 0
        u = 0
        v = random.choice(range(0,50))
        if "attackdown" in hero[2][2][1]:
                text = "-50% attack down"
                message(text,hero,20,"red",u,v)
                damage = damage/2
        if "attackrise" in hero[2][2][1]:
                text = "+50% attack rise"
                message(text,hero,20,"blue",u,v)
                damage = damage*1.5
        if "doubleattack" in hero[2][2][1]:
                text = "+100% Attack Rise"
                message(text,hero,25,"blue",u,v)
                damage = damage*2
        if "mirror" in target[2][2][1]:
                text = "mirror"
                message(text,target,20,"blue",u,v)
                hero[1][0] = int(hero[1][0]) - damage
        target[1][0] = int(target[1][0]) - damage
        
        
        u = 0
        v = random.choice(range(0,50))
        if critic == 1:
                text = "-"+ str(round(damage))
                message(text,target,30,"black",u,v)
        elif critic == 1.5:
                text = "-"+ str(round(damage))+" CRITICAL!"
                message(text,target,35,"blue",u,v)
                vplay("vx3")
        elif critic == 0.5:
                text = "-"+ str(round(damage))+" weak"
                message(text,target,25,"red",u,v)
        elif critic == 2:
                text = "-"+ str(round(damage))+" BRUTAL!!"
                message(text,target,35,"blue",u,v)
                vplay("vx3")
        elif critic == 0.25:
                text = "-"+ str(round(damage))+" pathetic"
                message(text,target,25,"red",u,v)
        return hero,target
def old(hero,target,skill):
    global allyno
    global eneno
    global attack
    if hero[0] == "ORIODRONE":
            return
    if target[3] <= 0:
            return
    if "orbing3" in hero[6][8]:
            push(hero,target,20)   
    if hero[0] == "ROCKETLADY":
                            if hero[6][16] == 0:
                                    text = "running out of bullets"
                                    message(text,hero,15,"red",60,60)
                                    return
                            else:
                                    hero[6][16] = hero[6][16] - 1
    if hero[0] == "GUNPRO":
                            if hero[6][16] == 0:
                                    text = "running out of bullets"
                                    message(text,hero,15,"red",60,60)
                                    return
                            else:
                                    hero[6][16] = hero[6][16] - 1
    if hero[5][0] == "z" and attack != 0:
                ob = hero[6][10]
                if attack in [2,3,4]:
                        try:
                                pr =  "i"+hero[0].lower()+"p2.png"
                                ob = pygame.image.load(pr)
                        except:
                                ob = hero[6][10]
                row = False
                if hero[0] == "ELLIE":
                            if attack == 2:
                                    row = True
                if hero[0] == "" and acc(50) == True:
                        row = True
                if hero[-2] == True and row == False:
                        xv, yv = pygame.mouse.get_pos()
                elif row == True:
                        xv = target[7][0] + 0
                        yv = target[7][1] + 0
                else:
                        if acc(50) == True:
                                xv = target[7][0] + 0
                                yv = target[7][1] + 0
                        else:
                               xv = target[7][0] + random.choice(range(50,300))
                               yv = target[7][1] + random.choice(range(50,300)) 
                if attack == 4:
                            rnge = hero[12] + 0
                elif attack == 3:
                            rnge = hero[10] + 0
                elif attack == 2:
                            rnge = hero[8] + 0
                else:
                        rnge = hero[6][5] + 0
                if abs(hero[7][0] - xv) >= rnge:
                        if hero[7][0] >= xv:
                                xv = hero[7][0] - rnge
                        if hero[7][0] <= xv:
                                xv = hero[7][0] + rnge
                if abs(hero[7][1] - yv) >= rnge:
                        if hero[7][0] >= yv:
                                yv = hero[7][1] - rnge
                        if hero[7][0] <= yv:
                                yv = hero[7][1] + rnge
                projectiles.append([ob,hero[7][0]+hero[7][2]-50,hero[7][1]+hero[7][3]-50,target[6][1],hero[7][4], [hero[-1], hero[6][1],xv,yv,hero[0]]])
                return
    elif hero[5][0] == "p":
        ob = hero[6][10]
        if attack in [2,3,4]:
                try:
                        pr =  "i"+hero[0].lower()+"p2.png"
                        ob = pygame.image.load(pr)
                except:
                        ob = hero[6][10]
        z = 1
        while z <= int(hero[5][3]):
            z = z + 1
            projectiles.append([ob,hero[7][0]+hero[7][2],hero[7][1]+hero[7][3],target[6][1],hero[7][4],False])
    elif hero[0] == "PIXELIXION":
            z = 1
    else:
        if hero[5][0] == "k":
            hero[7][0] = hero[7][0] + random.choice([10,-10,20,-20,5,-5,30,-30])
            hero[7][1] = hero[7][1] + random.choice([10,-10,20,-20,5,-5,30,-30])
                
        if hero[6][10] == 0:
            ob = random.choice(["ip1","ip2","ip3"])
            if attack in [2,3,4]:
                try:
                        pr =  "i"+hero[0].lower()+"p2.png"
                        ob = pygame.image.load(pr)
                except:
                        ob = ob
            objadd(target,ob,2)
        else:
            vplay("VD")
            ob = hero[6][10]
            if attack in [2,3,4]:
                try:
                        pr =  "i"+hero[0].lower()+"p2.png"
                        ob = pygame.image.load(pr)
                except:
                        ob = hero[6][10]
            objadd(target,ob,2)
    if hero[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
            vplay("VD")
    elif hero[6][10] != 0:
            if hero[0] in ["ICEFAIRY","DOLLA","COLLECTOR","MAGICMASTER"]:
                    vplay("wmagic")
            elif hero[0] in ["WILDA","MR_CUDDLES"]:
                    if attack in [2,4]:
                            vplay("wbear")
            elif hero[0] in ["LORD"]:
                    if attack in [4]:
                            vplay("wlord")
            elif hero[0] in ["ARAN","KORSANA","SPARTACUS","JANETT"]:
                    vplay("wswordcut")
            elif hero[0] in ["FANNY","FINN"]:
                    vplay("wswordcut2")        
            elif hero[0] in ["MASMANYAK"]:
                    vplay("wfastsword")
            elif hero[0] in ["NOXIOSON","AMAZONA","DYNAMAX"]:
                    vplay("wmagic2")
            elif hero[0] in ["CREEPYCRAZY"]:
                    vplay("wweird")          
            elif hero[0] in ["COMMANDERA","REVENGERA"]:
                    vplay("wmegalaser")
            elif hero[0] in ["GRAVEKEEPER","TYRANOSAURUS"]:
                    vplay("woldsword")
            elif hero[0] in ["TYLER"]:
                    vplay("wssoftfire")
            elif hero[0] in ["FROGLEGS"]:
                    vplay("wfasthit")
            elif hero[0] in ["PLATINEX"]:
                    vplay("wsoil")
            elif hero[0] in ["ALLMIGHT"]:
                    vplay("wchaos")
            elif hero[0] in ["LORD_OF_THE_FLAMES","IGNITUS","SURVIVORA","INFERIA","GRENADOR"]:
                    vplay("wsfire")
            elif hero[0] in ["NADIA","BUBLEE"]:
                    vplay("wswater")    
            elif hero[0] in ["TETNAM"]:
                    vplay("wssobad")
            elif hero[0] in ["EMPRESSA"]:
                    vplay("wshardhit")
            elif hero[0] in ["MANTO","ULMADRO"]:
                    vplay("wsstomp")
            elif hero[0] in ["MISS_MARVEL","EMILIA","ELLIE"]:
                    vplay("wlaser")
            elif hero[0] in ["BRAINDOM","SONICO"]:
                    vplay("wvortex")
            elif hero[0] in ["ANDROIDIANA","PIXELIXION"]:
                    vplay("wsshock")
            elif hero[0] in ["ROCKETLADY","GUNPRO"]:
                    vplay("wbullet")
            elif hero[0] in ["LITTLE_RAT","HITMAN"]:
                    vplay("wsmallbullet")        
            elif hero[0] in ["JEZZ"]:       
                    vplay("wfasthit")
            elif hero[0] in ["ROBIN"]:
                    vplay("wfastprojectile")
            elif hero[14] == "MAGE":
                vplay("vxx")
            elif hero[14] == "SUPPORT":
                vplay("vxx") 
            elif hero[14] == "TANK":
                vplay("VD")
            elif hero[14] == "FIGHTER":
                vplay("vx2")
            elif hero[14] == "MARKSMAN":
                vplay("vx3")
            elif hero[14] == "KILLER":
                vplay("vx2")
            else:
                vplay("VD")
    if hero[0] == "GRIMCANDY":
            if attack == 2:
                    return
    if hero[0] == "MANTO":
            if attack == 2:
                    return
            if attack == 3:
                    return
    attackpower = hero[6][4]
    if attack in [2,3,4,5]:
            attackpower = hero[6][26]
    if hero[0] in ["ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
            attackpower = 70
    if hero[0] in ["ALLYBASE","ENEBASE"]:
            attackpower = 200
    j = int(round(attack*0.1))
    if j <= 5:
            constant = random.choice(range(-(5-1),5+1))
    elif j >= 10:
            constant = random.choice(range(-(10-1),10+1))
    else:
            constant = random.choice(range(-(j-1),j+1))
    constant = round(constant)
    damage = attackpower + constant
    if "DODGE" in target[6][8]:
            text = "MISS"
            del target[6][8]["DODGE"]
            u = random.choice(range(30,80))
            v = random.choice(range(0,50))
            if hero[-1] == True or hero[0] in ["ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                message(text,target,15,"s3",u,v)
            elif hero[-1] == False or hero[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"]:
                message(text,target,15,"s4",u,v)
            else:
                message(text,target,20,"red",u,v)
            return 
    if "Shadow" in hero[6][8]:
            if acc(50) == True:
                    text = "MISS"
                    u = random.choice(range(30,80))
                    v = random.choice(range(0,50))
                    if hero[-1] == True or hero[0] in ["ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                        message(text,target,15,"s3",u,v)
                    elif hero[-1] == False or hero[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"]:
                        message(text,target,15,"s4",u,v)
                    else:
                        message(text,target,20,"red",u,v)
                    return
    if "Attackrise" in hero[6][8]:
        damage = damage * 1.5
    if "Attackrise2" in hero[6][8]:
        damage = damage * 2
    if "Attackrise3" in hero[6][8]:
        damage = damage * 2.8
    if "Attackdown" in hero[6][8]:
        damage = damage * 0.5
    if "Defenceup" in target[6][8]:
        damage = damage * 0.5
   # if hero[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
    #        damage = damage * 3
    if "GRAVEKEEPER" in hero[0] and attack == 3:
            damage = damage + (target[3]*0.2)
        
    if "Damagelimit" in target[6][8]:
        if damage > 200:
                damage = 0
    if "ALLMIGHT" in hero[0] and attack == 2:
            damage = damage * 2.8
    if "NOYA" in hero[0] and attack == 5:
            damage = damage * 2.8
    if "COMMANDERA" in hero[0] and attack == 4:
            damage = damage * 2.8
    if "ICEFAIRY" in hero[0] and "Freeze" in target[6][8]:
            damage = damage * 1.5
    if "IGNITUS" in hero[0]:
            try:
                    if "TANK" in target[14]:
                            damage = damage * 1.5
            except:
                    damage = damage
    if "GREENO" in hero[0] and "Poison" in target[6][8]:
            damage = damage * 2
    if "TYLER" in hero[0] and "Burn" in target[6][8]:
            damage = damage * 2
    if "BAKUGO" in hero[0] and "Explosion" in target[6][8]:
            damage = damage * 1.5
    if "FANNY" in hero[0] and "Fannyscar" in target[6][8]:
            damage = damage * 1.5
    if "MASMANYAK" in hero[0] and "Manyakscar" in target[6][8]:
            damage = damage * 1.5
    if "MASMANYAK" in hero[0]:
            eff(target,"Manyakscar",20)
    if "MISS_MARVEL" in hero[0] and "MARVELMARK" in target[6][8]:
            damage = damage * 2
    if "PROTOHAWK" in hero[0] and "MINION" in target[0].upper():
            damage = damage * 1.5
    if "HITMAN" in hero[0] and "MINION" in target[0].upper():
            if attack == 4:
                    damage = damage * 10
    if "MINION" in hero[0].upper() and "SHARINGAN" in target[0]:
            damage = 0
    if "TITANEATER" in hero[0]:
            if acc(5) == True:
                    damage = damage * 3
                    text = "CRITICAL!"
                    message(text,target,10,"red",80,50)
    if "FINN" in hero[0]:
            if target[0].upper() in ["LORD","LORDMASTER","DRAGON"]:# or target[14] == "BOSS":
                    damage = damage * 1.5
            if "MINION" in target[0].upper():
                    damage = damage * 1.5
    if "OZ" in hero[0]:
            if "MINION" in target[0].upper():
                    damage = damage * 2
    if "ANKACROWN" in hero[0]:
            if acc(5) == True:
                    damage = damage * 3
                    text = "CRITICAL!"
                    message(text,target,10,"red",80,50)
    if "COMMANDERA" in hero[0]:
            if "Commanded" not in target[6][8] and target[0].upper() not in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                    damage = damage * 2
    if "COLLECTOR" in hero[0]:
            if target[0].upper() in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]: 
                    damage = damage * 2
    if "DR.INVENTOR" in hero[0]:
            if target[0].upper() in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]: 
                    damage = damage * 2
    if "ANDROIDIANA" in hero[0]:
            if target[0].upper() in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]: 
                    damage = damage * 2
    if "STONETON" in hero[0]:
            if target[0].upper() in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]: 
                    damage = damage * 2
    if "PSYCHOT" in hero[0]:
            if target[0].upper() in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]: 
                    damage = damage * 2
    if hero[0] == "FANNY":
            dis = (int(round(target[7][1]+(target[7][3]/2)-(hero[7][1]+(hero[7][3]/2))))**2+int(round(target[7][0]+(target[7][2]/2)-(hero[7][0]+(hero[7][2]/2))))**2)**(1/2)
            dis = abs(dis)
            if dis < 100:
                    damage = damage * 2
    if hero[0] == "NOXIOSON":
            dis = (int(round(target[7][1]+(target[7][3]/2)-(hero[7][1]+(hero[7][3]/2))))**2+int(round(target[7][0]+(target[7][2]/2)-(hero[7][0]+(hero[7][2]/2))))**2)**(1/2)
            dis = abs(dis)
            if dis < 100:
                    damage = damage * 2
    if hero[0] == "HITMAN":
            dis = (int(round(target[7][1]+(target[7][3]/2)-(hero[7][1]+(hero[7][3]/2))))**2+int(round(target[7][0]+(target[7][2]/2)-(hero[7][0]+(hero[7][2]/2))))**2)**(1/2)
            dis = abs(dis)
            if dis > 50:
                    damage = damage * (200/dis)
            else:
                    damage = damage * (200/50)
    if "DYNAMAX" in target[0]:
            if target[3] > 1000:
                    damage = damage * 0.9
    if "Invincible"  in target[6][8]:
            damage = 0
    if "Evasion"  in target[6][8]:
            damage = 0        
    if "moveinvincible"  in target[6][8]:
            damage = 0
            text = "invincible"
            message(text,target,10,"purple",40,50)
##    if target[6][9] > 0:
##        text = "Shield Left:" + str(target[6][9] - damage)
##        if acc(30) == True:
##            objadd(target,"ish",2)
##        message(text,target,15,"black",20,50)
    #if hero[0] == "#VIO":
    if hero[7][0] < target[7][0]: #0 left 1 right
            if hero[0] not in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                    if hero[6][0] == hero[6][15][1][-3]:
                            hero[6][0] = hero[6][15][1][-2]
                    else:
                            hero[6][0] = hero[6][15][1][-3]
            #if target[0] == "#VIO":
            if target[0] not in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"] and acc(25) == True:    
                    target[6][0] = random.choice([target[6][15][1][-1],target[6][15][0][-1]])
    if hero[7][0] > target[7][0]:
            if hero[0] not in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                    if hero[6][0] == hero[6][15][0][-3]:
                            hero[6][0] = hero[6][15][0][-2]
                    else:
                            hero[6][0] = hero[6][15][0][-3]
            #if target[0] == "#VIO":
            if target[0] not in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"] and acc(25) == True:    
                    target[6][0] = random.choice([target[6][15][1][-1],target[6][15][0][-1]])
    if target[6][9] > 0:
        if "Burning_Shield" in hero[6][8]:
                if acc(30) == True:
                        objadd(target,"ifireshield",2)
        else:
                if acc(30) == True:
                    objadd(target,"ish",2)
        news = target[6][9] - damage
        damage = damage - target[6][9]
        if damage < 0:
                damage = 0
        target[6][9] = news
    target[3] = int(target[3]) - damage
  #  if hero[0] == "VIO":
   #         print(damage,"time:",nowtime()) #here

    
    text = "-"+ str(round(damage))
    u = random.choice(range(30,80))
    v = random.choice(range(0,50))
    if hero[-1] == True or hero[0] in ["ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
        message(text,target,15,"s3",u,v)
    elif hero[-1] == False or hero[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"]:
        message(text,target,15,"s4",u,v)
    else:
            message(text,target,20,"red",u,v)
    life = str(round(target[3]))
    maxh = str(target[6][6])
    #show = "                                ["+life+"/"+maxh+"]"
    show = "["+life+"/"+maxh+"]"
##    if target[0] in "ENEBASE":
##        message(show,target,25,"black",130,70)
##    elif target[0] in "ALLYBASE":
##        message(show,target,25,"black",130,70)
##    else:
##        message(show,target,15,"black",120,20)
    if "MINION" not in hero[0]:
            if hero[0] != target[6][17]:
                    target[6][19] = target[6][17]
                    target[6][17] = hero[0]
                    target[6][21] = nowtime()
    if "BARREL" in hero[0]:
            if hero[0] != target[6][17]:
                    target[6][19] = target[6][17]
                    target[6][17] = "BARRIOL"
                    target[6][21] = nowtime()
    if "DRONE" in hero[0]:
                    target[6][19] = target[6][17]
                    target[6][17] = "ORIODRONE"
                    target[6][21] = nowtime()
    if target[0] == "AYLEY" and "Fast" in target[6][8]:
            eff(hero,"Block",3)
    if target[0] == "MINILORD" and "Slow" in target[6][8]:
            eff(hero,"Attackdown",5)
    if hero[0] == "BUBLEE":
            if acc(20) == True: 
                    eff(hero,"Heal",50)
    if "PLATINEX" in hero[0]:
            if target[0].upper() in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]: 
                    towerpull(hero,target,50)
    if hero[0] == "ARAN":
            if hero[3] < 100:
                    eff(hero,"Shield",10)
            if target[3] < 0 and attack == 3:
                   eff(hero,"Attackrise",10)
    if "SAMANTRA" in target[0]:
                    eff(hero,"Cursed",4)
    if "MECHATRON" in hero[0]:
            if hero[3] < 100:
                    eff(hero,"Ultimaterise",4)
    if "BULLNOX" in hero[0]:
            if hero[3] < 200:
                    eff(hero,"Ultimafast",4)
                    eff(hero,"Fast",4)
    if "CREEPYCRAZY" in hero[0]:
            if hero[3] < 200:
                    eff(hero,"Areanexta",4)
                    eff(hero,"Ultimafast",4)
                    eff(hero,"Fast",4)
    if "NOYA" in hero[0]:
            if hero[3] < 500:
                eff(hero,"Attackrise2",4)
    if target[0] == "PIXRY":
            dis = (int(round(target[7][1]+(target[7][3]/2)-(hero[7][1]+(hero[7][3]/2))))**2+int(round(target[7][0]+(target[7][2]/2)-(hero[7][0]+(hero[7][2]/2))))**2)**(1/2)
            dis = abs(dis)
            if dis < 100:
                   eff(hero,"Freeze",2)
    if "GRAFFIT" in hero[0]:
            if hero[3] < 200:
                push(target,hero,100)   
    if "OBEDEON" in target[0]:
            if target[3] < 1000 and target[3] > 500:
                    eff(hero,"Slowattack",6)
    if "JOKIEJOKIE" in target[0]:
            if "Found" not in target[6][8] and "Invisible" in target[6][8]:
                    eff(target,"Found",2)
                    del target[6][8]["Invisible"]
    if "FROGLEGS" in hero[0]:
            chase(hero,target,30)
    if "Burning_Shield" in target[6][8]:
            eff(hero,"Burn",3)
    if "ERUPTAUR" in target[0] and acc(20) == True:
            eff(hero,"Burn",2)    
    if "Damagereturn" in target[6][8]:
            hero[3] = hero[3] - damage
            text = "-"+ str(round(damage))
            u = random.choice(range(30,80))
            v = random.choice(range(0,50))
            message(text,hero,15,"red",u,v)
    if target[0] == "PRECISIO":
            hero[3] = hero[3] - damage/5
            text = "-"+ str(round(damage/5))
            u = random.choice(range(30,80))
            v = random.choice(range(0,50))
            message(text,hero,15,"red",u,v)
    if "KORSANA" in hero[0]:
            eff(target,"Bleed",3)
    if "JEZZ" in target[0]:
            eff(target,"attaked",2)
    if "JEZZ" in hero[0]:
            if "attaked" not in hero[6][8]:
                    eff(hero,"Fast",5)
    if "RUNALDO" in hero[0]:
            eff(hero,"Fast",2)
    if "PLATFORMY" in hero[0]:
            eff(hero,"Energy",10)
    if "COMMANDERA" in hero[0]:
            eff(target,"Commanded",450)
    if "MINILORD" in target[0]:
            eff(target,"Firsthit",10)
    if hero[0] == "HAVHAV":
            eff(target,"Attacked",50)
    if "TETNAM" in hero[0]:
            eff(target,"Poison",5)
    if hero[0] == "HAVHAV":
            if "Attacked" in target[6][8]:
                    if nowtime() - target[6][8]["Attacked"][1] >= 10:
                            summon("MEGAHAVHAV",hero)
                            hero[3] = 0
##                            hero[3] = 0
##                            for u in heros:
##                                if u[0].upper() == "MEGAHAVHAV":
##                                    battleready(u,hero[-2],hero[-1])
                            del target[6][8]["Attacked"]
                            return
    if "JANETT" in hero[0]:
                eff(target,hero[0],100)
    if "TYRANOSAURUS" in hero[0]:
                    text = "-250 HP"
                    message(text,hero,15,"red",40,50)
                    if hero[3] > 250:
                            hero[3] = hero[3] - 250
                    else:
                            hero[3] = 1
    if "HITMAN" in hero[0]:
            push(target,hero,-10)
    if "MISS_MARVEL" in hero[0]:
                eff(target,hero[0],100)
                eff(target,"MARVELMARK",10)
    if "LITTLE_RAT" in hero[0]:
            if target[0].upper() in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]: 
                eff(target,hero[0],100)
    if "ULMADRO" in hero[0]:
            if hero[6][3] < 10:
                    #hero[6][3] = atspee
                    #hero[6][4] = attack
                    hero[6][3] = 100
                    hero[6][4] = 100
            else:
                    hero[6][3] = hero[6][3] / 2
                    hero[6][4] = hero[6][4] * 2
    ########################
    if target[3] < 0 and "MINION" not in target[0].upper() and  "BARREL" not in target[0].upper() and "DRONE" != target[0].upper():
        if "DEKU" in hero[0]:
                eff(hero,"Attackrise2",9)
                eff(hero,"Fast",9)
                hero[3] = hero[3] - damage/5
                text = "-"+ str(round(damage/5))
                u = random.choice(range(30,80))
                v = random.choice(range(0,50))
                message(text,hero,15,"red",u,v)
        if "SPARTACUS" in hero[0]:
                eff(hero,"Fast",9)
        if "GRIMCANDY" in target[0]:
                    areaeff(target,hero,"Freeze",8)
        if "REVENGERA" in hero[0]:
                eff(hero,"Attackrise",3)
                eff(hero,"Heal",300)
        if "GRAVEKEEPER" in hero[0]:
                eff(hero,"Attackrise",5)
                eff(hero,"Attackrise2",5)
        if "GRENADOR" in hero[0]:
                eff(hero,"Heal",300)
        if "MINILORD" in target[0]:
                if "Firsthit" in target[6][8] and "Onetime" not in target[6][8]:
                       eff(target,"Heal",1500)
                       eff(target,"Onetime",20)
                       return
        if "LOLA" in target[0]:
                 if "1time" not in target[6][8]:
                         push(hero,target,150)
                         eff(target,"1time",35)
                         while target[3] <= 0:
                                 target[3] = target[3] + damage
                         return
                 elif "2time" not in target[6][8]:
                         push(hero,target,150)
                         eff(target,"2time",35)
                         while target[3] <= 0:
                                 target[3] = target[3] + damage
                         return
                 elif "3time" not in target[6][8]:
                         push(hero,target,150)
                         eff(target,"3time",35)
                         while target[3] <= 0:
                                 target[3] = target[3] + damage
                         return
        if "CINDERS" in target[0]:
                areaeff(target,hero,"Burn",8)
        hero[6][11] = hero[6][11] + 1 #defeater
        for kllr in allo:
                if "AMAZONA" in kllr[0]:
                        if kllr[-1] == target[-1]:
                                if dist(kllr,target) <= 300:    
                                        eff(kllr,"Attackrise2",9)
                                        eff(kllr,"Attackrise",9)
                                        eff(kllr,"Attackrise3",9)
                                        eff(kllr,"Fast",9)
                                        eff(kllr,"Full_Shield",9)
                if "PENGUITOX" in kllr[0]:
                        if kllr[-1] == target[-1] and kllr[0] != target[0]:
                                if dist(kllr,target) <= 300:
                                        eff(kllr,"Heal",1000)
                if kllr[0] == target[6][19]:
                        if nowtime() - target[6][21] <= 6:
                                 kllr[6][20] = kllr[6][20] + 1 #assist
                                 kllr[6][22] = kllr[6][22] + 100
        target[6][12] = target[6][12] + 1 #defeated
        say = False
        if "Killedthree" in hero[6][8] and i != "m":
                if hero[-1] == False:
                        vplay("v37")
                else:
                        vplay("v38")
                say = True
        elif "Killedtwo" in hero[6][8] and i != "m":
                if hero[-1] == False:
                        vplay("v36")
                else:
                        vplay("v33")
                say = True
                eff(hero,"Killedthree",5)
        elif "Killedone" in hero[6][8] and i != "m":
                if hero[-1] == False:
                        vplay("v35")
                else:
                        vplay("v34")
                say = True
                eff(hero,"Killedtwo",5)
        else:
                eff(hero,"Killedone",5)
                
        if target[-2] == True:
            if say == False:
                    wplay("v3")
        elif target[-1] == True and target[-2] != True:
            wplay("v2")
        elif target[-1] == False:
            if say == False:
                    wplay("v20")
        elif target[0] in ["ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
            wplay("v18")
            eneno = eneno + 1
        elif target[0] in ["ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"]:
            wplay("v19")
            allyno = allyno + 1
        if hero[0] == "LORD" and acc(30) == True:
                wplay("vl4")
        if hero[-1] == True and target[0] in ["DRAGON","LORD"]:
                target[-1] = True
                if target[0] == "LORD":
                        wplay("vl3")
                else:
                        wplay("vej2")
        if hero[-1] == False and target[0] in ["DRAGON","LORD"]:
                target[-1] = False
                if target[0] == "LORD":
                        wplay("vl3")
                else:
                        wplay("vej2")
        hero[6][22] = hero[6][22] + 200
    if target[3] < 0 and "MINION" in target[0].upper():
               hero[6][22] = hero[6][22] + 40
    return
def projectile(projectiles):
    global attack
    #projectiles.append([ob,hero[7][0]+hero[7][2],hero[7][1]+hero[7][3],target[6][1],hero[7][4], [hero[-1], hero[6][1],xv,yv])
    for n in projectiles:   
        text,x,y,code,atsp,code2 = n[0],n[1],n[2],n[3],n[4],n[5]
        wow = False
        ror = True
        if code2 == False:
                for nnn in allo:
                    if code == nnn[6][1]:
                            x2 = nnn[7][0] + nnn[7][2]
                            y2 = nnn[7][1] + nnn[7][3]
                            wow = True
                            break
        elif code2 != False:
             if code2[-1] == "COSMOWORM" or code2[-1] in ["orbing","orbing2","orbing3"]:
                velo = False
                for nnnnz in allo:                
                    if code2[1] == nnnnz[6][1]:
                            ahero = nnnnz
                            velo = True
                            break
                if velo == False:
                        projectiles.remove(n)
                        return projectiles
                if code2[-1] in ["orbing","orbing2","orbing3"]:
                        try:
                                if code2[-1] not in ahero[6][8]:
                                        projectiles.remove(n)
                                        return projectiles
                        except:
                                return projectiles
                wow = True
                import math
                if code2[2] == 0:
                        x2 = 1
                else:
                        x2 = code2[2]
                if code2[3] == 0:
                        y2 = 1
                else:
                        y2 = code2[3]
                angle = code2[4]
                omega = 100
                angle = angle + omega
                x2 = ahero[7][0] + omega * math.cos(angle) #Starting position x
                y2 = ahero[7][1] - omega * math.sin(angle)
##                if x2 == 0:
##                        x2 = ahero[7][0] + 100 * math.cos(angle) #Starting position x
##                        y2 = ahero[7][1] - 100 * math.sin(angle)
##                x2 = x2 + 100 * omega * math.cos(angle + math.pi / 2) # New x
##                y2 = y2 - 100 * omega * math.sin(angle + math.pi / 2)
####                if x2 == 0:
####                       # ( x - h )^2 + ( y - k )^2 = r^2
####                       x2 = 1
##                        #(x2 - ahero[7][0])**2 + (y2 - ahero[7][1])**2 = 100**2
##                        #math.sqrt(100**2 - (x2 - ahero[7][0])**2)+ahero[7][1]
##                try:
##                        y2 = math.sqrt(100**2 - (x2 - ahero[7][0])**2)+ahero[7][1]
##                except:
##                        y2 = code2[3]
                code2[2] = x2
                code2[3] = y2
                code2[4] = angle
                if code2[-1] == "COSMOWORM" or code2[-1] in ["orbing","orbing2","orbing3"]:
                        ror = False
               # [hero[-1], hero[6][1],0,0,hero[0]]
             else:
                x2 = code2[2]
                y2 = code2[3]
                wow = True
        else:
                x2 = code2[2]
                y2 = code2[3]
                wow = True
                
        if wow == False:
            projectiles.remove(n)
            continue
        
        gg = abs(x2 - n[1]) #200 x2
        ff = abs(y2 - n[2]) #100 x1
        if gg == 0:
                gg = 1
        if ff == 0:
                ff = 1
        zx,zy = 1,1
        if gg > ff and ff < 100:
                zx = 1
                zy = 1/2
        if ff > gg and gg < 100:
                zx = 1/2
                zy = 1
        else:
                zx = 1
                zy = 1
        if n[1] > x2:
            n[1] = n[1] + zx*(- atsp - 25 - random.choice(range(5)))
        if n[1] < x2:
            n[1] = n[1] + zx*( + atsp + 25 + random.choice(range(5)))
        if n[2] > y2:
            n[2] = n[2] + zy*( - atsp - 25 - random.choice(range(5)))
        if n[2] < y2:
            n[2] = n[2] + zy*( + atsp + 25 + random.choice(range(5)))
        try:
            try:    
                    if code2[4] == "ROBIN":
                            import math
                            #angle = math.atan((x2-n[1])/(y2-n[2]))
                            angle = math.atan((n[1])/(n[2]))
                            angle = angle * math.pi
                            n[0] = pygame.transform.rotozoom(n[0], angle, 1)
            except:
                wow = True
            win.blit(text,(n[1],n[2],1,1))
            
        except:
            wow = False
        ######################
        if code2 != False:
             if code2[-1] == "COSMOWORM"  or code2[-1] in ["orbing","orbing2","orbing3"]:
                attackinghero,atarget = 0,0
                for nnnz in allo:
                    if code2[0] == True:
                            if nnnz[-1] == False or nnnz[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"] or (nnnz[0] in ["DRAGON","LORD"] and nnnz[-1] == None):
                                if abs( n[1] - nnnz[7][0]) < 50 and abs(n[2] - nnnz[7][1]) < 50:
                                   atarget = nnnz
                    elif code2[0] == False:
                            if nnnz[-1] == True or nnnz[0] in ["ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"] or (nnnz[0] in ["DRAGON","LORD"] and nnnz[-1] == None):
                                    if abs( n[1] - nnnz[7][0]) < 50 and abs(n[2] - nnnz[7][1]) < 50:
                                         atarget = nnnz                
                    if code2[1] == nnnz[6][1]:
                            attackinghero = nnnz
                if attackinghero != 0 and atarget != 0:
                        attack = 0
                        damage_(attackinghero,atarget)
                #return projectiles    
             else:
                attackinghero,atarget = 0,0
                for nnnz in allo:
                    if code2[0] == True:
                            if nnnz[-1] == False or nnnz[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"] or (nnnz[0] in ["DRAGON","LORD"] and nnnz[-1] == None):
                                if abs( n[1] - nnnz[7][0]) < 50 and abs(n[2] - nnnz[7][1]) < 50:
                                   atarget = nnnz
                    elif code2[0] == False:
                            if nnnz[-1] == True or nnnz[0] in ["ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"] or (nnnz[0] in ["DRAGON","LORD"] and nnnz[-1] == None):
                                    if abs( n[1] - nnnz[7][0]) < 50 and abs(n[2] - nnnz[7][1]) < 50:
                                         atarget = nnnz                
                    if code2[1] == nnnz[6][1]:
                            attackinghero = nnnz
                if attackinghero != 0 and atarget != 0:
                        attack = 0
                        damage_(attackinghero,atarget)
                        if attackinghero[0].upper() != "ELLIE":
                                projectiles.remove(n)
                                return projectiles
            ######################
        if code2 != False:                
                if code2[-1] == "COSMOWORM"  or code2[-1] in ["orbing","orbing2","orbing3"]:
                        dont = True
                else:
                        if x2 == n[1] and y2 == n[2]:
                            projectiles.remove(n)
                        elif abs(x2 - n[1]) < 33 and abs(y2 - n[2]) < 33:
                            projectiles.remove(n)
        else:
                if x2 == n[1] and y2 == n[2]:
                    projectiles.remove(n)
                elif abs(x2 - n[1]) < 33 and abs(y2 - n[2]) < 33:
                    projectiles.remove(n)
    return projectiles
def stopwindow():
    global allyno
    global eneno
    wplay("v8")
    k = nowtime()
    while nowtime() - k < 1:
            if round((nowtime())) % 2 == 0:
                    o1 = 0
                    o2 = 0
                    o3 = 0
                    win.fill((o1,o2,o3))
                    pygame.display.update()
            pygame.event.pump()
    return
def waiting():
        tx, ty = pygame.mouse.get_pos()
        xtime = nowtime()
        while (nowtime() - xtime) < 2:
                if round((nowtime()*10)) % 2 == 0:
                                showif = pygame.transform.scale(if1, (40,10))
                                win.blit(showif,(tx,ty))
                                if xtime != 0:
                                        cal = (nowtime() - xtime)*20
                                else:
                                        cal = 0
                                an = round(cal)
                                showbar = pygame.transform.scale(if2, (an,10))
                                win.blit(showbar,(tx,ty))
                                pygame.event.pump()
                                pygame.display.update()
        return
def windowdisp(allies,enemies):
        win.fill((0,0,0))
        win.blit(backgroundd[0],(backgroundd[1],backgroundd[2]))
        kz = 1
        for obj in allies:
                if obj[2][2][-1] == 1:
                      obj[2][2][3] = [500,350]
                if obj[2][2][-1] == 2:
                      obj[2][2][3] = [700,550]
                if obj[2][2][-1] == 3:
                      obj[2][2][3] = [500,750]  
                x = obj[2][2][3][0]
                y = obj[2][2][3][1]
                ################################
                if obj[2][2][6] == 1: 
                        obrect = obj[2][2][2].get_rect()
                        we, he = obrect.width, obrect.height
                        wow = random.choice(range(35,60))
                        showrange = pygame.transform.scale(irangey, (we+wow,round(he/2)))
                        win.blit(showrange,(x-round(we/2)-round(wow/2),y+20,0,0))
                        ######################
                if "elementum" in obj[0][0].lower():
                        x = x - 200
                        y = y - 100
                if obj[2][2][10] != 0:
                        if obj[2][2][8] == 0:
                                obj[2][2][8] = 1.1
                                obj[2][2][9] = 0.1
                        if obj[2][2][8] > 1.2:
                                obj[2][2][9] = -0.1
                        if obj[2][2][8] < 1.1:
                                obj[2][2][10] = 0
                                obrect = obj[2][2][2].get_rect()
                                we, he = obrect.width, obrect.height
                                win.blit(obj[2][2][2],(x-round(we/2),y-round(he/2),we,he)) 
                        else:
                                obj[2][2][8] = obj[2][2][8] + obj[2][2][9]
                                IMAGE_BIG = pygame.transform.rotozoom(obj[2][2][2], 0, obj[2][2][8])
                                #win.blit(IMAGE_BIG,(x,y,10,10))
                                obrect = IMAGE_BIG.get_rect()
                                we, he = obrect.width, obrect.height
                                win.blit(IMAGE_BIG,(x-round(we/2),y-round(he/2),we,he))
                else:
                        obj[2][2][8] = 0
                        obj[2][2][10] = 0
                        obrect = obj[2][2][2].get_rect()
                        we, he = obrect.width, obrect.height
                        win.blit(obj[2][2][2],(x-round(we/2),y-round(he/2),we,he)) #characterdisplay
                if "elementum" in obj[0][0].lower():
                        x = x + 200
                        y = y + 100
                
                obj[1][0] = int(obj[1][0])
                #win.blit(hlvl,(x-25-50,y - 25 - 50,1,1))
                #printmessage3(str(round(obj[2][2][5]/100)),x-11-50,y -13 - 50)
                ty = y-130
                tx = x-170
                ################
                #showbar = pygame.transform.scale(istatb, (600,200))
                #win.blit(showbar,(tx,ty,1,1))
                if obj[-2] == True:
                        printmessage5(str(str(obj[0][0])+"¦ HP: "+str(round(int(obj[1][0])))+ "  Lvl: "+str(round(int(obj[2][2][5]/100)))),tx+200,ty-85)
                else:
                        printmessage5(str(str(obj[0][0])+"¦ HP: "+str(round(int(obj[1][0])))+ "  Lvl: "+str(round(int(obj[2][2][5]/100)))),tx+200,ty-85)
                ######################################
                ty = y - 20 - 50 - 150 -26 + 40
                alife = round(obj[1][0]*2.5)
                afullife = round(obj[2][2][4]*2.5)
                full = 400
                maxi = (full* alife)/ afullife
                if alife < 0:
                       alife = 0
                if afullife < 0:
                       afullife = 0
                afullife = round(full)
                alife = round(maxi)
                showbar = pygame.transform.scale(barde, (afullife,20))
                win.blit(showbar,(tx,ty,1,1))
                if alife < afullife/5:
                       showbar = pygame.transform.scale(baren, (alife,20))
                       win.blit(showbar,(tx,ty,1,1))
                else:
                       showbar = pygame.transform.scale(baral, (alife,20))
                       win.blit(showbar,(tx,ty,1,1))
                showbar = pygame.transform.scale(bardu, (round(afullife),20))
                win.blit(showbar,(tx,ty,1,1))
                if obj[2][1] == "star":
                        sym = isstar
                elif obj[2][1] == "static":
                        sym = isstatic
                elif obj[2][1] == "sea":
                        sym = issea
                elif obj[2][1] == "plant":
                        sym = isplant
                elif obj[2][1] == "gem":
                        sym = isgem
                elif obj[2][1] == "cloud":
                        sym = iscloud
                elif obj[2][1] == "balance":
                        sym = isbalance
                elif obj[2][1] == "chaos":
                        sym = ischaos
                showel = pygame.transform.scale(sym, (40,40))
                win.blit(showel,(tx-10,ty-10,1,1))
                ################
                cx = tx + 30
                cy = ty + 20
                for efek in obj[2][2][1]:
                        try:
                                ep = "ie_"+str(efek)+".png"
                                imeff = pygame.image.load(ep)
                                imeff = pygame.transform.scale(imeff, (30,30))
                                win.blit(imeff,(cx,cy,1,1))
                        except:
                                continue
                        cx = cx + 40
                ##############
                kz = kz + 1
                if obj[2][2][-1] == 1:
                      obj[2][2][3] = [500,350]
                if obj[2][2][-1] == 2:
                      obj[2][2][3] = [700,550]
                if obj[2][2][-1] == 3:
                      obj[2][2][3] = [500,750]
        kz = 1
        for obj in enemies:
                if obj[2][2][-1] == 1:
                      anytt[2][2][3] = [1400,350]
                if obj[2][2][-1] == 2:
                      anytt[2][2][3] = [1200,550]
                if obj[2][2][-1] == 3:
                      anytt[2][2][3] = [1400,750]  
                x = obj[2][2][3][0]
                y = obj[2][2][3][1]
                ################################
                if obj[2][2][6] == 1:
                        if kz == 1:     
                                anytt[2][2][3] = [500,350]
                        if kz == 2:
                              anytt[2][2][3] = [700,550]
                        if kz == 3:
                              anytt[2][2][3] = [500,750] 
                        obrect = obj[2][2][2].get_rect()
                        we, he = obrect.width, obrect.height
                        wow = random.choice(range(35,60))
                        showrange = pygame.transform.scale(irangey, (we+wow,round(he/2)))
                        win.blit(showrange,(x-round(we/2)-round(wow/2),y+20,0,0))
                        ######################
                if "elementum" in obj[0][0].lower():
                        x = x - 200
                        y = y - 100
                if obj[2][2][10] != 0:
                        if obj[2][2][8] == 0:
                                obj[2][2][8] = 1.1
                                obj[2][2][9] = 0.1
                        if obj[2][2][8] > 1.2:
                                obj[2][2][9] = -0.1
                        if obj[2][2][8] < 1.1:
                                obj[2][2][10] = 0
                                obrect = obj[2][2][2].get_rect()
                                we, he = obrect.width, obrect.height
                                win.blit(obj[2][2][2],(x-round(we/2),y-round(he/2),we,he)) 
                        else:
                                obj[2][2][8] = obj[2][2][8] + obj[2][2][9]
                                IMAGE_BIG = pygame.transform.rotozoom(obj[2][2][2], 0, obj[2][2][8])
                                #win.blit(IMAGE_BIG,(x,y,10,10))
                                obrect = IMAGE_BIG.get_rect()
                                we, he = obrect.width, obrect.height
                                win.blit(IMAGE_BIG,(x-round(we/2),y-round(he/2),we,he))
                else:
                        obj[2][2][8] = 0
                        obj[2][2][10] = 0
                        obrect = obj[2][2][2].get_rect()
                        we, he = obrect.width, obrect.height
                        win.blit(obj[2][2][2],(x-round(we/2),y-round(he/2),we,he)) #characterdisplay
                if "elementum" in obj[0][0].lower():
                        x = x + 200
                        y = y + 100
                ################################
                obj[1][0] = int(obj[1][0])
                #win.blit(hlvl,(x-25-50,y - 25 - 50,1,1))
                #printmessage3(str(round(obj[2][2][5]/100)),x-11-50,y -13 - 50)
                ty = y-130
                tx = x-170
                ################
                #showbar = pygame.transform.scale(istatb, (600,200))
                #win.blit(showbar,(tx,ty,1,1))
                #printmessage5(obj[0][0],tx+200,ty-85)
                if obj[-2] == True:
                        printmessage5(str(str(obj[0][0])+"¦ HP: "+str(round(int(obj[1][0])))+ "  Level: "+str(round(int(obj[2][2][5]/100)))+"      "+str(obj[2][2][5])+"xp"),tx+200,ty-85)
                else:
                        printmessage5(str(str(obj[0][0])+"¦ HP: "+str(round(int(obj[1][0])))+ "  Level: "+str(round(int(obj[2][2][5]/100)))),tx+200,ty-85)
                ######################################
                ty = y - 20 - 50 - 150 -26 + 40
                alife = round(obj[1][0]*3.5)
                afullife = round(obj[2][2][4]*3.5)
                full = 400
                maxi = (full* alife)/ afullife
                if alife < 0:
                       alife = 0
                if afullife < 0:
                       afullife = 0
                afullife = round(full)
                alife = round(maxi)
                showbar = pygame.transform.scale(barde, (afullife,20))
                win.blit(showbar,(tx,ty,1,1))
                if alife < afullife/5:
                       showbar = pygame.transform.scale(baren, (alife,20))
                       win.blit(showbar,(tx,ty,1,1))
                else:
                       showbar = pygame.transform.scale(baral, (alife,20))
                       win.blit(showbar,(tx,ty,1,1))
                showbar = pygame.transform.scale(bardu, (round(afullife),20))
                win.blit(showbar,(tx,ty,1,1))
                if obj[2][1] == "star":
                        sym = isstar
                elif obj[2][1] == "static":
                        sym = isstatic
                elif obj[2][1] == "sea":
                        sym = issea
                elif obj[2][1] == "plant":
                        sym = isplant
                elif obj[2][1] == "gem":
                        sym = isgem
                elif obj[2][1] == "cloud":
                        sym = iscloud
                elif obj[2][1] == "balance":
                        sym = isbalance
                elif obj[2][1] == "chaos":
                        sym = ischaos
                showel = pygame.transform.scale(sym, (40,40))
                win.blit(showel,(tx-10,ty-10,1,1))
                cx = tx + 30
                cy = ty + 20
                for efek in obj[2][2][1]:
                        try:
                                ep = "ie_"+str(efek)+".png"
                                imeff = pygame.image.load(ep)
                                imeff = pygame.transform.scale(imeff, (30,30))
                                win.blit(imeff,(cx,cy,1,1))
                        except:
                                continue
                        cx = cx + 40
##                if kz == 2:     
##                        tx = 220
##                        ty = 800
##                elif kz == 1:     
##                        tx = 120
##                        ty = 600
##                elif kz == 3:     
##                        tx = 320
##                        ty = 1000
##                
                kz = kz + 1
                x = obj[2][2][3][0]
                y = obj[2][2][3][1]
                xv, yv = pygame.mouse.get_pos()
                if abs(xv - obj[2][2][3][0]) < 100 and abs(yv - obj[2][2][3][1]) < 100:
                                                obrect = obj[2][2][2].get_rect()
                                                we, he = obrect.width, obrect.height
                                                showrange = pygame.transform.scale(itarget, (100,100))
                                                win.blit(showrange, (x, y,0,0))
                ##################
        #projectile(projectiles)
##        if "sea_elementum" in target[0][0].lower():
##                if target[2][2][6] == 1 and acc(10) == True:
##                        if target[2][2][7] == 8:
##                                win.fill((0,0,0))        
        kz = 0 
        for obj in allies:
                kz = kz + 1
                if obj[2][2][6] == 1:
                        ##############
                        tx = 220
                        ty = 800
                        k = 1
                        level = round((obj[2][2][5]/100))
##                        if level >= 30:
##                            lt =  8
##                        elif level >= 25:
##                            lt =  8
##                        elif level >= 20:
##                           lt =  7
##                        elif level >= 15:
##                            lt =  6
                        if level >= 10:
                            lt =  5
                        elif level >= 5:
                            lt =  4
                        else:
                           lt =  3
                        while k < lt:
                                if k in obj[2][2][7]:
                                        tx = tx + 300
                                        k = k + 1
                                        continue
                                if obj[k+2][10] == "p":
                                        img = istatb
                                else:
                                        if obj[2][1] == "star":
                                                img = iboxstar
                                        elif obj[2][1] == "static":
                                                img = iboxstatic
                                        elif obj[2][1] == "sea":
                                                img = iboxsea
                                        elif obj[2][1] == "plant":
                                                img = iboxplant
                                        elif obj[2][1] == "cloud":
                                                img = iboxcloud
                                        elif obj[2][1] == "gem":
                                                img = iboxgem
                                        elif obj[2][1] == "balance":
                                                img = iboxbalance
                                        elif obj[2][1] == "chaos":
                                                img = iboxchaos
                                        else:
                                                img = istatb
                                        if obj[2][1] == "star":
                                                sym = isstar
                                        elif obj[2][1] == "static":
                                                sym = isstatic
                                        elif obj[2][1] == "sea":
                                                sym = issea
                                        elif obj[2][1] == "plant":
                                                sym = isplant
                                        elif obj[2][1] == "gem":
                                                sym = isgem
                                        elif obj[2][1] == "cloud":
                                                sym = iscloud
                                        elif obj[2][1] == "balance":
                                                sym = isbalance
                                        elif obj[2][1] == "chaos":
                                                sym = ischaos
                                        showel = pygame.transform.scale(sym, (80,80))
                                showbar = pygame.transform.scale(img,(290,150))
                                win.blit(showbar,(tx,ty,1,1))
                                if obj[k+2][10] != "p":
                                        win.blit(showel,(tx-20,ty-20,1,1))
                                printmessage5(obj[k+2][0],tx+150,ty+30)
                                printmessage5(str(obj[k+2][1])+"  "+str(obj[k+2][3])+"%",tx+150,ty+50)
                                if obj[k+2][4] != "no":
                                        printmessage5(str(obj[k+2][4])+"  "+str(obj[k+2][6])+"%",tx+150,ty+80)
                                if obj[k+2][7] != "no":
                                        printmessage5(str(obj[k+2][7])+"  "+str(obj[k+2][9])+"%",tx+150,ty+110)
                                tx = tx + 300
                                k = k + 1
                        if level >= 3000000:
                                if obj[k+2][10] == "p":
                                        img = istatb
                                else:
                                        if obj[2][1] == "star":
                                                img = iboxstar
                                        elif obj[2][1] == "static":
                                                img = iboxstatic
                                        elif obj[2][1] == "sea":
                                                img = iboxsea
                                        elif obj[2][1] == "plant":
                                                img = iboxplant
                                        elif obj[2][1] == "cloud":
                                                img = iboxcloud
                                        elif obj[2][1] == "gem":
                                                img = iboxgem
                                        else:
                                                img = istatb
                                        if obj[2][1] == "star":
                                                sym = isstar
                                        elif obj[2][1] == "static":
                                                sym = isstatic
                                        elif obj[2][1] == "sea":
                                                sym = issea
                                        elif obj[2][1] == "plant":
                                                sym = isplant
                                        elif obj[2][1] == "gem":
                                                sym = isgem
                                        elif obj[2][1] == "cloud":
                                                sym = iscloud
                                        elif obj[2][1] == "balance":
                                                sym = isbalance
                                        elif obj[2][1] == "chaos":
                                                sym = ischaos
                                        showel = pygame.transform.scale(sym, (80,80))
                                showbar = pygame.transform.scale(img, (225,150))
                                win.blit(showbar,(tx,ty,1,1))
                                if obj[k+2][10] != "p":
                                        win.blit(showel,(tx-40,ty-40,1,1))
                                printmessage5(obj[k+2][0],tx+100,ty+30)
                                printmessage5(str(obj[k+2][1])+"  "+str(obj[k+2][3])+"%",tx+100,ty+50)
                                if obj[k+2][4] != "no":
                                        printmessage5(str(obj[k+2][4])+"  "+str(obj[k+2][6])+"%",tx+100,ty+80)
                                if obj[k+2][7] != "no":
                                        printmessage5(str(obj[k+2][7])+"  "+str(obj[k+2][9])+"%",tx+100,ty+110)
                                tx = tx + 180
                        #########################
                        x = obj[2][2][3][0]
                        y = obj[2][2][3][1]
        
        for o in objtim:
                if nowtime() - o[2] < o[1]:
                            if type(o[0]) == list:
                                    shw = random.choice(o[0])
                            else:
                                    shw = o[0]
                            win.blit(shw,(o[3],o[4],0,0))
                else:
                            objtim.remove(o)
        for m in msgtim:
            if nowtime() - m[2] < 2:
                    TextSurf = m[0] 
                    TextRect = m[1]
                    m[1][1] = m[1][1] - 4 
                   # if m[3] == True:
                    #    win.blit(ibk,TextRect)
                   # else:
                        #win.blit(ibk2,TextRect)
                    win.blit(TextSurf, TextRect)
            else:
                    msgtim.remove(m)
        ###############################
##        ty = y - 20 - 50 - 150 -40 + 160
##        tx = x - 50 - 50
##        if (nowtime() - turntime) < 10:
##                                showif = pygame.transform.scale(if1, (200,10))
##                                win.blit(showif,(tx,ty))
##                                if  turntime != 0:
##                                        cal = (nowtime() - turntime)*20
##                                else:
##                                        cal = 0
##                                an = round(cal)
##                                showbar = pygame.transform.scale(if2, (an,10))
##                                win.blit(showbar,(tx,ty))
        ###############################
        grid = False
        if grid == True:
            v = 0
            while v < 2000:
                        printmessage(str(v),400,v)
                        win.blit(gridh,(400,v))
                        v = v + 50
            h = 0
            while h < 2000:
                        printmessage(str(h),h,400)
                        win.blit(gridv,(h,400))
                        h = h + 50  
        pygame.display.update()
        return
def window():
    return
    global allyno
    global eneno
    keys = pygame.key.get_pressed()
    allo.sort(key=lambda student: student[7][1])
    oballo.sort(key=lambda student: student[7][1])
   # win.blit([bg,(0,0)])
    win.fill((0,0,0))
    win.blit(background[0],(background[1],background[2]))
    if keys[pygame.K_q]:
            for obj in allo:
                if "ENETOWER" in obj[0] or "ENEBASE" in obj[0]:
                        rnge = obj[6][5]
                        showrange = pygame.transform.scale(irangee, (rnge*2,rnge*2))
                        win.blit(showrange,(obj[7][0]-rnge,obj[7][1]-rnge,0,0))
                if obj[-2] == True:
                                rnge = obj[6][5]
                                showrange = pygame.transform.scale(irangey, (rnge*2,rnge*2))
                                win.blit(showrange,(obj[7][0]-rnge,obj[7][1]-rnge,0,0))
    for obj in allo:
        runesselection(obj)
        if obj[0] == "JOKIEJOKIE":
                if "Invisible" not in obj[6][8] and "Found" not in obj[6][8]:
                        eff(obj,"Invisible",60)    
        if obj[3] <= 0:
            #if obj[0] == "KITTY":
            if "attached" in obj[6][8]:
                             del obj[6][8]["attached"]  
            obj[6][7] = nowtime()
            allo.remove(obj)
            deadall.append(obj)
            #####################
            try:
                    if "Possess" in obj[6][8]:
                             if obj[-1] == True:
                                    obj[-1] = False
                             elif hero[-1] == False:
                                    obj[-1] = True
                             del obj[6][8]["Possess"]   
            except:
                    obj[6][7] = obj[6][7]
            #####################
        x = int(round(obj[7][0]))
        y = int(round(obj[7][1]))
        w = int(round(obj[7][2]))
        h = int(round(obj[7][3]))
       # if x in range(-200,2000) and y in range(-200,1500):
        if obj[-1] in [True,False] or obj[0] in ["LORD","DRAGON","ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
               if "Invisible" in obj[6][8]:
                       continue
               if x in range(-200,2000) and y in range(-200,1500) and i in ["t","z"]:
                       if obj[6][18] != 0:
                               printmessage2(obj[6][18],x+30-50,y-30-50)
                       if "MINION" not in obj[0].upper():
                               win.blit(hlvl,(x-25-50,y - 25 - 50,1,1))
                               printmessage3(str(round(obj[6][22]/100)),x-11-50,y -13 - 50)
                       ty = y - 20 - 50
                       tx = x - 50
                       alife = round(obj[3]/20)
                       afullife = round(obj[6][6]/20)
                       if alife < 0:
                               alife = 0
                       if afullife < 0:
                               afullife = 0
                        ##########
                       if obj[-1] in [True, False] and "MINION" not in obj[0].upper():
                               if obj[6][27] <= 0:
                                       obj[6][27] = 0
                               showbar = pygame.transform.scale(barde, (round(obj[6][29]),5))
                               win.blit(showbar,(tx,ty+12,1,1))
                               showbar = pygame.transform.scale(barst, (round(obj[6][27]),5))
                               win.blit(showbar,(tx,ty+12,1,1))
                               ##############
                               if obj[6][27] > round(obj[6][29]):
                                       showbar = pygame.transform.scale(bardu2, (round(obj[6][27]),5))
                                       win.blit(showbar,(tx,ty+12,1,1))
                               else:
                                       showbar = pygame.transform.scale(bardu2, (round(obj[6][29]),5))
                                       win.blit(showbar,(tx,ty+12,1,1))
                       showbar = pygame.transform.scale(barde, (afullife,13))
                       win.blit(showbar,(tx,ty,1,1))
                       if obj[6][9] > 0:
                               showbar = pygame.transform.scale(barsh, (round(alife+(round(obj[6][9])/20)),13))
                               win.blit(showbar,(tx,ty,1,1))
                       
                       if obj[-2] == True:
                               showbar = pygame.transform.scale(baryu, (alife,13))
                               win.blit(showbar,(tx,ty,1,1))
                       elif obj[-1] == True or obj[0] in ["ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                               showbar = pygame.transform.scale(baral, (alife,13))
                               win.blit(showbar,(tx,ty,1,1))
                       elif obj[-1] == False or obj[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"]:
                               showbar = pygame.transform.scale(baren, (alife,13))
                               win.blit(showbar,(tx,ty,1,1))
                       else:
                               showbar = pygame.transform.scale(barlo, (alife,13)) 
                               win.blit(showbar,(tx,ty,1,1))
                       if afullife > round(alife+(obj[6][9]/10)):
                               showbar = pygame.transform.scale(bardu, (afullife,13))
                               win.blit(showbar,(tx,ty,1,1))
                       else:
                               showbar = pygame.transform.scale(bardu, (round(alife+(obj[6][9]/20)),13))
                               win.blit(showbar,(tx,ty,1,1))
               elif x in range(-200,2000) and y in range(-200,1500): 
                       #lifebar
                       ite = 3000/20
                       lif = 0
                       ##################################
                       if obj[6][18] != 0:
                               printmessage2(obj[6][18],x+30-50,y-30-50)
                       if "MINION" not in obj[0].upper():
                               win.blit(hlvl,(x-25-50,y - 25 - 50,1,1))
                               printmessage3(str(round(obj[6][22]/100)),x-11-50,y -13 - 50)
                       ###################################### 
                       ty = y - 20 - 50
                       tx = x - 50
                       while lif <= obj[3]:
                               if obj[0] == "KITTY":
                                       if "attached" in obj[6][8]:
                                               win.blit(hlo,(tx,ty,1,1))
                                       elif obj[-2] == True:
                                               win.blit(hyu,(tx,ty,1,1))
                                       elif obj[-1] == True or obj[0] in ["ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                                               win.blit(hal,(tx,ty,1,1))
                                       elif obj[-1] == False or obj[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"]:
                                               win.blit(hen,(tx,ty,1,1))
                                       else:
                                               win.blit(hlo,(tx,ty,1,1))
                               elif obj[-2] == True:
                                       win.blit(hyu,(tx,ty,1,1))
                               elif obj[-1] == True or obj[0] in ["ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                                       win.blit(hal,(tx,ty,1,1))
                               elif obj[-1] == False or obj[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"]:
                                       win.blit(hen,(tx,ty,1,1))
                               else:
                                       win.blit(hlo,(tx,ty,1,1))
                               lif = lif + ite
                               tx = tx + 10
                       if obj[6][9] > 0:
                               #shield left #shieldleft
                               while lif <= obj[3]+obj[6][9]:
                                       win.blit(hsh,(tx,ty,1,1))
                                       lif = lif + ite
                                       tx = tx + 10
                       while lif <= obj[6][6]:
                               win.blit(hde,(tx,ty,1,1))
                               lif = lif + ite
                               tx = tx + 10
                               #if  _hero[6][6] = _hero[3] #maxheal
        if obj[-1] in [True,False]:
                if "Timedheal" in obj[6][8] and obj[0] == "MAKINA":
                        #obj[6][0] = pygame.transform.rotozoom(obj[6][0], 0, 2)
                        obj[6][0] = pygame.transform.scale(obj[6][0], (130, 150))
                if obj[0] == "STARCAKE":
                        if "MIRPOWER" in obj[6][8]:
                                obj[6][0] = obj[6][15][-1]
                               #obj[6][0] = pygame.transform.rotate(obj[6][0], 5)
                           #    obj[6][0] = pygame.transform.rotozoom(obj[6][0], 5, 1)
        win.blit(obj[6][0],(x-50,y-50,w,h))
    for objs in oballo:
            x = int(round(objs[7][0]))
            y = int(round(objs[7][1]))
            w = int(round(objs[7][2]))
            h = int(round(objs[7][3]))
            win.blit(objs[6][0],(x-50,y-50,w,h))
    if date("hour") > 18:
            win.blit(iback2,(100,100))
            win.blit(ibk4,(320,180))
    else:   
            win.blit(iback,(320,180))
    r = 0
    for nr in range(allyno):
            r = r +50
            win.blit(ibkk1,(820+r,180))
    r = 0
    for nr in range(eneno):
            r = r +50
            win.blit(ibkk2,(820+r,200))
    for m in msgtim:
            if nowtime() - m[2] < 2:
                    TextSurf = m[0]
                    TextRect = m[1]
                    if m[3] == True:
                        win.blit(ibk,TextRect)
                    else:
                        win.blit(ibk2,TextRect)
                    win.blit(TextSurf, TextRect)
            else:
                    msgtim.remove(m)
    for o in objtim:
        if nowtime() - o[2] < o[1]:
                    win.blit(o[0],(o[3],o[4],0,0))
        else:
                    objtim.remove(o)
    if date("hour") > 18:
            win.blit(ibk5,(1105,865))
    else:
            win.blit(ibk3,(1105,865))
    rum = False
    
    for ss in allo:     
        if ss[-2] == True:
                runesshow(ss)
                rum = True
                if "Shadow" in ss[6][8]:
                        win.blit(idark,(-200,-200))
                ###################
                    
                if ss[7][0] > 950+150 or ss[7][0] < 900+150:
                           if ss[7][0] < 900-150:#and ss[7][0] < 450:
                                   #x-vel
                                   vv = 900+150 - ss[7][0]
                                   background[1] = int(round(background[1] + vv))
                                   for obj in allo:
                                        if obj[-2] != True:
                                                obj[7][0] = int(round(obj[7][0])) + vv
                                   for obj in oballo:
                                        if obj[-2] != True:
                                                obj[7][0] = int(round(obj[7][0])) + vv     
                                   ss[7][0] = ss[7][0] + vv
                           if ss[7][0] > 950+150:#and ss[7][0] > 500:
                                   #x+vel
                                   vv = ss[7][0] - (950+150)
                                   background[1] = int(round(background[1] - vv))
                                   for obj in allo:
                                        if obj[-2] != True:   
                                                obj[7][0] = int(round(obj[7][0])) - vv
                                   for obj in oballo:
                                        if obj[-2] != True:   
                                                obj[7][0] = int(round(obj[7][0])) - vv
                                   ss[7][0] = ss[7][0] - vv
                if ss[7][1] > 500+150 or ss[7][1] < 450+130:
                           if  ss[7][1] < 450+130:#and ss[7][1] < 250:
                                   #y - vel
                                   vv = 450+130 - ss[7][1]
                                   background[2] = int(round(background[2] + vv))
                                   for obj in allo:
                                        if obj[-2] != True:   
                                                obj[7][1] = int(round(obj[7][1])) + vv
                                   for obj in oballo:
                                        if obj[-2] != True:   
                                                obj[7][1] = int(round(obj[7][1])) + vv
                                   ss[7][1] = ss[7][1] + vv
                           if  ss[7][1] > 500+150:#and ss[7][1] > 300:
                                   #y + vel
                                   vv = ss[7][1] - (500+150)
                                   background[2] = int(round(background[2] - vv))
                                   for obj in allo:
                                        if obj[-2] != True:   
                                                obj[7][1] = int(round(obj[7][1])) - vv
                                   for obj in oballo:
                                        if obj[-2] != True:   
                                                obj[7][1] = int(round(obj[7][1])) - vv
                                   ss[7][1] = ss[7][1] - vv
                ######################
                    
                #targets =[]
                #target = False
                attack = 0
                aldist = []
                for sets in allo:
                        if sets[-1] == False or sets[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"] or (sets[0] in ["DRAGON","LORD"] and sets[-1] == None):
                            dis = abs((int(round(sets[7][1]+(sets[7][3]/2)-(ss[7][1]+(ss[7][3]/2))))**2+int(round(sets[7][0]+(sets[7][2]/2)-(ss[7][0]+(ss[7][2]/2))))**2)**(1/2))
                            aldist.append(dis)
                
                                #break
                if len(aldist) > 0:
                        closest = min(aldist)  
                        if nowtime() - (ss[6][2][0]) >= (ss[6][3]/10) and closest <= ss[6][5]:
                           win.blit(iespace2,(1325,861))
                        elif closest <= ss[6][5]:
                                showif = pygame.transform.scale(if1, (75,10))
                                win.blit(showif,(1325,870))
                                if (ss[6][2][0]) != 0:
                                        cal = (75 * (nowtime() - (ss[6][2][0])))/(ss[6][3]/10)
                                else:
                                        cal = 0
                                an = round(cal)
                                showbar = pygame.transform.scale(if2, (an,10))
                                win.blit(showbar,(1325,870))
                        if closest <= ss[6][5]:
                           win.blit(ier,(1405,855))
                           #hero[8] RNGE
                            #hero[9] CD
                            #hero[10] RNGE
                            #hero[11] CD
                            #hero[12] RNGE
                            #hero[13] CD
                            #hero[14] #TYPE o o 
                        if round(ss[6][22]/100) >= 5:
                                if ss[6][27] < 10:
                                        win.blit(ierr,(1125,861))
                                elif nowtime() - (ss[6][2][1]) >= ss[9] and closest <= ss[8]:
                                    win.blit(iw22,(1125,861))
                                elif closest <= ss[8]:
                                        showif = pygame.transform.scale(if1, (40,10))
                                        win.blit(showif,(1125,870))
                                        if (ss[6][2][1]) != 0:
                                                cal = (40 * (nowtime() - (ss[6][2][1])))/ss[9]
                                        else:
                                                cal = 0
                                        an = round(cal)
                                        showbar = pygame.transform.scale(if2, (an,10))
                                        win.blit(showbar,(1125,870))

                        if round(ss[6][22]/100) >= 10:
                                if ss[6][27] < 25:
                                        win.blit(ierr,(1175,861))
                                elif nowtime() - (ss[6][2][2]) >= ss[11] and closest <= ss[10]:
                                    win.blit(ie22,(1175,861))
                                elif closest <= ss[10]:
                                        showif = pygame.transform.scale(if1, (40,10))
                                        win.blit(showif,(1175,870))
                                        if (ss[6][2][2]) != 0:
                                                cal = (40 * (nowtime() - (ss[6][2][2])))/ss[11]
                                        else:
                                                cal = 0
                                        an = round(cal)
                                        showbar = pygame.transform.scale(if2, (an,10))
                                        win.blit(showbar,(1175,870))

                        if round(ss[6][22]/100) >= 15:
                                if ss[6][27] < 50:
                                        win.blit(ierr,(1225,861))
                                elif nowtime() - (ss[6][2][3]) >= ss[13] and closest <= ss[12]:
                                    win.blit(ir22,(1225,861))
                                elif closest <= ss[12]:
                                        showif = pygame.transform.scale(if1, (40,10))
                                        win.blit(showif,(1225,870))
                                        if (ss[6][2][3]) != 0:
                                                cal = (40 * (nowtime() - (ss[6][2][3])))/ss[13]
                                        else:
                                                cal = 0
                                        an = round(cal)
                                        showbar = pygame.transform.scale(if2, (an,10))
                                        win.blit(showbar,(1225,870))
                        if round(ss[6][22]/100) >= 20:
                                if ss[6][27] < 80:
                                        win.blit(ierr,(1275,861))
                                elif nowtime() - (ss[6][2][4]) >= (ss[13]+5) and closest <= ss[6][5]:
                                    win.blit(it22,(1275,861))
                                elif closest <= ss[6][5]:
                                        showif = pygame.transform.scale(if1, (40,10))
                                        win.blit(showif,(1275,870))
                                        if (ss[6][2][4]) != 0:
                                                cal = (40 * (nowtime() - (ss[6][2][4])))/(ss[13]+5)
                                        else:
                                                cal = 0
                                        an = round(cal)
                                        showbar = pygame.transform.scale(if2, (an,10))
                                        win.blit(showbar,(1275,870))

                        break
                break
    #######
    if rum == False and mode == "show":
        for ss in allo:
            if ss[-1] == True:
                if "show" in ss[6][8]:
                 rum = True       
                 if ss[7][0] > 950+50 or ss[7][0] < 900+50:
                           if ss[7][0] < 900+50:#and ss[7][0] < 450:
                                   #x-vel
                                   vv = 900+50 - ss[7][0]
                                   background[1] = int(round(background[1] + vv))
                                   for obj in allo:
                                        if obj != ss:
                                                obj[7][0] = int(round(obj[7][0])) + vv
                                   for obj in oballo:
                                        if obj != ss:
                                                obj[7][0] = int(round(obj[7][0])) + vv     
                                   ss[7][0] = ss[7][0] + vv
                           if ss[7][0] > 950+50:#and ss[7][0] > 500:
                                   #x+vel
                                   vv = ss[7][0] - (950+50)
                                   background[1] = int(round(background[1] - vv))
                                   for obj in allo:
                                        if obj != ss:  
                                                obj[7][0] = int(round(obj[7][0])) - vv
                                   for obj in oballo:
                                        if obj != ss:  
                                                obj[7][0] = int(round(obj[7][0])) - vv
                                   ss[7][0] = ss[7][0] - vv
                 if ss[7][1] > 500+50 or ss[7][1] < 450+50:
                           if  ss[7][1] < 450+50:#and ss[7][1] < 250:
                                   #y - vel
                                   vv = 450+50 - ss[7][1]
                                   background[2] = int(round(background[2] + vv))
                                   for obj in allo:
                                        if obj != ss:   
                                                obj[7][1] = int(round(obj[7][1])) + vv
                                   for obj in oballo:
                                        if obj != ss:   
                                                obj[7][1] = int(round(obj[7][1])) + vv
                                   ss[7][1] = ss[7][1] + vv
                           if  ss[7][1] > 500+50:#and ss[7][1] > 300:
                                   #y + vel
                                   vv = ss[7][1] - (500+50)
                                   background[2] = int(round(background[2] - vv))
                                   for obj in allo:
                                        if obj != ss:  
                                                obj[7][1] = int(round(obj[7][1])) - vv
                                   for obj in oballo:
                                        if obj != ss:  
                                                obj[7][1] = int(round(obj[7][1])) - vv
                                   ss[7][1] = ss[7][1] - vv
                 break    
    #######
    if rum == False:
        for ss in allo:
                if ss[-1] == True and "MINION" not in ss[0].upper() and ss[0].upper() not in ["DRONE","ROBOT","MACHINE","MR_CUDDLES","PEARLAS_PET","TOWER","ANDROIROBOT","MEGAHAVHAV","GUNTER","BARREL"]:
                 if ss[7][0] > 950+50 or ss[7][0] < 900+50:
                           if ss[7][0] < 900+50:#and ss[7][0] < 450:
                                   #x-vel
                                   vv = 900+50 - ss[7][0]
                                   background[1] = int(round(background[1] + vv))
                                   for obj in allo:
                                        if obj != ss:
                                                obj[7][0] = int(round(obj[7][0])) + vv
                                   for obj in oballo:
                                        if obj != ss:
                                                obj[7][0] = int(round(obj[7][0])) + vv     
                                   ss[7][0] = ss[7][0] + vv
                           if ss[7][0] > 950+50:#and ss[7][0] > 500:
                                   #x+vel
                                   vv = ss[7][0] - 950-50
                                   background[1] = int(round(background[1] - vv))
                                   for obj in allo:
                                        if obj != ss:  
                                                obj[7][0] = int(round(obj[7][0])) - vv
                                   for obj in oballo:
                                        if obj != ss:  
                                                obj[7][0] = int(round(obj[7][0])) - vv
                                   ss[7][0] = ss[7][0] - vv
                 if ss[7][1] > 500 or ss[7][1] < 450+50:
                           if  ss[7][1] < 450+50:#and ss[7][1] < 250:
                                   #y - vel
                                   vv = 450+50 - ss[7][1]
                                   background[2] = int(round(background[2] + vv))
                                   for obj in allo:
                                        if obj != ss:   
                                                obj[7][1] = int(round(obj[7][1])) + vv
                                   for obj in oballo:
                                        if obj != ss:   
                                                obj[7][1] = int(round(obj[7][1])) + vv
                                   ss[7][1] = ss[7][1] + vv
                           if  ss[7][1] > 500+50:#and ss[7][1] > 300:
                                   #y + vel
                                   vv = ss[7][1] - 500+50
                                   background[2] = int(round(background[2] - vv))
                                   for obj in allo:
                                        if obj != ss:  
                                                obj[7][1] = int(round(obj[7][1])) - vv
                                   for obj in oballo:
                                        if obj != ss:  
                                                obj[7][1] = int(round(obj[7][1])) - vv
                                   ss[7][1] = ss[7][1] - vv
                 break
    projectile(projectiles)
    xx = 500 + 30
    yy = 200
    lefttime = round(400-nowtime())
    if lefttime <= 30 and lefttime >= 0 and i in ["a","t","w","c","z"]:
             ms = str(lefttime) + " seconds left"
             printmessage(ms,xx+900,yy)
   
    
    grid = True
    if grid == True:
            v = 0
            while v < 2000:
                        printmessage(str(v),400,v)
                        win.blit(gridh,(400,v))
                        v = v + 50
            h = 0
            while h < 2000:
                        printmessage(str(h),h,400)
                        win.blit(gridv,(h,400))
                        h = h + 50         
    pygame.display.update()
    return
def zonewindow():
    global allyno
    global eneno
    keys = pygame.key.get_pressed()
    allo.sort(key=lambda student: student[7][1])
    oballo.sort(key=lambda student: student[7][1])
   # win.blit([bg,(0,0)])
    win.fill((0,0,0))
    win.blit(background[0],(background[1],background[2]))
    for obj in allo:
        if obj[0] == "JOKIEJOKIE":
                if "Invisible" not in obj[6][8] and "Found" not in obj[6][8]:
                        eff(obj,"Invisible",60)    
        x = int(round(obj[7][0]))
        y = int(round(obj[7][1]))
        w = int(round(obj[7][2]))
        h = int(round(obj[7][3]))
       # if x in range(-200,2000) and y in range(-200,1500):
        win.blit(obj[6][0],(x-50,y-50,w,h))
    for objs in oballo:
            x = int(round(objs[7][0]))
            y = int(round(objs[7][1]))
            w = int(round(objs[7][2]))
            h = int(round(objs[7][3]))
            win.blit(objs[6][0],(x-50,y-50,w,h))
##    if date("hour") > 18:
##            win.blit(iback2,(100,100))
##            win.blit(ibk4,(320,180))
##    else:   
##            win.blit(iback,(320,180))
    r = 0
    for nr in range(allyno):
            r = r +50
            win.blit(ibkk1,(820+r,180))
    r = 0
    for nr in range(eneno):
            r = r +50
            win.blit(ibkk2,(820+r,200))
    for m in msgtim:
            if nowtime() - m[2] < 2:
                    TextSurf = m[0]
                    TextRect = m[1]
                    if m[3] == True:
                        win.blit(ibk,TextRect)
                    else:
                        win.blit(ibk2,TextRect)
                    win.blit(TextSurf, TextRect)
            else:
                    msgtim.remove(m)
##    if date("hour") > 18:
##            win.blit(ibk5,(1105,865))
##    else:
##            win.blit(ibk3,(1105,865))
    rum = False
    
    for ss in allo:     
        if ss[-2] == True:
                rum = True
                if "Shadow" in ss[6][8]:
                        win.blit(idark,(-200,-200))
                ###################
                    
                if ss[7][0] > 950+150 or ss[7][0] < 900+150:
                           if ss[7][0] < 900-150:#and ss[7][0] < 450:
                                   #x-vel
                                   vv = 900+150 - ss[7][0]
                                   background[1] = int(round(background[1] + vv))
                                   for obj in allo:
                                        if obj[-2] != True:
                                                obj[7][0] = int(round(obj[7][0])) + vv
                                   for obj in oballo:
                                        if obj[-2] != True:
                                                obj[7][0] = int(round(obj[7][0])) + vv     
                                   ss[7][0] = ss[7][0] + vv
                           if ss[7][0] > 950+150:#and ss[7][0] > 500:
                                   #x+vel
                                   vv = ss[7][0] - (950+150)
                                   background[1] = int(round(background[1] - vv))
                                   for obj in allo:
                                        if obj[-2] != True:   
                                                obj[7][0] = int(round(obj[7][0])) - vv
                                   for obj in oballo:
                                        if obj[-2] != True:   
                                                obj[7][0] = int(round(obj[7][0])) - vv
                                   ss[7][0] = ss[7][0] - vv
                if ss[7][1] > 500+150 or ss[7][1] < 450+130:
                           if  ss[7][1] < 450+130:#and ss[7][1] < 250:
                                   #y - vel
                                   vv = 450+130 - ss[7][1]
                                   background[2] = int(round(background[2] + vv))
                                   for obj in allo:
                                        if obj[-2] != True:   
                                                obj[7][1] = int(round(obj[7][1])) + vv
                                   for obj in oballo:
                                        if obj[-2] != True:   
                                                obj[7][1] = int(round(obj[7][1])) + vv
                                   ss[7][1] = ss[7][1] + vv
                           if  ss[7][1] > 500+150:#and ss[7][1] > 300:
                                   #y + vel
                                   vv = ss[7][1] - (500+150)
                                   background[2] = int(round(background[2] - vv))
                                   for obj in allo:
                                        if obj[-2] != True:   
                                                obj[7][1] = int(round(obj[7][1])) - vv
                                   for obj in oballo:
                                        if obj[-2] != True:   
                                                obj[7][1] = int(round(obj[7][1])) - vv
                                   ss[7][1] = ss[7][1] - vv
                ######################
                    
                #targets =[]
                #target = False
                attack = 0
                aldist = []
                for sets in allo:
                        if sets[-1] == False or sets[0] in ["ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP"] or (sets[0] in ["DRAGON","LORD"] and sets[-1] == None):
                            dis = abs((int(round(sets[7][1]+(sets[7][3]/2)-(ss[7][1]+(ss[7][3]/2))))**2+int(round(sets[7][0]+(sets[7][2]/2)-(ss[7][0]+(ss[7][2]/2))))**2)**(1/2))
                            aldist.append(dis)
                        break
                break
    #######
    for m in msgtim:
            if nowtime() - m[2] < 2:
                    TextSurf = m[0]
                    TextRect = m[1]
                   # if m[3] == True:
                    #    win.blit(ibk,TextRect)
                   # else:
                        #win.blit(ibk2,TextRect)
                    win.blit(TextSurf, TextRect)
            else:
                    msgtim.remove(m)
        
   # projectile(projectiles)
    xx = 500 + 30
    yy = 200
   
    gg = True
    gg = False    
    if gg == True:
            for sss in allo:
                  if sss[-2] == True:
                    text   =  str(-background[1]+sss[7][0])+" , "+str(-background[2]+sss[7][1] )   
                    printmessage(text,sss[7][0],sss[7][1])
    grid = True
    grid = False
    if grid == True:
        for sss in allo:
          if sss[-2] == True:
            v = 0
            while v < sss[7][0]+2000:
                        printmessage(str(v),400,v)
                        win.blit(gridh,(400,v))
                        v = v + 50
            h = 0
            while h < sss[7][0]+2000:
                        printmessage(str(h),h,400)
                        win.blit(gridv,(h,400))
                        h = h + 50         
    pygame.display.update()
    return
def nowtime():
        ntime = time.time() - begtime
        return ntime
def dist(hro,trget):
        dis = (int(round(trget[7][1]+(trget[7][3]/2)-(hro[7][1]+(hro[7][3]/2))))**2+int(round(trget[7][0]+(trget[7][2]/2)-(hro[7][0]+(hro[7][2]/2))))**2)**(1/2)
        return dis
def push(hero,target,num):
    if target[-1] == None:
        return
    vplay("wchase")
    xxxs = False
    yyys = False
    if target[7][1] >= hero[7][1]:
        target[7][1] = target[7][1] + num
        xxxs = True
    if target[7][0] >= hero[7][0]:
        target[7][0] = target[7][0] + num
        yyys = True
    if target[7][1] <= hero[7][1] and yyys == False:
        target[7][1] = target[7][1] - num
    if target[7][0] <= hero[7][0] and xxxs == False:
        target[7][0] = target[7][0] - num
   # window()
    return hero,target
def towerpull(hero,target,num):
    num = - num
    if target[7][1] >= hero[7][1]:
        target[7][1] = target[7][1] + num
    if target[7][0] >= hero[7][0]:
        target[7][0] = target[7][0] + num
    if target[7][1] <= hero[7][1]:
        target[7][1] = target[7][1] - num
    if target[7][0] <= hero[7][0]:
        target[7][0] = target[7][0] - num
    window()
    return hero,target
def pull(hero,target,num):
    if target[-1] == None:
        return
    vplay("wchase")
    if target[7][1] >= hero[7][1]:
        target[7][1] = hero[7][1]
    if target[7][0] >= hero[7][0]:
        target[7][0] = hero[7][0]
    if target[7][1] <= hero[7][1]:
        target[7][1] = hero[7][1]
    if target[7][0] <= hero[7][0]:
        target[7][0] = hero[7][0]
    window()
    return hero,target
def areapull(hero,target,num):
    global attack
    if attack == 4:
            rnge = hero[12] + 0
    if attack == 3:
            rnge = hero[10] + 0
    if attack == 2:
            rnge = hero[8] + 0
    ###
    rangetars = []
    targets = []
    if hero[-1] == False:
        for n in allo:
            if n[-1] == True:
                targets.append(n)     
    elif hero[-1] == True:
        for n in allo:
            if n[-1] ==False:
                targets.append(n)
    for sets in targets:
        dis = (int(round(sets[7][1]+(sets[7][3]/2)-(hero[7][1]+(hero[7][3]/2))))**2+int(round(sets[7][0]+(sets[7][2]/2)-(hero[7][0]+(hero[7][2]/2))))**2)**(1/2)
        if dis <= rnge:
              rangetars.append(sets)
    for selecteds in rangetars:
            if selecteds[-1] == None:
                continue
            vplay("wchase") 
            if selecteds[7][1] >= hero[7][1]:
                selecteds[7][1] = hero[7][1]
            if selecteds[7][0] >= hero[7][0]:
                selecteds[7][0] = hero[7][0]
            if selecteds[7][1] <= hero[7][1]:
                selecteds[7][1] = hero[7][1]
            if selecteds[7][0] <= hero[7][0]:
                selecteds[7][0] = hero[7][0]
    return 
    ###
   # window()
def areapush(hero,target,num):
    global attack
    if attack == 4:
            rnge = hero[12] + 0
    if attack == 3:
            rnge = hero[10] + 0
    if attack == 2:
            rnge = hero[8] + 0
    ###
    rangetars = []
    targets = []
    if hero[-1] == False:
        for n in allo:
            if n[-1] == True:
                targets.append(n)     
    elif hero[-1] == True:
        for n in allo:
            if n[-1] == False:
                targets.append(n)
    for sets in targets:
        dis = (int(round(sets[7][1]+(sets[7][3]/2)-(hero[7][1]+(hero[7][3]/2))))**2+int(round(sets[7][0]+(sets[7][2]/2)-(hero[7][0]+(hero[7][2]/2))))**2)**(1/2)
        if dis <= rnge:
              rangetars.append(sets)
    for selecteds in rangetars:
            if selecteds[-1] == None:
                continue
            vplay("wchase")
            if selecteds[7][1] >= hero[7][1]:
                selecteds[7][1] = selecteds[7][1] + num
            if selecteds[7][0] >= hero[7][0]:
                selecteds[7][0] = selecteds[7][0] + num
            if selecteds[7][1] <= hero[7][1]:
                selecteds[7][1] = selecteds[7][1] - num
            if selecteds[7][0] <= hero[7][0]:
                selecteds[7][0] = selecteds[7][0] - num
    return   
def chase(hero,target,num):
    vplay("wchase")
    if target[-1] == None:
        return
    if target[7][1] >= hero[7][1]:
        hero[7][1] = target[7][1]
    if target[7][0] >= hero[7][0]:
        hero[7][0] = target[7][0]
    if target[7][1] <= hero[7][1]:
        hero[7][1] = target[7][1]
    if target[7][0] <= hero[7][0]:
        hero[7][0] = target[7][0]
    window()
    return hero,target
def eff(hero,effect):
        global attack
        if effect == "no":
                return
        if effect == "extraturn":
                return
        for alread in hero[2][2][1]:
                if "immune" in alread:
                        if effect in alread and "traitdisable" not in hero[2][2][1]:
                                message("IMMUNE",hero,20,"black",random.choice(range(10,20)),random.choice(range(10,20)))
                                return
        immuneto = effect+"immune"
        if immuneto in hero[2][2][1] and "traitdisable" not in hero[2][2][1]:
                                message("IMMUNE",hero,20,"black",random.choice(range(10,20)),random.choice(range(10,20)))
                                return
        if "-" in effect or "+" in effect:
                no = int(effect[1] + effect[2])
                stat = effect[3] + effect[4]
                stat = stat.upper()
                if "-" in effect:
                        no = -1 * no
                        objadd2(hero,"idown","idown2",1)
                        if "elementum" in hero[0][0].lower():
                             if "cloud_elementum" in hero[0][0].lower():
                                     if "D" in effect.upper():
                                        message("IMMUNE",hero,20,"black",random.choice(range(10,50)),random.choice(range(10,50)))
                                        return
                             if "sea_elementum" in hero[0][0].lower():
                                     if "D" in effect.upper():
                                        message("IMMUNE",hero,20,"black",random.choice(range(10,50)),random.choice(range(10,50)))
                                        return
                             if "gem_elementum" in hero[0][0].lower():
                                     if "A" in effect.upper():
                                        message("IMMUNE",hero,20,"black",random.choice(range(10,50)),random.choice(range(10,50)))
                                        return
                             if "static_elementum" in hero[0][0].lower():
                                        message("IMMUNE",hero,20,"black",random.choice(range(10,50)),random.choice(range(10,50)))
                                        return
                             if "star_elementum" in hero[0][0].lower():
                                        message("IMMUNE",hero,20,"black",random.choice(range(10,50)),random.choice(range(10,50)))
                                        return
                else:
                        objadd2(hero,"iup","iup2",1)
                if stat == "HP":
                                hero[1][0] = int(hero[1][0]) + no
                                
                if stat == "EA":
                                hero[1][1] = int(hero[1][1]) + no
                if stat == "PA":
                                hero[1][2] = int(hero[1][2]) + no
                if stat == "ED":
                                hero[1][3] = int(hero[1][3]) + no
                if stat == "PD":
                                hero[1][4] = int(hero[1][4]) + no
                if stat == "SP":
                                hero[1][5] = int(hero[1][5]) + no
                message(effect.upper(),hero,30,"white",random.choice(range(-50,70)),random.choice(range(-50,70)))
                return hero
        if effect in ["confuse","complete_confuse","deepsleep"]:
                if effect in hero[2][2][1] or "elementum" in hero[0][0].lower():
                        message("IMMUNE",hero,20,"black",random.choice(range(10,50)),random.choice(range(10,50)))
                        return
        hero[2][2][1][effect] = 0
        if effect in ["cooldown4","cooldown3"]:
                return
        message(effect.upper(),hero,20,"white",random.choice(range(10,50)),random.choice(range(10,50)))
        return hero
def applyeffects(hero):
    if len(hero[2][2][1]) > 0:
                for effect in hero[2][2][1]:
                        hero[2][2][1][effect] = hero[2][2][1][effect] + 1
                effect = "cooldown3"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] >= 3:
                                del hero[2][2][1][effect]
                effect = "cooldown4"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] >= 4:
                                del hero[2][2][1][effect] 
                
                effect = "toxic"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 3:
                            text = "-10 Toxic"
                            message(text,hero,25,"s1",-20,-30)
                            hero[1][0] = int(hero[1][0]) - 10
                        else:
                                del hero[2][2][1][effect]
                effect = "poison"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 3:
                            tort = round(0.1 * hero[2][2][4]) #maxhp
                            text = "-"+str(tort)+str(effect).capitalize()
                            message(text,hero,25,"s1",-20,-30)
                            hero[1][0] = int(hero[1][0]) - tort
                        else:
                                del hero[2][2][1][effect]
                effect = "burn"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 3:
                            tort = round(0.1 * hero[2][2][4]) #maxhp
                            text = "-"+str(tort)+str(effect).capitalize()
                            message(text,hero,25,"red",-20,-30)
                            hero[1][0] = int(hero[1][0]) - tort
                        else:
                                del hero[2][2][1][effect]
                effect = "bleed"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 3:
                            tort = round(0.1 * hero[2][2][4]) #maxhp
                            text = "-"+str(tort)+str(effect).capitalize()
                            message(text,hero,25,"red",-20,-30)
                            hero[1][0] = int(hero[1][0]) - tort
                        else:
                                del hero[2][2][1][effect]
                effect = "shock"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 5:
                            tort = round(0.05 * hero[2][2][4]) #maxhp
                            text = "-"+str(tort)+str(effect).capitalize()
                            message(text,hero,25,"red",-20,-30)
                            hero[1][0] = int(hero[1][0]) - tort
                        else:
                                del hero[2][2][1][effect]
                effect = "ignite"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 2:
                            tort = round(0.2 * hero[2][2][4]) #maxhp
                            text = "-"+str(tort)+str(effect).capitalize()
                            message(text,hero,25,"red",-20,-30)
                            hero[1][0] = int(hero[1][0]) - tort
                        else:
                                del hero[2][2][1][effect]
                effect = "regeneration"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 3:
                            tort = round(0.15 * hero[2][2][4]) #maxhp
                            text = "+"+str(tort)+str(effect).capitalize()
                            message(text,hero,25,"green",-20,-30)
                            hero[1][0] = int(hero[1][0]) + tort
                        else:
                                del hero[2][2][1][effect]
                effect = "stun"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 1:
                            text = "stun"
                            message(text,hero,15,"red",-20,-50)
                        else:
                                del hero[2][2][1][effect]
                effect = "freeze"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 1:
                            text = "frozen"
                            message(text,hero,15,"blue",-20,-50)
                        else:
                                del hero[2][2][1][effect]
                effect = "deepsleep"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 3:
                            text = "stun"
                            message(text,hero,25,"purple",-20,-50)
                            return False
                        else:
                                del hero[2][2][1][effect]
                effect = "confuse"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 1:
                            text = "CONFUSE"
                            message(text,hero,25,"purple",-20,-30)
                        else:
                                del hero[2][2][1][effect]
                effect = "complete_confuse"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 3:
                            text = "COMPLETE CONFUSE"
                            message(text,hero,25,"purple",-20,-30)
                        else:
                                del hero[2][2][1][effect]
                effect = "bright"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 2:
                            text = "-50% Accuracy"
                            message(text,hero,25,"black",-20,-70)
                        else:
                                del hero[2][2][1][effect]
                effect = "focus"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 2:
                            text = "+50% Accuracy"
                            message(text,hero,25,"black",-20,-60)
                        else:
                                del hero[2][2][1][effect]
                effect = "mirror"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] <= 2:
                            text = "Mirror"
                            message(text,hero,25,"purple",-20,-60)
                        else:
                                del hero[2][2][1][effect]
                effect = "attackrise"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] >= 3:
                                del hero[2][2][1][effect]
                effect = "attackdown"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] >= 3:
                                del hero[2][2][1][effect]
                effect = "doubleattack"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] >= 3:
                                del hero[2][2][1][effect]
                effect = "traitdisable"
                if effect in hero[2][2][1]:
                        if hero[2][2][1][effect] >= 3:
                                del hero[2][2][1][effect]
                tobedel = []
                for yu in hero[2][2][1]:
                        if "immune" in yu:
                                if hero[2][2][1][yu] >= 4:
                                        tobedel.append(yu)
                for ani in tobedel:
                      del hero[2][2][1][ani]



                                
    return hero
def leagueshow():
    league= "1"
    return league
def summon(name,hero):
        aaa = 0
        new = 0
        new_heros = []
        for t in heros:
                new_heros.append(t)
        for um in new_heros:
                if um[0].upper() == name.upper():
                            aaa = um
                            battleready(aaa,False,hero[-1])
        for n in allo:
                if n[0] == name:
                        chase(n,hero,0)
                        n[6][22] = hero[6][22] + 0
                        break
        return
#######################################
def shop():
    gm = fileop("! Points")
    heros = fileop("xmonsters")
    owned = fileop("!owned")
    print()
    print("~~~~~~~~~~~SHOP~~~~~~~~~~~")
    print("You have:",int(gm[7][0]),"coins")
    print()
    print("a - Buy a common hero [100 Coins!]")
    print("b - Buy a rare hero [200 Coins!]")
    print("c - Buy an epic hero [1000 Coins!]")
    print("d - Increase Max Levels {common+20, rare+15, epic+10, legend+5} [5000 Coins!]")
    print("e - Buy an epic balance or chaos hero [5000 Coins!]")
    s = input("Select: ")
    while s not in ["a","b","c","d","e"]:
        s = input("Select: ")
    if s == "a":
        if int(gm[7][0]) >= 100:
            while True:
                    v = random.choice(heros)
                    rn = fileop("y-"+v[0].lower())
                    #print(rn[2][0])
                  #  rn = fileop("y-"+v[0].lower())
                    #v = random.choice(heros)
                    if rn[2][0] == "common":    
                            print("New Hero:", v[0])
                            owned.append([v[0].upper()])
                            s = input("Type OK: ")
                            if s == "ok" or s == "OK":
                                      break
            gm[7][0] = int(gm[7][0]) - 100
        else:
            print("Not Enough Money")
    if s == "b":
        if int(gm[7][0]) >= 200:
            while True:
                    v = random.choice(heros)
                    rn = fileop("y-"+v[0].lower())
                    #print(rn[2][0])
                  #  rn = fileop("y-"+v[0].lower())
                    #v = random.choice(heros)
                    if rn[2][0] == "rare":    
                            print("New Hero:", v[0])
                            owned.append([v[0].upper()])
                            s = input("Type OK: ")
                            if s == "ok" or s == "OK":
                                      break
            gm[7][0] = int(gm[7][0]) - 200
        else:
            print("Not Enough Money")
    if s == "c":
        if int(gm[7][0]) >= 1000:
            while True:
                    v = random.choice(heros)
                    rn = fileop("y-"+v[0].lower())
                    #print(rn[2][0])
                  #  rn = fileop("y-"+v[0].lower())
                    #v = random.choice(heros)
                    if rn[2][0] == "epic" and int(v[-1]) == 0 and rn[2][1] not in ["balance","chaos"]:    
                            print("New Hero:", v[0])
                            owned.append([v[0].upper()])
                            s = input("Type OK: ")
                            if s == "ok" or s == "OK":
                                      break
            gm[7][0] = int(gm[7][0]) - 1000
        else:
            print("Not Enough Money")
    if s == "e":
        if int(gm[7][0]) >= 5000:
            while True:
                    v = random.choice(heros)
                    rn = fileop("y-"+v[0].lower())
                    #print(rn[2][0])
                  #  rn = fileop("y-"+v[0].lower())
                    #v = random.choice(heros)
                    if rn[2][0] == "epic" and int(v[-1]) == 0 and rn[2][1] in ["balance","chaos"]:    
                            print("New Hero:", v[0])
                            owned.append([v[0].upper()])
                            s = input("Type OK: ")
                            if s == "ok" or s == "OK":
                                      break
            gm[7][0] = int(gm[7][0]) - 5000
        else:
            print("Not Enough Money")    
    if s == "d":
        if int(gm[7][0]) >= 5000:
            while True:
                    s = input("Levels increased! OK: ")
                    if s == "ok" or s == "OK":
                        break
            gm[16][0] = int(gm[16][0]) + 20
            gm[19][0] = int(gm[19][0]) + 15
            gm[22][0] = int(gm[22][0]) + 10
            gm[25][0] = int(gm[25][0]) + 5
            gm[7][0] = int(gm[7][0]) - 5000
        else:
            print("Not Enough Money")
    save(gm,"! Points")
    print()
    print()
    print("______________")
    print()
    return
def hrc(league):
   
    hr = random.choice(alls)
    if hr[-1] == "y":
            return hrc(league)
    if league[-1] == "1" and acc(50) == True:
        hr = random.choice(alls[0:30])
    elif league[-1] == "2" and acc(50) == True:
        hr = random.choice(alls[0:40])
    elif league[-1] == "3" and acc(50) == True:
        hr = random.choice(alls[10:50])
    elif league[-1] == "4" and acc(50) == True:
        hr = random.choice(alls[20:60])
    elif league == "5" and acc(50) == True:
        hr = random.choice(alls[0:60])
    elif league == "6" and acc(50) == True:
        hr = random.choice(alls[30:])
    elif league[-1] == "7" and acc(50) == True:
        hr = random.choice(alls[40:])
    else:
        hr = random.choice(alls)
    if hr[-1] == "y":
            return hrc(league)
#    while hr[0] not in ["NOYA","GUNPRO","JETMAX","ICEFAIRY","ALLMIGHT","DEKU","AYLEY","IGNITUS","KEN","SPRAYRAY", "MAKINA","FINN","DYNAMAX","GUNPRO","CRYSTOFROST","SURVIVORA","REVENGERA","FANNY","EMILIA","GRAVEKEEPER"]:
   #         hr = random.choice(alls)
    return hr
def wait(sec):
        now = nowtime()
        while True:
                if round(nowtime()) % 1 == 0:
                        if nowtime() - now >= sec:
                                return
        return
lord = False
minio = False
print("~~~~~~~~~~~~~~~~~~~~~~CREATURES OF ADVENTURELAND~~~~~~~~~~~~~~~~~~~~~~")
league = leagueshow()
#print("z - STARWORLD CHAMPIONSHIP BATTLE ARENA [Season 1: Lockdown Summer]!")
#print("x - FINAL WAR ARENA! [3 CHANCES!]")
#print("a - AOTSA ARENA!")
#print("c - CHAMPIONS ARENA [Yo
#print("f - My Friends"
#print("~THE WORLD LEAGUE [COMING SOON!]  ")
pointsmap = fileop("! Points")
mapstage = int(pointsmap[13][0])
print("r - Arena")
print("w - Difficult Arena")
print("a - Adventure Map | Stage:",mapstage)
print("s - Shop")
print()
ku = 0
mod2 = "2"
while ku not in ["a","s","r","w"]:
        ku = input("Enter: ")
if ku == "a":
        mode = "adventuremap"
if ku == "r":
        mode = "battlearena"
        print()
        print("HOW TO PLAY:")
        print("-Click on the target you want to attack. Choose skill by pressing 1,2,3,4.")
        print("-Every skill has a 1 turn cooldown")
        print()
if ku == "w":
        ku = "r"
        mode = "battlearena"
        mod2 = "new"
if ku == "s":
        shop()
heros = fileop("xheroes")
monsters = fileop("xmonsters")
ateam = []
eteam = []
found = False
owned = []
ownd = fileop("!owned")
for ow in ownd:
        owned.append(ow[0])

print("OWNED:",owned)
if mod2 == "new":
        for ow in monsters:
                owned.append(ow[0])
while found != True:
        mons1 = input("1 - Enter a monster:")
        if mons1 == "r":
                mons1 = random.choice(monsters)[0]
        if mons1.upper() not in ateam and  mons1.upper() in owned:
                for n in monsters:
                        if n[0] == mons1.upper():
                                lev = round(int(n[1])/100)
                                if lev > 30:
                                        lev = 30
                                print("Lvl:",lev)
                                found = True
                                break

found = False
while found != True:
        mons2 = input("2 - Enter a monster:")
        if mons2 == "r":
                mons2 = random.choice(monsters)[0]
        if mons2.upper() not in ateam and  mons1.upper() in owned:
                for n in monsters:
                        if n[0] == mons2.upper():
                                lev = round(int(n[1])/100)
                                if lev > 30:
                                        lev = 30
                                print("Lvl:",lev)
                                found = True
                                break
found = False
while found != True:
        mons3 = input("3 - Enter a monster:")
        if mons3 == "r":
                mons3 = random.choice(monsters)[0]
        if mons3.upper() not in ateam and  mons1.upper() in owned:
                for n in monsters:
                        if n[0] == mons3.upper():
                                lev = round(int(n[1])/100)
                                if lev > 30:
                                        lev = 30
                                print("Lvl:",lev)
                                found = True
                                break

ateam = []
mons1w = fileop(str("y-"+mons1.lower()))
ateam.append(mons1w)
mons2w = fileop(str("y-"+mons2.lower()))
ateam.append(mons2w)
mons3w = fileop(str("y-"+mons3.lower()))
ateam.append(mons3w)

alls = []
for ss in heros:
        alls.append(ss)
i = "z"
allyno = 0
eneno = 0
mode = 0
stage = 0
mychoice = "?"

if i == "x":
            mode = "multi"
            i = "z"
while i not in ["a","s","t","w","m","c","f","z"]:
    i = input("Select: ")
if i == "s":
    shop()
if i == "f":
    friends = fileop("xfriends")
##    for x in heros:
##	j = False
##	for p in friends:
##		if x[-1] == "y":
##			j = True
##			break
##		if x[0] in p and x[-1] == "x":
##			j = True
##			break
##	if j == False:
##		print(x[0])
    #save(friends,"xfriends")
    for f in friends:
            print(f[0], "\t\tFavourites: ",end="")
            for ada in f[1:]:
                    print(ada,end=", ")
            print()    
    print()
    i = input("Select: ")
    while i not in ["a","s","t","w","m","c","z"]:
            i = input("Select: ")
if i == "a" or i == "t" or i == "w" or i == "m" or i == "c" or i == "z":
    u = False
    hr = ""
    k = True
    if i == "m":
            print()
            print("~~~~~~~~~~Map of the Adventures~~~~~~~~~~")
            print("CHAPTER 1: Save The Town [1-10]")
            print("CHAPTER 2: Save The Town Part 2 [11-20]")
            print("CHAPTER 3: Adventure Time! [21-30]")
            print("CHAPTER 4: Disasterlands [31-40]")
            print("CHAPTER 5: Forgotten Arena [41-75]")
            print()
            stage = 0
            while stage not in range(1,100):
                    stage = int(input("Select a stage 1-75: "))
    while u == False:
        if i == "w":
                hr = input("Which hero do you want to watch: ")
                playerr = fileop("xplayers")
                players = []
                for hh in playerr:
                        players.append(hh[0])
                print()
                print("Player:",random.choice(players))
                print()
        else:
                if int(league) > 13 and league[-1] in ["4"] and k == True and i != "m" and i != "z":
                        print()
                        banned = []
                        while True:
                                p=1
                                bn = input("Which champion do you want to BAN?:")
                                for n4 in alls:
                                       if n4[0].upper() == bn.upper():
                                               p=0
                                               break
                                if p==0:
                                        break
                        banned.append(n4)
                        alls.remove(n4)
                        print("       !!!       ")
                        print("Banned Champions:")
                        
                        st = False
                        while st == False:
                                bn = random.choice(alls)
                                while bn[-1] != "x":
                                        bn = random.choice(alls)
                                if int(bn[4]) >= 300 and int(bn[1][0] + bn[1][1] + bn[1][2]) >= 100:
                                        if acc(50) == True:
                                                st = True
                                if acc(10) == True:
                                        st = True
                        banned.append(bn)
                        alls.remove(bn)
                        
                        st = False
                        while st == False:
                                bn = random.choice(alls)
                                while bn[-1] != "x":
                                        bn = random.choice(alls)
                                if int(bn[4]) >= 300 and int(bn[1][0] + bn[1][1] + bn[1][2]) >= 100:
                                        if acc(50) == True:
                                                st = True
                                if acc(10) == True:
                                        st = True
                        banned.append(bn)
                        alls.remove(bn)
                      
                        st = False
                        while st == False:
                                bn = random.choice(alls)
                                while bn[-1] != "x":
                                        bn = random.choice(alls)
                                if int(bn[4]) >= 300 and int(bn[1][0] + bn[1][1] + bn[1][2]) >= 100:
                                        if acc(50) == True:
                                                st = True
                                if acc(5) == True:
                                        st = True
                        banned.append(bn)
                        alls.remove(bn)
                        
                        st = False
                        while st == False:
                                bn = random.choice(alls)
                                while bn[-1] != "x":
                                        bn = random.choice(alls)
                                if int(bn[4]) >= 300 or int(bn[1][0] + bn[1][1] + bn[1][2]) >= 100:
                                        if acc(50) == True:
                                                st = True
                                if acc(10) == True:
                                        st = True
                        banned.append(bn)
                        alls.remove(bn)
                        
                        st = False
                        while st == False:
                                bn = random.choice(alls)
                                while bn[-1] != "x":
                                        bn = random.choice(alls)
                                if int(bn[4]) >= 300 and int(bn[1][0] + bn[1][1] + bn[1][2]) >= 100:
                                        if acc(50) == True:
                                                st = True
                                if acc(10) == True:
                                        st = True
                        banned.append(bn)
                        alls.remove(bn)
                       
                        st = False
                        while st == False:
                                bn = random.choice(alls)
                                while bn[-1] != "x":
                                        bn = random.choice(alls)
                                if int(bn[4]) >= 300 and int(bn[1][0] + bn[1][1] + bn[1][2]) >= 100:
                                        if acc(50) == True:
                                                st = True
                                if acc(10) == True:
                                        st = True
                        banned.append(bn)
                        alls.remove(bn)
                       
                        st = False
                        while st == False:
                                bn = random.choice(alls)
                                while bn[-1] != "x":
                                        bn = random.choice(alls)
                                if int(bn[4]) >= 300 and int(bn[1][0] + bn[1][1] + bn[1][2]) >= 100:
                                        if acc(50) == True:
                                                st = True
                                if acc(5) == True:
                                        st = True
                        banned.append(bn)
                        alls.remove(bn)
                       
                        st = False
                        while st == False:
                                bn = random.choice(alls)
                                while bn[-1] != "x":
                                        bn = random.choice(alls)
                                if int(bn[4]) >= 300 or int(bn[1][0] + bn[1][1] + bn[1][2]) >= 100:
                                        if acc(50) == True:
                                                st = True
                                if acc(10) == True:
                                        st = True
                        banned.append(bn)
                        alls.remove(bn)
                      
                        st = False
                        while st == False:
                                bn = random.choice(alls)
                                while bn[-1] != "x":
                                        bn = random.choice(alls)
                                if int(bn[4]) >= 300 and int(bn[1][0] + bn[1][1] + bn[1][2]) >= 100:
                                        if acc(50) == True:
                                                st = True
                                if acc(10) == True:
                                        st = True
                        banned.append(bn)
                        alls.remove(bn)
                      
                        print("Allies banned: ",end="")
                        for z in banned[:5]:
                                print(z[0],end=", ")
                        print()
                        print("Enemies banned: ",end="")
                        for z in banned[5:]:
                                print(z[0],end=", ")
                                
                        print()
                        k =  False
                        print()
                hr = "ME"
               # hr = hrc(league)[0]
               # print(hr)
##        lastuse = fileop("xlastuse")
##        mx = True
##        for n in lastuse[0][(len(lastuse[0])-2):]:
##                if hr.upper() == n.upper():
##                        print("You can't use the same hero again  [",3-(len(lastuse[0])-lastuse[0].index(n.upper())),"left]")
##                        mx = False
##                        break
##                if 3-(len(lastuse[0])-lastuse[0].index(n.upper())) <= 0:
##                        lastuse[0].remove(n)
        #if mx == True:
        for y in alls:
            if y[0].upper() == hr.upper() and y[-1] == "x":
                hr = y
                u = True
                break
        if u == False:
               print("Try again please :)") 
##        save(lastuse,"xlastuse")
    if i not in ["m","w","z"]:
            mychoice = input("Attack or Defense? {a/d}: ")
            while mychoice not in ["a","d"]:
                    mychoice = input("Attack or Defense? {a/d}: ")
    if i in ["z"]:
            mychoice = "u"
    #ally
    allied = False
    if i == "m":
            if stage in [3,4,5,6,7,8,10,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,46,47,48,49,51,52,53,54,55,37] or (stage > 55) or (stage > 30 and stage % 2 == 0) or (stage > 30 and stage % 5 == 0) or (stage > 55):
               hr2 = input("Select your ally: ")
               for y in alls:
                    if y[0].upper() == hr2.upper() and y[-1] == "x":
                        hr2 = y
                        u = True
                        break
    if i == "m" and stage in [20,26,27,29,30,46,47,48,49,51,52,53,54,55] or (stage > 30 and stage % 5 == 0) or (stage > 55):
               hr3 = input("Select your other ally: ")
               for y in alls:
                    if y[0].upper() == hr3.upper() and y[-1] == "x":
                        hr3 = y
                        u = True
                        break
    if i != "z" and i != "t" and mode != "multi":
            friends = fileop("xfriends")
            allied = True
            print()
            somevar = True
            while somevar == True:
                    hname = input("Select your ally: ")
                    for nf in friends:
                            if hname.upper() == nf[0].upper():
                                    somevar = False
                                    break
            while True:
                    hr2 = random.choice(nf[1:])
                    u = False
                    for y in alls:
                            if y[0].upper() == hr2.upper() and y[-1] == "x":
                                hr2 = y
                                u = True
                                break
                    if u == True:
                            break
            print(hname.capitalize(), "will use",hr2[0])
            hname2 = hname.upper()
            alls.remove(hr2)
            move = input(">>>")
            somevar = True
            while somevar == True:
                    hname = input("Select your other ally: ")
                    for nf in friends:
                            if hname.upper() == nf[0].upper():
                                    somevar = False
                                    break
            while True:
                    hr3 = random.choice(nf[1:])
                    u = False
                    for y in alls:
                            if y[0].upper() == hr3.upper() and y[-1] == "x":
                                hr3 = y
                                u = True
                                break
                    if u == True:
                            break
            print(hname.capitalize(), "will use",hr3[0])
            hname3 = hname.upper()
            alls.remove(hr3)
            move = input(">>>")
            somevar = True
            while somevar == True:
                    hname = input("Select your other ally: ")
                    for nf in friends:
                            if hname.upper() == nf[0].upper():
                                    somevar = False
                                    break
            while True:
                    hr4 = random.choice(nf[1:])
                    u = False
                    for y in alls:
                            if y[0].upper() == hr4.upper() and y[-1] == "x":
                                hr4 = y
                                u = True
                                break
                    if u == True:
                            break
            print(hname.capitalize(), "will use",hr4[0])
            hname4 = hname.upper()
            alls.remove(hr4)
            move = input(">>>")
            somevar = True
            while somevar == True:
                    hname = input("Select your other ally: ")
                    for nf in friends:
                            if hname.upper() == nf[0].upper():
                                    somevar = False
                                    break
            while True:
                    hr5 = random.choice(nf[1:])
                    u = False
                    for y in alls:
                            if y[0].upper() == hr5.upper() and y[-1] == "x":
                                hr5 = y
                                u = True
                                break
                    if u == True:
                            break
            print(hname.capitalize(), "will use",hr5[0])
            hname5 = hname.upper()
            alls.remove(hr5)
            move = input(">>>")
            print()
            #i = "a"
    ostlist = ["ostn1","ostn2"]        
    music = random.choice(ostlist) 
    import pygame
    import time
    global time
    #images
    allyno = 0
    eneno = 0
    ischaos = pygame.image.load("ischaos.png")
    isbalance = pygame.image.load("isbalance.png")
    iscloud = pygame.image.load("iscloud.png")
    isgem = pygame.image.load("isgem.png")
    isplant = pygame.image.load("isplant.png")
    issea = pygame.image.load("issea.png")
    isstatic = pygame.image.load("isstatic.png")
    isstar = pygame.image.load("isstar.png")
    itarget = pygame.image.load("itarget.png")
    istatb = pygame.image.load("istatb.png")
    iboxstar = pygame.image.load("iboxstar.png")
    iboxstatic = pygame.image.load("iboxstatic.png")
    iboxsea = pygame.image.load("iboxsea.png")
    iboxplant = pygame.image.load("iboxplant.png")
    iboxgem = pygame.image.load("iboxgem.png")
    iboxcloud = pygame.image.load("iboxcloud.png")
    iboxbalance = pygame.image.load("iboxbalance.png")
    iboxchaos = pygame.image.load("iboxchaos.png")
    gridh = pygame.image.load("gridh.png")
    gridv = pygame.image.load("gridv.png")
    ibk = pygame.image.load("ibk.png")
    ibkk1 = pygame.image.load("ibkk1.png")
    ibkk2 = pygame.image.load("ibkk2.png")
    ibk2 = pygame.image.load("ibk2.png")
    ibk3 = pygame.image.load("ibk3.png")
    ibk4 = pygame.image.load("ibk4.png")
    ibk5 = pygame.image.load("ibk5.png")
    ip1 = pygame.image.load("ip1.png")
    ip2 = pygame.image.load("ip2.png")
    iback = pygame.image.load("iback.png")
    iback2 = pygame.image.load("iback2.png")
    ipr1 = pygame.image.load("ipr1.png")
    iw = pygame.image.load("iw.png")
    ie = pygame.image.load("ie.png")
    ir = pygame.image.load("ir.png")
    iw22 = pygame.image.load("iw22.png")
    ie22 = pygame.image.load("ie22.png")
    ir22 = pygame.image.load("ir22.png")
    it22 = pygame.image.load("it22.png")
    iespace2 = pygame.image.load("iespace2.png")
    ier = pygame.image.load("ier.png")
    idark = pygame.image.load("idark.png")
    iinv = pygame.image.load("iinv.png")
    hal = pygame.image.load("hal.png")
    hen = pygame.image.load("hen.png")
    hyu = pygame.image.load("hyu.png")
    hde = pygame.image.load("hde.png")
    hlo = pygame.image.load("hlo.png")
    hlvl = pygame.image.load("hlvl.png")
    hsh = pygame.image.load("hsh.png")
    het = pygame.image.load("het.png")
    ivictory = pygame.image.load("ivictory.png")
    idefeat = pygame.image.load("idefeat.png")
    i2back = pygame.image.load("i2back.png")
    i2ene = pygame.image.load("i2ene.png")
    i2ally = pygame.image.load("i2ally.png")
    i2kill = pygame.image.load("i2kill.png")
    i2ded = pygame.image.load("i2ded.png")
    i2asst = pygame.image.load("i2asst.png")
    h2al = pygame.image.load("h2al.png")
    h2en = pygame.image.load("h2en.png")
    h2yu = pygame.image.load("h2yu.png")
    h2de = pygame.image.load("h2de.png")
    h2lo = pygame.image.load("h2lo.png")
    h2sh = pygame.image.load("h2sh.png")
    h2et = pygame.image.load("h2et.png")
    irange = pygame.image.load("irange.png")
    irangee = pygame.image.load("irangee.png")
    irangey = pygame.image.load("irangey.png")
    baral = pygame.image.load("baral.png")
    baren = pygame.image.load("baren.png")
    barst = pygame.image.load("barst.png")
    baryu = pygame.image.load("baryu.png")
    barde = pygame.image.load("barde.png")
    bardu = pygame.image.load("bardu.png")
    bardu2 = pygame.image.load("bardu2.png")
    barlo = pygame.image.load("barlo.png")
    barsh = pygame.image.load("barsh.png")
    iespace = pygame.image.load("iespace.png")
    if1 = pygame.image.load("if1.png")
    if2 = pygame.image.load("if2.png")
    ierr = pygame.image.load("ierr.png")
   # if3 = pygame.image.load("if1.png")
    begtime = time.time()
    pygame.init()
    pygame.mixer.init()
    #win = pygame.display.set_mode((1000,600))
    win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.toggle_fullscreen()
    pygame.display.set_caption("WOTER")
    allo = []
    oballo = []
    projectiles = []
    deadall = []
    
    
    for ant in allo:
            if ant[-1] == None and ant[0] not in ["ALLYSPAWN","ALLYSPAWN2","ENESPAWN","ENESPAWN2","ENEBASE","ENETOWERMID", "ENETOWERDOWN", "ENETOWERUP","ALLYBASE","ALLYTOWERMID", "ALLYTOWERDOWN", "ALLYTOWERUP"]:
                    allo.remove(ant)
                    oballo.append(ant)
    count = 0
##    for anytt in ateam:
##              count = count + 1
##              anytt[2].append([0,{},[],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) #[2][3]
##              resm = "i"+anytt[0][0].lower()+".png"
##              resm = pygame.image.load(resm) 
##              resm2 = pygame.transform.flip(resm,True,False)
##              we, he = obrect.width, obrect.height
##              text = pygame.transform.rotozoom(text, 0, 0.6)
##              anytt[2][2][2] = resm2
##              if count == 1:
##                      anytt[2][2][3] = [500,350]
##              if count == 2:
##                      anytt[2][2][3] = [700,550]
##              if count == 3:
##                      anytt[2][2][3] = [500,750]  
##              
##              anytt[2][2][4] = int(anytt[1][0]) #maxhp
##              for mm in monsters:
##                      if mm[0] == anytt[0][0]:
##                              anytt[2][2][5] = int(mm[1])
##                              break
##              
##              for anyt in anytt:
##                for at in anyt:
##                        try:
##                                at = int(at)
##                        except:
##                                at = at
##              anytt.append(True)
##              anytt.append("X")      
   #allies
    hname = 0
    battleready(hr,True,True)
    #window()
    #music
     #,
   # win.blit(idefeat,(600,400))
   # pygame.display.update()
    lmessage("LOADING!",400,400)
   # window()
    lmessage("START!",400, 400)
    
    if league[-1] == "7" or league[-1] == "0":
            ltimel = 200
    else:
            ltimel = 310
##    x=50
##    y=50
##    w = 40
##    h = 60
##    vel = 5
    run = True
    timerebs = 1
    print("STARTED! PLEASE OPEN THE OTHER WINDOW :)")
    wait(1)
    battlemode = "ZONE"
    zone = 0
    prezone = 0
    world = 1
    preworld = 0
     #BACK
    battlemode = "ON"
      ########battle
    zonelake = []
    if ku == "a":
            mode = "adventuremap"
            dungeon = fileop("!map")
            dunstage = dungeon[mapstage]
            monsters = fileop("xmonsters")
            #print(dunstage)
            for rn in monsters:
                      soe = fileop("y-"+rn[0].lower())
                      if rn[0].upper() in dunstage:
                                     zonelake.append(soe)
    if ku == "r":  
        mode = "battlearena"
        #print(dunstage)
        monsters = fileop("xmonsters")
        while True:
            enm = random.choice(monsters)
            rn = fileop("y-"+enm[0].lower())
            if rn[2][0] in ["epic","legend"]:
                      break
        zonelake.append(rn)
        while True:
            enm = random.choice(monsters)
            rn = fileop("y-"+enm[0].lower())
            if rn[2][0] in ["legend"]:
                      break
        zonelake.append(rn)
        while True:
            enm = random.choice(monsters)
            rn = fileop("y-"+enm[0].lower())
            if rn[2][0] in ["legend"]:
                      break
        zonelake.append(rn)
    zone = "common"
    if mode == "battlearena":
            batb = pygame.image.load("iarena.png")
    elif mode == "adventuremap":
            if mapstage > 110:
                    batb = pygame.image.load("iadv6.png")
            elif mapstage > 100:
                    batb = pygame.image.load("iadv5.png")
            elif mapstage > 90:
                    batb = pygame.image.load("iadv4.png")
            elif mapstage > 80:
                    batb = pygame.image.load("iadv1.png")
            elif mapstage > 70:
                    batb = pygame.image.load("iadv2.png")
            elif mapstage > 60:
                    batb = pygame.image.load("iadv3.png")    
            elif mapstage > 50:
                    batb = pygame.image.load("iadv6.png")
            elif mapstage > 40:
                    batb = pygame.image.load("iadv5.png")
            elif mapstage > 30:
                    batb = pygame.image.load("iadv4.png")
            elif mapstage > 20:
                    batb = pygame.image.load("iadv1.png")
            elif mapstage > 10:
                    batb = pygame.image.load("iadv2.png")
            else:
                    batb = pygame.image.load("iadv3.png")    
    cplay(random.choice(["ost1","ost2","ost3","ost3"]))
    eteam = []  
     # zonelake = ["nen"]
      #name = "y-"+random.choice(zonelake[0].lower())
     # mons = fileop(name)
    for monst in zonelake:
            eteam.append(monst)
    allyle = []    
    for birsey in ateam: 
            for sdn in monsters:
                      if sdn[0].upper() == birsey[0][0].upper():
                             allyle.append(int(sdn[1]))
    while progress == True:
      #battlemode  
      if battlemode == "ON":
        backgroundd = [batb,0,0]
        begtime = time.time()
        stopwindow()
        #prepare
        objtim = []
        ateam = []
        mons1w = fileop(str("y-"+mons1.lower()))
        ateam.append(mons1w)
        mons2w = fileop(str("y-"+mons2.lower()))
        ateam.append(mons2w)
        mons3w = fileop(str("y-"+mons3.lower()))
        ateam.append(mons3w)
        count = 0
        for anytt in eteam:
              count = count + 1
              anytt[2].append([0,{},[],0,0,0,0,[],0,0,0,0,0,0,0,0,0,0,0]) #[2][3]
              resm = "i"+anytt[0][0].lower()+".png"
              resm = pygame.image.load(resm) #positions
              resm2 = pygame.transform.flip(resm,True,False)
              #resm2 = "i"+anytt[0][0].lower()+"2.png"
              anytt[2][2][2] = resm
              if count == 1:
                      anytt[2][2][3] = [1400,350]
              if count == 2:
                      anytt[2][2][3] = [1200,550]
              if count == 3:
                      anytt[2][2][3] = [1400,750]  
              
              #####levels
              if mode == "adventuremap":
                      expre = int(dunstage[-1])
                      anytt[2][2][5]= expre*100
              if mode == "battlearena":
                      anytt[2][2][5] = sum(allyle)/len(allyle)
              if zone == "arena":
                      anytt[2][2][5] = 30000
              if "elementum" in zone:
                      anytt[2][2][5] = 30000
              if "wizard" in zone:
                      anytt[2][2][5] = anytt[2][2][5] + 1000
              if mod2 == "new":
                      anytt[2][2][5] = 1000  
              for anyt in anytt:
                for at in anyt:
                        try:
                                at = int(at)
                        except:
                                at = at
              anytt[1][0] = round(int(anytt[1][0]) * (1 + anytt[2][2][5]/1000))
              if mode == "adventuremap":
                      if count == 2 or len(eteam) == 1:
                              if mapstage % 5 == 0 and mapstage != 0:
                                      if mapstage >= 25:   
                                              anytt[1][0] = anytt[1][0] * 5
                                      elif mapstage >= 15:   
                                              anytt[1][0] = anytt[1][0] * 4
                                      elif mapstage >= 10:
                                              anytt[1][0] = anytt[1][0] * 3 
                                      if mapstage >= 70:
                                              eff(anytt,"stunimmune")
                                      if mapstage >= 80:  
                                              eff(anytt,"brightimmune")
                                      if mapstage >= 90:  
                                              eff(anytt,"poisonimmune")
                                      if mapstage >= 100:  
                                              eff(anytt,"burnimmune")
                                              eff(anytt,"confuseimmune")
                                      if mapstage >= 110:
                                              eff(anytt,"bleedimmune")
                                              #bosseffects
              if anytt[2][0] == "epic" or anytt[2][0] == "legend":
                      if anytt[2][1] == "star":
                              eff(anytt,"burnimmune")
                      if anytt[2][1] == "static":
                              eff(anytt,"shockimmune")
                      if anytt[2][1] == "cloud":
                              eff(anytt,"confuseimmune")
                      if anytt[2][1] == "plant":
                              eff(anytt,"poisonimmune")
                      if anytt[2][1] == "sea":
                              eff(anytt,"attackdownimmune")
                      if anytt[2][1] == "gem":
                              eff(anytt,"stunimmune")
                      if anytt[2][1] == "chaos":
                              eff(anytt,"burnpoisonbleedshockblindimmune")
                      if anytt[2][1] == "balance":
                              eff(anytt,"brightstunconfuseattackdownfreezeimmune")        
              anytt[1][1] = round(int(anytt[1][1]) * (1 + anytt[2][2][5]/1000))
              anytt[1][2] = round(int(anytt[1][2]) * (1 + anytt[2][2][5]/1000))
              anytt[1][3] = int(anytt[1][3])/2 + (int(anytt[1][3])/2 * round((anytt[2][2][5]/100)) ) / 30
              anytt[1][4] = int(anytt[1][4])/2 + (int(anytt[1][4])/2 * round((anytt[2][2][5]/100)) ) / 30
              anytt[1][5] = round(int(anytt[1][5]) * (1 + anytt[2][2][5]/1000))
              anytt[2][2][4] = int(anytt[1][0]) #maxhp
              anytt.append(False)
              anytt.append("X")
              anytt[1].append(random.choice(range(10000,1000000))) #code
        countww = 0
        for anytt in ateam:
              countww = countww + 1
              anytt[2].append([0,{},[],0,0,0,0,[],0,0,0,0,0,0,0,0,0,0,countww]) #[2][3]
              resm = "i"+anytt[0][0].lower()+".png"
              resm = pygame.image.load(resm)
              #optimizer###############################
             # we, he = resm.width, resm.height
              #text = pygame.transform.rotozoom(text, 0, 0.6)
              ####################################################
              resm2 = pygame.transform.flip(resm,True,False)
              #resm2 = "i"+anytt[0][0].lower()+"2.png" #positions2
              anytt[2][2][2] = resm2
              if countww == 1:
                      anytt[2][2][3] = [500,350]
              if countww == 2:
                      anytt[2][2][3] = [700,550]
              if countww == 3:
                      anytt[2][2][3] = [500,750]  
              
              #anytt[2][2][3] = [400,400]
              
              for dn in monsters:
                      if dn[0].upper() == anytt[0][0].upper():
                             anytt[2][2][5] = int(dn[1])
              if mode == "adventuremap":  
                      expre = int(dunstage[-1])
                      nowsta = expre*100  
                      if anytt[2][2][5] < (nowsta-1000): #levelcap
                              anytt[2][2][5] = nowsta
              if mod2 == "new":
                      anytt[2][2][5] = 1000   
              caps = fileop("! Points")
              commoncap = int(caps[16][0])*100
              rarecap = int(caps[19][0])*100
              epiccap = int(caps[22][0])*100
              legendcap = int(caps[25][0])*100
              rarity = anytt[2][0]
              if rarity == "common":
                      if anytt[2][2][5] > commoncap:
                              anytt[2][2][5] = commoncap
              if rarity == "rare":
                      if anytt[2][2][5] > rarecap:
                              anytt[2][2][5] = rarecap
              if rarity == "epic":
                      if anytt[2][2][5] > epiccap:
                              anytt[2][2][5] = epiccap
              if rarity == "legend":
                      if anytt[2][2][5] > legendcap:
                              anytt[2][2][5] = legendcap   
              for anyt in anytt:
                for at in anyt:
                        try:
                                at = int(at)
                        except:
                                at = at
                                #30 lvl
                                #stat ?
              if anytt[2][0] == "epic" or anytt[2][0] == "legend":
                      if anytt[2][1] == "star":
                              eff(anytt,"burnimmune")
                      if anytt[2][1] == "static":
                              eff(anytt,"shockimmune")
                      if anytt[2][1] == "cloud":
                              eff(anytt,"confuseimmune")
                      if anytt[2][1] == "plant":
                              eff(anytt,"poisonimmune")
                      if anytt[2][1] == "sea":
                              eff(anytt,"attackdownimmune")
                      if anytt[2][1] == "gem":
                              eff(anytt,"stunimmune")
                      if anytt[2][1] == "chaos":
                              eff(anytt,"burnpoisonbleedshockblindimmune")
                      if anytt[2][1] == "balance":
                              eff(anytt,"brightstunconfuseattackdownfreezeimmune")                   
              anytt[1][0] = round(int(anytt[1][0]) * (1 + anytt[2][2][5]/1000))
              anytt[1][1] = round(int(anytt[1][1]) * (1 + anytt[2][2][5]/1000))
              anytt[1][2] = round(int(anytt[1][2]) * (1 + anytt[2][2][5]/1000))
              anytt[1][3] = int(anytt[1][3])/2 + (int(anytt[1][3])/2 * round((anytt[2][2][5]/100)) ) / 30
              anytt[1][4] = int(anytt[1][4])/2 + (int(anytt[1][4])/2 * round((anytt[2][2][5]/100)) ) / 30
              anytt[1][5] = round(int(anytt[1][5]) * (1 + anytt[2][2][5]/1000))
              anytt[2][2][4] = int(anytt[1][0]) #maxhp
              anytt.append(True)
              anytt.append("X")
              anytt[1].append(random.choice(range(10000,1000000))) #code
        #print(ateam,eteam)
        
        #eteam[0][-1] = True
        #ateam[0][-1] = True
        #eteam[0][2][2][6] = 0
        #ateam[0][2][2][6] = 0
        turntime = 0
        first = False
        run = True
        for mons in ateam:
                mons[1][5] = mons[1][5] + random.choice(range(10,500))/100
        for mons in eteam:
                mons[1][5] = mons[1][5] + random.choice(range(10,500))/100       
        while run == True:
                #window()
                
                pygame.time.delay(10)
                keys = pygame.key.get_pressed()
                
                #here 
                turncalculator(ateam,eteam)
                text = ""
                
                if len(ateam) == 0 and testing_game == False:
                            lmessage("YOU LOST!",400,400)
                            #win.blit(idefeat,(600,400))
                            #cplay("ostlost")
                            pygame.display.update()
                            wplay("v7")
                            #print()
                            battlemode = "ZONE"
                            if mode == "battlearena":
                                    points = fileop("! Points")
                                    points[4][0] = int(points[4][0]) + 1
                                    save(points,"! Points")
                            run = False
                            progress = False
                            u = False
                            prezone = 0
                            #break
                            waiting()
                            pygame.quit()
                if len(eteam) == 0 and testing_game == False:
                            #win.blit(ivictory,(600,400))
                            pygame.display.update()
                            lmessage("YOU WIN!",400,400)
                            #cplay("ostwin")
                            wplay("v1")
                            points = fileop("! Points")
                            if mode == "battlearena":
                                    points[1][0] = int(points[1][0]) + 1
                                    points[7][0] = int(points[7][0]) + 70
                            if mode == "adventuremap":
                                    points[7][0] = int(points[7][0]) + random.choice(range(50,100))
                                    if mapstage % 5 == 0:
                                            points[7][0] = int(points[7][0]) + random.choice(range(5,100))
                                            points[7][0] = int(points[7][0]) + random.choice(range(5,100))
                                    if mapstage >= 40:
                                            points[7][0] = int(points[7][0]) + random.choice(range(50,100))
                            if mode == "adventuremap":
                                    points[13][0] = int(points[13][0]) + 1 #position#
                            save(points,"! Points")
                            xp = 50
                            if "elementum" in zone:
                                    points = fileop("! Points")
                                    points[1][0] = int(points[1][0]) + 1
                                    points[7][0] = int(points[7][0]) + random.choice(range(50,100))
                                    save(points,"! Points")
                                    xp = 200
                            monsteall = fileop("xmonsters")
                            avxp = sum(allyle)/len(allyle)
                            for an in monsteall:
                                    for al in ateam:
                                            if al[0][0].upper() == an[0].upper():
                                                   xp = random.choice(range(70,90))
                                                   if mode == "adventuremap":
                                                           if mapstage % 5 == 0:
                                                                   xp = xp + random.choice(range(70,90))
                                                   if mode == "battlearena":
                                                           xp = xp + 80
                                                   lmessage("+"+str(xp)+"XP",400,random.choice(range(200,500)))     
                                                   an[1] = int(an[1]) +xp #xp
                                                   if int(an[1]) < avxp:
                                                           an[1] = round(avxp)
                            save(monsteall,"xmonsters")
                            #print()
                            #battlemode = "OFF"
                            run = False
                            prezone = 0
                            waiting()
                            progress = False
                            u = False
                            pygame.quit()
                            break
                           # break
            
