p = lambda g, k=23, l=1: -k * g or p(
    [
        [
            ([a | b * (a > 0), l := l * 2][a & 1], (a > 0) + (a.bit_count() == 6))[
                k < 1
            ]
            for a, b in zip(r, (*r[1:], 0))
        ]
        for r in zip(*g[::-1])
    ],
    k - 1,
)
