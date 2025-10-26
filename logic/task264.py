def p(g):
 o=[[5]*9for _ in[0]*9]
 for r in range(len(g)-2):
  for c in range(len(g[0])-2):
   if all(g[r+i//3][c+i%3]for i in range(9)):
    y=x=0
    for i in range(9):
     v=g[r+i//3][c+i%3]
     if v-5:y+=i//3-1;x+=i%3-1
    for i in range(9):
     v=g[r+i//3][c+i%3]
     if v-5:o[3*((y>=0)+(y>0))+i//3][3*((x>=0)+(x>0))+i%3]=v
 return o