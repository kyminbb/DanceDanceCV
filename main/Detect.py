import numpy
import cv2
import pygame
from Constants import *


class Detect(object):

    def initRegions(self):
        frame = self.frame
        self.region1 = (0, REGION, 0, REGION)
        self.region2 = (0, REGION, WIDTH - REGION, WIDTH)
        self.region3 = (HEIGHT - REGION, HEIGHT, 0, REGION)
        self.region4 = (HEIGHT - REGION, HEIGHT, WIDTH - REGION, WIDTH)
        self.regions = (self.region1, self.region2, self.region3, self.region4)
        if LEVEL >= 6:
            self.region5 = (HALF_HEIGHT_UP, HALF_HEIGHT_DOWN, 0, REGION)
            self.region6 = (HALF_HEIGHT_UP, HALF_HEIGHT_DOWN,
                            WIDTH - REGION, WIDTH)
            self.regions.append(self.region5)
            self.regions.append(self.region6)
        if LEVEL == 8:
            self.region7 = (0, REGION, HALF_WIDTH_LEFT, HALF_WIDTH_RIGHT)
            self.region8 = (HEIGHT - REGION, HEIGHT,
                            HALF_WIDTH_LEFT, HALF_WIDTH_RIGHT)
            self.regions.append(self.region7)
            self.regions.append(self.region8)

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        WIDTH = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        HEIGHT = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.bsmog = []
        self.bgAdapt = []
        for i in range(4):
            self.bsmog.append(cv2.createBackgroundSubtractorMOG2(0, 0.2))
            self.bgAdapt.append(0.5)

        ret, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1)
        self.initRegions()
        self.previous = [False for i in range(LEVEL)]
        self.current = [False for i in range(LEVEL)]

    def getFrameImage(self):
        frame = numpy.rot90(self.frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 0)
        frame = pygame.surfarray.make_surface(frame)
        return frame

    def check(self, arrow):
        frame = self.frame
        region = frame[self.regions[arrow][0]:self.regions[arrow][1],
                       self.regions[arrow][2]:self.regions[arrow][3]]
        region = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
        region = cv2.GaussianBlur(region, (5, 5), 0)
        minHand = numpy.array([30, 34, 45], dtype=numpy.uint8)
        maxHand = numpy.array([180, 206, 255], dtype=numpy.uint8)
        result = cv2.inRange(region, minHand, maxHand)
        return MIN_THRESHOLD < cv2.countNonZero(result) < MAX_THRESHOLD

    def update(self):
        for i in range(LEVEL):
            self.previous[i] = self.current[i]
            self.current[i] = self.check(i)

    def run(self):
        ret, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1)
        self.update()
        cv2.waitKey(1)
