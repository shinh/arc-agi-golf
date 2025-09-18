import argparse
import base64
import lzma
import bz2
import os
import re
import sys
import warnings
import zlib
import zopfli.zlib

from concurrent.futures import ProcessPoolExecutor

import code_golf_utils
import python_minifier

import myzlib
import myminifier


def write_code(code, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if isinstance(code, bytes):
        with open(filename, "wb") as f:
            f.write(code)
    else:
        with open(filename, "w") as f:
            f.write(code)


def inline_create(code):
    return re.sub(r"create\((\w+),(\w+)\)", r"[[0]*\2 for _ in range(int(\1))]", code)


def base85_literal(data):
    """Return a code snippet that decodes the given data using base85."""
    encoded = base64.b85encode(data).decode()
    return f'base64.b85decode("{encoded}")'


def build_decompression_snippet_base85(data, algorithm, args):
    """Create source code that decompresses base85-encoded data."""
    code = f"import base64,{algorithm}\n"
    code += f"exec({algorithm}.decompress(" + base85_literal(data) + f",{args}))"
    return code


def build_decompression_snippet_bytes(data, algorithm, args):
    """Create source code that decompresses a byte literal."""
    code = b"#coding:l1\n"
    code += f"import {algorithm}\n".encode()
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
    literal = b"bytes('" + bytes(escaped) + b"','l1')"
    code += f"exec({algorithm}.decompress(".encode() + literal + args.encode() + b"))"
    return code


def build_decompression_snippet(data, algorithm, args=""):
    """Return the shorter of the byte or base85 decompression snippets."""
    bytes_snippet = build_decompression_snippet_bytes(data, algorithm, args)
    base85_snippet = build_decompression_snippet_base85(data, algorithm, args)
    if len(bytes_snippet) < len(base85_snippet):
        return bytes_snippet, "bytes"
    return base85_snippet, "base85"


def compress_with_algorithm(code, algorithm="zlib"):
    """Compress *code* using the given algorithm.

    Returns a tuple of (decompression snippet, method description)."""
    method = algorithm
    if algorithm in ("zlib", "zlib_fixed", "zopfli"):
        args = ""
        if algorithm == "zlib":
            compressed = zlib.compress(code.encode(), 9)
            # cmpobj = zlib.compressobj(9, wbits=15)
            # compressed = cmpobj.compress(code.encode()) + cmpobj.flush()
        elif algorithm == "zlib_fixed":
            wbits = 15
            cmpobj = zlib.compressobj(9, wbits=-wbits, strategy=zlib.Z_FIXED)
            compressed = cmpobj.compress(code.encode()) + cmpobj.flush()
            args = f",-{wbits}"
        else:
            compressed = zopfli.zlib.compress(
                code.encode(),
                numiterations=1000,
                blocksplitting=True,
                blocksplittinglast=False,
                blocksplittingmax=100,
            )
        snippet, encoding = build_decompression_snippet(compressed, "zlib", args)
    elif algorithm == "lzma":
        compressed = lzma.compress(code.encode(), format=2)
        snippet, encoding = build_decompression_snippet(compressed, "lzma")
    elif algorithm == "lzma_raw":
        filters = [{"id": lzma.FILTER_LZMA1, "preset": 9 | lzma.PRESET_EXTREME}]
        compressed = lzma.compress(code.encode(), format=3, filters=filters)
        args = ',3,None,[{"id":33}]'
        snippet, encoding = build_decompression_snippet(compressed, "lzma", args)
    elif algorithm == "bz2":
        compressed = bz2.compress(code.encode())
        snippet, encoding = build_decompression_snippet(compressed, "bz2")
    method += "+" + encoding
    return snippet, method


def _compress_single_variant(code, algorithm, seed):
    """Compress code for a specific algorithm and seed."""
    if "eval" not in code and "exec" not in code and "zlib" not in code:
        code = myzlib.map_identifiers(code, ["p"], seed=seed)

    if algorithm == "asis":
        compressed = code
        method = "asis"
    else:
        compressed, method = compress_with_algorithm(code, algorithm)

    method += f"+seed{seed}"
    return len(compressed), compressed, code, method


def compress_code(code, verbose, use_lzma, use_bzip2, max_seed):
    """Try various algorithms/seeds and return the best compression."""
    results = []
    algorithms = ["asis", "zlib", "zopfli"]
    # TODO: Seems bad.
    algorithms += ["zlib_fixed"]
    if use_lzma:
        algorithms += ["lzma", "lzma_raw"]
    if use_bzip2:
        algorithms += ["bz2"]
    for algorithm in algorithms:
        for seed in range(max_seed + 1):
            if seed and algorithm == "asis":
                break
            result = _compress_single_variant(code, algorithm, seed)
            if verbose:
                print(result[-1], len(result[2]), "=>", result[0])
            results.append(result)
            #if isinstance(result[1], bytes) and b"\\" not in result[1]:
            #    break
    results.sort(key=lambda r: r[0])

    _, compressed_code, original_code, method = results[0]
    return compressed_code, original_code, method


def squeeze(source_code):
    """Merge simple indented blocks onto a single line.

    The function scans *source_code* line by line.  If a block of code is
    indented exactly one level deeper than the current line and contains no
    nested blocks or control-flow keywords, the block is collapsed into the
    current line separated by semicolons."""

    control_words = {
        "if",
        "for",
        "while",
        "try",
        "with",
        "class",
        "def",
        "else",
        "elif",
        "except",
        "finally",
    }

    lines = source_code.split("\n")
    merged_lines = []
    line_index = 0

    while line_index < len(lines):
        current_line = lines[line_index]
        current_indent = len(current_line) - len(current_line.lstrip())
        next_index = line_index + 1
        collected_block = []
        allow_merge = True
        candidate_indent = current_indent

        while next_index < len(lines):
            candidate_line = lines[next_index]
            candidate_indent = len(candidate_line) - len(candidate_line.lstrip())
            if candidate_indent <= current_indent:
                break
            stripped_line = candidate_line.lstrip()
            first_word = stripped_line.split()[0] if stripped_line.split() else ""
            if (
                candidate_indent > current_indent + 1
                or ":" in stripped_line
                or first_word in control_words
            ):
                allow_merge = False
                break
            collected_block.append(stripped_line)
            next_index += 1

        if allow_merge and collected_block and candidate_indent <= current_indent:
            merged = current_line + collected_block[0]
            merged += "".join(";" + stmt for stmt in collected_block[1:])
            merged_lines.append(merged)
            line_index = next_index
        else:
            merged_lines.append(current_line)
            line_index += 1

    return "\n".join(merged_lines)


def jam(source_code):
    """Join adjacent lines when their combination is safe.

    Lines at the same indentation level that are not control-flow statements
    can be concatenated with semicolons, provided that bracket pairs remain
    balanced."""

    control_words = {
        "if",
        "for",
        "while",
        "try",
        "with",
        "class",
        "def",
        "else",
        "elif",
        "except",
        "finally",
    }

    def bracket_balance(text):
        return sum((char in "([{") - (char in ")]}" ) for char in text)

    def first_identifier(text):
        match = re.match("[a-z]+", text)
        return match.group() if match else None

    lines = source_code.split("\n")
    result_lines = [lines[0]]
    balance = bracket_balance(lines[0])

    for candidate in lines[1:]:
        last_line = result_lines[-1]
        last_indent = len(last_line) - len(last_line.lstrip())
        candidate_indent = len(candidate) - len(candidate.lstrip())

        if (
            balance == 0
            and last_indent == candidate_indent
            and not last_line.rstrip().endswith(":")
            and first_identifier(last_line.lstrip()) not in control_words
            and first_identifier(candidate.lstrip()) not in control_words
        ):
            result_lines[-1] += ";" + candidate.lstrip()
            balance += bracket_balance(candidate)
            continue

        result_lines.append(candidate)
        balance += bracket_balance(candidate)

    return "\n".join(result_lines)


def minify(code, verbose, show_minify, expand_variables):
    minified_codes = []

    minified_codes.append(("myminifier", myminifier.minify(code, expand_variables=expand_variables)))

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=SyntaxWarning)
        minified_codes.append((
            "python_minifier",
            python_minifier.minify(
                code,
                rename_locals=False,
                hoist_literals=False,
            ).replace("\t", " ")))

    if verbose:
        for used_minifier, minified_code in minified_codes:
            print(f"Minified code from {len(code)} to {len(minified_code)} bytes by {used_minifier}", flush=True)

    if show_minify:
        for used_minifier, minified_code in minified_codes:
            print(used_minifier, ":")
            print(minified_code)

    minified_codes.sort(key=lambda x: len(x[1]))

    used_minifier, minified_code = minified_codes[0]
    if minified_codes[0][1] == minified_codes[1][1]:
        used_minifier += "(same)"
    elif len(minified_codes[0][1]) == len(minified_codes[1][1]):
        used_minifier += "(tie)"

    return used_minifier, minified_code


