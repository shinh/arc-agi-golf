# center/corners decide color
# p=lambda g:[[536968>>3*sum(map(bool,(g:=sum(g,[]))[::2]+g[4:5]))&7]]
# def p(g):
#     a,b,c=g[0]
#     return [[a==b and 1 or a and 2 or c and 3 or 6]]

# 59
# def p(g):
#     a,b,c=g[0]
#     return [[[[[6,3][c>0],2][a>0],1][a==b]]]

# p=lambda g:[[hash((g[0][1]>g[1][2],g[0][1]<g[1][0],5112))%7]]
# p=lambda g:[[hash((*map(bool,g[0]),5112))%7]]
# p=lambda g:[[(g[0]>g[1])+(g[1]<g[2])*2]]
# def p(g):
#     a,b,c=map(sum,g)
#     return [[a//b*3+b//c]]

# 49
# def p(g):
#     a,b,c=g
#     return [[6*(a<b)+2*(b<c)+(a!=c)]]

# p=lambda g:[[sum(g[2])//sum(g[0])*2+g[1][0]]]

#
# 6*(a<b)+2*(b<c)+(a!=c)
# ((a<b)+(2*b>c)-1)%7+1
# (a<b)*2+(c>b)or 6

# (g[1][1]*2+g[0][1])//30or 6

# 45
# p=lambda g:[[(g[0]!=g[2])+2*(g[1]<g[2])or 6]]
#            len({*g})   [:2],etc   3 2 2 2    %3 -> 0 2 2 2
#                        [::2]      2 1 2 1
#            (g>[[1]])              1 1 1 0
#            (g>[g[0]])   1 2 inferior to ranges
#            (g>g[::-1])  -2,2       > = < =
#            (g>g[1:])          >1:  1 1 0 0
#                               >2:  1 1 0 1
#                               >::2 1 0 0 1
#            0**g[1][2]
#            (g.pop()in g)
#            (g[2]==g[0])
#            (g!=g[::-1])
#            {*g}<{g[0]}

# 42
# p=lambda g:[[3**(g<g[1:])*-~(g==g[::-1])]]
#            (g<g[1:]or-3)

# 41
p=lambda g:[[(g<g[::2])*3^(g>g[1:])or 6]]