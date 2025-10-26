def p(g):
 d=[sum(g[i*4+ii][j*4+jj]%5>0for ii in range(3)for jj in range(3))for i in range(3)for j in range(3)]
 return[[5*(i%4>2or j%4>2)or(sum({*sum(g,[])})-5)*(d[i//4*3+j//4]==max(d))for j in range(11)]for i in range(11)]