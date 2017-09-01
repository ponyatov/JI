######## Stack ########

class Stack:
    def __init__(self,init=None):
        if init: self.dat=init
        else: self.dat=[]
    def push(self,o): self.dat.append(o); return self
    def __iadd__(self,o): return self.push(o)
    def pop(self):
        if self.size() > 0: return self.dat.pop()
        else: raise RuntimeError(self)
    def top(self): return self.dat[-1]
    def size(self): return len(self.dat)
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
        self.ticks = 0      # block infty loop
        self.dispatch = {   # bc/semantic dispatch
            'nop':  self.nop,
            '+':    self.add,
            '*':    self.mul,
            'jmp':  self.jmp,
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
            opcode = self.code[self.ip] ; self.ip += 1 ; self.ticks +=1
            if self.ticks > 0x100: raise RuntimeError(self.ticks)
            # dispatch command
            if opcode in self.dispatch: self.dispatch[opcode]() # command
            else: self.push(opcode)
        return self
    # command semantics
    def nop(self): pass
    def add(self): last = self.pop() ; self.push(self.pop() + last)
    def mul(self): last = self.pop() ; self.push(self.pop() * last)
    def jmp(self):
        addr = self.pop()
        if isinstance(addr, int) and 0 <= addr < len(self.code): self.ip = addr
        else: raise RuntimeError('jmp %s' % addr.__class__) 

def test_vm():
    m = Machine([]) ; assert m.code == [] ; assert m.ip == 0
    assert m.dat.dat == [] ; assert m.ret.dat == []
def test_addmul():
    assert Machine(['nop',1,2,3,'*','+']).run().pop() == 7
def test_jmp():
    try: z = Machine([0, 'jmp']).run()
    except: z = None
    assert z == None

print Machine(['nop',1,2,3,'*','+']).push([1,2,3]).run()

