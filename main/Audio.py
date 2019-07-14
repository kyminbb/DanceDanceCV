import pygame


class Audio(object):
    def preOpen(self, frequency=44100, size=16, channels=True, buffer=1024):
        pygame.mixer.pre_init(frequency, size, channels, buffer)
        return True

    def open(self, frequency=44100, size=16, channels=True, buffer=1024):
        pygame.mixer.init(frequency, size, channels, buffer)
        return True

    def getChannel(self, n):
        return Channel(n)

    def getChannelCount(self):
        return pygame.mixer.get_num_channels()

    def pause(self):
        pygame.mixer.pause()

    def unpause(self):
        pygame.mixer.unpause()

    def quit(self):
        pygame.mixer.quit()


class Music(object):
    def __init__(self, fileName):
        pygame.mixer.music.load(fileName)

    def play(self, loops=0, start=0.0):
        pygame.mixer.music.play(loops, start)

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def fadeout(self, time):
        pygame.mixer.music.fadeout(time)

    def setVolume(self, value):
        pygame.mixer.music.set_volume(value)

    def isPlaying(self):
        return pygame.mixer.music.get_busy()

    def getPos(self):
        return pygame.mixer.music.get_pos()


class Channel(object):
    def __init__(self, ch):
        self.channel = pygame.mixer.Channel(ch)

    def play(self, sound):
        self.channel.play(sound)

    def stop(self):
        self.channel.stop()

    def fadeout(self, time):
        self.channel.fadeout(time)

    def setVolume(self, value):
        self.channel.set_volume(value)


class Sound(object):
    def __init__(self, fileName):
        self.sound = pygame.mixer.Sound(fileName)

    def play(self, loops=0):
        self.sound.play(loops)

    def stop(self):
        self.sound.stop()

    def fadeout(self, time):
        self.sound.fadeout(time)

    def setVolume(self, value):
        self.soud.set_volume(value)
