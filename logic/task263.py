# find unique 3x3 block by zero pattern
def p(g):
 b,m=zip(*((t:=[r[x:x+3]for r in g[y:y+3]],[c<1for c in sum(t,[])])for y in range(0,len(g),3)for x in range(0,len(g[0]),3)));return b[m.index(min(m,key=m.count))]

