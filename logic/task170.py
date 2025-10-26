def p(g):
  b=bytes(map(any,g));r=b.rfind(1);B=bytes(map(bool,g[r]));a=B.find(1);B=B.rfind(1)-a+1;d=g[r-B+1:r+1];x=[u[a:a+B]for u in d];b=[0]*B
  for u in d:u[a:a+B]=b
  b=bytes(map(any,g));C=b.find(1);r=b.rfind(1);a=bytes(map(any,zip(*g))).find(1);s=(r-C+1)//B;return[[g[C+i*s][a+j*s]and x[i][j]for j in range(B)]for i in range(B)]
