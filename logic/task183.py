def p(g):H,W=len(g),len(g[0]);return[[g[y][x]and g[-(y*2>=H)][-(x*2>=W)]for x in range(2,W-2)]for y in range(2,H-2)]# crop border color quadrants
