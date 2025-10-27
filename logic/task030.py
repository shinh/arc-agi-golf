def p(g):
 h=[[0]*10 for _ in g];f=sum(g,[]);i=f.index
 for k,v in enumerate(f):h[k//10+i(1)//10-i(v or 1)//10][k%10]+=v
 return h
