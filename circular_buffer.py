class CircularBuffer(object):

    def __init__(self,max_size):
        self.max_size = max_size
        self.log = [0] * self.max_size
        self.current = 0

    def record(self, eye_num):
        self.log[self.current] = eye_num
        self.current = ((self.current+1) % self.max_size) #O(1) insertion

    
