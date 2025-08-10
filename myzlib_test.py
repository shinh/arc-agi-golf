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
    assert [p.name for p in positions] == [
        "p", "g", "b", "g", "g", "R", "a", "R", "b", "R", "g", "a", "r", "b", "c", "r", "R", "c", "R", "s", "i", "j", "j", "R", "i", "R", "s"
    ]


def test_exclude_ranges():
    positions = myzlib.get_identifier_positions(code)
    positions = myzlib.exclude_reserved_names(positions)
    chunks = myzlib.exclude_ranges(code, positions)
    print(chunks)
    assert chunks == [
        'def ',
        '(',
        '):\n ',
        '=max(',
        '[0],key=',
        '[0].count)\n'
        ' ',
        '=range\n'
        ' for ',
        ' in ',
        '(3):\n'
        '  for ',
        ' in ',
        '(3):\n'
        '   if sum(',
        '[',
        '*4+',
        '][',
        '*4+',
        ']==0for ',
        ' in ',
        '(3)for ',
        ' in ',
        '(3))==5:\n'
        '    ',
        '=[[5if ',
        '%4==3or ',
        '%4==3else 0for ',
        ' in ',
        '(11)]for ',
        ' in ',
        '(11)]\n'
        '    return ',
        '\n',
    ]
