def p(g):
    # paint interior of smallest and largest rectangles of 4
    r=[]
    for y in range(10):
        for x in range(10):
            if g[y][x]==4 and (y<1 or g[y-1][x]-4) and (x<1 or g[y][x-1]-4):
                h=w=1
                while y+h<10 and g[y+h][x]==4:h+=1
                while x+w<10 and g[y][x+w]==4:w+=1
                r+=[(h*w,y,x,h,w)]
    for k,(a,y,x,h,w) in enumerate((min(r),max(r)),1):
        for i in range(y+1,y+h-1):
            g[i][x+1:x+w-1]=[k]*(w-2)
    return g
