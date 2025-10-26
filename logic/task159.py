B=enumerate
def p(g):D,E=map(min,zip(*((a,d)for a,c in B(g)for d,e in B(c)if e&-3)));R=range(A:=sum(2in a for a in g));return[[(2,g[D+(3*i+1)//A][E+(3*j+1)//A])[0<i<A-1>j>0]for j in R]for i in R]
