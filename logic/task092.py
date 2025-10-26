import re
# flood-fill between matching digits horizontally and vertically via transposes
def p(g):
 for _ in'00':
  g=eval(re.sub(r'([1-9])((?:, \d)+), \1',lambda m:re.sub(r'\d',m[1],m[0]),str(g)))
  g=[*zip(*g)]
 return g
