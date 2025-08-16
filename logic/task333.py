# draw lines from each colored cell toward a nearby 3
def p(g):
 for r in g:
  for j,c in enumerate(r):
   if c and c-3:
    k=j+1
    while k<10 and r[k]==0:k+=1
    if k<10 and r[k]==3:r[j+1:k]=[c]*(k-j-1)
 g=[*map(list,zip(*g[::-1]))]
 for r in g:
  for j,c in enumerate(r):
   if c and c-3:
    k=j+1
    while k<10 and r[k]==0:k+=1
    if k<10 and r[k]==3:r[j+1:k]=[c]*(k-j-1)
 g=[*map(list,zip(*g[::-1]))]
 for r in g:
  for j,c in enumerate(r):
   if c and c-3:
    k=j+1
    while k<10 and r[k]==0:k+=1
    if k<10 and r[k]==3:r[j+1:k]=[c]*(k-j-1)
 g=[*map(list,zip(*g[::-1]))]
 for r in g:
  for j,c in enumerate(r):
   if c and c-3:
    k=j+1
    while k<10 and r[k]==0:k+=1
    if k<10 and r[k]==3:r[j+1:k]=[c]*(k-j-1)
 g=[*map(list,zip(*g[::-1]))]
 return g

