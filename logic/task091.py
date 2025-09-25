# def p(g):y,x=zip(*(divmod(i,len(g[0]))for i,v in enumerate(sum(g,[]))if v==5));return[r[min(x):max(x)+1]for r in g[y[0]-(y[0]>0):y[-1]+2]]

# def p(g):
#     a=sum(g,[])
#     first=a.index(5)
#     last=len(a)-1-a[::-1].index(5)
#     n=len(g[0])
#     return [y[first%n:last%n+1]for y in g[first//n-1:last//n+2]]


# def p(g):
#     for i in range(4):
#         g=[*zip(*g[::-1])]
#         a=sum(map(list,g),[])
#         n=len(g[0])
#         first=a.index(5)//n
#         g=g[first-i%2:]
#     return g

# def p(g):
#     for i in range(4):
# #         first=min((r+[5]).index(5)for r in g)
#         g=[*map(list,zip(*g[::-1]))]
#         first=sum(g,[]).index(5)//len(g[0])
#         g=g[first-i%2:]
#     return g

# def p(g):
#     for i in range(80):
#         g=[*map(list,zip(*g[::-1]))]
#         if 5 not in g[i%2]: g=g[1:]
#     return g
#
# def p(g):
#     for i in range(80):
#         g=[*zip(*g[::-1])]
#         g=g[(5in g[i%2])<1:]
#     return g

#
# def p(g):
#     for i in range(1,81):
#         g=[*zip(*g[(5in g[i%2])<1:][::-1])]
#     return g

# 68
# p=lambda g,i=80:i and p([*zip(*g[(5in g[i%2^1])<1:][::-1])],i-1)or g

# 64
p=lambda g,i=-79:g*i or p([*zip(*g[(5in g[i%2])<1:][::-1])],i+1)
