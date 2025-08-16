# flood fill using rotation like task002
f=lambda G,n=63:-n*G or f([[a or b&1 for a,b in zip(r,r[1:]+(0,))]for r in zip(*G[::-1])],n-1)
p=lambda g:(A:=f([[1]*(l:=len(g[0])+2)]+[[1]+[2*(c<9)for c in r]+[1]for r in g]+[[1]*l]),B:=f([[-~c%3 for c in r]for r in A]),[[[9,8-7*(b<1)][a>1]for a,b in zip(r1,r2)][1:-1]for r1,r2 in zip(A,B)][1:-1])[2]

