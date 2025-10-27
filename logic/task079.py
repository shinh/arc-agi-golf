R=range(12);p=lambda g:max(m:=[B for y in R for x in R if sum(t:=sum(B:=[r[x:x+3]for r in g[y:y+3]],[]))==sum(r[x-(x>0):x+4].count(c:=max(t))for r in g[y-(y>0):y+4])*c>0],key=m.count)
