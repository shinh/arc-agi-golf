def p(g):#copy
 s=sum(g,[]);f=s.index;r,c=divmod(f(8),10);o=create(10,10)
 for v in{*s}-{8}:o[r+(r<f(v)//10)][c+(c<f(v)%10)]|=v
 return o
