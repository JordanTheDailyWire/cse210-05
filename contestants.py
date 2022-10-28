from points import point
from direction import Direction
from keyboard import keyboard_service

class Contestants():
    def __init__(self):
        super().__init__()
        #Begins the instance of two players
        '''Attributes:'''
        ks=keyboard_service()
        self.direct = Direction()
        self.a = (-1,0)
        self.s = (0,-1)
        self.d = (+1,0)
        self.w = (0,+1)
        self.j = (-1,0)
        self.k = (0,-1)
        self.l = (+1,0)
        self.i = (0,+1)
        self.x = point.get_x()
        self.y = point.get_y()
        

    def execute(self,point):
        if self.direct == self.a:
            self.x -= 1 
        elif self.direct == self.s:
            self.y -= 1
        elif self.direct == self.d:
            self.x += 1
        elif self.direct == self.w:
            self.y += 1
        elif self.direct == self.k:
            self.y -= 1
        elif self.direct == self.l:
            self.x += 1
        elif self.direct == self.i:
            self.y += 1
        elif self.direct == self.j:
            self.x -= 1