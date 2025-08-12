# flood fill using rotation like task002
f=lambda G,n=64:n and f([[a or b==1 for a,b in zip(r,r[1:]+(2,))]for r in zip(*G[::-1])],n-1)or G
p=lambda g:(A:=f([[2*(c<9)or i*(len(g)-1-i)<1 or j*(len(g[0])-1-j)<1 for j,c in enumerate(r)]for i,r in enumerate(g)]),[[[9,8-7*(b<1)][a>1]for a,b in zip(r1,r2)]for r1,r2 in zip(A,f([[(c+1)%3 for c in r]for r in A]))])[1]

