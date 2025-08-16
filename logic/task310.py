# crop box around least common color
def p(m):
 a=[v for r in m for v in r if v]
 if not a:return[]
 l=min(a,key=a.count)
 y=[i for i,r in enumerate(m)if l in r];x=[i for i,c in enumerate(zip(*m))if l in c]
 return[r[x[0]:x[-1]+1]for r in m[y[0]:y[-1]+1]]

