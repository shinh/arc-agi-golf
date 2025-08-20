#bbox
def p(g):
 s=str(sum(g,[]))[1::3];w=len(g[0])
 k=max(s,key=lambda c:c>'0'and~(a:=s.find(c))and((l:=s.rfind(c)-a)%w+1)*(l//w+1))
 return [[int(k)]*2]*2

