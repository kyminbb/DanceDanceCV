import pygame
from pygame.locals import *
from Audio import Audio
from Song import *
from Detect import Detect
from View import View
from Constants import *


class Play():

    def __init__(self, song):
        self.audio = Audio()
        self.audio.preOpen()
        self.detect = Detect()
        pygame.init()
        self.audio.open()
        self.song = LoadSong(song).song
        pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('DanceDanceCV')
        screen = pygame.display.get_surface()
        self.view = View(screen, self.detect, self.song)

    def run(self):
        playing = True
        while playing:
            for events in pygame.event.get():
                if events.type == QUIT:
                    return 'quit'
            self.detect.run()
            self.view.run()
            pygame.display.update()
        pygame.quit()
