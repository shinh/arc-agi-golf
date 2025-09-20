# pick the color whose row counts have the most distinct values
p=lambda g:[[max(range(1,10),key=lambda c:len({r.count(c)for r in g}))]]
