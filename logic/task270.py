def p(m):
 n=len(m);l=sum(m,[]);i=l.index;a=i(1);b=i(2);o=l[:]
 for k,v in enumerate(l):
  if v>2:c=(b,a)[v>3];t=k-c;e=abs(t);o[c+t//(e//n or e)]=v;o[k]^=o[k]*(o[k]==v)
 return[*zip(*[iter(o)]*n)]