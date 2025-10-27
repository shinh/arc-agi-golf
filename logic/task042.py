def p(g):
 # extend arms
 for i in range(10):
  for j in range(10):
   if 3==g[i][j]:
    m=1
    while i+m<10 and 3==g[i+m][j]:m+=1
    for i in range(10):
     for j in range(10):
      if 3==g[i][j]:
       for s in-1,1:
        if-1<i+m<10>j+s*m>-1 and 3==g[i+m][j+s*m]:
         if-1<i-m<10>j+2*s*m>-1:g[i-m][j+2*s*m]=8
         if-1<i+2*m<10>j-s*m>-1:g[i+2*m][j-s*m]=8
    return g
