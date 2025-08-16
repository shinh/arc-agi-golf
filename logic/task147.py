# recolor any 3 touching another 3 to 8
def p(g):
        s={(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==3}
        for y,x in s:
                if {(y+1,x),(y-1,x),(y,x+1),(y,x-1)}&s:g[y][x]=8
        return g

