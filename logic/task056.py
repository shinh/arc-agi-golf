# center/corners decide color
# p=lambda g:[[536968>>3*sum(map(bool,(g:=sum(g,[]))[::2]+g[4:5]))&7]]
# def p(g):
#     a,b,c=g[0]
#     return [[a==b and 1 or a and 2 or c and 3 or 6]]

# 59
def p(g):
    a,b,c=g[0]
    return [[[[[6,3][c>0],2][a>0],1][a==b]]]

# p=lambda g:[[hash((g[0][1]>g[1][2],g[0][1]<g[1][0],5112))%7]]
# p=lambda g:[[hash((*map(bool,g[0]),5112))%7]]
# p=lambda g:[[(g[0]>g[1])+(g[1]<g[2])*2]]
# def p(g):
#     a,b,c=map(sum,g)
#     return [[a//b*3+b//c]]