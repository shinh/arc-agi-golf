def p(g):# surround unique cell with 2s
    a=sum(g,[]);v=min(a,key=a.count);y,x=divmod(a.index(v),10);o=create(10,10)
    for Y in y-1,y,y+1:
        for X in x-1,x,x+1:
            if-1<Y<10 and-1<X<10:o[Y][X]=2
    o[y][x]=v;return o
