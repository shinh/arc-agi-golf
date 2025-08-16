# fill zeros in a 3x3 window whose sides contain 4
def p(g,O=range):
 for y in O(len(g)-2):
  R=g[y:y+3]
  for x in O(len(g[0])-2):
   if all(4 in i for i in[R[0][x:x+3],R[2][x:x+3],[r[x]for r in R],[r[x+2]for r in R]]):
    for r in R:
     for b in O(x,x+3):r[b]=r[b] or 7
 return g
