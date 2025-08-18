def p(g):
        # surround non-unique colors with a frame including the lone cell
        h=len(g);w=len(g[0]);f=sum(g,[])
        i=[i for i,v in enumerate(f) if v and f.count(v)<2][0];u=f[i];uy,ux=divmod(i,w)
        Y,X=zip(*[divmod(i,w)for i,v in enumerate(f) if v and v!=u])
        t=min(Y);b=max(Y);l=min(X);r=max(X);B,C=g[t][l],g[t+1][l+1]
        t=min(t,uy);b=max(b,uy);l=min(l,ux);r=max(r,ux)
        return [[0 if y<t or y>b or x<l or x>r else B if y in(t,b) or x in(l,r) else C for x in range(w)]for y in range(h)]
