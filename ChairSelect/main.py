import pygame as pg
import random as rd
import config
from PIL import Image

windowsize = [1020,680] 

NameList = config.NameList


List = [str(i) + '. ' + str(NameList[i-1]) for i in range (1, 27)]

Person = []
Person2 = []
def initGame() :
    global gamepad, clock, Large_font, font, background, horse_1, horse_2, horse_3, horse_4, horse_5, horse_1_flipped , horse_2_flipped ,horse_3_flipped, horse_4_flipped, horse_5_flipped
    pg.init()
    pg.display.set_caption("ChairSelect")
    font = pg.font.Font('./ChairSelect/font/CookieRunBlack.ttf',20)
    Large_font = pg.font.Font('./ChairSelect/font/CookieRunBlack.ttf',40)

    background=pg.image.load ('./ChairSelect/image/background.png')
    background = pg.transform.scale(background,windowsize)

    horse_1 = pg.image.load('./ChairSelect/image/horses/horseback(1).png')
    horse_1 = pg.transform.scale(horse_1, (75, 75))
    horse_2 = pg.image.load('./ChairSelect/image/horses/horseback(2).png')
    horse_2 = pg.transform.scale(horse_2, (75, 75))
    horse_3 = pg.image.load('./ChairSelect/image/horses/horseback(3).png')
    horse_3 = pg.transform.scale(horse_3, (75, 75))
    horse_4 = pg.image.load('./ChairSelect/image/horses/horseback(4).png')
    horse_4 = pg.transform.scale(horse_4, (75, 75))
    horse_5 = pg.image.load('./ChairSelect/image/horses/horseback(6).png')
    horse_5 = pg.transform.scale(horse_5, (75, 75))

    horse_1_flipped = pg.transform.flip(horse_1, True, False)
    horse_2_flipped = pg.transform.flip(horse_2, True, False)
    horse_3_flipped = pg.transform.flip(horse_3, True, False)
    horse_4_flipped = pg.transform.flip(horse_4, True, False)
    horse_5_flipped = pg.transform.flip(horse_5, True, False)

    clock = pg.time.Clock()

def startGame() :
    global gamepad, clock, Large_font, font, background
    pg.init()
    gamepad = pg.display.set_mode(windowsize)
    done = False
    t=0
    while not done :
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
                break
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_SPACE  :
                    ViewPlayer()
        gamepad.fill((255,255,255))
        PM = '현재 참여자 : '
        for s in Person :
            PM += s + ', '
        textSurface = Large_font.render(PM,True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]/3)
        gamepad.blit(TextSurf , TextRect)

        PM = ''
        for s in Person2 :
            PM += s + ', '
        textSurface = Large_font.render(PM,True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]/3 + 40)
        gamepad.blit(TextSurf , TextRect)

        if t <= 255 :
            textSurface = font.render("PRESS 'SPACE BAR' TO START",True,(0,t,0))
        else :
            textSurface = font.render("PRESS 'SPACE BAR' TO START",True,(0,510 - t,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]*4/5)
        gamepad.blit(TextSurf , TextRect)
        t+=5
        if t == 510 :
            t = 0
        pg.display.update() 
        clock.tick(60)


def ViewPlayer () :
    global gamepad, clock, Large_font
    done = False
    t1 = 0
    printmessage=['', '', '', '', '']
    rd.shuffle(List)

    while not done :
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
                break
        gamepad.fill((255,255,255))

        textSurface = Large_font.render("이번 경마에 참가할 인물은",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]/2 - 50)
        gamepad.blit(TextSurf , TextRect)

        t1 += 1
        if t1 == 30 :
            printmessage.insert(0, "5번 레인 : " + str(List[0]))
        elif t1 == 60 :
            printmessage.insert(0, "4번 레인 : " + str(List[1]))
        elif t1 == 120 :
            printmessage.insert(0, "3번 레인 : " + str(List[2]))
        elif t1 ==180 : 
            printmessage.insert(0, "2번 레인 : " + str(List[3]))
        elif t1 == 210 :
            printmessage.insert(0, "1번 레인 : " + str(List[4]))
        elif t1 > 300 :
            done = True
            runningGame(printmessage)
            
        textSurface = Large_font.render(printmessage[0],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]* 2/3 - 40)
        gamepad.blit(TextSurf , TextRect)

        textSurface = Large_font.render(printmessage[1],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]* 2/3)
        gamepad.blit(TextSurf , TextRect)

        textSurface = Large_font.render(printmessage[2],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]* 2/3 + 40*1)
        gamepad.blit(TextSurf , TextRect)

        textSurface = Large_font.render(printmessage[3],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]* 2/3 + 40*2)
        gamepad.blit(TextSurf , TextRect)

        textSurface = Large_font.render(printmessage[4],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]* 2/3 + 40*3)
        gamepad.blit(TextSurf , TextRect)
        pg.display.update()
        clock.tick(60)


def runningGame (printmessage) :
    global gamepad, clock, font, horse_1, horse_2, horse_3, horse_4, horse_5, horse_1_flipped , horse_2_flipped ,horse_3_flipped, horse_4_flipped, horse_5_flipped
    done = False
    horseList = [[horse_1, horse_1_flipped, [10, 10]], [horse_2, horse_2_flipped, [10, windowsize[1]* 1/5 + 20]], [horse_3, horse_3_flipped, [10, windowsize[1]* 2/5 + 15]], [horse_4, horse_4_flipped, [10, windowsize[1]* 3/5 + 10]], [horse_5, horse_5_flipped, [10, windowsize[1]* 4/5 + 10]]]
    moveList = [-1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    t=0
    clearPerson = []
    i = 0
    for horse in horseList :
        horse.append(printmessage[i])
        i += 1
    while not done :
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
                break
        gamepad.blit(background,(0, 0))
        
        if t % 5 == 0 :
            rd.shuffle(moveList)
        i = 0

        

        
        textSurface = Large_font.render(printmessage[0],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2, 40)
        gamepad.blit(TextSurf , TextRect)

        textSurface = Large_font.render(printmessage[1],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]* 1/5 + 40)
        gamepad.blit(TextSurf , TextRect)

        textSurface = Large_font.render(printmessage[2],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]* 2/5 + 40)
        gamepad.blit(TextSurf , TextRect)

        textSurface = Large_font.render(printmessage[3],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]* 3/5 + 40)
        gamepad.blit(TextSurf , TextRect)

        textSurface = Large_font.render(printmessage[4],True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowsize[0]/2,windowsize[1]* 4/5 + 40 )
        gamepad.blit(TextSurf , TextRect)

        

        for horse in horseList :
            horse[2][0] += moveList[i] * 5
            if horse[2][0] > windowsize[0] - 75 :
                a = 0
                for p in printmessage :
                    if p == horse[3] :
                        printmessage[a] = 'CLEAR!'
                        break
                    a+= 1
                horseList.remove(horse)
                continue
            
            if len(horseList) == 1 : 
                if len(Person) > 2 :
                    Person2.append(horse[3][8:])
                else :
                    Person.append(horse[3][8:])
                try :
                    List.remove(horse[3][8:])
                except Exception as e :
                    print("오류 발생! 오류 내용 :" + str(e))
                    pass
                done = True
                startGame()

            if moveList[i] < 0 :
                gamepad.blit(horse[1],(horse[2][0], horse[2][1]))
            else :
                gamepad.blit(horse[0],(horse[2][0], horse[2][1]))
            i+=1
        
        t+=1
        pg.display.update()
        clock.tick(60)

initGame ()
startGame()
print(Person + Person2)