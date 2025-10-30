def p(m):#slide
 n=len(m);o=sum(m,[]);i=o.index
 for k,v in enumerate(o*1):
  if v>2:d=abs(t:=k-i(2-v//4));o[k-t+t//(d//n or d)]=v;o[k]*=o[k]!=v
 return[*zip(*[iter(o)]*n)]
