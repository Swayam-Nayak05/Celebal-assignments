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
