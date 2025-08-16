# alternate columns expanding from marker
def p(g,I=range):
 w=len(g[0])
 b=max(i for i,v in enumerate(sum(g,[]))if v)
 a,b=b//w+2,b%w
 for i in I(w):
  a,c=a-1,7+i%2;[w>b+j>=0 and g[y].__setitem__(b+j,c)for y in I(a)for j in(-i,i)]
 return g
