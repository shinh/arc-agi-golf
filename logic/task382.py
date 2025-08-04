def p(g):
    r=lambda G:[list(x)for x in zip(*G[::-1])]
    for k in range(4):
        t=g
        for _ in range(k):t=r(t)
        if 2 in t[-1]:
            f=0
            if not any(row[0]==8 for row in t):
                if any(row[-1]==8 for row in t):t=[row[::-1]for row in t];f=1
                else:continue
            h=len(t);w=len(t[0])
            o=[[2*(c==2)for c in row]for row in t]
            b=t[-1]
            for y,row in enumerate(t):
                if row[0]==8:
                    kk=y
                    for x in range(w):
                        if b[x]==2:
                            kk-=1
                            if kk<0:break
                        o[kk][x]=8
            if f:o=[row[::-1]for row in o]
            for _ in range(4-k):o=r(o)
            return o

