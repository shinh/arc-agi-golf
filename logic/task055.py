# [0,2,0]
# [4,6,3]
# [0,1,0]
def p(g):
    dy=0
    for y in range(len(g)):
        dx=0
        if all(c==8for c in g[y]):
            dy+=1
        else:
            for x in range(len(g[0])):
                if g[y][x]==8:
                    dx+=1
                else:
                    g[y][x]=[0,2,0,4,6,3,0,1,0][dy*3+dx]
    return g
