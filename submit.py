import argparse
import base64
import lzma
import os
import re
import sys
import zlib
import zopfli.zlib

from concurrent.futures import ProcessPoolExecutor

import code_golf_utils
import python_minifier

import myzlib


def write_code(code, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if isinstance(code, bytes):
        with open(filename, "wb") as f:
            f.write(code)
    else:
        with open(filename, "w") as f:
            f.write(code)


def reindent(code):
    lines = []
    cur_indent = 0
    prev_indent = 0
    indents = {}
    for line in code.splitlines():
        line = re.sub(r"#.*", "", line)
        line = line.rstrip()
        if not line:
            continue

        n = len(line) - len(line.lstrip())
        if n > prev_indent:
            cur_indent += 1
        elif n < prev_indent:
            cur_indent = indents[n]
        prev_indent = n
        indents[n] = cur_indent

        lines.append(" " * cur_indent + line.lstrip())
    return "\n".join(lines)


def squeeze(s):
    W='if for while try with class def else elif except finally'.split()
    L=s.split('\n');R=[];i=0
    while i<len(L):
        a=L[i];n=len(a)-len(a.lstrip());j=i+1;B=[];ok=1
        while j<len(L):
            c=L[j];m=len(c)-len(c.lstrip())
            if m<=n:break
            d=c.lstrip();w=d.split()
            if m>n+1 or ':'in d or w[:1]and w[0]in W:ok=0;break
            B+=[d];j+=1
        if ok and B and m<=n:R+=[a+B[0]+''.join(';'+x for x in B[1:])];i=j
        else:R+=[a];i+=1
    return'\n'.join(R)


def inline_create(code):
    return re.sub(r"create\((\w+),(\w+)\)", r"[[0]*\2 for _ in range(int(\1))]", code)


def use_base85(z):
    c = base64.b85encode(z)
    return 'base64.b85decode("' + c.decode() + '")'


def use_decompress_and_base85(z, algo):
    code = f"import base64,{algo}\n"
    code += f"exec({algo}.decompress(" + use_base85(z) + "))"
    return code


def use_decompress_and_bytes(z, algo):
    code = b"#coding:l1\n"
    code += f"import {algo}\n".encode()
    r = bytearray()
    i = 0
    while i < len(z):
        c = z[i]
        if c == 92:
            r += b"\\\\"
        elif c == 0:
            n = z[i + 1:i + 2]
            r += b"\\x00" if n and 48 <= n[0] <= 57 else b"\\0"
        elif c == 10:
            r += b"\\n"
        elif c == 13:
            r += b"\\r"
        elif c == 39:
            r += b"\\'"
        else:
            r.append(c)
        i += 1
    b = b"bytes('" + bytes(r) + b"','l1')"
    code += f"exec({algo}.decompress(".encode() + b + b"))"
    return code


def use_decompress_and_bytes_or_base85(z, algo):
    b1 = use_decompress_and_bytes(z, algo)
    b2 = use_decompress_and_base85(z, algo)
    if len(b1) < len(b2):
        return b1, "bytes"
    else:
        return b2, "base85"


def compress(code, algo="zlib"):
    method = algo
    if algo == "zlib":
        z1 = zlib.compress(code.encode(),9)
        #z2 = zopfli.zlib.compress(code.encode())
        z2 = zopfli.zlib.compress(
            code.encode(),
            numiterations=1000,
            blocksplitting=True,
            blocksplittinglast=False,
            blocksplittingmax=100
        )
        if len(z2) < len(z1):
            method = "zopfli"
            z1 = z2

        main, enc_method = use_decompress_and_bytes_or_base85(z1, "zlib")
    elif algo == "lzma":
        filters = [{
            "id": lzma.FILTER_LZMA1,
            "preset": 9 | lzma.PRESET_EXTREME,
        }]
        #compressed = base64.b85encode(lzma.compress(code.encode(),format=lzma.FORMAT_RAW,filters=filters))
        z = lzma.compress(code.encode(),format=2)

        main, enc_method = use_decompress_and_bytes_or_base85(z, "lzma")

    method += "+" + enc_method

    return main, method


def compress_code_impl(code, algo, seed):
    code = myzlib.map_identifiers(code, ["p"], seed=seed)
    rename_locals = False
    #rename_locals = True
    #print(code, flush=True)

    code = python_minifier.minify(
        code,
        rename_locals=rename_locals,
        # TODO: Consider enabling this for non-LZ tasks.
        hoist_literals=False,
    )
    code = code.replace("\t", " ")

    info = algo
    if algo == "asis":
        compressed_code = code
    else:
        compressed_code, info = compress(code, algo)

    info += f"+seed{seed}"

    return len(compressed_code), compressed_code, code, info


def compress_code(code):
    results = []
    for algo in ["asis", "zlib", "lzma"]:
        for seed in range(30):
            if seed and algo == "asis":
                break
            r = compress_code_impl(code, algo, seed)
            # print(r[-1], r[0])
            results.append(r)
            #if isinstance(r[1], bytes) and b"\\" not in r[1]:
            #    break
    results.sort(key=lambda a:a[0])

    size, compress_code, code, info = results[0]
    return compress_code, code, info


def check_task(task_id, filename, verbose):
    if verbose:
        print(f"Checking === {filename} ===", flush=True)

    if not os.path.exists(filename):
        return False, "TODO", None

    kind = os.path.basename(os.path.dirname(filename))
    basedir = os.path.join("/tmp", kind)

    os.makedirs(basedir, exist_ok=True)

    result = "N/A"
    ok = False

    logic = open(filename).read()
    code = inline_create(logic)
    #code = reindent(code)
    #code = squeeze(code)

    code, orig_code, info = compress_code(code)

    if len(code) >= len(orig_code):
        assert len(code) == len(orig_code)
        print(f"Task {task_id} not compressed: {len(code)} bytes", flush=True)
    else:
        print(f"Task {task_id} compressed: {len(orig_code)} -> {len(code)} bytes ({info})", flush=True)

    write_code(orig_code, f"stages/task{task_id:03d}.py")
    task_path = f"{basedir}/task{task_id:03d}.py"
    write_code(code, task_path)

    try:
        examples = code_golf_utils.load_examples(int(task_id))
        if code_golf_utils.verify_program(task_id, examples, task_path, quiet=not verbose):
            result = str(2500 - len(code))
            ok = True
        else:
            result = "FAIL"
    except Exception as e:
        if verbose:
            raise
        result = "ERROR"

    return ok, result, code


def submit(task_id, verbose, skip_verify=False, code_dir="logic"):
    if skip_verify:
        return

    # print("Submitting task", task_id)

    ok, result, code = check_task(task_id, f"{code_dir}/task{task_id:03d}.py", verbose)

    # dsl_filename = f"dsl/task{task_id:03d}.py"
    # if os.path.exists(dsl_filename) and os.path.getsize(dsl_filename) < 4000:
    #     ok_c, result_c, code_c = check_task(task_id, dsl_filename, verbose)
    #     lc = len(code_c)
    #     if ok_c and (not ok or lc < len(code_c)) and len(code_c) < 2500:
    #         ok = ok_c
    #         result = result_c + " (" + result + ")"
    #         code = code_c

    open(f"reports/task{task_id:03d}.txt", "w").write(result)
    if code:
        write_code(code, f"submissions/task{task_id:03d}.py")

    print(f"Task {task_id:03d}: {result}", flush=True)

    return ok


def report():
    score = 0
    fail_tests = []
    error_tests = []
    todo_tests = []
    negative_tests = []
    for task_id in range(1, 401):
        result = open(f"reports/task{task_id:03d}.txt").read()
        result = result.split()[0]
        if result == "FAIL":
            fail_tests.append(task_id)
        elif result == "ERROR":
            error_tests.append(task_id)
        elif result == "TODO":
            todo_tests.append(task_id)
        else:
            score += int(result)
            if int(result) < 0:
                negative_tests.append(task_id)
    print(f"Failed tests: {len(fail_tests)} {list(sorted(fail_tests))}")
    print(f"Error tests: {error_tests}")
    print(f"TODO tests: {len(todo_tests)} {list(sorted(todo_tests))}")
    if negative_tests:
        print(f"Negative tests: {len(negative_tests)} {list(sorted(negative_tests))}")
    print(f"Total score: {score}")


def main():
    parser = argparse.ArgumentParser(description="Submit code golf.")
    parser.add_argument("task_id")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--skip_verify", action="store_true")
    parser.add_argument("--code_dir", default="logic")
    args = parser.parse_args()

    if args.task_id == "all":
        executor = ProcessPoolExecutor()
        futures = []
        for task_id in range(1, 401):
            futures.append(executor.submit(submit, task_id, args.verbose, args.skip_verify, code_dir=args.code_dir))
        for future in futures:
            future.result()
        report()
    else:
        if not submit(int(args.task_id), True, code_dir=args.code_dir):
            print("FAIL!!")
            sys.exit(1)


if __name__ == "__main__":
    main()
