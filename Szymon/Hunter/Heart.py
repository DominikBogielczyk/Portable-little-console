import pygame
from random import randrange
import time

class Heart(pygame.sprite.Sprite):

    def __init__(self,screen):

        self.image_= pygame.image.load("serce.png")
        self.screen_=screen
        self.rect_=self.image_.get_rect()
        self.x_ =randrange(70, 300, 1)
        self.y_ =-40
        self.dx_=0
        self.dy_=10

    def draw(self):
        self.screen_.blit(self.image_, self.rect_)
        self.rect_.center = [self.x_, self.y_]
    def move(self,player):
        if   self.y_+self.dy_<352:
            self.x_ += self.dx_
            self.y_ += self.dy_
        else:
            self.x_ = randrange(70, 300, 1)
            self.y_ =-40
    def kolizja(self,player):
        if pygame.Rect(player.x_,player.y_,6,6).colliderect(
                pygame.Rect(self.x_-16,self.y_-16,32,32)) == True and  pygame.key.get_pressed()[pygame.K_SPACE]:
            player.zycia_+=1
            self.x_=self.x_ = randrange(70, 300, 1)
            self.y_ = -40