def p(g):
 s=sum(g,[]);a,b=divmod(s.index(2),10)
 while 5 in s:g[(i:=s.index(5))//10][i%10]=s[i]=0;g[min(a+2,max(a-1,i//10))][min(b+2,max(b-1,i%10))]=5
 return g