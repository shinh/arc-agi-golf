def p(g):
    # recolor 3s by shape
    for o in range(80):
        g=[[[[[c,[u for u in[2,6,1,c]if u in(c,p)][0]][p*c and o>8],6][c==3 and p==n==1],(p>0)+(n>0)+(u>0)][c==t==3 and p+n>0]for x,(c,p,n,t,u) in enumerate(zip(r,[0]+r,r[1:]+[0],pr,nr))]for y,(r,pr,nr) in enumerate(zip(g,[[0]*99]+g,g[1:]+[[0]*99]))]
        g=[*map(list,zip(*g[::-1]))]
    return g
