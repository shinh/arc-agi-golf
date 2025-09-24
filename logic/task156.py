#
def p(g):
    # skip non-top-left 4s and fill rectangles in ascending area order
    k=0
    for s in range(60):
        for y in range(10):
            for x in range(10):
                #
                #
                if g[y][x]-4:continue
                if y and g[y-1][x]==4:continue
                if x and g[y][x-1]==4:continue
                h=w=1
                while y+h<10 and g[y+h][x]==4:h+=1
                while x+w<10 and g[y][x+w]==4:w+=1
                if h*w==s:
                    k+=1
                    for r in g[y+1:y+h-1]:r[x+1:x+w-1]=[k]*(w-2)
    return g
