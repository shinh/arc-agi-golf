def p(g):#two4x4s
    a=g[0][1]<3;b=g[1][0]<3;c=4*(a^b)+b;o=[9*[0]for _ in[0]*9];d=c^4
    for i in 0,1,2,3:o[a+i][c:c+4]=o[a+4+i][d:d+4]=4*[3]
    return o
