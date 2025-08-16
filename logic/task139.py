# fill 3x3 frame's zeros with 7
def p(g):
 for y in range(len(g)-2):
  S=g[y:y+3]
  for x in range(len(S[0])-2):
   if 4in S[0][x:x+3]and 4in S[2][x:x+3]and 4in(r[x]for r in S)and 4in(r[x+2]for r in S):
    for r in S:r[x:x+3]=[v or 7for v in r[x:x+3]]
 return g
