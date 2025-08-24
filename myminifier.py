import ast
import re
import warnings


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
        "match",
        "case",
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
            m = re.match("[a-z]+", stripped)
            if stripped.endswith(":") or m and m.group() in control_words:
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
    parts = re.split(r"('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")", code)
    for i in range(0, len(parts), 2):
        segment = parts[i]
        segment, _ = re.subn(r"(\S) +([\[({,:+\-*/%\]})\"'=;!])", r"\1\2", segment)
        segment, _ = re.subn(r"([\[({,:+\-*/%\]})'\"=;!]) +(\w)", r"\1\2", segment)
        segment = segment.replace("= ", "=")
        segment, _ = re.subn(r"(\b[0-9]+) +([a-np-wyz])", r"\1\2", segment)
        parts[i] = segment
    return "".join(parts)


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
        "match",
        "case",
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


def _split_top_level_commas(text):
    """Split *text* on commas not nested in brackets or strings."""
    parts = []
    cur = []
    depth = 0
    quote = None
    i = 0
    while i < len(text):
        ch = text[i]
        if quote:
            cur.append(ch)
            if ch == "\\" and i + 1 < len(text):
                cur.append(text[i + 1])
                i += 1
            elif ch == quote:
                quote = None
        else:
            if ch in "'\"":
                quote = ch
                cur.append(ch)
            elif ch in "([{":
                depth += 1
                cur.append(ch)
            elif ch in ")]}":
                depth -= 1
                cur.append(ch)
            elif ch == "," and depth == 0:
                parts.append("".join(cur))
                cur = []
            else:
                cur.append(ch)
        i += 1
    parts.append("".join(cur))
    return [p.strip() for p in parts]


def bundle_assignments(code):
    """Bundle consecutive simple assignments into a tuple assignment."""
    lines = code.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"(\s*)([A-Za-z_]\w*)=(.+)", line)
        if m and "#" not in line and ";" not in line:
            indent, name, value = m.groups()
            names = [name.strip()]
            values = [value.strip()]
            j = i + 1
            while j < len(lines):
                m2 = re.match(r"(\s*)([A-Za-z_]\w*)=(.+)", lines[j])
                if not (m2 and m2.group(1) == indent and "#" not in lines[j] and ";" not in lines[j]):
                    break
                names.append(m2.group(2).strip())
                values.append(m2.group(3).strip())
                j += 1
            if len(names) > 1:
                out.append(indent + ",".join(names) + "=" + ",".join(values))
                i = j
                continue
        out.append(line)
        i += 1
    return "\n".join(out)


def expand_assignments(code):
    """Expand tuple assignments into multiple lines with the same indent."""
    lines = code.splitlines()
    out = []
    for line in lines:
        m = re.match(r"(\s*)((?:[A-Za-z_]\w*\s*,\s*)+[A-Za-z_]\w*)=(.+)", line)
        if m and "#" not in line and ";" not in line:
            indent, names_part, values_part = m.groups()
            names = [n.strip() for n in names_part.split(",")]
            values = _split_top_level_commas(values_part)
            if len(names) == len(values) and all(re.match(r"[A-Za-z_]\w*$", n) for n in names):
                out.extend(f"{indent}{n}={v.strip()}" for n, v in zip(names, values))
                continue
        out.append(line)
    return "\n".join(out)


def replce_fixed_range(code):
    code = code.replace("in range(2):", "in 0,1:")
    code = code.replace("in range(3):", "in 0,1,2:")
    code = code.replace("in range(4):", "in 0,1,2,3:")
    return code


def remove_trivial_parens(code):
    code, _ = re.subn(r"(=)\(([^)]+)\)([;\n])", r"\1\2\3", code)
    code, _ = re.subn(r"(else)\(([^),]+)\)([;\n])", r"\1 \2\3", code)
    return code


def remove_parens_with_ast(code):
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=SyntaxWarning)
        orig_canonical_code = ast.unparse(ast.parse(code))
    start_parens = []
    for idx in range(len(code)):
        if code[idx] == "(":
            start_parens.append(idx)
        if code[idx] == ")":
            start_idx = start_parens.pop()
            new_code = code[:start_idx] + code[start_idx+1:idx] + code[idx+1:]
            new_ast = None
            try:
                with warnings.catch_warnings():
                    warnings.filterwarnings("ignore", category=SyntaxWarning)
                    new_ast = ast.parse(new_code)
            except:
                pass
            if new_ast is not None:
                if orig_canonical_code == ast.unparse(new_ast):
                    return new_code
    return None


def remove_parens(code):
    while new_code := remove_parens_with_ast(code):
        code = new_code
    return code


