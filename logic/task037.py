def p(g):
 t=sum(g,[])
 for v in {*t}-{0}:
  a=t.index(v);d=t.index(v,a+1)-a;s=9+(d%9>0)*2;t[a:a+d+s:s]=[v]*-~(d//s)
 return[*zip(*[iter(t)]*10)]