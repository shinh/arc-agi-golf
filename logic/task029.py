# Just solved.
#
# Test cases are somewhat tough. There are tasks which assume 1px output like
#
# 111
# 121
# 111
#
# and and another task contains both the above pattern and a larger pattern.
def p(g):
    m=[]
    for sy in range(1,len(g)-1):
        for sx in range(1,len(g[0])-1):
            for ey in range(sy,len(g)-1):
                for ex in range(sx,len(g[0])-1):
                    if{g[sy][sx-1]}=={*g[sy-1][sx-1:ex+2],*g[ey+1][sx-1:ex+2],g[sy][ex+1],*[g[y][sx-1]for y in range(sy-1,ey+2)]}:
                        m+=[r[sx:ex+1]for r in g[sy:ey+1]],
    return max(m,key=lambda x:len(x))
