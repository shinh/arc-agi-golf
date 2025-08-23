def p(g):#frame 5-rect via set
 s={(i%10,i//10)for i,v in enumerate(sum(g,[]))if v>4}
 for x,y in s:g[y][x]=len(s&{(x+1,y),(x-1,y),(x,y+1),(x,y-1)})*3%5
 return g
