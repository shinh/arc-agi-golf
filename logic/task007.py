def p(g):
    # fill diagonals with last seen color
    c=[0]*3;i=0
    for v in sum(g,[]):c[i]=v or c[i];i=-~i%3
    return[(c*3)[i:][:7]for i in[0,1,2]*3][:7]
