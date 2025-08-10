import re


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


def merge_indented_blocks(source_code):
    """Merge a simple nested block into a single line."""

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
        base_indent = len(current_line) - len(current_line.lstrip())
        next_index = line_index + 1
        block_indent = None
        block = []
        allow_merge = True

        while next_index < len(lines):
            candidate_line = lines[next_index]
            candidate_indent = len(candidate_line) - len(candidate_line.lstrip())

            if block_indent is None:
                if candidate_indent <= base_indent:
                    break
                block_indent = candidate_indent

            if candidate_indent < block_indent:
                break
            if candidate_indent > block_indent:
                allow_merge = False
                break

            stripped = candidate_line.lstrip()
            word = stripped.split()[0] if stripped.split() else ""
            if ":" in stripped or word in control_words:
                allow_merge = False
                break

            block.append(stripped)
            next_index += 1

        if allow_merge and block:
            merged = current_line + block[0]
            merged += "".join(";" + stmt for stmt in block[1:])
            merged_lines.append(merged)
            line_index = next_index
        else:
            merged_lines.append(current_line)
            line_index += 1

    return "\n".join(merged_lines)


def remove_spaces(code):
    # TODO: Consider not replacing code in string literals.
    code, _ = re.subn(r"(\S) +([\[({,:+\-*/%\]})])", r"\1\2", code)
    code, _ = re.subn(r"([\[({,:+\-*/%\]})]) +(\w)", r"\1\2", code)
    # o and x will be confused as octal/hex numbers.
    code, _ = re.subn(r"(\b[0-9]+) +([a-np-wyz])", r"\1\2", code)
    return code


def combine_adjacent_lines(source_code):
    """Join adjacent lines when it is safe to do so."""

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
        return sum((ch in "([{") - (ch in ")]}" ) for ch in text)

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


def replce_fixed_range(code):
    code = code.replace("in range(2):", "in 0,1:")
    code = code.replace("in range(3):", "in 0,1,2:")
    code = code.replace("in range(4):", "in 0,1,2,3:")
    return code


def minify(code):
    code = reindent(code)
    code = merge_indented_blocks(code)
    code = remove_spaces(code)
    code = combine_adjacent_lines(code)
    code = jam(code)

    # Bad with LZ.
    # code = replce_fixed_range(code)

    return code