def find_expandable_variables(code):
    """Return a mapping of variables that can be expanded and their usage counts.

    A variable is considered expandable when it is assigned exactly once in the
    provided code. The returned dictionary maps such variable names to the
    number of times they are read afterwards. Variables that are assigned but
    never used will therefore appear with a count of ``0``.
    """

    tree = ast.parse(code)

    # Count assignments for each variable. Variables assigned more than once
    # are not safe to expand.
    assigns = {}

    class AssignCounter(ast.NodeVisitor):
        def visit_Assign(self, node):
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                assigns[name] = assigns.get(name, 0) + 1
            self.generic_visit(node)

        def visit_AugAssign(self, node):
            if isinstance(node.target, ast.Name):
                name = node.target.id
                assigns[name] = assigns.get(name, 0) + 1
            self.generic_visit(node)

        def visit_AnnAssign(self, node):
            if isinstance(node.target, ast.Name):
                name = node.target.id
                assigns[name] = assigns.get(name, 0) + 1
            self.generic_visit(node)

    AssignCounter().visit(tree)

    # Count how many times each variable is read.
    loads = {}

    class LoadCounter(ast.NodeVisitor):
        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Load) and assigns.get(node.id) == 1:
                loads[node.id] = loads.get(node.id, 0) + 1
            self.generic_visit(node)

    LoadCounter().visit(tree)

    # Include variables assigned once but never used (default to zero).
    return {name: loads.get(name, 0) for name, c in assigns.items() if c == 1}


def expand_variable(code, name):
    """Expand the variable ``name`` by inlining its assigned value.

    If the variable is never used, the assignment statement is simply removed.
    """

    tree = ast.parse(code)
    assign = None

    # Locate the assignment to the target variable.
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == name
        ):
            assign = node
            break

    if assign is None:
        return code

    value_src = ast.get_source_segment(code, assign.value)

    # Compute string offsets from line/column pairs.
    lines = code.splitlines(keepends=True)
    starts = []
    idx = 0
    for line in lines:
        starts.append(idx)
        idx += len(line)

    def offset(line, col):
        return starts[line - 1] + col

    # Remove the assignment statement.
    # Determine where to start removing. If the assignment appears after a
    # semicolon on the same line, remove everything following that semicolon.
    line_start = offset(assign.lineno, 0)
    assign_start = offset(assign.lineno, assign.col_offset)
    prev_semicolon = code.rfind(';', line_start, assign_start)
    if prev_semicolon >= 0:
        start = prev_semicolon + 1
        while start < len(code) and code[start] == ' ':
            start += 1
    else:
        start = line_start
    end = offset(assign.end_lineno, assign.end_col_offset)
    while end < len(code) and code[end] in " \t":
        end += 1
    if end < len(code) and code[end] == ';':
        end += 1
        while end < len(code) and code[end] == ' ':
            end += 1
    if end < len(code) and code[end] == '\n':
        end += 1
    code = code[:start] + code[end:]

    # Parse the code without the assignment to locate usages of the variable.
    tree = ast.parse(code)
    lines = code.splitlines(keepends=True)
    starts = []
    idx = 0
    for line in lines:
        starts.append(idx)
        idx += len(line)

    def offset2(line, col):
        return starts[line - 1] + col

    positions = []

    class UseFinder(ast.NodeVisitor):
        def visit_Name(self, node):
            if node.id == name and isinstance(node.ctx, ast.Load):
                s = offset2(node.lineno, node.col_offset)
                e = offset2(node.end_lineno, node.end_col_offset)
                positions.append((s, e))
            self.generic_visit(node)

    UseFinder().visit(tree)

    # Replace each occurrence from the end to preserve offsets.
    for s, e in sorted(positions, reverse=True):
        code = code[:s] + value_src + code[e:]

    return code


def remove_semicolons(code):
    res=[]
    for line in code.split("\n"):
        base=len(line)-len(line.lstrip())
        line=line.strip()
        ind=base
        tok=""
        for ch in line:
            if ch==';':
                if tok.strip():
                    res.append(" "*ind+tok.strip())
                tok=""
            elif ch==':':
                res.append(" "*ind+tok.strip()+':')
                tok=""
                ind+=1
            else:
                tok+=ch
        if tok.strip():
            res.append(" "*ind+tok.strip())
    return "\n".join(res)


def replace_unpacking_funcs(code):
    """Replace list()/set() calls with their unpacking forms."""
    # loop through both names and their corresponding braces
    for name,l,r in(("list","[*","]"),("set","{*","}")):
        i=0
        while True:
            j=code.find(name+"(",i)
            if j<0:break
            k=j+len(name)+1
            n=1
            s=0
            while n and k<len(code):
                if code[k:k+3] in("'''","\"\"\""):
                    s=1;q=code[k:k+3];k+=3
                    while k<len(code)and code[k:k+3]!=q:
                        if code[k]=='\\':k+=1
                        k+=1
                    k+=3
                else:
                    c=code[k]
                    if c in"'\"":
                        s=1;q=c;k+=1
                        while k<len(code)and code[k]!=q:
                            if code[k]=='\\':k+=1
                            k+=1
                        k+=1
                    else:
                        n+=(c=="(")-(c==")")
                        k+=1
            a=code[j+len(name)+1:k-1]
            if s:warnings.warn(name+"() contains string literal; skipping")
            elif a.strip() and "for"not in a:
                code=code[:j]+l+a+r+code[k:]
            i=j+1
    return code

def replace_def_p(code):
    code = re.sub(r"^def p\((\w+)\):return\s*(.*)$", r"p=lambda \1:\2", code)
    return code


def minify(code):
    code = reindent(code)
    code = replace_unpacking_funcs(code)
    code = merge_indented_blocks(code)
    code = remove_spaces(code)
    code = combine_adjacent_lines(code)
    code = remove_trivial_parens(code)
    if "eval" not in code and "exec" not in code:
        code = remove_parens(code)

    code = replace_def_p(code)

    if len(code) < 150:
        # Bad with LZ.
        code = replce_fixed_range(code)

    return code
