def p(g):#mode of 3x3 centers with color confined in 5x5
    g=[[0]*16,*[[0,*r,0]for r in g],[0]*16]
    m=[a for y in range(12)for x in range(12)if(c:=max(t:=sum(a:=[r[x+1:x+4]for r in g[y+1:y+4]],[])))and t.count(c)+t.count(0)>8 and sum(r[x:x+5].count(c)for r in g[y:y+5])==t.count(c)]
    return max(m,key=m.count)
