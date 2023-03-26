
def makeGood(s):
    stack = []
    for i in s: 
        if stack and stack[-1] != i and stack[-1].lower() == i.lower():
            print(stack[0])
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)

#test case
s = 'leEeeEEetcode'
print(makeGood(s))