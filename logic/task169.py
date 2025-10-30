def p(g):
    #recolor5s
    def f(y,x,t,u):
        if 9>=y>=0<=x<=9>=g[y][x]==t:
            g[y][x]=u;return f(y+1,x,t,u)+f(y-1,x,t,u)+f(y,x+1,t,u)+f(y,x-1,t,u)+1
        return 0
    return[5==g[y][x]and f(y,x,-9,5-f(y,x,5,-9))for y in range(10)for x in range(10)]and g
