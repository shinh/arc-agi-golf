# pick rare 2x2 quadrant
p=lambda g:min(a:=[(g[y][x:x+2],g[y+1][x:x+2])for y in(0,3)for x in(0,3)],key=a.count)
