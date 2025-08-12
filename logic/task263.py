# find unique 3x3 block by zero pattern
def p(g):
 R=range;b=[];m=[]
 for y in R(0,len(g),3):
  for x in R(0,len(g[0]),3):
   t=[r[x:x+3]for r in g[y:y+3]]
   b+=t,;m+=[[c<1 for c in r]for r in t],
 return b[m.index(min(m,key=m.count))]

