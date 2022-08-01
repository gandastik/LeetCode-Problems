#20. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#1. Open brackets must be closed by the same type of brackets.
#2. Open brackets must be closed in the correct order.

class Stack:
    def __init__(self, items = None):
        if(items == None):
            self.items = []
        else:
            self.items = items
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.itmes == []
    
def isMatch(open, close) -> bool:
    return (open == '(' and close == ')') or (open == '[' and close == ']') or (open == '{' and close == '}')

def isValid(s: str) -> bool:
    stack = Stack()
    i = 0
    error = 0
    for i in s:
        if(i in '([{'):
            stack.push(i)
        else:
            if(i in ')]}'):
                if(stack.size() > 0):
                    if(not isMatch(stack.pop(), i)):
                        error += 1
                else:
                    error += 1
    if(stack.size() > 0):
        error+=1
    return error == 0

if __name__ == "__main__":
    s = str(input())
    print(isValid(s))