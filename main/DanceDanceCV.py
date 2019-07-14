import pygame
from pygame.locals import *
from Intro import Intro
from Choose import Choose
from HighScore import HighScore
from Play import Play
from Constants import *


class DanceDanceCV(object):

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('DanceDanceCV')
        self.intro = Intro(self.screen)
        self.choose = Choose(self.screen)
        self.highScore = HighScore(self.screen)
        self.song1 = 'fire'
        self.song2 = 'summer'

    def run(self):
        playing = True
        mode = 'intro'
        while playing:
            if mode == 'intro':
                mode = self.intro.run()
            elif mode == 'choose':
                mode = self.choose.run()
            elif mode == 'high score':
                mode = self.highScore.run()
            elif mode == 'play1':
                self.play = Play(self.song1)
                mode = self.play.run()
            elif mode == 'play2':
                self.play = Play(self.song2)
                mode = self.play.run()
            elif mode == 'quit':
                playing = False
        pygame.quit()


if __name__ == "__main__":
    game = DanceDanceCV()
    game.run()
