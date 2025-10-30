import re

p = lambda g, k=3: -k * g or (
    p(
        eval(
            re.sub(
                r"(0)(?=.{%d}(?:.{%d}){0,9}([1-9]).{2}\2.{%d}\2.{2}0.{%d}([1-9]))"
                % (len(g) * 3 + 4, len(g) * 3 + 5, len(g) * 3 - 2, len(g) * 3 + 4),
                r"\3",
                str([*zip(*g[::-1])]),
            )
        ),
        k - 1,
    )
)
