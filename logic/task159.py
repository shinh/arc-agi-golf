B=enumerate
def p(g):
 A=sum(2in a for a in g);D,E=map(min,zip(*((a,d)for a,c in B(g)for d,e in B(c)if e&-3)));R=range(A);return[[(2,g[D+(3*i+1)//A][E+(3*j+1)//A])[(i>0<j)*(i<A-1>j)]for j in R]for i in R]