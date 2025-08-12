# flood fill using rotation like task002
f=lambda G,n=64:n and f([[a or b==1 for a,b in zip(r,r[1:]+(2,))]for r in zip(*G[::-1])],n-1)or G
def p(g):
    h=len(g);w=len(g[0])
    A=f([[2*(c<9)or(i<1 or i==h-1 or j<1 or j==w-1)for j,c in enumerate(r)]for i,r in enumerate(g)])
    B=f([[(1,2,0)[c]for c in r]for r in A])
    return [[[(8,1)[b<1],9][a<2]for a,b in zip(r1,r2)]for r1,r2 in zip(A,B)]

