class Stack:

    def __init__(self):
        self.compon = []
        self.top = -1
        self.length = 0

    def displayStack(self):
        print("[",end="")
        for i in range(self.length):
            if (i == self.top):
                print(self.compon[i],end="")
            else:
                print(self.compon[i],end="")
                print(",",end="")
        print("]")

    def isEmpty_Stack(self):
        return self.length == 0
    
    def infoTop(self):
        if (self.length > 0):
            return self.compon[self.top]
        
    def push(self,val):
        self.compon.append(val)
        self.top += 1
        self.length += 1

    def pop(self):
        if (self.length > 0):
            n = self.infoTop()
            self.compon.remove(self.infoTop())
            self.top -= 1
            self.length -= 1
            return n
        
class Rules:

    def __init__ (self,cur_state,input_word,stack_take,next_state,stack_store):
        self.cur_state = cur_state
        self.input_word = input_word
        self.stack_take = stack_take
        self.next_state = next_state
        self.stack_store = stack_store

    def displayRules(self):
        print("<"+self.cur_state+","+self.input_word+","+self.stack_take+","+self.next_state+","+self.stack_store+">",end='')