def check_task(task_id, filename, verbose, args):
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
    #code = squeeze(code)

    size_before_minify = len(code)

    used_minifier, code = minify(code, verbose, args.show_minify, args.expand_variables)

    code, orig_code, info = compress_code(code, verbose, args.use_lzma, args.use_bzip2, args.max_seed)

    info += f"+{used_minifier}"

    if len(code) >= len(orig_code):
        assert len(code) == len(orig_code)
        print(f"Task {task_id} only minified: {size_before_minify} -> {len(code)} bytes ({used_minifier})", flush=True)
    else:
        print(f"Task {task_id} minified and compressed: {size_before_minify} -> {len(orig_code)} -> {len(code)} bytes ({info})", flush=True)

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


def submit(task_id, args, verbose):
    skip_verify = args.skip_verify
    code_dir = args.code_dir

    if skip_verify:
        return

    # print("Submitting task", task_id)

    ok, result, code = check_task(task_id, f"{code_dir}/task{task_id:03d}.py", verbose, args)

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


def report(task_ids=None):
    """Collect and report results for the given task ids.

    If *task_ids* is None, results for all 400 tasks are aggregated.
    Otherwise only the specified ids are included in the totals.
    """

    if task_ids is None:
        task_ids = range(1, 401)

    score = 0
    fail_tests = []
    error_tests = []
    todo_tests = []
    negative_tests = []
    for task_id in task_ids:
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
    parser.add_argument("--show_minify", action="store_true")
    parser.add_argument("--skip_verify", action="store_true")
    parser.add_argument("--code_dir", default="logic")
    parser.add_argument("--use_lzma", action="store_true")
    parser.add_argument("--use_bzip2", action="store_true")
    parser.add_argument("--max_seed", type=int, default=0)
    parser.add_argument("--expand_variables", action="store_true")
    args = parser.parse_args()

    if args.task_id == "all":
        executor = ProcessPoolExecutor()
        futures = []
        for task_id in range(1, 401):
            futures.append(executor.submit(submit, task_id, args, args.verbose))
        for future in futures:
            future.result()
        report()
    elif "-" in args.task_id:
        # Run a consecutive range of tasks such as "1-10".
        start, end = args.task_id.split("-", 1)
        start_id = int(start)
        end_id = int(end)
        for task_id in range(start_id, end_id + 1):
            submit(task_id, args, args.verbose)
        report(range(start_id, end_id + 1))
    else:
        if not submit(int(args.task_id), args, True):
            print("FAIL!!")
            sys.exit(1)


if __name__ == "__main__":
    main()
