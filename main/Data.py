import sys
import os


class Data(object):

    def __init__(self, path=os.path.join('..', 'data')):
        self.path = path

    def fileName(self, *name, **args):
        return os.path.join(self.path, *name)
