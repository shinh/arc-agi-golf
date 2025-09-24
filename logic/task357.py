def p(g):# bounce
    m=len(g[0])-1
    return[[8**(j!=m-abs(~i%(m*2)-m))for j in range(-~m)]for i in range(-len(g),0)]
