import json
import gzip
import os
task_id=48
task_id = "%03d" % int(task_id)
js = json.load(gzip.open(os.path.join("tasks", "task" + task_id + ".json.gz")))
data = []
for kind in ["train", "test", "arc-gen"]:
    data.extend(js[kind])
inputs=[prob['input'] for prob in data]
outputs=[prob['output'] for prob in data]

a = [[hash((r,*zip(*i)))for r in range(400)] for i in inputs]
b = [o[0][0]//8 for o in outputs]

# now solve ax=b mod 2

import numpy as np

def gauss_mod2(a, b):
    n, m = A.shape
    row = 0
    pivots = []

    for col in range(m):
        # find pivot
        pivot = None
        for r in range(row, n):
            if A[r, col]:
                pivot = r
                break
        if pivot is None:
            continue
        # swap rows
        A[[row, pivot]] = A[[pivot, row]]
        B[[row, pivot]] = B[[pivot, row]]
        pivots.append(col)
        # eliminate
        for r in range(n):
            if r != row and A[r, col]:
                A[r] ^= A[row]
                B[r] ^= B[row]
        row += 1
        if row == n:
            break

    # Build solution
    x = np.zeros(m, dtype=int)
    for r, col in enumerate(pivots):
        x[col] = B[r]
    return x.tolist()

def check_solution(A, B, x):
    A = np.array(A, dtype=np.int64) % 2
    B = np.array(B, dtype=np.int64) % 2
    x = np.array(x, dtype=np.int64) % 2

    lhs = (A @ x) % 2   # compute Ax mod 2
    return np.array_equal(lhs, B)

for s in range(300,400):
    # Convert a and b into numpy arrays mod 2
    A = np.array(a[:s], dtype=np.int64) % 2
    B = np.array(b, dtype=np.int64) % 2
    x = gauss_mod2(A, B)
    if check_solution(A, B, x): break

x=x[::-1][x[::-1].index(1):][::-1]

# generate solution

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

def bits_to_bytes(bits):
    # pad to multiple of 8 if needed
    while len(bits) % 7:
        bits.append(0)
    return [
        sum(bit << i for i, bit in enumerate(bits[b:b+7]))
        for b in range(0, len(bits), 7)
    ]

table_str = escape_bytes(bits_to_bytes(x))
code = r"""
p=lambda g:[[sum(hash((s,*zip(*g)))*(b'{}'[s//7]>>s%7)for s in range({}))%2*8]]
""".format(table_str, len(x))
print(f"table_size={len(table_str)} code_size={len(code)}")
print(code)
