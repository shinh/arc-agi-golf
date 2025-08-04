def p(g):
    h,w=len(g),len(g[0]);v=set()
    for y in range(h):
        for x in range(w):
            if g[y][x]==2 and (y,x)not in v:
                s=[(y,x)];o=[]
                while s:
                    i,j=s.pop()
                    if (i,j)in v:continue
                    v.add((i,j));o+=[(i,j)]
                    for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                        ni=i+a;nj=j+b
                        if 0<=ni<h and 0<=nj<w and g[ni][nj]==2 and (ni,nj)not in v:s.append((ni,nj))
                b=max((p for p in o if p[0]in(0,h-1)or p[1]in(0,w-1)),default=None)
                if b:
                    m=len(o)//2
                    for i,j in o:
                        if abs(i-b[0])+abs(j-b[1])<m:g[i][j]=8
    return g
