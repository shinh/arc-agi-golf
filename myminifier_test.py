import myminifier


def test_merge_indented_blocks():
    src = (
        "def p(g):\n"
        "    a=g[0][0];h=sum(a not in r for r in g)+1;"
        "w=sum(a not in c for c in zip(*g))+1;"
        "return[[a]*w for _ in range(h)]"
    )
    expected = (
        "def p(g):a=g[0][0];h=sum(a not in r for r in g)+1;"
        "w=sum(a not in c for c in zip(*g))+1;"
        "return[[a]*w for _ in range(h)]"
    )
    assert myminifier.merge_indented_blocks(src) == expected


def test_combine_adjacent_lines_simple():
    src = "a=1\nb=2\nc=3"
    assert myminifier.combine_adjacent_lines(src) == "a=1;b=2;c=3"


def test_merge_handles_internal_colons():
    src = (
        "def p(g):\n"
        " y=min(i for i,r in enumerate(g)if any(r));"
        "x=min(i for i in range(10)if any(r[i]for r in g));"
        "return[r[x:x+3]for r in g[y:y+3]]"
    )
    expected = (
        "def p(g):y=min(i for i,r in enumerate(g)if any(r));"
        "x=min(i for i in range(10)if any(r[i]for r in g));"
        "return[r[x:x+3]for r in g[y:y+3]]"
    )
    assert myminifier.merge_indented_blocks(src) == expected


def test_merge_handles_slice():
    src = "def p(g):\n b=g[-5:];return b[::-1]+b"
    expected = "def p(g):b=g[-5:];return b[::-1]+b"
    assert myminifier.merge_indented_blocks(src) == expected

