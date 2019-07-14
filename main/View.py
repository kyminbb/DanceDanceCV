import math
import numpy
import cv2
import pygame
from Data import Data
from Song import *
from Constants import *


class View(object):

    def initImages(self):
        self.upLeft = pygame.image.load(
            self.data.fileName('images', 'upLeft.jpg'))
        self.upLeftOn = pygame.image.load(
            self.data.fileName('images', 'upLeftOn.jpg'))
        self.upRight = pygame.image.load(
            self.data.fileName('images', 'upRight.jpg'))
        self.upRightOn = pygame.image.load(
            self.data.fileName('images', 'upRightOn.jpg'))
        self.downLeft = pygame.image.load(
            self.data.fileName('images', 'downLeft.jpg'))
        self.downLeftOn = pygame.image.load(
            self.data.fileName('images', 'downLeftOn.jpg'))
        self.downRight = pygame.image.load(
            self.data.fileName('images', 'downRight.jpg'))
        self.downRightOn = pygame.image.load(
            self.data.fileName('images', 'downRightOn.jpg'))
        self.center = pygame.image.load(
            self.data.fileName('images', 'center.jpg'))
        self.glow = pygame.image.load(
            self.data.fileName("images", "Glow.png"))

    def __init__(self, screen, detect, song):
        self.data = Data()
        self.detect = detect
        self.song = song
        self.screen = screen
        self.initImages()
        self.dis = math.sqrt(2 * (HEIGHT / 2 - SPRITE)**2)
        self.score = 0
        self.song.play()

    def displayFrame(self):
        frame = self.detect.getFrameImage()
        self.screen.blit(frame, (0, 0))

    def drawCorners(self):
        if self.detect.check(0):
            self.screen.blit(self.upLeftOn, (0, 0))
        else:
            self.screen.blit(self.upLeft, (0, 0))
        if self.detect.check(1):
            self.screen.blit(self.upRightOn, (WIDTH - SPRITE, 0))
        else:
            self.screen.blit(self.upRight, (WIDTH - SPRITE, 0))
        if self.detect.check(2):
            self.screen.blit(self.downLeftOn, (0, HEIGHT - SPRITE))
        else:
            self.screen.blit(self.downLeft, (0, HEIGHT - SPRITE))
        if self.detect.check(3):
            self.screen.blit(
                self.downRightOn, (WIDTH - SPRITE, HEIGHT - SPRITE))
        else:
            self.screen.blit(self.downRight, (WIDTH - SPRITE, HEIGHT - SPRITE))

    def drawCenters(self):
        self.screen.blit(
            self.center, (HEIGHT / 2 - SPRITE, HEIGHT / 2 - SPRITE))
        self.screen.blit(
            self.center, (WIDTH - HEIGHT / 2, HEIGHT / 2 - SPRITE))
        self.screen.blit(self.center, (HEIGHT / 2 - SPRITE, HEIGHT / 2))
        self.screen.blit(self.center, (WIDTH - HEIGHT / 2, HEIGHT / 2))

    def updateNotes(self):
        pass

    def drawNotes(self, arrow, dis):
        if arrow == 0:
            self.screen.blit(self.upLeft, (dis, dis))
        elif arrow == 1:
            self.screen.blit(self.upRight, (WIDTH - dis - SPRITE, dis))
        elif arrow == 2:
            self.screen.blit(self.downLeft, (dis, HEIGHT - dis - SPRITE))
        elif arrow == 3:
            self.screen.blit(self.downRight, (WIDTH - dis - SPRITE,
                                              HEIGHT - dis - SPRITE))

    def drawScore(self):
        font = pygame.font.Font(None, 80)
        size = font.size(str(self.score))
        score = font.render(str(self.score), 0, (0, 0, 0))
        self.screen.blit(score, ((WIDTH - size[0]) / 2, 15))

    def redrawAll(self):
        self.displayFrame()
        self.drawCorners()
        self.drawCenters()
        self.updateNotes()
        self.drawScore()

    def updateScore(self):
        pass

    def run(self):
        self.screen.fill((0, 0, 0))
        self.updateScore()
        self.redrawAll()
        pygame.display.update()
