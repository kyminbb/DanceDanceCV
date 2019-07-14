import pygame
from pygame.locals import *
from Data import Data
from Choose import Choose
from Constants import *


class Intro(object):

    def __init__(self, screen):
        self.data = Data()
        img = self.data.fileName('images', 'background.jpg')
        self.background = pygame.image.load(img)
        self.playBound = ((200, 240), (240, 50))
        self.scoreBound = ((200, 330), (240, 50))

        pygame.init()
        self.screen = screen

    def isInside(self, bound, x, y):
        return (bound[0][0] < x < bound[0][0] + bound[1][0] and
                bound[0][1] < y < bound[0][1] + bound[1][1])

    def mousePressed(self, event):
        x, y = event.pos
        if self.isInside(self.playBound, x, y):
            return 'choose'
        elif self.isInside(self.scoreBound, x, y):
            return 'high score'

    def drawHead(self):
        font = pygame.font.Font(None, 80)
        size = font.size('Dance Dance CV')
        head = font.render('Dance Dance CV', 0, (255, 255, 255))
        self.screen.blit(head, ((WIDTH - size[0]) / 2, 100))

    def drawMenu(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.playBound)
        pygame.draw.rect(self.screen, (255, 255, 255), self.scoreBound)
        font = pygame.font.Font(None, 40)
        size = font.size('Play')
        text = font.render('Play', 0, (255, 0, 0))
        self.screen.blit(text, ((WIDTH - size[0]) / 2, 252))
        size = font.size('High Score')
        text = font.render('High Score', 0, (255, 0, 0))
        self.screen.blit(text, ((WIDTH - size[0]) / 2, 342))

    def redrawAll(self):
        self.drawHead()
        self.drawMenu()

    def run(self):
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return self.mousePressed(event)
                if event.type == QUIT:
                    return 'quit'
            self.screen.blit(self.background, (0, 0))
            self.redrawAll()
            pygame.display.update()
        pygame.quit()
