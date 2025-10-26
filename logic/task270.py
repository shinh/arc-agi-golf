def p(m):# slide tiles
 n=len(m);l=sum(m,[]);i=l.index;s=i(2),i(1);o=l*1
 for k,v in enumerate(l):
  if v>2:d=abs(t:=k-s[v>3]);o[k-t+t//(d//n or d)]=v;o[k]*=o[k]!=v
 return[*zip(*[iter(o)]*n)]
