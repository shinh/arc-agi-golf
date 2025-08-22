# infer tile with setdefault
p=lambda g:next([[d.get((y%k,x%k),0)for x in range(18)]for y in range(18)]for k in range(1,19)if(d:={}) or all(d.setdefault((y%k,x%k),v)==v for y,r in enumerate(g) for x,v in enumerate(r) if v))
