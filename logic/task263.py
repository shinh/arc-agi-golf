# find unique 3x3 block by zero pattern
def p(g):
 b=[];m=[]
 for y in range(0,len(g),3):
  for x in range(0,len(g[0]),3):
   b+=[t:=[r[x:x+3]for r in g[y:y+3]]];m+=[[c<1for c in sum(t,[])]]
 return b[m.index(min(m,key=m.count))]

