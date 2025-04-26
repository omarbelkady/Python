class StacksUsingLists:
    def __init__(self):
        self._L=[]

    def _push(self,toPush):
        self._L.append(toPush)

    def _peek(self):
        if not self.isEmpty():
            return self._L[-1]
        return None
    def _pop(self):
        if not self._L:
            print("Stack underflow")
            return None
        return self._L.pop()
    def isEmpty(self):
        return(len(self._L)==0)
obj1 = StacksUsingLists()
obj1._push(3)
print("element popped: "+str(obj1._pop()))
