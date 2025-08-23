def p(g):# bounce
    h=len(g);m=len(g[0])-1
    return[[8**(j!=m-abs((h+~i)%(m*2)-m))for j in range(-~m)]for i in range(h)]
