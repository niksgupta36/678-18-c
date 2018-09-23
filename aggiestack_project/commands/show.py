'''
Created on Sep 22, 2018

@author: sharm
'''
from .base import Base
from json import dumps

class Show(Base):
    """Say hello, world!"""

    def run(self):
        print('show, world!')
        #print(self.options)