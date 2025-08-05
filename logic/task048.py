def p(g):
    h=len(g);w=len(g[0]);v=set();d={}
    for y in range(h):
        for x in range(w):
            if(y,x)in v:continue
            c=g[y][x];q=[(y,x)];v.add((y,x))
            for i,j in q:
                for Y,X in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0<=Y<h and 0<=X<w and g[Y][X]==c and(Y,X)not in v:v.add((Y,X));q.append((Y,X))
            d[c]=d.get(c,[])+[q]
    def n(o):a=min(y for y,_ in o);b=min(x for _,x in o);return{(y-a,x-b)for y,x in o}
    for c,L in d.items():
        if c and len(L)==2 and sum(map(len,L))==8 and n(L[0])==n(L[1]):
            a,b=L;A=set(a);B=set(b)
            for k,L2 in d.items():
                if k not in(0,c):
                    for o in L2:
                        O={(y+1,x)for y,x in o}|{(y-1,x)for y,x in o}|{(y,x+1)for y,x in o}|{(y,x-1)for y,x in o}
                        if O&A and O&B:return[[k]]
            return[[0]]
    return[[0]]

