import pygame as pg
import random

res = width, height = 800, 600
Clock = pg.time.Clock()

pg.font.init()
font = pg.font.SysFont(None, 75)
game_font = pg.font.SysFont(None, 40)

rect_start = pg.Rect((width/3), (height/3),250,50)
rect_exit = pg.Rect((width/3), (height/2),250,50)
rect_undo = pg.Rect(10,height-50,100,30)
rect_hip_hop = pg.Rect((width/3), (height/3),250,50)
rect_rock = pg.Rect((width/3),(height/2),250,50)

screen = pg.display.set_mode(res)
pg.display.set_caption("Wisielec")

life = 5

def shuffle_word(file_name):
    global word, letter_of_word
    file = open(file_name, "r")
    word = ""
    x = 0
    number_of_words = 0
    letter_of_word = []
    for line in file:
        number_of_words += 1
    random_number = random.randint(1, number_of_words + 1)
    file = open(file_name, "r")
    for line in file:
        x+=1
        if x == random_number:
            word = line.strip()
            for letter in word:
                letter_of_word.append(letter)
            game()



def draw_keyboard():
    global list_rect_of_key
    z = -70
    d = 60
    row = 3
    column = 9
    number_of_letter = 0
    array_of_letters = [[0 for x in range(column)] for x in range(row)]
    list_rect_of_key = [[0 for x in range(column)] for x in range(row)]

    for i in range(row):
        for j in range(column):
            list_rect_of_key[i][j] = i, pg.Rect((width / 5)+z, (height / 3)+d, 60, 60)
            array_of_letters[i][j] = i, chr(65+number_of_letter)
            number_of_letter += 1
            z += 70
        z = -70
        d+=70

    z = -50
    d = 80
    for i in range(3):
        for j in range(9):
            rect = (list_rect_of_key[i][j])
            rect = rect[1]
            letter = array_of_letters[i][j]
            letter = letter[1]
            pg.draw.rect(screen,(255,255,255), rect,3)
            draw_text(letter,game_font,(255,255,255),screen, (width / 5)+z, (height / 3)+d)
            z += 70
        z = -50
        d += 70
    pg.draw.rect(screen, (255, 255, 255), rect_undo, 3)
    draw_text("Menu", game_font, (255, 255, 255), screen, 25, height - 48)

    mouse_pos = pg.mouse.get_pos()
    i=0


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def game_setting():
    while True:
        mouse_pos = pg.mouse.get_pos()
        screen.fill("black")
        draw_text("Wybierz Kategorie", font,(255,255,255), screen, width/5+40, height/8)

        pg.draw.rect(screen,(255, 255, 255), rect_hip_hop, 3)
        draw_text("HIP-HOP",font, (255, 255, 255), screen, width / 3 + 18, height / 3 + 2)

        pg.draw.rect(screen, (255, 255, 255), rect_rock, 3)
        draw_text("ROCK", font, (255, 255, 255), screen, width / 3 + 60, height / 2 + 2)

        pg.draw.rect(screen, (255, 255, 255), rect_undo, 3)
        draw_text("Menu", game_font, (255, 255, 255), screen, 25, height - 48)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if rect_rock.collidepoint(mouse_pos[0],mouse_pos[1]):
                if event.type == pg.MOUSEBUTTONDOWN:
                    game_rock()

            if rect_hip_hop.collidepoint(mouse_pos[0], mouse_pos[1]):
                if event.type == pg.MOUSEBUTTONDOWN:
                    game_hip_hop()

            if rect_undo.collidepoint(mouse_pos[0], mouse_pos[1]):
                if event.type == pg.MOUSEBUTTONDOWN:
                    main_menu()
        pg.display.update()
        Clock.tick(60)


def main_menu():
    while True:
        screen.fill("black")
        mouse_pos = pg.mouse.get_pos()


        draw_text("Main Menu", font, (255,255,255), screen, ((width/2)-150), 80)

        pg.draw.rect(screen, (255,255,255), rect_start, 3)
        draw_text("START",font,(255,255,255), screen, (width/3+40), (height/3+3))

        pg.draw.rect(screen,(255,255,255), rect_exit, 3)
        draw_text("EXIT",font, (255,255,255), screen, (width/3+60), (height/2+3))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if rect_exit.collidepoint(mouse_pos[0], mouse_pos[1]):
                if event.type == pg.MOUSEBUTTONDOWN:
                    pg.quit()

            if rect_start.collidepoint(mouse_pos[0], mouse_pos[1]):
                if event.type == pg.MOUSEBUTTONDOWN:
                    game_setting()

        pg.display.update()
        Clock.tick(60)

