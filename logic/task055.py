# [0,2,0]
# [4,6,3]
# [0,1,0]
def p(g,dy=0):
    for r in g:
        dx=0
        dy+=sum(r)>16
        for x in range(len(r)):
            if r[x]:
                dx+=1
            else:
                r[x]=[0,2,0,4,6,3,0,1,0][dy*3+dx]
    return g
