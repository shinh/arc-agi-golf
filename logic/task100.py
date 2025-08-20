#max bbox color
def p(g):
 s=''.join(map(str,sum(g,[])));w=len(g[0]);m=k=0
 for c in'123456789':
  a=s.find(c);b=s.rfind(c);a+1 and(t:=(b%w-a%w+1)*(b//w-a//w+1))>m and(m:=t,k:=int(c))
 return [[k]*2]*2

