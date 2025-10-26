R=range(10)
a=any
p=lambda g:[[8*(a(g[A][:B+1])&a(g[A][B:])|a((C:=[*zip(*g)][B])[:A])&a(C[A:]))for B in R]for A in R]