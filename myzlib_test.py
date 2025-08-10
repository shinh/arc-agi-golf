import myzlib


code = r"""def p(g):
 b=max(g[0],key=g[0].count)
 R=range
 for a in R(3):
  for b in R(3):
   if sum(g[a*4+r][b*4+c]==0for r in R(3)for c in R(3))==5:
    s=[[5if i%4==3or j%4==3else 0for j in R(11)]for i in R(11)]
    return s
"""


def test_get_identifier_positions():
    positions = myzlib.get_identifier_positions(code)
    assert [p.name for p in positions] == [
        "p", "g", "b", "max", "g", "count", "g", "R", "range", "a", "R", "b", "R", "sum", "g", "a", "r", "b", "c", "r", "R", "c", "R", "s", "i", "j", "j", "R", "i", "R", "s"
    ]


def test_exclude_reserved_names():
    positions = myzlib.get_identifier_positions(code)
    positions = myzlib.exclude_reserved_names(positions)
    print(positions)
    assert [p.name for p in positions] == [
        "p", "g", "b", "g", "g", "R", "a", "R", "b", "R", "g", "a", "r", "b", "c", "r", "R", "c", "R", "s", "i", "j", "j", "R", "i", "R", "s"
    ]
