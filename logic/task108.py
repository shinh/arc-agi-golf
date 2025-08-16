def p(g,t=(0,2,4,6,8)):
    # get max of each 2x2 block then upscale by 4
    return sum([[sum([[max(g[i][j:j+2]+g[i+1][j:j+2])]*4 for j in t],[])]*4 for i in t],[])
