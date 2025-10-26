def p(g):
  b=bytes(map(any,g));r=len(g)-1-b[::-1].find(1)
  R=g[r];B=bytes(map(bool,R));a=B.find(1);h=len(R)-B[::-1].find(1)-a
  x=[u[a:a+h]for u in g[r-h+1:r+1]]
  for u in g[r-h+1:r+1]:u[a:a+h]=[0]*h
  b=bytes(map(any,g));C=b.find(1);Y=len(g)-1-b[::-1].find(1)
  A=bytes(map(any,zip(*g))).find(1);s=(Y-C+1)//h
  return [[g[C+i*s][A+j*s]and x[i][j]for j in range(h)]for i in range(h)]