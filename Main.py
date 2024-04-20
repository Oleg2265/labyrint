import pygame
from pygame import image
import pygame
from Character import *
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("Sound_kaka.mp3")

pygame.mixer.music.load("Sound_play.mp3")
pygame.mixer.music.play(-1)

back_theme = 0









roma = Player(320 , 260, 80, 80, "img.png", 4)
worog = Bad(400, 100, 35, 35, "img_1.png", 4, 25, 10, 4, 4)
worog1 = Bad(400, 200, 35, 35, "img_1.png", 4, 25, 180, 4, 4)


apple1 = object(200, 30, 50, 50, "img_2.png")
lever = object(20, 420, 60, 60, "Right_lever.png")
back = object(0, 0, 700, 500, "Space_background.png")
stiny =[]
stiny.append(wall(180,390,300,30, "img_3.png"))

stiny.append(wall(460,230,20,400, "img_3.png"))
stiny.append(wall(180,230,20,400, "img_3.png"))
stiny.append(wall(180,450,20,400, "img_3.png"))
def defeat():
    roma.hitbox.x = 320
    roma.hitbox.y = 260
    lever.change_photo("Right_lever.png")
    stiny[0].hitbox.x = 180

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if roma.hitbox.colliderect(worog.hitbox):
            defeat()
        if roma.hitbox.colliderect(apple1.hitbox):
             apple1.hitbox.x = 2993213
        for styna in stiny:
            if roma.hitbox.colliderect(styna.hitbox):
                defeat()
        if roma.hitbox.colliderect(worog1.hitbox):
            defeat()
        if roma.hitbox.colliderect(lever.hitbox):
            lever.change_photo("Left_lever.png")
            sound.play()
            stiny[0].hitbox.x = 29319319
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            back_theme += 1
            back.change_photo("img_6.png")
        if back_theme == 3:
            back_theme = 0
            back.change_photo("Space_background.png")







    roma.move()
    worog.move()
    worog1.move()

    back.draw(window)
    apple1.draw(window)
    roma.draw(window)
    worog.draw(window)
    worog1.draw(window)
    lever.draw(window)
    for stina in stiny:
        stina.draw(window)
    pygame.display.flip()
    fps.tick(60)


