import os 

class Ribosome:

    def __init__(self,p = -1):
        self.pos = p
        self.image_path = os.path.join(*[
            'C:\\','Users','Akhlore','visualization','40s_60s.png'
        ])

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value