def p(g):
    g=[[0]*16]+[[0]+r+[0]for r in g]+[[0]*16];m=[]
    for y in range(12):
        for x in range(12):
            w=[r[x:x+5]for r in g[y:y+5]];a=[r[1:4]for r in w[1:4]]
            t=sum(a,[]);s=set(t)-{0}
            if s and len(s)<2 and sum(w,[]).count(c:=s.pop())==t.count(c):m+=a,
    return max(m,key=m.count)
