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
    def __init__(self, code):
        self.dat = Stack()  # data stack
        self.ret = Stack()  # return stack
        self.code = code    # byte-code
        self.ip = 0         # instruction pointer
        self.dispatch = {   # bc/semantic dispatch
            'nop':  self.nop,
            '+':    self.add,
            '*':    self.mul,
        }  
    def push(self,o): self.dat.push(o) ; return self
    def pop(self): return self.dat.pop()
    def top(self): return self.dat[-1]
    def __repr__(self):
        S = '%s @ %.4X\n\n'%(self.__class__.__name__,self.ip)
        S += 'dat: %s\n'%self.dat
        S += 'ret: %s\n'%self.ret
        S += '\n%s\n\n'%self.code
        return S
    def run(self):
        while self.ip < len(self.code):
            # fetch command
            opcode = self.code[self.ip] ; self.ip += 1  # fetch
            # dispatch command
            if opcode in self.dispatch: self.dispatch[opcode]() # command
            elif isinstance(opcode, int): self.push(opcode)     # integer
            elif isinstance(opcode, float): self.push(opcode)   # float
            elif isinstance(opcode, str): self.push(opcode)     # string
            else: raise RuntimeError(opcode)
        return self
    # command semantics
    def nop(self): pass
    def add(self): self.push(self.pop() + self.pop())
    def mul(self): self.push(self.pop() * self.pop())

def test_vm():
    m = Machine([]) ; assert m.code == [] ; assert m.ip == 0
    assert m.dat.dat == [] ; assert m.ret.dat == []
def test_addmul():
    assert Machine(['nop',1,2,3,'*','+']).run().pop() == 7

print Machine(['nop',1,2,3,'*','+']).push([1,2,3]).run()

