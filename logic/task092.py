# hv flood fill
import re;s=re.sub
def p(g):
 for _ in'00':
  g=[*zip(*eval(s(r'([1-9])(?:, \d)+, \1',lambda m:s(r'\d',m[1],m[0]),str(g))))]
 return g
