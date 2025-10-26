def p(g):
  b=bytes(map(any,g));r=b.rfind(1);b=bytes(map(bool,g[r]));a=b.find(1);B=b.rfind(1)-a+1;y=r-B+1;R=range(B);x=[g[y+i][a:a+B]for i in R];b=[0]*B
  for i in R:g[y+i][a:a+B]=b
  b=bytes(map(any,g));C=b.find(1);r=b.rfind(1);a=bytes(map(any,zip(*g))).find(1);s=(r-C+1)//B;return[[g[C+i*s][a+j*s]and x[i][j]for j in R]for i in R]
