def p(m):
  f={int(max("123456789",key=str(m).count))}.intersection
  return [*zip(*filter(f,zip(*filter(f,m))))]