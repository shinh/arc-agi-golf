def p(g):
 f=sum(g,[]);i=f.index;w=10;u=i(1)//w;h=[[0]*w for _ in g]
 for k,v in enumerate(f):h[k//w+u-i(v or 1)//w][k%w]+=v
 return h