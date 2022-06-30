import os
import sys
from collections import deque
if __name__ == '__main__':
    ip = 0
    stack = deque()
    #while True:
    com = input("cal>> ").split(' ')
    for ip in range(len(com)):
        print(stack)
        if com[ip] == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a) + int(b))
            ip += 1
        elif com[ip] == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a) - int(b))
            ip += 1
        else:
            stack.append(com)
            a = stack.pop()
            stack.append(a)
            # stack.append(a)
        ip += 1