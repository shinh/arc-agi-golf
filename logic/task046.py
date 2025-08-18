def p(g):
    # glue blocks together by matching gray pins
    o=[[]for _ in g];v=0;s=[]
    for col in (*zip(*g),0):
        if col==(0,0,0) or col==0:
            if s:
                b=list(zip(*s))
                c=max(n for r in b for n in r if n%5)
                t=[r[0]for r in b];l=5 in t and t.index(5)
                t=[r[-1]for r in b];r=5 in t and t.index(5)
                d=l-v;w=len(b[0])
                for y in range(3):
                    f=y+d
                    o[y]+=[c if n==5 else n for n in b[f]] if 0<=f<3 else [0]*w
                v+=r-l;s=[]
        else:s.append(col)
    return o
