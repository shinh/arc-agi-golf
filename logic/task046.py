# glue blocks together by matching gray pins
def p(g):
    o=[[],[],[]];v=0;s=[]
    for c in(*zip(*g),0):
        if c and any(c):s+=c,
        elif s:
            c=max(n for t in s for n in t if n%5);l=5 in s[0] and s[0].index(5);r=5 in s[-1] and s[-1].index(5);d=l-v;w=len(s)
            for y in 0,1,2:
                f=y+d;o[y]+=0<=f<3 and [t[f]==5 and c or t[f]for t in s] or [0]*w
            v+=r-l;s=[]
    return o