def game_rock():
    while True:
        screen.fill("black")
        mouse_pos = pg.mouse.get_pos()
        shuffle_word("rock.txt")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        if rect_undo.collidepoint(mouse_pos[0], mouse_pos[1]):
            if event.type == pg.MOUSEBUTTONDOWN:
                main_menu()

        pg.display.update()
        Clock.tick(60)

def game_hip_hop():
    while True:
        screen.fill("black")
        mouse_pos = pg.mouse.get_pos()
        shuffle_word("hip-hop.txt")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        if rect_undo.collidepoint(mouse_pos[0], mouse_pos[1]):
            if event.type == pg.MOUSEBUTTONDOWN:
                main_menu()

        pg.display.update()
        Clock.tick(60)

def game():
    drop_life = False
    life = 5
    while life > 0:
        array_of_word_usr = []
        for i in range(len(word)):
            array_of_word_usr.append("#")
        word_of_user = "-"
        while True:
            mouse_pos = pg.mouse.get_pos()
            screen.fill("black")

            letter = ""
            d = 0
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            draw_keyboard()
            result = True
            if rect_undo.collidepoint(mouse_pos[0], mouse_pos[1]):
                if event.type == pg.MOUSEBUTTONDOWN:
                    main_menu()
            for i in range(3):
                for j in range(9):
                    rect_of_key = list_rect_of_key[i][j]
                    letter = chr(65+d)
                    rect_of_key = rect_of_key[1]
                    d += 1
                    if rect_of_key.collidepoint(mouse_pos[0], mouse_pos[1]):
                        if event.type == pg.MOUSEBUTTONDOWN:
                            for elem in word_of_user:
                                if elem != letter:
                                    drop_life = True
                                    continue
                                else:
                                    result = False
                                    break
                            if result == True:
                                word_of_user += letter
                            else:
                                print("JEST!")
            if drop_life == True:
                life -= 1
                drop_life = False
            if life > 1:
                draw_text("pozostało {} prób".format(life),game_font,(255,255,255),screen,20,50)
            elif life == 1:
                draw_text("pozostała {} próba".format(life),game_font,(255,255,255),screen,20,50)
            else:
                screen.fill("black")
                draw_text("KONIEC GRY",game_font,(255,255,255),screen,(width/2)-100,height/2-50)
            d = len(word)
            x = 0

            for i in word:
                for j in word_of_user:
                    if i == j:
                        array_of_word_usr[x] = j
                        break
                x += 1
            print(array_of_word_usr)
            i = 25
            i = 0

            z = len(word)
            if z // 2 == 0:
                z = z*20
            else:
                z = z*20-10
            for k in array_of_word_usr:
                letter = k
                if len(array_of_word_usr) > 9:
                    draw_text(letter, game_font, (255, 255, 255), screen, width / 2 - z - 40 + i, height / 4 - 25)
                    i += 50
                else:
                    draw_text(letter,game_font,(255,255,255), screen, width/2-z+i,height/4-25)
                    i+=50
            print(array_of_word_usr)
            if d%2==0:
                i = 25
                for c in range(d//2):
                    for e in range(2):
                        i *=-1
                        rect_of_word = pg.Rect((width/2)+i, height/4,40,5)
                        pg.draw.rect(screen,(255,255,255),rect_of_word)
                    i+=50
            else:
                i = 0
                for c in range(d // 2):
                    if i == 0:
                        rect_of_word = pg.Rect((width / 2), height / 4, 40, 5)
                        pg.draw.rect(screen, (255, 255, 255), rect_of_word)
                        i += 50
                    for e in range(2):
                        i *= -1
                        rect_of_word = pg.Rect((width / 2) + i, height / 4, 40, 5)
                        pg.draw.rect(screen, (255, 255, 255), rect_of_word)
                    i += 50
            slowo = ""
            for x in array_of_word_usr:
                slowo += x
            if slowo == word:
                screen.fill("black")
                draw_text("WYGRALES", game_font, (255, 255,255), screen, width / 2 - 100, height / 2)
                pg.draw.rect(screen,(255,255,255), rect_undo, 3)
                draw_text("Menu", game_font, (255, 255, 255), screen, 25, height - 48)

            pg.display.update()
            Clock.tick(60)

main_menu()