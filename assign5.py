# 1)
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

# 2)
def average(array):
    sum = 0 
    for x in set(array): 
        sum = sum + x 
        
    return float(round(sum/len(set(array)), 3))

# 3)
import textwrap 
def wrap(string, max_width):
    wraptext = textwrap.wrap(string, max_width)
    return '\n'.join(wraptext)

# 4)
def print_rangoli(s):
    
    ab='abcdefghijklmnopqrstuvwxyz'
    mid=((n+(n-1))*2)-1
    rev=[]
    for i in range(s):
        r=''
        k=''
        for j in range(i+1):
            if j==i:
                r+=ab[s-1-j]
                top=r+k[::-1]
                t=top.center(mid,"-")
                rev.append(t)
                print(t)
            else:
                r+=ab[s-1-j]+"-"
                k=r
    for i in range(s-1):
        print(rev[s-2-i])

# 5)
def merge_the_tools(string, k):
    # your code goes here
     for t in range(0,len(string),k):
        u = set()
        for i in range(t,t+k):
            if string[i] not in u:
                u.add(string[i])
                print(string[i],end="")
        print()


# 6)
from collections import Counter
X = int(input())
sizes = list(map(int, input().split()))
money = 0
N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    cnt = Counter(sizes)
    if lst[0] in cnt.keys():
        money += lst[1]
        sizes.remove(lst[0])
    else:
        money += 0
print(money)


# 7)
T = int(input())
for i in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)


# 8)
import re
n = int(input())
for _ in range(n):
    try:
        s = input()
        p = re.compile(s)
        print("True")
    except re.error:
        print("False")


# 9)
n = input()
s = [val for val in input().split(" ")]
s = s[::-1]
s = set(s)
N = int(input())

for _ in range(N):
    command = input().split(" ")
    try:
        if command[0] == "pop":
            s.pop()
        elif command[0] == "discard":
            s.discard(command[1])
        else:
            s.remove(command[1])
    except Exception as e:
        continue
print(sum(map(int, s)))  
