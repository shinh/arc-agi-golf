def p(m):
 # slide tiles to anchors
 n=len(m);l=sum(m,[]);i=l.index;s=i(2),i(1);o=l[:]
 for k,v in enumerate(l):
  if v>2:e=abs(t:=k-s[v>3]);o[k-t+t//(e//n or e)]=v;o[k]*=o[k]!=v
 return[*zip(*[iter(o)]*n)]
