import ast
import glob
import pytest

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


def test_minify_all_solutions():
    for py in glob.glob("logic/*.py"):
        code = open(py).read()
        minified = myminifier.minify(code)
        ast.parse(minified)


def test_remove_semicolons():
    assert myminifier.remove_semicolons("a=1;b=2;c=3") == "a=1\nb=2\nc=3"
    assert myminifier.remove_semicolons("if a:b=2;c=3") == "if a:\n b=2\n c=3"
    assert myminifier.remove_semicolons("if a:\n b=2;c=3") == "if a:\n b=2\n c=3"


def test_remove_spaces_ignores_strings():
    # remove_spaces should not touch contents of string literals
    src = "a='1 + 2'; b + c"
    assert myminifier.remove_spaces(src) == "a='1 + 2';b+c"


def test_replace_unpacking_funcs_handles_nested():
    # ensure list() and set() become unpacking
    f=myminifier.replace_unpacking_funcs
    assert f("list(a)")=="[*a]"
    assert f("list(map(all,a))")=="[*map(all,a)]"
    assert f("set(a)")=="{*a}"
    assert f("set(map(all,a))")=="{*map(all,a)}"
    assert f("set()")=="set()"


def test_replace_unpacking_funcs_skips_strings():
    # should skip if argument has string literal
    f=myminifier.replace_unpacking_funcs
    with pytest.warns(UserWarning):
        assert f('list(")")')=='list(")")'
    with pytest.warns(UserWarning):
        assert f('set("(")')=='set("(")'
    with pytest.warns(UserWarning):
        assert f("list(')')")=="list(')')"
    with pytest.warns(UserWarning):
        assert f("set('(')")=="set('(')"


def test_bundle_and_expand_assignments():
    """Bundling should combine lines and expansion should restore them."""
    src = (
        "a=1\n"
        "b=2\n"
        "if 1:\n"
        "    x=3\n"
        "    y=4\n"
        "    z=5\n"
        "c=6"
    )
    bundled = myminifier.bundle_assignments(src)
    assert bundled == (
        "a,b=1,2\n"
        "if 1:\n"
        "    x,y,z=3,4,5\n"
        "c=6"
    )
    assert myminifier.expand_assignments(bundled) == src


def test_expand_assignments_handles_internal_commas():
    # values containing commas inside brackets should be preserved
    src = "a,b=[1,2],[3,4]"
    assert myminifier.expand_assignments(src) == "a=[1,2]\nb=[3,4]"
