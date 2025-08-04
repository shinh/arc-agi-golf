def p(g):
    h=len(g);w=len(g[0]);v=set();d={}
    for y in range(h):
        for x in range(w):
            if(y,x)in v:continue
            c=g[y][x];q=[(y,x)];v.add((y,x))
            for i,j in q:
                for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
                    Y,X=i+di,j+dj
                    if 0<=Y<h and 0<=X<w and g[Y][X]==c and(Y,X)not in v:v.add((Y,X));q.append((Y,X))
            d.setdefault(c,[]).append(set(q))
    def n(o):
        a=min(y for y,_ in o);b=min(x for _,x in o)
        return{(y-a,x-b)for y,x in o}
    for c,L in d.items():
        if c and sum(len(o)for o in L)==8 and len(L)==2 and len({frozenset(n(o))for o in L})==1:
            a,b=L
            for cc,L2 in d.items():
                if cc not in(0,c):
                    for o in L2:
                        if any(abs(y-y1)+abs(x-x1)==1 for y,x in o for y1,x1 in a)and any(abs(y-y2)+abs(x-x2)==1 for y,x in o for y2,x2 in b):
                            return[[cc]]
            return[[0]]
    return[[0]]
