from Data import Data
from Audio import *


class Song(object):
    def __init__(self, fileName):
        self.isPlaying = False
        self.start = 0.0
        self.bpm = None
        self.period = 0
        self.music = Music(fileName)

    def setBPM(self, value):
        self.bpm = value
        self.period = 60000.0 / self.bpm

    def play(self, start=0.0):
        self.start = start
        self.music.play(0, start / 1000.0)
        self.isPlaying = True

    def pause(self):
        self.music.pause()
        self.engine.audio.pause()

    def unpause(self):
        self.music.unpause()
        self.engine.audio.unpause()

    def setVolume(self, value):
        self.music.setVolume(value)

    def fadeout(self, time):
        self.music.fadeout(time)
        self.isPlaying = False

    def stop(self):
        self.music.stop()
        self.isPlaying = False

    def getPos(self):
        if not self.isPlaying:
            pos = 0.0
        else:
            pos = self.music.getPos()
        if pos < 0.0:
            pos = 0.0
        return pos + self.start

    def isPlaying(self):
        return self.isPlaying and self.music.isPlaying()

    def getBeat(self):
        return self.getPosition() / self.period


class LoadSong(object):

    def __init__(self, fileName):
        self.data = Data()
        song = '%s.mp3' % fileName
        self.song = Song(self.data.fileName('songs', song))
