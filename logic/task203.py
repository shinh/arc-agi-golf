# 146
# def p(g,r=range,i=0):# fill concentric frames using reversed diagonal
#     n=len(g)
#     for c in[g[i][i]for i in r(n//2)][::-1]:
#         for j in r(i,n-i):g[i][j]=g[~i][j]=g[j][i]=g[j][~i]=c
#         i+=1
#     return g

# new approach, start creating a small square, rotate and append 1 edge at a time spiralling outward
# 129
# def p(g0):
#     g = [[]]
#     x=0
#     for i in range(len(g0)//2):
#         for j in range(3+x):
#             g = [*zip(*[[g0[i][i],*r] for r in g][::-1])]
#         x=1
#     return g

# 98 could be golfed further
p=lambda g,i=4:i<len(g)*2+3and[*zip(*[[g[j:=len(g)//2-i//4][j],*r] for r in p(g,i+1)][::-1])]or[[]]
