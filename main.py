import pygame, sys
from button import Button
from pygame import mixer
import pygame.gfxdraw
import math
import random
from network import Network


class Gauge:
    def __init__(self, screen, FONT, x_cord, y_cord, thickness, radius, circle_colour, glow=True):
        self.screen = screen
        self.Font = FONT
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.thickness = thickness
        self.radius = radius
        self.circle_colour = circle_colour
        self.glow = glow

    def draw(self, percent):
        fill_angle = int(percent * 270 / 100)
        per = percent
        if percent > 100:
            percent = 100
        if per <= 40:
            per = 0
        if per > 100:
            per = 100
        ac = [int(255 - per * 255 / 100), int(per * 255 / 100), int(0), 255]
        for indexi in range(len(ac)):
            if ac[indexi] < 0:
                ac[indexi] = 0
            if ac[indexi] > 255:
                ac[indexi] = 255
        # print(ac)

        pertext = self.Font.render(str(percent) + "%", True, ac)
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(pertext, pertext_rect)

        for i in range(0, self.thickness):

            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225,
                               self.circle_colour)
            if percent > 4:
                pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225,
                                   fill_angle - 225 - 8, ac)

        if percent < 4:
            return

        if self.glow:
            for i in range(0, 15):
                ac[3] = int(150 - i * 10)
                pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius + i, -225,
                                   fill_angle - 225 - 8, ac)

            for i in range(0, 15):
                ac[3] = int(150 - i * 10)
                pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - self.thickness - i, -225,
                                   fill_angle - 225 - 8, ac)

            angle_r = math.radians(fill_angle - 225 - 8)
            lx, ly = int((self.radius - self.thickness / 2) * math.cos(angle_r)), int(
                (self.radius - self.thickness / 2) * math.sin(angle_r))
            ac[3] = 255
            lx = int(lx + self.x_cord)
            ly = int(ly + self.y_cord)

            pygame.draw.circle(self.screen, ac, (lx, ly), int(self.thickness / 2), 0)

            for i in range(0, 10):
                ac[3] = int(150 - i * 15)
                pygame.gfxdraw.arc(screen, int(lx), int(ly), (self.thickness // 2) + i, fill_angle - 225 - 10,
                                   fill_angle - 225 - 180 - 10, ac)


pygame.init()

screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("REAL TIME SIMULATION")
zzz = 'img/rec2.png'
bbb = 'img/tyara2.png'

BGi = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play(zzz, bbb):
    net = Network()

    # def send_data():
    #     """
    #     Send position to server
    #     :return: None
    #     """
        # data = str(net.id) + ":" + str(receiverX) + "," + str(receiverY)
        # reply = net.send(data)
        # return reply

    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0, 0

    # set framerate
    clock = pygame.time.Clock()
    FPS = 60

    # define colours
    BG = (0, 0, 0)
    bg_img = pygame.image.load('img/back.jpg')
    bgi = pygame.transform.scale(bg_img, (1300, 700))
    bg_img2 = pygame.image.load('img/backr.jpg')
    bgii = pygame.transform.scale(bg_img2, (1300, 700))
    frame = pygame.image.load('img/Picture3.png')
    framei = pygame.transform.scale(frame, (frame.get_width(), frame.get_height()))
    pfd = pygame.image.load('img/pfd4.jpg')
    pfdi = pygame.transform.scale(pfd, (pfd.get_width(), pfd.get_height()))
    wing = pygame.image.load('img/wing8.png')
    wingi = pygame.transform.scale(wing, (wing.get_width(), wing.get_height()))
    hei = pygame.image.load('img/fig9.png')
    heii = pygame.transform.scale(hei, (hei.get_width(), hei.get_height()))
    spee = pygame.image.load('img/fig10.png')
    speei = pygame.transform.scale(spee, (spee.get_width(), spee.get_height()))
    rad = pygame.image.load('img/radar.png')
    radi = pygame.transform.scale(rad, (rad.get_width(), rad.get_height()))
    poi = pygame.image.load('img/gplane.png')
    poii = pygame.transform.scale(poi, (25, 25))
    hea = pygame.image.load('img/indicator.png')
    heai = pygame.transform.scale(hea, (150, 150))
    heap = pygame.image.load('img/ii.png')
    heapi = pygame.transform.scale(heap, (72, 72))
    gas = pygame.image.load('img/gas.png')
    gasi = pygame.transform.scale(gas, (gas.get_width(), gas.get_height()))
    #gau = pygame.image.load('img/gauge.png')
    #gaui = pygame.transform.scale(gau, (gau.get_width(), gau.get_height()))
    #nee = pygame.image.load('img/needle.png')
    #neei = pygame.transform.scale(nee, (nee.get_width(), nee.get_height()))


    green = pygame.image.load('img/green.png')
    greeni = pygame.transform.scale(green, (green.get_width(), green.get_height()))
    red = pygame.image.load('img/red.png')
    redi = pygame.transform.scale(red, (red.get_width(), red.get_height()))
    yellow = pygame.image.load('img/yellow.png')
    yellowi = pygame.transform.scale(yellow, (yellow.get_width(), yellow.get_height()))
    hose = pygame.image.load('img/tuyoo.png')
    hosei = pygame.transform.scale(hose, (100, 50))

    autoi = pygame.image.load('img/Auto.png')
    auto = pygame.transform.scale(autoi, (100, 200))
    manueli = pygame.image.load('img/Manuel.png')
    manuel = pygame.transform.scale(manueli, (100, 200))
    #EWD
    screenn = pygame.image.load('img/TT.png')
    screenni = pygame.transform.scale(screenn, (600, 200))
# cursor
    motalat = pygame.image.load('img/tj.png')
    motalati = pygame.transform.scale(motalat, (25, 25))

    width = 1300
    i = 0
    mixer.music.load('img/airplane_prop.ogg')
    mixer.music.play(-1)

    def draw_bg():
        screen.fill(BG)

    img = pygame.image.load(bbb)
    image = pygame.transform.scale(img, (300, 300))
    img1 = pygame.image.load(zzz)
    image1 = pygame.transform.scale(img1, (150, 150))

    # receiver
    receiverX = 10
    receiverY = 10
    receiverX_change = 0
    receiverY_change = 0
    pfdy = 0
    pfdy_change = 0

    def receiver(x, y):
        screen.blit(image1, (x, y))

    # tanker
    tankerX = 400
    tankerY = 100
    tankerX_change = 0
    tankerY_change = 0

    def tanker(x, y):
        screen.blit(image, (x, y))

    font = pygame.font.Font('freesansbold.ttf', 16)
    vit = 100
    vit_change = 0
    mx, my = pygame.mouse.get_pos()
    angle = 0
    angle_change = 0
    radangle = 0
    radangle_change = 5
    needang = 0
    needang_change = 0

    circle_c = (55, 77, 91)
    FONT = pygame.font.SysFont('Franklin Gothic Heavy', 40)
    FONT2 = pygame.font.SysFont('Franklin Gothic Heavy', 20)
    my_gauge = Gauge(
        screen=screen,
        FONT=FONT,
        x_cord=820,
        y_cord=620,
        thickness=20,
        radius=80,
        circle_colour=circle_c,
        glow=True)

    percentage = 100

    mode = font.render("manual", True, (255, 255, 255))
    war1 = font.render("your speed is fine", True, (0, 255, 0))
    war2 = font.render("your fuel is fine", True, (0, 255, 0))

    def isCollision(receiverX, receiverY, tankerX, tankerY):
        distance = math.sqrt(math.pow(receiverX - (tankerX - 80), 2) + (math.pow(receiverY - (tankerY + 100), 2)))
        if distance < 100:
            return True
        else:
            return False

    fu = 0

    p = 1
    n1v = 70
    egtv = 300
    ii = 1
    ii2 = 1
    i3 = 1
    i4 = 1
    needang_change = 60
    m = 1

    run = True
    isManuel = False
    while run:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        clock.tick(FPS)

        draw_bg()

        # Create looping background
        screen.blit(bgi, (i, 0))
        screen.blit(bgii, (width + i, 0))
        if i <= -width:
            i = 0
            screen.blit(bgi, (width + i, 0))
        i -= vit / 10

        screen.blit(pfdi, (1130, pfdy))
        wingii = pygame.transform.rotate(wingi, angle)
        screen.blit(wingii, (1210 - int(wingii.get_width() / 2), 350 - int(wingii.get_height() / 2)))
        # screen.blit(wingii, (1132, 325))

        collision = isCollision(receiverX, receiverY, tankerX, tankerY)

        # Send Network Stuff
        # tankerX, tankerY = parse_data(send_data())


        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

            # keyboard presses
            if event.type == pygame.KEYDOWN:
                if m == 1:
                    if event.key == pygame.K_q:
                        receiverX_change = -10
                        #angle_change += -10
                    if event.key == pygame.K_d:
                        receiverX_change = 10
                        #angle_change += 10
                    if event.key == pygame.K_z:
                        receiverY_change = -10
                        pfdy_change = 5
                    if event.key == pygame.K_s:
                        receiverY_change = 10
                        pfdy_change = -5
                    if event.key == pygame.K_LEFT:
                        tankerX_change = -10
                    if event.key == pygame.K_RIGHT:
                        tankerX_change = 10
                    if event.key == pygame.K_UP:
                        tankerY_change = -10
                    if event.key == pygame.K_DOWN:
                        tankerY_change = 10
                    if event.key == pygame.K_t:
                        vit_change = 50
                    if event.key == pygame.K_r:
                        vit_change = -50
                    if event.key == pygame.K_w:
                        angle_change += -1
                    if event.key == pygame.K_x:
                        angle_change += 1
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_1:
                    mode = font.render("auto on LEVEL1", True, (255, 255, 255))
                    receiverY = 2500
                    tankerY = 2500
                    m = 0
                    #screen.blit(auto, (0, 0))
                if event.key == pygame.K_2:
                    mode = font.render("auto on LEVEL2", True, (255, 255, 255))
                    receiverY = 300
                    tankerY = 300
                    m = 0
                    isManuel = True
                    #screen.blit(auto, (0, 0))
                if event.key == pygame.K_3:
                    mode = font.render("auto on LEVEL3", True, (255, 255, 255))
                    receiverY = 200
                    tankerY = 200
                    m = 0
                    isManuel = True
                    #screen.blit(auto, (0, 0))
                if event.key == pygame.K_4:
                    mode = font.render("auto on LEVEL4", True, (255, 255, 255))
                    receiverY = 100
                    tankerY = 100
                    m = 0

                    isManuel = True
                    #screen.blit(auto, (0, 0))
                if event.key == pygame.K_5:
                    mode = font.render("auto on LEVEL5", True, (255, 255, 255))
                    receiverY = 0
                    tankerY = 0
                    m = 0

                    isManuel = True
                    #screen.blit(auto, (0, 0))
                if event.key == pygame.K_0:
                    mode = font.render("manual", True, (255, 255, 255))
                    m = 1

                    isManuel = False
                    #screen.blit(manuel, (0, 0))
                if event.key == pygame.K_SPACE:
                    fu = 1
                    percentage = percentage + 10
                if event.key == pygame.K_p:
                    fu = 0

            # keyboard button released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    receiverX_change = 0
                    angle_change = 0
                    #angle = 0
                if event.key == pygame.K_d:
                    receiverX_change = 0
                    angle_change = 0
                    #angle = 0
                if event.key == pygame.K_z:
                    receiverY_change = 0
                    pfdy_change = 0
                    pfdy = 0
                if event.key == pygame.K_s:
                    receiverY_change = 0
                    pfdy_change = 0
                    pfdy = 0
                if event.key == pygame.K_LEFT:
                    tankerX_change = 0
                if event.key == pygame.K_RIGHT:
                    tankerX_change = 0
                if event.key == pygame.K_UP:
                    tankerY_change = 0
                if event.key == pygame.K_DOWN:
                    tankerY_change = 0
                if event.key == pygame.K_t:
                    vit_change = 0
                if event.key == pygame.K_r:
                    vit_change = 0
        if isManuel:
            screen.blit(auto, (0, 0))
        if not isManuel:
            screen.blit(manuel, (0, 0))

        tankerX += tankerX_change
        if tankerX <= 0:
            tankerX = 0
        elif tankerX >= 930:
            tankerX = 930

        tankerY += tankerY_change
        if tankerY <= -50:
            tankerY = -50
        elif tankerY >= 370:
            tankerY = 370

        receiverX += receiverX_change
        if receiverX <= 0:
            receiverX = 0
        elif receiverX >= 980:
            receiverX = 980

        receiverY += receiverY_change
        if receiverY <= -50:
            receiverY = -50
        elif receiverY >= 400:
            receiverY = 400
        pfdy += pfdy_change
        if pfdy <= -350:
            pfdy = -350
        elif pfdy >= 350:
            pfdy = 350

        vit += vit_change
        if vit >= 1000:
            vit = 1000
        elif vit <= 100:
            vit = 100

        angle += angle_change
        radangle += radangle_change
        #if angle >= 60:
        #    angle = 60
        #elif angle <= -60:
        #    angle = -60

        if i3 == -1:
            needang_change = needang_change + 0.1
        if i3 == 1:
            needang_change = needang_change - 0.1

        needang += needang_change
        if needang >= 60:
            needang = 59
            i3 = 1
        elif needang <= 0:
            needang = 1
            i3 = -1

        if ii == 1:
            egtv = egtv + 0.1
        if egtv >= 500:
            ii = -1
            egtv = 499
        if ii == -1:
            egtv = egtv - 0.1
        if egtv <= 300:
            ii = 1
            egtv = 301

        if ii2 == 1:
            n1v = n1v + 0.1
        if n1v >= 90:
            ii2 = -1
            n1v = 89
        if ii2 == -1:
            n1v = n1v - 0.1
        if n1v <= 70:
            ii2 = 1
            n1v = 71

        if percentage == 0:
            vit = 0
        if percentage >= 120:
            percentage = 120

        if fu == 1:
            screen.blit(hosei, (receiverX- 10, receiverY + 200))

        screen.blit(framei, (0, 0))
        screen.blit(speei, (1135, 5))
        screen.blit(heii, (1220, 5))
        height = font.render(str((-receiverY + 500) * 25), True, (255, 255, 255))
        screen.blit(height, (1263, 120))
        speed = font.render(str(vit), True, (255, 255, 255))
        screen.blit(speed, (1135, 120))
        screen.blit(heai, (1125, 525))
        screen.blit(screenni, (150, 525))
        screen.blit(motalati, (200+tankerX/3, 600+tankerY/3))
        # screen.blit(gaui, (500, 525))
        #screen.blit(gaui, (500, 525))
        #screen.blit(gaui, (300, 525))
        # screen.blit(neei, (600, 580))
        # screen.blit(neei, (400, 580))
        #neeii = pygame.transform.rotate(neei, needang)
        #neeii2 = pygame.transform.rotate(neei, -0.5 * needang)
        #screen.blit(neeii, (635 - int(neeii.get_width() / 2), 590 - int(neeii.get_height() / 2)))
        #screen.blit(neeii2, (435 - int(neeii.get_width() / 2), 590 - int(neeii.get_height() / 2)))
        heapii = pygame.transform.rotate(heapi, 1.5 * angle)
        screen.blit(heapii, (1200 - int(heapii.get_width() / 2), 600 - int(heapii.get_height() / 2)))
        radii = pygame.transform.rotate(radi, -radangle)
        screen.blit(radii, (1000 - int(radii.get_width() / 2), 615 - int(radii.get_height() / 2)))
        p = p + 0.5
        if p >= 5:
            p = 0
        if p == 1:
            screen.blit(poii, (1020, 640))
        N1 = font.render("N1(%)", True, (255, 255, 255))
        EGT = font.render("EGT(²C)", True, (255, 255, 255))
        screen.blit(N1, (540, 600))
        screen.blit(EGT, (340, 600))
        n1 = FONT2.render(str(round(n1v)), True, (0, 255, 0))
        egt = FONT2.render(str(round(egtv)), True, (0, 255, 0))
        screen.blit(n1, (610, 620))
        screen.blit(egt, (400, 620))

        if (percentage > 60):
            war2 = font.render("your fuel is fine", True, (0, 255, 0))
        if (vit <= 600):
            war1 = font.render("your speed is fine", True, (0, 255, 0))
        if (percentage <= 60) and (percentage > 35):
            ya = mixer.Sound('img/alarm.ogg')
            ya.play()

            war2 = font.render("WARNING2 : fuel under 60%", True, (255, 255, 0))
        if vit > 600 and vit < 900:
            ya = mixer.Sound('img/alarm.ogg')
            ya.play()

            war1 = font.render("WARNING1 : speed exceeding", True, (255, 255, 0))
        if vit >= 900:
            ra = mixer.Sound('img/alarm.wav')
            ra.play()

            war1 = font.render("WARNING1 : speed exceeding!!!!", True, (255, 0, 0))
        if percentage < 35:
            ra = mixer.Sound('img/alarm.wav')
            ra.play()

            war2 = font.render("WARNING2 : fuel under 35%", True, (255, 0, 0))
        receiver(receiverX, receiverY)
        tanker(tankerX, tankerY)

        # FOR SHOWING CHANGE IN GAUGE 0.1
        percentage += -0.1
        if percentage < 0:
            percentage = 0
        my_gauge.draw(percent=round(percentage, 1))
        screen.blit(gasi, (805, 570))
        screen.blit(mode, (0, 510))
        screen.blit(war1, (0, 550))
        screen.blit(war2, (0, 600))



        pygame.display.update()


def options():
    zzz = 'img/tayara6.png'
    bbb = 'img/tyara2.png'
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_BACK = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=get_font(75), base_color="black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        OPTIONS_r = Button(image=None, pos=(200, 50),
                           text_input="RECEIVER", font=get_font(40), base_color="Black", hovering_color="Blue")

        OPTIONS_r.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_r.update(screen)
        OPTIONS_t = Button(image=None, pos=(1150, 50),
                           text_input="TANKER", font=get_font(40), base_color="Black", hovering_color="Blue")

        OPTIONS_t.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_t.update(screen)

        xxx = 'img/rec.png'
        yyy = 'img/Biplane1.png'

        x2 = 'img/rec2.png'
        y2 = 'img/Biplane2.png'

        x3 = 'img/rec3.png'
        y3 = 'img/Biplane3.png'

        OPTIONS_1 = Button(image=pygame.image.load(xxx), pos=(200, 150),
                           text_input="A", font=get_font(10), base_color="Black", hovering_color="Green")

        OPTIONS_1.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_1.update(screen)

        OPTIONS_2 = Button(image=pygame.image.load(x2), pos=(200, 300),
                           text_input="B", font=get_font(10), base_color="Black", hovering_color="Green")

        OPTIONS_2.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_2.update(screen)

        OPTIONS_3 = Button(image=pygame.image.load(x3), pos=(200, 450),
                           text_input="C", font=get_font(10), base_color="Black", hovering_color="Green")

        OPTIONS_3.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_3.update(screen)

        OPTIONS_4 = Button(image=pygame.image.load(yyy), pos=(1150, 150),
                           text_input="A", font=get_font(10), base_color="Black", hovering_color="Red")

        OPTIONS_4.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_4.update(screen)

        OPTIONS_5 = Button(image=pygame.image.load(y2), pos=(1150, 300),
                           text_input="B", font=get_font(10), base_color="Black", hovering_color="Red")

        OPTIONS_5.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_5.update(screen)

        OPTIONS_6 = Button(image=pygame.image.load(y3), pos=(1150, 450),
                           text_input="C", font=get_font(10), base_color="Black", hovering_color="Red")

        OPTIONS_6.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_6.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu(zzz, bbb)
                if OPTIONS_1.checkForInput(OPTIONS_MOUSE_POS):
                    zzz = xxx
                if OPTIONS_2.checkForInput(OPTIONS_MOUSE_POS):
                    zzz = x2
                if OPTIONS_3.checkForInput(OPTIONS_MOUSE_POS):
                    zzz = x3
                if OPTIONS_4.checkForInput(OPTIONS_MOUSE_POS):
                    bbb = yyy
                if OPTIONS_5.checkForInput(OPTIONS_MOUSE_POS):
                    bbb = y2
                if OPTIONS_6.checkForInput(OPTIONS_MOUSE_POS):
                    bbb = y3

        pygame.display.update()


def main_menu(zzz, bbb):
    while True:
        screen.blit(BGi, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="START", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(zzz, bbb)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


#main_menu(zzz, bbb)
play(zzz,bbb)
