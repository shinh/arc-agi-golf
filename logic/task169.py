def p(g):
    #recolor5s
    def f(y,x,t,u):
        if 9>=y>=0<=x<=9>=g[y][x]==t:
            g[y][x]=u;return 1+f(y+1,x,t,u)+f(y-1,x,t,u)+f(y,x+1,t,u)+f(y,x-1,t,u)
        return 0
    return[g[y][x]==5and f(y,x,-99,5-f(y,x,5,-99))for y in range(10)for x in range(10)]and g
