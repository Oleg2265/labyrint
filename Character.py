import pygame

class Player:


    def __init__(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.w = w
        self.h = h


    def draw(self, window):
        #pygame.draw.rect(window, (0,0,255), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))
    def change_photo(self, photo):
        self.photo = pygame.transform.scale(pygame.image.load(photo), (self.w, self.h))


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed
            self.change_photo("img.png")
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed
            self.change_photo("img_5.png")
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
            self.change_photo("img_4.png")
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
            self.change_photo("img.png")

class Bad:
    def __init__(self, x, y, w, h, img, speed, ex, ey, speedx, speedy):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.ex = ey
        self.ey = ey
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy




    def draw(self, window):
        #pygame.draw.rect(window, (0,0,255), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))

    def move(self):
        if self.ex >= self.hitbox.x:
            self.speedx *= -1
        elif self.x <= self.hitbox.x:
            self.speedx *= -1




        self.hitbox.x += self.speedx


    def move_y(self):
        if self.ey >= self.hitbox.y:
            self.speedy *= -1
        elif self.y <= self.hitbox.y:
            self.speedy *= -1




        self.hitbox.y += self.speedy


class object:
    def __init__(self,x, y, w, h, img,):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.w = w
        self.h = h
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        #pygame.draw.rect(window, (0,0,255), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))

    def change_photo(self, photo):
        self.photo = pygame.transform.scale(pygame.image.load(photo), (self.w, self.h))


class wall:
    def __init__(self,x, y, w, h, img,):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()

        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        #pygame.draw.rect(window, (0,0,255), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))