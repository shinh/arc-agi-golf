# extend colors to 3
def p(g):
 for _ in[0]*4:
  for r in g:
   for j in range(9):
    if 0<r[j]!=3:
     k=j+1
     while k<9>=r[k]<1:k+=1
     if k<10>r[k]==3:r[j+1:k]=[r[j]]*(k+~j)
  g=[*map(list,zip(*g[::-1]))]
 return g

