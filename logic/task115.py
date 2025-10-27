# unique colors row or column
p=lambda g,f={}.fromkeys:(a:=f(sum(g,[])))and([*zip(a)],[[*a]])[a==f(g[0])]
