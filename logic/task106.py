# tile grid with rotations
p=lambda g,r=lambda x:[*map(list,zip(*x[::-1]))]:(h:=[*map(list.__add__,g,r(g))])+r(r(h))
