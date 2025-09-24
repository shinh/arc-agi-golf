# def p(g):#arch->4
#  for r,b in zip(g,g[1:]):
#   for j in range(1,len(r)-1):g[-1][j]|=4*(b[j-1]==b[j+1]==r[j]>b[j]<1)
#  return g

# def p(g):
#     for x in range(len(g[0])):
#         g[-1][x] = 4*(len(g)-1==[*zip(*g)][x].count(0))
#     return g


# def p(g):
#     g[-1]=[4*(len(g)-1==[*zip(*g)][x].count(0)) for x in range(len(g[0]))]
#     return g

# 83
# p=lambda g:g[:-1]+[[4*(len(g)-1==[*zip(*g)][x].count(0)) for x in range(len(g[0]))]]

# 62
# p=lambda g:g[:-1]+[[4*(len(g)-1==x.count(0))for x in zip(*g)]]

# 60
# p=lambda g:g[:-1]+[[4*(x.count(max(x))==1)for x in zip(*g)]]
# p=lambda g:g[:-1]+[[x.count(max(1,*x))%2*4for x in zip(*g)]]

# 58
p=lambda g:g[:-1]+[[sum(x)/max(1,*x)%2*4for x in zip(*g)]]


#
# def p(g):
#     t=[*zip(*g)]
#     for x in range(1,len(g[0])-1):
#         g[-1][x] = 4*(t[x-1]==t[x+1])
#     return g

