import re

def p(g):
 for _ in'00':
  g=eval(re.sub(r'([1-9])((?:, \d)+), \1',lambda m:(v:=m[1])+re.sub(r'\d',v,m[2])+', '+v,str(g)))
  g=[*zip(*g)]
 return g