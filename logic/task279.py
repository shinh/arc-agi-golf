# flood fill using rotation like task002
f=lambda G,n=64:n and f([[a or b==1 for a,b in zip(r,r[1:]+(2,))]for r in zip(*G[::-1])],n-1)or G
p=lambda g:(w:=len(g[0])+2,A:=f([[1]*w]+[[1]+[2*(c<9)for c in r]+[1]for r in g]+[[1]*w]),[[[9,8-7*(b<1)][a>1]for a,b in zip(r1[1:-1],r2[1:-1])]for r1,r2 in zip(A[1:-1],f([[-~c%3 for c in r]for r in A])[1:-1])])[2]

