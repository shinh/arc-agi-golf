# Very bad. I don't know how to check frames in a shorter manner.
def p(g):
    m=[]
    for y in range(12):
        for x in range(12):
            a=[r[x:x+3]for r in g[y:y+3]]
            b=[]
            if y:b+=g[y-1][max(x-1,0):x+4]
            if y<11:b+=g[y+3][max(x-1,0):x+4]
            if x:b+=[g[y][x-1],g[y+1][x-1],g[y+2][x-1]]
            if x<11:b+=[g[y][x+3],g[y+1][x+3],g[y+2][x+3]]
            s=set(sum(a,[]))-{0}
            if len(s)==1:
                c=[*s][0]
                if c not in b:
                    m.append(a)
    return max(m,key=m.count)
