def p(g):b=bytes(sum(g,[]));m=len(g[0]);j=b.rfind(c:=b.strip(b'\0')[0]);i=b.find(c)-~m;return[[c*(x>0)for x in r[i%m:j%m]]for r in g[i//m:j//m]]#crop
