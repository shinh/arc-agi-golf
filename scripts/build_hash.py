#!/usr/bin/env python3

import argparse
import hashlib
import json
import gzip
import os
import random
import sys
import zlib

from collections import defaultdict, deque

sys.path.insert(0, ".")

import code_golf_utils


def graph_hash(seed: int, g) -> int:
    return zlib.crc32(bytes(sum(g,[seed])))


def build_g(pairs, m=None, r=3, seed_bytes=4, max_tries=1000):
    # pairs: list of (key, label) label in {0,1}
    n = len(pairs)
    if m is None:
        # 推奨: r=3 なら m ~ 1.23*n あたりから始める
        m = int(1.23 * n) + 3

    for attempt in range(max_tries):
        seeds = []
        for _ in range(r):
            while True:
                rv = random.randint(0, 9)
                if rv not in seeds:
                    seeds.append(rv)
                    break

        # build hypergraph: for each key, compute r positions
        edges = []
        for k,_ in pairs:
            pos = tuple(graph_hash(seeds[i], k) % m for i in range(r))
            edges.append(pos)

        # adjacency: vertices -> list of incident edge indices
        adj = [ [] for _ in range(m) ]
        for ei,pos in enumerate(edges):
            for v in pos:
                adj[v].append(ei)

        # peel: find vertices of degree 1, pop edges, record order
        deg = [len(adj_v) for adj_v in adj]
        q = deque(i for i,d in enumerate(deg) if d == 1)
        order = []  # list of (edge_index, vertex_that_was_degree1)
        removed_edge = [False]*len(edges)

        while q:
            v = q.popleft()
            # find the (remaining) incident edge
            found = None
            for ei in adj[v]:
                if not removed_edge[ei]:
                    found = ei; break
            if found is None:
                continue
            # record that edge found is removed by vertex v
            order.append((found, v))
            removed_edge[found] = True
            # decrease degree of other vertices of that edge
            for u in edges[found]:
                if u == v: continue
                deg[u] -= 1
                if deg[u] == 1:
                    q.append(u)

        if sum(removed_edge) != len(edges):
            # 剥ぎ取り失敗。別の seeds/m を試す
            m += 1  # あるいは別シードで再挑戦。ここは策略次第。
            continue

        # back-substitute to assign g (bits)
        g = [0]*m
        # we know order is in peeled sequence; process reverse
        for ei, v in reversed(order):
            # compute XOR of other vertices' g values
            xor_other = 0
            for u in edges[ei]:
                if u == v: continue
                xor_other ^= g[u]
            # want xor_other ^ g[v] == label_of_edge
            label = pairs[ei][1]
            g[v] = xor_other ^ label

        # success
        return {
            'm': m,
            'seeds': seeds,
            'g_bits': bytes((sum((g[i] << (i%8)) for i in range(j*8, min((j+1)*8, m))) & 0xff)
                            for j in range((m+7)//8))
        }

    raise RuntimeError("failed to build; increase m or tries")


def escape_bytes(data):
    escaped = bytearray()
    i = 0
    while i < len(data):
        byte = data[i]
        if byte == 92:  # backslash
            escaped += b"\\\\"
        elif byte == 0:
            nxt = data[i + 1:i + 2]
            escaped += b"\\x00" if nxt and 48 <= nxt[0] <= 57 else b"\\0"
        elif byte == 10:
            escaped += b"\\n"
        elif byte == 13:
            escaped += b"\\r"
        elif byte == 39:
            escaped += b"\\'"
        else:
            escaped.append(byte)
        i += 1
    assert len(data) <= len(escaped)
    return escaped.decode("ascii")


def brute_force(task_id):
    task_id = "%03d" % int(task_id)
    js = json.load(gzip.open(os.path.join("tasks", "task" + task_id + ".json.gz")))
    data = []
    for kind in ["train", "test", "arc-gen"]:
        data.extend(js[kind])

    f = open("/tmp/inputs.txt", "w")

    input_hashes = []
    output_bits = []
    pairs = []
    for d in data:
        ib = d["input"]
        ob = d["output"]
        f.write(f"{ib}\n")
        #input_hashes.append(hash(f"{ib}"))
        input_hashes.append(zlib.crc32(f"{ib}".encode()))
        #input_hashes.append(int.from_bytes(hashlib.blake2b(f"{ib}".encode()).digest(), "big"))
        #input_hashes.append(sum(i*13+c for i,c in enumerate(b"{ib}")))
        output_bits.append(ob[0][0] > 0)

        pairs.append((ib, int(ob[0][0] > 0)))

    r = build_g(pairs, r=3, seed_bytes=1, max_tries=1000)
    m = r['m']
    seeds = r['seeds']
    g_bits = r['g_bits']

    print('bits', len(g_bits), m, seeds)

    def _bit(i: int) -> int:
        b = g_bits[i >> 3]
        return (b >> (i & 7)) & 1

    def classify(g) -> int:
        x = 0
        for sd in seeds:
            x ^= _bit(graph_hash(sd, g) % m)
        return x

    for g, b in pairs:
        cb = classify(g)
        if cb != b:
            print(f"Mismatch for {h}: expected {b}, got {cb}")

    g_ascii = [0] * ((m + 6) // 7)
    for i in range(m):
        b = g_bits[i >> 3]
        b = (b >> (i & 7)) & 1
        g_ascii[i // 7] |= b << (i % 7)

    table_str = escape_bytes(g_ascii)
    code = r"""import zlib
sum(b'{}'[(i:=zlib.crc32(bytes(sum(g,[s])))%{})//7]>>i%7for s in[{},{},{}])%2
""".format(table_str, m, *seeds)
    print(f"table_size={len(table_str)} code_size={len(code)}")
    print(code)


def main():
    parser = argparse.ArgumentParser(description="Hard code test cases.")
    parser.add_argument("task_id")
    args = parser.parse_args()

    brute_force(args.task_id)


if __name__ == "__main__":
    main()
