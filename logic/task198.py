# 217
def p(g):
    for _ in range(80):
        g=[[[a,3,4][(a in(0,3))*(1+(a==4 or b==4 or(b==c and b in[1,2,5,6,7,8,9]) or(b==d and b in[1,2,5,6,7,8,9])))]for a,b,c,d in zip(r,[*r[1:],3],[*r[2:],3,3],[3,*r])]for r in zip(*g[::-1])]
    return g
