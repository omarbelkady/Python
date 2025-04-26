def next_greater_el(myli):
    #[4,5,2]
    stack = []
    output= [-1]*len(myli)
    for i in range(len(myli)-1,-1,-1):
        while stack and myli[i]>=stack[-1]:
            stack.pop()
        if stack:
            output[i]=stack[-1]
        stack.append(myli[i])
    return output

def stackCalc(exp):
    operands=[]
    operators=[]
    for i in range(len(exp)):
            if exp[i]=='(':
                continue
            elif exp[i] in '^+-*/':
                operators.append(exp[i])
            elif exp[i]==')':
                right=operands.pop()
                left=operands.pop()
                op=operators.pop()

                if op == '+':
                    operands.append(left+right)
                elif op == '-':
                    operands.append(left-right)
                elif op == '*':
                    operands.append(left*right)
                elif op == '/':
                    operands.append(left/right)
                elif op == '^':
                    operands.append(left**right)
            else:
                operands.append(int(exp[i]))
    return operands[-1]
print(stackCalc('(1+(2*3))'))



class Min_stack:
    def __init__(self):
        self._L=[]
        self._min_stack=[]
    def push(self,value):
        self._min_stack.append(value)
        if not self._min_stack or value<self._min_stack[-1]:
            self._min_stack.append(value)

    def pop(self):
        if not self._min_stack:
            print("Empty")
        else:
            top_el = self._min_stack.pop()
            if top_el == self._min_stack[-1]:
                self._min_stack.pop()
            return top_el
    def top(self):
        if not self._min_stack:
            print("Empty")
        return self._min_stack[-1]





def infixToPostfix(myexp):
    operatpreced = {"(": 1, ")": 1, "**": 2, "*": 3, "/": 4, "+": 5, "-": 6}
    toPush = []
    toPop = []
    for i in range(len(myexp)):
        token = myexp[i]
        if token.isalnum():
            toPop.append(token)
        elif token == "(":
            toPush.append(token)
        elif token == ")":
            while toPush and toPush[-1] != '(':
                toPop.append(toPush.pop())
            toPush.pop()
        else:
            while toPush and operatpreced.get(toPush[-1], 0) > operatpreced.get(token, 0):
                toPop.append(toPush.pop())
            toPush.append(token)
    while toPush:
        toPop.append(toPush.pop())
    return ''.join(toPop)


print(infixToPostfix("A+B*C"))

m = Min_stack()
for v in [1,24,21,31,231]:
    m.push(v)
print(m.top())

print(next_greater_el([1,22,31,21,41]))