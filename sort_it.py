import pygame
import sys
import random

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((480,800))
pygame.display.set_caption("Sort it Game")
clock = pygame.time.Clock()

background_image = pygame.image.load('images/background.jpg')
bottom_image = pygame.image.load('images/bottom.jpg')
rules_image = pygame.image.load('images/rules.jpg')
pause_image = pygame.image.load('images/pause.png')

tanks = [pygame.image.load('images/tank_1.png'), pygame.image.load('images/tank_2.png'),
         pygame.image.load('images/tank_3.png'), pygame.image.load('images/tank_4.png')]

trashes = [[pygame.image.load('images/trash_1_1.png'), pygame.image.load('images/trash_1_2.png')],
           [pygame.image.load('images/trash_2_1.png'), pygame.image.load('images/trash_2_2.png')],
           [pygame.image.load('images/trash_3_1.png'), pygame.image.load('images/trash_3_1.png')],
           [pygame.image.load('images/trash_4_1.png'), pygame.image.load('images/trash_4_1.png')]]

mascot = pygame.image.load('images/mascot.png')
mascot = pygame.transform.scale(mascot, (mascot.get_width()//7,
                                         mascot.get_height()//7))

lifes = [pygame.image.load('images/life_4.png'),pygame.image.load('images/life_3.png'),
         pygame.image.load('images/life_2.png'),pygame.image.load('images/life_1.png')]

for n in range(4):
    lifes[n] = pygame.transform.scale(lifes[n], (lifes[n].get_width()//16,
                                                 lifes[n].get_height()//16))

font = pygame.font.Font('fonts/font_1.ttf', 42)

sound_true = pygame.mixer.Sound('sounds/true_tank.wav')
sound_false = pygame.mixer.Sound('sounds/mistake.wav')
sound_gameover = pygame.mixer.Sound('sounds/game_over.wav')
sound_button = pygame.mixer.Sound('sounds/button.wav')

x = random.randint(0, 450)
y = 0
speed = 3
j = random.randint(0, 7)
score = 0
count_try = 0
count_play = 0


class Menu:
    def __init__(self, punkts = []):
        self.punkts = punkts

    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        if punkts[0][2] == 'Game' or punkts[0][2] == 'Replay':
            pygame.mixer.music.load('sounds/menu_music.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
        elif punkts[0][2] == 'Resume':
            pygame.mixer_music.pause()

        done = True
        punkt = 0

        while done:
            screen.blit(background_image, (0, 0))

            if punkts[0][2] == 'Replay':
                text = font.render("GAME OVER", True, [250, 0, 0])
                screen.blit(text, [105, 100])

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+80:
                    punkt = i[5]

            self.render(screen, font, punkt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    #sound_button.play()
                    if event.key == pygame.K_RETURN:
                        if punkt == 0:
                            done = False
                        if punkt == 1:
                            menu_rules()
                        if punkt == 2:
                            sys.exit()
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if event.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #sound_button.play()

                    if punkt == 0:
                        done = False
                    if punkt == 1:
                        menu_rules()
                    if punkt == 2:
                        sys.exit()

            screen.blit(screen, (0, 30))

            pygame.display.update()


def menu_rules():
    done = True
    back_button = 0
    while done:
        screen.blit(rules_image, (0, 0))
        screen.blit(font.render("Back", 1, (250, 250, 30)), (160, 600))

        mp = pygame.mouse.get_pos()

        if mp[0]>180 and mp[0]<300 and mp[1]>600 and mp[1]<660:
            screen.blit(font.render("Back", 1, (250, 0, 0)), (160, 600))
            back_button = 1

        for event in pygame.event.get():
            #sound_button.play()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button == 1:
                    done = False

        pygame.display.update()


def draw_tanks():
    i = 0
    for tank in tanks:
        scale = pygame.transform.scale(tank, ((tank.get_width()*3)//4,
                                              (tank.get_height()*3)//4))
        screen.blit(scale, (i, 650))
        i += 120


def draw_score():
    font = pygame.font.Font('fonts/font_1.ttf', 25)
    text = font.render("Score: " + str(score), True, [0, 0, 0])
    screen.blit(text, [30, 30])


def draw_mascot(q, p=650, up=1, mascot_isRun: bool = True):
    while mascot_isRun:
        screen.blit(background_image, (0, 0))
        screen.blit(mascot, ((q // 120) * 120, p))
        if up:
            p -= 5
        else:
            p += 5

        if p <= 570:
            up = 0
        if p >= 660:
            y = 0
            x = random.randint(0, 450)
            j = random.randint(0, 3)
            p = 650
            up = 1
            mascot_isRun = False

        screen.blit(bottom_image, (0, 655))
        draw_tanks()
        draw_score()
        screen.blit(lifes[count_try],(20,60))
        screen.blit(pause_image,(400,30))


        pygame.display.update()
        clock.tick(30)


punkts = [(174, 140, u'Game', (250, 250, 30), (250, 0, 0), 0),
          (172, 210, u'Rules', (250, 250, 30), (250, 0, 0), 1),
          (186, 280, u'Quit', (250, 250, 30), (250, 0, 0), 2)]

game = Menu(punkts)
game.menu()

pygame.mixer.music.load('sounds/fon_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

run = True
while run:
    screen.blit(background_image, (0, 0))

    if y < 650:
        screen.blit(trashes[j//2][j - j//2 * 2], (x, y))

    mp = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if mp[0] > 400 and mp[0] <450 and mp[1] > 30 and mp[1] < 80 and event.type == pygame.MOUSEBUTTONDOWN:
            punkts = [(150, 140, u'Resume', (250, 250, 30), (250, 0, 0), 0),
                      (172, 210, u'Rules', (250, 250, 30), (250, 0, 0), 1),
                      (186, 280, u'Quit', (250, 250, 30), (250, 0, 0), 2)]

            game_pause = Menu(punkts)
            game_pause.menu()

            pygame.mixer.music.unpause()
        if event.type == pygame.QUIT:
            run= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                punkts = [(150, 140, u'Resume', (250, 250, 30), (250, 0, 0), 0),
                          (172, 210, u'Rules', (250, 250, 30), (250, 0, 0), 1),
                          (186, 280, u'Quit', (250, 250, 30), (250, 0, 0), 2)]

                game_pause = Menu(punkts)
                game_pause.menu()

                pygame.mixer.music.load('sounds/fon_music.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed*2
    if keys[pygame.K_RIGHT] and x < 475 - trashes[j//2][j - j//2*2].get_width():
        x += speed*2
    if keys[pygame.K_DOWN]:
        y += speed*2

    fl = False
    if y < 650:
        y += speed
    else:
        if j//2 == 0 and (x + trashes[j//2][j - j//2*2].get_width()/2) < tanks[0].get_width()*3//4 :
            fl = True
        elif j//2 == 1 and 120 < (x + trashes[j//2][j - j//2*2].get_width()/2) < tanks[1].get_width()*3//4 + 120:
            fl = True
        elif j//2 == 2 and 240 < (x + trashes[j//2][j - j//2*2].get_width()/2) < tanks[2].get_width()*3//4 + 240:
            fl = True
        elif j//2 == 3 and 360 < (x + trashes[j//2][j - j//2*2].get_width()/2) < tanks[0].get_width()*3//4 + 360:
            fl = True

        if fl == True:
            sound_true.play()
            score += 1
            draw_mascot(x + trashes[j//2][j - j//2*2].get_width()/2)
        else:
            if score > 0:
                score -= 1
            count_try +=1
            if count_play == 0:
                sound_false.play()

        y = 0
        x = random.randint(0, 450)
        j2 = j
        while j == j2:
            j = random.randint(0, 7)

    if count_try > 3:
        pygame.mixer.music.pause()
        if count_play == 0:
            sound_gameover.play()
            count_play = 1

        punkts = [(150, 200, u'Replay', (250, 250, 30), (250, 0, 0), 0),
                  (172, 270, u'Rules', (250, 250, 30), (250, 0, 0), 1),
                  (186, 340, u'Quit', (250, 250, 30), (250, 0, 0), 2)]
        game_over = Menu(punkts)
        game_over.menu()
        x = random.randint(0, 450)
        y = 0
        speed = 3
        j = random.randint(0, 7)
        score = 0
        count_try = 0
        count_play = 0
        pygame.mixer.music.load('sounds/fon_music.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    else:
        screen.blit(lifes[count_try],(20,60))

    screen.blit(bottom_image, (0, 655))

    draw_tanks()
    draw_score()
    screen.blit(pause_image,(400,30))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
