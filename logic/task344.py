# swap 2 next to 3 with 0 and 8
def p(g):
 for _ in'00':
  for r in g:
   r[:]=map(int,''.join(map(str,r)).replace('23','08').replace('32','80'))
  g=[*map(list,zip(*g))]
 return g
