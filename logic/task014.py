def p(g):
    h=len(g);w=len(g[0])
    r=[i for i,t in enumerate(g) if set(t)=={0}]
    c=[j for j in range(w) if {g[i][j] for i in range(h)}=={0}]
    a,b=r[0],r[-1]+1;d=c[0];e=c[-1]+1
    q=[(0,a,0,d),(0,a,e,w),(b,h,0,d),(b,h,e,w)]
    s=[next(g[y][x] for y in range(y0,y1) for x in range(x0,x1) if g[y][x]) for y0,y1,x0,x1 in q]
    i=next(i for i,v in enumerate(s) if s.count(v)==1)
    y0,y1,x0,x1=q[i]
    return [row[x0:x1] for row in g[y0:y1]]
