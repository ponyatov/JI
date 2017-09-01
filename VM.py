######## Stack ########

class Stack:
    def __init__(self,init=None):
        if init: self.dat=init
        else: self.dat=[]
    def push(self,o): self.dat.append(o); return self
    def __iadd__(self,o): return self.push(o)
    def pop(self): return self.dat.pop()
    def top(self): return self.dat[-1]
    def __repr__(self):
        S='[ '
        for i in self.dat: S += '%s '%i
        return S+']'

def test_init(): assert Stack([1,2,3]).dat==[1,2,3] 
def test_push(): s= Stack([1,2,3]) ; s += 4 ; assert s.dat == [1,2,3,4]
def test_pop(): assert Stack([1,2,3]).pop() == 3
def test_top(): assert Stack([1,2,3]).top() == 3

######### Machine ########

class Machine:
    pass