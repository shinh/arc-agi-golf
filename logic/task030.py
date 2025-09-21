def p(g):# align to row of 1
 f=sum(g,[]);i=f.index;w=len(g[0]);g=[w*[0]for _ in g];u=i(1)//w
 for k,c in enumerate(f):g[k//w+u-i(c or 1)//w][k%w]+=c
 return g
