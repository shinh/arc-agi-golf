# find unique 3x3 block by zero pattern
def p(g):
 # group rows every 3 then find the unique zero mask
 b,m=zip(*((t:=[r[x:x+3]for r in R],[c<1for c in sum(t,[])])for R in zip(*[iter(g)]*3)for x in range(len(R[0]))[::3]));return b[[*map(m.count,m)].index(1)]
