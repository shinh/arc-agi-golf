def p(g):
  a=len({*str(g)})-5
  return sum(([sum(zip(*[r]*a),())]*a for r in g),[])