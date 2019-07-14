import pygame
from pygame.locals import *
from Data import Data
from Constants import *


class Choose(object):

    def __init__(self, screen):
        self.data = Data()
        img = self.data.fileName('images', 'background.jpg')
        self.background = pygame.image.load(img)
        img = self.data.fileName('images', 'backward.jpg')
        self.backward = pygame.image.load(img)
        albums = ['blackpink-square-two.jpg', 'calvinharris-summer.jpg']
        albums = [self.data.fileName('images', album) for album in albums]
        self.albums = [pygame.image.load(album) for album in albums]
        self.albumBound1 = ((130, 220), (150, 150))
        self.albumBound2 = ((350, 220), (150, 150))
        pygame.init()
        self.font = pygame.font.Font(None, 50)
        self.msg = 'Choose a song and click to start!'
        self.msgSize = self.font.size(self.msg)
        self.screen = screen

    def isInside(self, bound, x, y):
        return (bound[0][0] < x < bound[0][0] + bound[1][0] and
                bound[0][1] < y < bound[0][1] + bound[1][1])

    def mousePressed(self, event):
        x, y = event.pos
        if self.isInside(self.albumBound1, x, y):
            return 'play1'
        elif self.isInside(self.albumBound2, x, y):
            return 'play2'
        elif self.isInside(((0, 0), (64, 64)), x, y):
            return 'intro'

    def drawMessage(self):
        head = self.font.render(self.msg, 0, (255, 255, 255))
        self.screen.blit(head, ((WIDTH - self.msgSize[0]) / 2, 120))

    def drawAlbumCovers(self):
        self.screen.blit(self.albums[0], self.albumBound1[0])
        self.screen.blit(self.albums[1], self.albumBound2[0])

    def redrawAll(self):
        self.drawMessage()
        self.drawAlbumCovers()

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
