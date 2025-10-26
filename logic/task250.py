def p(g):
 s=sum(g,[]);a,b=divmod(s.index(2),10)
 for i in range(100):
  if s[i]&1:g[i//10][i%10]=0;g[min(a+2,max(a-1,i//10))][min(b+2,max(b-1,i%10))]=5
 return g