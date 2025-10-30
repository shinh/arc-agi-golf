def p(g):return (r:=[(d:=max(s[:9],s[10:19],s[~8:]))+([4]+d)*s.count(4)for s in map(max,g,g[10:])])+[g[9]]+r
