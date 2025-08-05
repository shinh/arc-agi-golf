def p(g):
    H=W=10;R=range
    v=set();o=[r[:]for r in g]
    for y in R(H):
        for x in R(W):
            if g[y][x]==3 and (y,x)not in v:
                q=[(y,x)];p=[];rs=set();cs=set()
                while q:
                    i,j=q.pop()
                    if(i,j)in v:continue
                    v.add((i,j));p.append((i,j));rs.add(i);cs.add(j)
                    for Y in R(i-1,i+2):
                        for X in R(j-1,j+2):
                            if 0<=Y<H and 0<=X<W and g[Y][X]==3 and(Y,X)not in v:q.append((Y,X))
                my,my2=min(rs),max(rs);mx,mx2=min(cs),max(cs)
                h=my2-my+1;w=mx2-mx+1
                for i,j in p:
                    X=mx+mx2-j
                    for a in(0,1):
                        I=(i-my)*2+a+my-h//2
                        for b in(0,1):
                            J=(X-mx)*2+b+mx-w//2
                            if 0<=I<H and 0<=J<W and I not in rs and J not in cs:o[I][J]=8
    return o
