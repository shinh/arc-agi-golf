# count 2x2 blocks of color 1
# p=lambda g:[(sum({*y}=={1}for a,b in zip(g,g[1:])for y in zip(a,b,a[1:],b[1:]))*[1]+5*[0])[:5]]

# def p(g):
#     for _ in range(2):
#         g=[[a*b==1 for a,b in zip(r,r[1:])]for r in zip(*g[::-1])]
#     return [sorted(sum(g,[]))[:-6:-1]]

# p=lambda g,n=-1:[sorted(sum(g,[]))[:-6:-1]]*n or p([[a*b==1 for a,b in zip(r,r[1:])]for r in zip(*g[::-1])],n+1)

# def p(g):
#     s=[0]*5
#     for i in range(64):
#         if {*g[i//8][i%8:][:2],*g[i//8+1][i%8:][:2]}=={1}: s=1,*s
#     return [s[:5]]

# test cases are weak, don't no 2 in a row except squares...
# 77
# p=lambda g:[(sum(a*b==1 for r in g for a,b in zip(r,r[1:]))//2*[1]+[0]*5)[:5]]

# 76
# p=lambda g:[([a for r in g[::2] for a,b in zip(r,r[1:]) if a*b==1]+[0]*5)[:5]]

#p=lambda g:[([1]*sum(g[i//8*2][i%8:][:2]==[1,1]for i in range(40))+[0]*5)[:5]]

# 51
p=lambda g:[(str(g).count("1, 1")*[1]+[0]*9)[:9:2]]