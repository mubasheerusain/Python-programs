def check_parantheses(s):
    stack = []
    opened = ['[','{','(']
    closed = [']','}',')']
    for i in s:
        if i in opened:
            stack.append(i)
        elif i in closed:
            pos = closed.index(i)
            if len(stack)>0 and opened[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                return "unbalanced"
    if len(stack) == 0:
        return "balanced"
    else:
        return "unbalanced"




s =input("Enter the input: ")
check_parantheses(s)
