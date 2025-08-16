# crop box around least common color
def p(m):
 b=sum(m,[]);w=len(m[0]);s={*b}-{0}
 if s:
  l=min(s,key=b.count)
  y,x=divmod(b.index(l),w);Y,X=divmod(len(b)+~b[::-1].index(l),w)
  return[r[x:X+1]for r in m[y:Y+1]]
 return[]

