import pygame
from pygame import image
from Character import *
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()


background = pygame.transform.scale(image.load("background.png"), (700, 500))

roma = Player(350 , 250, 80, 80, "img.png", 4)
worog = Bad(400, 100, 65, 65, "img_1.png", 4, 90, 90, 4, 4)
worog1 = Bad(400, 400, 65, 65, "img_1.png", 4, 90, 90, 4, 4)
worog2 = Bad(100, 400, 65, 65, "img_1.png", 4, 90, 90, 4, 4)
worog3 = Bad(300, 200, 65, 65, "img_1.png", 4, 90, 90, 4, 4)
worog4 = Bad(100, 300, 65, 65, "img_1.png", 4, 90, 90, 4, 4)
apple1 = object(10, 10, 50, 50, "img_2.png")
apple2 = object(690 , 10, 50, 50, "img_2.png")
apple3 = object(10, 490, 50, 50, "img_2.png")
apple4 = object(690, 490, 50, 50, "img_2.png")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if roma.hitbox.colliderect(worog.hitbox):
            print("ПРОГРАВ!!!!")
            pygame.quit()
        if roma.hitbox.colliderect(apple1.hitbox):
            apple1.x == 21093190


    roma.move()
    worog.move()
    worog1.move()
    worog2.move_y()
    worog3.move_y()
    worog4.move_y()
    window.blit(background, (0, 0))
    roma.draw(window)
    worog.draw(window)
    worog1.draw(window)
    worog2.draw(window)
    worog3.draw(window)
    worog4.draw(window)
    apple1.draw(window)
    apple2.draw(window)
    apple3.draw(window)
    apple4.draw(window)
    pygame.display.flip()
    fps.tick(60)


