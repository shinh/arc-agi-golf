p = lambda g, t=3: (
    -t*g
    or p(
        [
            (f := 0)
            or [
                [[c, 8][2 > f > c], f := f + 1 if c == 5 and (d < 4 or f > 0) else f][0]
                for d, c in enumerate(r)
            ]
            for r in zip(*g[::-1])
        ],
        t - 1,
    )
)
