def p(g):#mode of 3x3 centers with color confined in 5x5
    g=[[0]*16]+[[0]+r+[0]for r in g]+[[0]*16]
    m=[a for y in range(12)for x in range(12)if(w:=[r[x:x+5]for r in g[y:y+5]])and(a:=[r[1:4]for r in w[1:4]])and len(s:=set(sum(a,[]))-{0})==1 and sum(w,[]).count(c:=s.pop())==sum(a,[]).count(c)]
    return max(m,key=m.count)
