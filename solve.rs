// Union-Find (Disjoint Set Union) implementation

struct UnionFind {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self { parent: (0..n).collect(), size: vec![1; n] }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] == x { x } else {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
            root
        }
    }
    fn union(&mut self, a: usize, b: usize) -> bool {
        let mut a = self.find(a);
        let mut b = self.find(b);
        if a == b { return false; }
        if self.size[a] < self.size[b] { std::mem::swap(&mut a, &mut b); }
        self.parent[b] = a;
        self.size[a] += self.size[b];
        true
    }
    fn same(&mut self, a: usize, b: usize) -> bool {
        self.find(a) == self.find(b)
    }
    fn comp_size(&mut self, x: usize) -> usize {
        let r = self.find(x);
        self.size[r]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn singletons_are_separate() {
        let mut uf = UnionFind::new(3);
        assert!(!uf.same(0, 1));
        assert_eq!(uf.comp_size(2), 1);
    }

    #[test]
    fn unions_connect_components() {
        let mut uf = UnionFind::new(5);
        assert!(uf.union(0, 1));
        assert!(uf.same(0, 1));
        assert!(uf.union(1, 2));
        assert!(uf.same(0, 2));
        assert_eq!(uf.comp_size(0), 3);
    }

    #[test]
    fn union_returns_false_when_already_connected() {
        let mut uf = UnionFind::new(4);
        uf.union(1, 2);
        assert!(!uf.union(2, 1));
        assert_eq!(uf.comp_size(1), 2);
    }
}
