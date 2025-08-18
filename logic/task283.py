def p(g):#frame 5-rect via set
 s={(x,y)for y,r in enumerate(g)for x,v in enumerate(r)if v>4}
 for x,y in s:g[y][x]=[1,4,2][len(s&{(x+1,y),(x-1,y),(x,y+1),(x,y-1)})-2]
 return g
