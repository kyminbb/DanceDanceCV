import pygame
from pygame.locals import *
from Data import Data


class HighScore(object):

    def __init__(self, screen):
        self.data = Data()
        img = self.data.fileName('images', 'background.jpg')
        self.background = pygame.image.load(img)
        img = self.data.fileName('images', 'backward.jpg')
        self.backward = pygame.image.load(img)
        self.screen = screen

    def isInside(self, bound, x, y):
        return (bound[0][0] < x < bound[0][0] + bound[1][0] and
                bound[0][1] < y < bound[0][1] + bound[1][1])

    def mousePressed(self, event):
        x, y = event.pos
        if self.isInside(((0, 0), (64, 64)), x, y):
            return 'intro'

    def redrawAll(self):
        pass

    def run(self):
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return self.mousePressed(event)
                if event.type == QUIT:
                    return 'quit'
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.backward, (0, 0))
            self.redrawAll()
            pygame.display.update()
        pygame.quit()
