"""Problem generators for algebra and linear algebra practice.

Every generator returns a dict with:
    kind    : str   what type of problem this is
    problem : str   what to show the user
    answer  : str   the expected answer as text
    steps   : list[str]   worked solution
    hint    : str
    check   : callable(str) -> (ok: bool, feedback: str)

Factoring answers are graded by *polynomial equality*, not by matching the
factor structure the generator happened to use. A different factorisation
that expands to the same thing is accepted.
"""

from __future__ import annotations

import random
import re
from math import gcd
from typing import Any, Callable

import sympy as sp

x, y, z, t = sp.symbols("x y z t")

_LOCALS = {
    "x": x, "y": y, "z": z, "t": t,
    "alpha": "a", "beta": "b", "lambda": "lam",
}


# ---------------------------------------------------------------- parsing

_IMPLICIT = (sp.parsing.sympy_parser.implicit_multiplication_application,)


def _insert_mult(s: str) -> str:
    """Make hand-typed maths parseable: '5x^2(6x+4)' -> '5*x**2*(6*x+4)'."""
    s = re.sub(r"(?<=[\d\)])\s*\(", r"*(", s)          # ) (   and  2 (
    s = re.sub(r"(?<=\d)\s*(?=[a-zA-Z(])", "*", s)      # 2x  2(
    s = re.sub(r"(?<=\))\s*(?=[\w(])", "*", s)          # )x  )(
    s = re.sub(r"\s+", "", s)
    return s


def parse(raw: str) -> Any:
    """Turn user input into a SymPy expression.

    Accepts ^ for powers and tolerates missing multiplication signs.
    """
    s = raw.strip().replace("^", "**").replace("π", "pi").replace("√", "sqrt")
    s = _insert_mult(s)
    return sp.parsing.sympy_parser.parse_expr(
        s, local_dict=dict(_LOCALS), transformations=_IMPLICIT, evaluate=True
    )


def parse_assignments(raw: str, names: tuple[sp.Symbol, ...]) -> dict[str, sp.Expr]:
    """Parse input like 'x=2, y=-1' or 'x = 2 and y = -1' into a dict.

    Uses parse_expr per assignment so that '=' never reaches sympify.
    """
    s = raw.strip().replace("^", "**").replace(";", ",")
    s = re.sub(r"\band\b", ",", s)
    s = re.sub(r"\bwith\b", ",", s)
    out: dict[str, sp.Expr] = {}
    for part in s.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError(f"expected 'name=value', got {part!r}")
        name, val = part.split("=", 1)
        name = name.strip()
        if name not in {str(v) for v in names}:
            raise ValueError(f"unknown variable {name!r}; expected {[str(v) for v in names]}")
        out[name] = parse(val)
    return out


def _fmt(e: Any) -> str:
    return sp.sstr(e)


def _pstr(e: Any) -> str:
    """Readable math: 12x^2 - 5x + 3 instead of 12*x**2 - 5*x + 3.

    Only strips the * between a coefficient and a variable -- the * before a
    bracket is kept so the result stays parseable.
    """
    s = sp.sstr(e).replace("**", "^")
    s = re.sub(r"(?<=\d)\*(?=[a-zA-Z])", "", s)   # 3*x -> 3x
    s = s.replace("1*(", "(")
    s = s.replace("+ -", "- ")
    return s


def _ok(msg: str = "Correct.") -> tuple[bool, str]:
    return True, msg


def _no(why: str) -> tuple[bool, str]:
    return False, why


def _same(a: Any, b: Any) -> bool:
    """Polynomial/expression equality."""
    if a is None or b is None:
        return False
    try:
        return sp.simplify(sp.expand(a - b)) == 0
    except Exception:  # noqa: BLE001
        return False


def _mk_check(poly: sp.Expr, advice: str) -> Callable[[str], tuple[bool, str]]:
    """Grader for 'expand back to this polynomial' questions."""

    def check(raw: str) -> tuple[bool, str]:
        try:
            got = parse(raw)
        except Exception as exc:  # noqa: BLE001
            return _no(f"Could not read that ({exc}). Use * for multiplication.")
        if _same(got, poly):
            return _ok()
        return _no(f"{_fmt(got)} does not expand to the original. {advice}")

    return check


def _int_factors(p: int) -> list[tuple[int, int]]:
    out = []
    for i in range(1, abs(p) + 1):
        if p % i:
            continue
        j = p // i
        out += [(i, j)] if p > 0 else [(-i, -j)]
    return out


# ---------------------------------------------------------------- factoring

def factor_gcf() -> dict:
    while True:
        g = random.randint(2, 6)
        e = random.randint(1, 2)
        p, q = random.randint(2, 9), random.randint(2, 9)
        k = random.randint(1, 2)
        # coefficients are g*p and g*q, so the true GCF is g*gcd(p,q)*x^e.
        # Requiring gcd(p,q)==1 makes g*x^e exactly the GCF.
        if gcd(p, q) != 1:
            continue
        break
    poly = g * x**e * (p * x**k + q)
    answer = poly
    steps = [
        f"GCF of the numbers {g}, {p}, {q} is {g}.",
        f"Lowest power of x is x^{e}.",
        f"Greatest common factor = {_pstr(g * x**e)}",
        f"Divide every term by it:  {_pstr(poly)} = {_factor_str(g*x**e)} * ({_pstr(p)}x^{k} + {q})",
    ]
    return dict(
        kind="Factoring — greatest common factor",
        problem=f"Factor completely:   {_pstr(poly)}",
        answer=_pstr(answer),
        steps=steps,
        hint="Take the GCF of the numbers and the *lowest* x-power. Pull it out in front.",
        check=_mk_check(poly, "Did you divide every term, or only some?"),
    )


def factor_diff_squares() -> dict:
    # every factoring problem must contain x, otherwise it is just arithmetic
    mon = random.choice([x, x**2])
    a, b = random.sample(range(2, 10), 2)
    A = a * mon
    poly = sp.expand(A**2 - b**2)
    answer = (A - b) * (A + b)
    steps = [
        f"({_pstr(A)})^2 and {b}^2 are both perfect squares.",
        "a^2 - b^2 = (a-b)(a+b)",
        f"= {_factor_str(A - b)} * {_factor_str(A + b)}",
    ]
    return dict(
        kind="Factoring — difference of squares",
        problem=f"Factor completely:   {_pstr(poly)}",
        answer=_pstr(answer),
        steps=steps,
        hint="Both pieces must be perfect squares. Then (a-b)(a+b). Watch the signs.",
        check=_mk_check(poly, "Is the middle sign correct — difference or sum?"),
    )


def factor_perfect_square() -> dict:
    a = random.randint(2, 6)
    b = random.randint(1, 9)
    A = a * x          # keep the x: (a+b)^2 with no variable is not algebra
    poly = sp.expand((A + b) ** 2)
    steps = [
        f"First term ({_pstr(A)})^2 is a square, last term {b}^2 is a square.",
        f"Middle term is +2*({_pstr(A)})*{b}, so this is the (a+b)^2 pattern.",
        "(A negative middle term would have given (a-b)^2 instead.)",
        f"= ({_pstr(A + b)})^2",
    ]
    return dict(
        kind="Factoring — perfect square trinomial",
        problem=f"Factor completely:   {_pstr(poly)}",
        answer=_pstr((A + b) ** 2),
        steps=steps,
        hint="Does it match a^2 + 2ab + b^2 (or a^2 - 2ab + b^2)?",
        check=_mk_check(poly, "Double-check the sign of the middle term."),
    )


def factor_trinomial_monic() -> dict:
    m, n = random.choice([f for f in _int_factors(random.randint(4, 24)) if abs(f[0]) > 1])
    s = m + n
    if random.random() < 0.4:
        m, n, s = -m, -n, -s
    poly = sp.expand(x**2 + s * x + m * n)
    answer = (x + m) * (x + n)
    how = (
        "both positive" if m * n > 0 and s > 0
        else "both negative" if m * n > 0 and s < 0
        else "opposite signs"
    )
    steps = [
        f"Need two numbers with  product = {m*n}  and  sum = {s}.",
        f"They are {m} and {n}  ({how}).",
        f"= {_factor_str(x + m)} * {_factor_str(x + n)}",
    ]
    return dict(
        kind="Factoring — trinomial x^2 + bx + c",
        problem=f"Factor completely:   {_pstr(poly)}",
        answer=_pstr(answer),
        steps=steps,
        hint="List the factor pairs of c, then pick the pair whose sum is b.",
        check=_mk_check(poly, "Check your product equals c and your sum equals b."),
    )


def _s(n: int) -> str:
    """Signed integer for prose: 6 -> '+ 6', -6 -> '- 6'."""
    return f"+ {n}" if n > 0 else f"- {abs(n)}"


def _factor_str(f: Any) -> str:
    """Parenthesise a factor unless it is a single monomial, so that
    '(5x + 3)' + '(3x + 4)' never renders as the ambiguous '5x + 3(3x + 4)'."""
    s = _pstr(f)
    return f"({s})" if " " in s else s


def factor_trinomial_leading() -> dict:
    """Build (r1 x + s1)(r2 x + s2) directly.

    The textbook split of the middle term is then known without searching:
    a = r1 r2, b = r1 s2 + r2 s1, c = s1 s2, and the split is
    m = r1 s2, n = r2 s1  (so m n = a c and m + n = b).
    """
    while True:
        r1, r2 = random.randint(1, 6), random.randint(2, 6)
        s1 = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
        s2 = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
        a, b, c = r1 * r2, r1 * s2 + r2 * s1, s1 * s2
        if b == 0:                      # would be a difference of squares, not a trinomial
            continue
        if gcd(gcd(abs(a), abs(b)), abs(c)) != 1:   # a GCF would make this a different exercise
            continue
        if b * b == 4 * a * c:          # secretly a perfect square trinomial
            continue
        if abs(b) > 40 or abs(c) > 36:  # keep it hand-checkable
            continue
        break
    f1, f2 = r1 * x + s1, r2 * x + s2
    poly = sp.expand(f1 * f2)
    m, n = r1 * s2, r2 * s1
    assert m + n == b and m * n == a * c
    steps = [
        f"a*c = {a}*{c} = {a*c}",
        f"Two numbers with product {a*c} and sum {b}:  they are {m} and {n}",
        f"Split the middle term:  {_pstr(a)}x^2 {_s(m)}x {_s(n)}x {_s(c)}",
        f"Group:  x({_pstr(a)}x {_s(m)}) + ({n}x {_s(c)})",
        f"Pull {r2} from the first group and {s1} from the second (they are hidden factors)",
        f"= {_factor_str(f1)} * {_factor_str(f2)}",
    ]
    return dict(
        kind="Factoring — trinomial ax^2 + bx + c",
        problem=f"Factor completely:   {_pstr(poly)}",
        answer=_factor_str(f1) + "*" + _factor_str(f2),
        steps=steps,
        hint=f"Multiply a*c = {a*c}, find that pair, then split the middle term and group.",
        check=_mk_check(poly, "Did the split middle term add back up to b?"),
    )


def answer_of(*fs: sp.Expr) -> sp.Expr:
    out = fs[0]
    for f in fs[1:]:
        out = out * f
    return sp.expand(out)


def factor_grouping() -> dict:
    while True:
        B = random.choice([-4, -3, -2, 2, 3, 4])
        C = random.randint(1, 5)
        E = random.choice([-5, -3, -2, 2, 3, 5])
        if gcd(C, E) != 1:
            continue  # would leave a GCF, which is a different exercise
        poly = sp.expand((x + B) * (C * x**2 + E))
        # the leftover C x^2 + E is irreducible over Q iff disc = -4CE is not a square
        if not sp.sqrt(sp.Integer(-4 * C * E)).is_Rational:
            break
    ans = sp.factor(poly)
    steps = [
        "No common factor and it is not a trinomial — four terms, so group.",
        f"Group the x^3 with the x^2 term:  ({C}x^3 {_s(B*C)}x^2) + ({E}x {_s(B*E)})",
        f"= {_pstr(C*x**2)}(x {_s(B)}) {_s(E)}(x {_s(B)})",
        f"= {_factor_str(x + B)} * {_factor_str(C*x**2 + E)}",
    ]
    return dict(
        kind="Factoring — grouping",
        problem=f"Factor completely:   {_pstr(poly)}",
        answer=_pstr(ans),
        steps=steps,
        hint="Split into two groups that share a binomial, factor each group, then factor the leftover.",
        check=_mk_check(poly, "Both groups must factor to the *same* binomial."),
    )


# ---------------------------------------------------------------- systems

def _fmt_system(A: sp.Matrix, b: sp.Matrix, vs: tuple) -> str:
    rows = []
    for i in range(A.rows):
        parts = []
        for j, v in enumerate(vs):
            c = A[i, j]
            if c == 0:
                continue
            mag = "" if abs(c) == 1 else str(abs(c))
            parts.append((("" if not parts else " + ") + mag + str(v)))
        lhs = "".join(parts) or "0"
        rows.append(f"{lhs} = {b[i]}")
    return "\n".join(rows)


def _rref_steps(aug: sp.Matrix) -> tuple[sp.Matrix, list[str]]:
    """Row reduce with a recorded operation for each step."""
    steps: list[str] = []
    cur = aug.copy()  # in-place row ops below would otherwise mutate the caller's matrix
    nrows, ncols = cur.rows, cur.cols
    r = 0
    for c in range(ncols):
        if r >= nrows:
            break
        p = next((i for i in range(r, nrows) if cur[i, c] != 0), None)
        if p is None:
            continue
        if p != r:
            cur.row_swap(p, r)  # NOTE: row_swap mutates in place and returns None
            steps.append(f"R{p+1} <-> R{r+1}\n{cur}")
        f = sp.Rational(cur[r, c])
        if f != 1:
            cur[r, :] = cur[r, :] / f
            steps.append(f"R{r+1} = ({_fmt(f)})*R{r+1}\n{cur}")
        for i in range(nrows):
            if i != r and cur[i, c] != 0:
                fct = cur[i, c]
                cur[i, :] = cur[i, :] - fct * cur[r, :]
                steps.append(f"R{i+1} = R{i+1} - ({_fmt(fct)})*R{r+1}\n{cur}")
        r += 1
    return cur, steps


def system(kind: str = "2x2") -> dict:
    n = 2 if kind == "2x2" else 3
    vs = (x, y) if n == 2 else (x, y, z)
    mode = random.choice(["unique", "unique", "unique", "none", "infinite"])

    if mode == "unique":
        sol = sp.Matrix([random.randint(-6, 6) for _ in range(n)])
        A = sp.Matrix(n, n, lambda i, j: random.randint(-5, 5))
        tries = 0
        while A.det() == 0 and tries < 40:
            A = sp.Matrix(n, n, lambda i, j: random.randint(-5, 5))
            tries += 1
        if A.det() == 0:
            A = sp.diag(*[random.choice([-3, -2, -1, 1, 2, 3]) for _ in range(n)])
        b = A * sol
    elif mode == "none":
        A = sp.Matrix(n, n, lambda i, j: random.choice([-4, -3, 2, 3, 4]))
        k = random.choice([2, 3, -1, -2])
        A[n - 1, :] = k * A[0, :]
        b = sp.zeros(n, 1)
        for i in range(n - 1):
            b[i, 0] = random.randint(-8, 8)
        b[n - 1, 0] = b[0, 0] + random.choice([1, 2, 3, -1, -2])
    else:
        A = sp.Matrix(n, n, lambda i, j: random.choice([-4, -3, 2, 3, 4]))
        A[n - 1, :] = A[0, :]
        b = sp.zeros(n, 1)
        for i in range(n):
            for j in range(n):
                b[i] += A[i, j] * t**j
        b[n - 1] = b[0]

    aug = A.row_join(b)
    final, op_steps = _rref_steps(aug)
    steps = [f"Augmented matrix:\n{aug}", *op_steps, f"Reduced:\n{final}"]

    if mode == "none":
        steps.append("A row reads 0 = (nonzero), so the system is inconsistent: no solution.")
        answer = "no solution"
    elif mode == "infinite":
        steps.append("A row reads 0 = 0, so a variable is free: infinitely many solutions.")
        answer = "infinitely many solutions"
    else:
        vals = [sp.simplify(final[i, -1]) for i in range(n)]
        steps.append("Read the last column: " + ", ".join(f"{vs[i]} = {vals[i]}" for i in range(n)))
        answer = ", ".join(f"{vs[i]}={vals[i]}" for i in range(n))

    def check(raw: str) -> tuple[bool, str]:
        s = raw.strip().lower()
        if mode == "none":
            hit = re.search(r"\bno[\s_]*sol", s) or re.search(r"\bnone\b", s) or re.search(r"\bno\s+answer\b", s)
            return _ok("Correct — no solution.") if hit and len(s) > 4 else _no(
                "Look for a row that reads 0 = something nonzero."
            )
        if mode == "infinite":
            hit = (
                re.search(r"\binf", s)
                or re.search(r"\bmany\b", s)
                or re.search(r"\bfree\b", s)
                or re.search(r"\bdepend", s)
            )
            return _ok("Correct — infinitely many.") if hit and len(s) > 4 else _no(
                "Is there a free variable in the reduced matrix?"
            )
        try:
            as_dict = parse_assignments(raw, vs)
        except Exception as exc:  # noqa: BLE001
            return _no(f"Write it like  x=2, y=-1  ({exc})")
        for i, v in enumerate(vs):
            key = str(v)
            if key not in as_dict:
                return _no(f"No value given for {key}.")
            if not _same(sp.nsimplify(as_dict[key], rational=True), final[i, -1]):
                return _no(f"{key} should be {final[i, -1]}, you said {as_dict[key]}.")
        return _ok()

    return dict(
        kind=f"Systems of equations — {kind} ({mode})",
        problem=f"Solve the system:\n{_fmt_system(A, b, vs)}",
        answer=answer,
        steps=steps,
        hint="Augment with the constants, then row reduce. A row 0 = nonzero means no solution; 0 = 0 means infinitely many.",
        check=check,
    )


# ---------------------------------------------------------------- matrices

def gauss_jordan() -> dict:
    n = random.choice([2, 3])
    A = sp.Matrix(n, n, lambda i, j: random.randint(-4, 4))
    tries = 0
    while A.det() == 0 and tries < 60:
        A = sp.Matrix(n, n, lambda i, j: random.randint(-4, 4))
        tries += 1
    if A.det() == 0:
        A = sp.diag(*[random.choice([-3, -2, -1, 1, 2, 3]) for _ in range(n)])
    # Build b from a known integer solution so the answer is always clean
    # integers -- random b would produce ugly fractions like -1/170.
    planted = sp.Matrix([random.randint(-6, 6) for _ in range(n)])
    b = A * planted
    aug = A.row_join(b)
    final, ops = _rref_steps(aug)
    vs = (x, y, z)[:n]
    sol = [sp.simplify(final[i, -1]) for i in range(n)]
    steps = [
        f"Start:\n{aug}",
        *ops,
        f"Reduced row echelon form:\n{final}",
        f"det(A) = {A.det()} != 0, so the solution is unique.",
        "Read the last column: " + ", ".join(f"{vs[i]} = {sol[i]}" for i in range(n)),
    ]

    def check(raw: str) -> tuple[bool, str]:
        s = raw.strip().lower().replace(" ", "")
        if "rref" in s or "echelon" in s:
            return _ok("Right goal — now read the last column for the answer.")
        try:
            d = parse_assignments(raw, vs)
        except Exception as exc:  # noqa: BLE001
            return _no(f"Write it like  x=1, y=-2  ({exc})")
        vec = []
        for v in vs:
            if str(v) not in d:
                return _no(f"No value for {v}.")
            vec.append(sp.nsimplify(d[str(v)], rational=True))
        res = A * sp.Matrix(vec) - b
        if all(sp.simplify(e) == 0 for e in res):
            return _ok()
        bad = next(i for i, e in enumerate(res) if sp.simplify(e) != 0)
        return _no(f"That vector fails equation {bad+1} of the system.")

    return dict(
        kind=f"Linear algebra — Gauss-Jordan ({n}x{n})",
        problem=f"Row reduce the augmented matrix, then read off the solution to A x = b:\n{aug}",
        answer=", ".join(f"{vs[i]}={sol[i]}" for i in range(n)),
        steps=steps,
        hint="Work left to right: swap for a nonzero pivot, scale the pivot to 1, clear the column above and below.",
        check=check,
    )


def eigenvalues_2x2() -> dict:
    # Only matrices whose eigenvalues are real *integers* -- complex roots are
    # noise at this stage, and fractional roots defeat hand-checking.
    while True:
        A = sp.Matrix(2, 2, lambda i, j: random.randint(-4, 4))
        tr, det = A.trace(), A.det()
        disc = tr * tr - 4 * det
        if disc < 0:
            continue
        rt = sp.sqrt(sp.Integer(disc))
        if not rt.is_Integer:
            continue
        rt = int(rt)
        if (int(tr) + rt) % 2 or (int(tr) - rt) % 2:
            continue
        if random.random() < 0.85 and rt == 0:
            continue  # mostly avoid the double-root case
        break
    lam = sp.Symbol("lam")
    M = A - lam * sp.eye(2)
    charpoly = sp.expand(M.det())
    evals = [sp.simplify(e) for e in sp.solve(sp.Eq(charpoly, 0), lam)]
    steps = [
        f"A - lam*I =\n{M}",
        f"det(A - lam*I) = {_pstr(charpoly)}",
        f"Set it to zero: {charpoly} = 0",
    ]
    desc = []
    for e in evals:
        ker = (A - e * sp.eye(2)).nullspace()
        v = sp.simplify(ker[0]) if ker else None
        if v is not None and all(sp.simplify(k) == 0 for k in v):
            v = None
        desc.append((e, v))
        if v is not None:
            steps.append(f"lam = {e}:  null space of (A - {e}I) is spanned by [{_pstr(v[0])}, {_pstr(v[1])}]^T")
    answer = "; ".join(
        f"lam={e}" + (f", v=[{_pstr(v[0])},{_pstr(v[1])}]" if v is not None else ", no eigenvector")
        for e, v in desc
    )
    steps.append("Check: A v must equal lam v.")

    def check(raw: str) -> tuple[bool, str]:
        found = re.findall(r"lam(?:bda)?\s*=\s*([^,;]+)", raw, flags=re.I)
        if not found:
            return _no("No eigenvalue found. Write it as  lam=3, lam=-1  (or lambda=...).")
        got = []
        for piece in found:
            try:
                got.append(sp.nsimplify(sp.sympify(piece.strip(), locals=_LOCALS)))
            except Exception:  # noqa: BLE001
                return _no(f"Could not read the eigenvalue {piece!r}.")
        for e in evals:
            hit = next(
                (g for g in got if sp.simplify(g - e) == 0 or abs(complex(g) - complex(e)) < 1e-6),
                None,
            )
            if hit is None:
                return _no(f"Missing or wrong eigenvalue {e}. Recheck det(A - lam*I).")
        if "v" not in raw.lower() and "[" not in raw:
            return _ok("Eigenvalues correct. Now add an eigenvector, e.g. v=[1,2].")
        return _ok()

    return dict(
        kind="Linear algebra — eigenvalues and eigenvectors (2x2)",
        problem=f"Find the eigenvalues and eigenvectors of\n{A}",
        answer=answer,
        steps=steps,
        hint="det(A - lam*I) = 0 gives the eigenvalues. Eigenvectors are the null space of (A - lam*I).",
        check=check,
    )


def determinant_3x3() -> dict:
    while True:
        M = sp.Matrix(3, 3, lambda i, j: random.randint(-5, 5))
        if M.det() != 0:
            break
    a, b, c = M[0, 0], M[0, 1], M[0, 2]
    d, e, f = M[1, 0], M[1, 1], M[1, 2]
    g, h, i = M[2, 0], M[2, 1], M[2, 2]
    steps = [
        "Expand along the first row. Cofactor signs: + - +",
        f"det = {a}*({e}{i} - ({f})({h})) - ({b})*({d}{i} - ({f})({g})) + ({c})*({d}{h} - ({e})({g}))",
        f"= ({e*i-f*h})*{a} - ({d*i-f*g})*{b} + ({d*h-e*g})*{c}",
        f"= {M.det()}",
    ]

    def check(raw: str) -> tuple[bool, str]:
        try:
            got = sp.simplify(parse(raw))
        except Exception as exc:  # noqa: BLE001
            return _no(f"Could not read that ({exc}).")
        if got == M.det():
            return _ok()
        return _no(f"You got {got}; it is {M.det()}. Check the + - + pattern.")

    return dict(
        kind="Linear algebra — 3x3 determinant",
        problem=f"Compute the determinant of\n{M}",
        answer=_fmt(M.det()),
        steps=steps,
        hint="Expand along the first row: signs alternate + - +.",
        check=check,
    )


# ---------------------------------------------------------------- registry

def factoring_all() -> list[str]:
    return [f"F{k+1}" for k in range(len(FACTORING))]


FACTORING = [
    factor_gcf,
    factor_diff_squares,
    factor_perfect_square,
    factor_trinomial_monic,
    factor_trinomial_leading,
    factor_grouping,
]
LINEAR_ALGEBRA = [
    lambda: system("2x2"),
    lambda: system("3x3"),
    gauss_jordan,
    eigenvalues_2x2,
    determinant_3x3,
]
ALL = {"factoring": FACTORING, "linear_algebra": LINEAR_ALGEBRA}


# ---------------------------------------------------------------- cli

_TOPICS = {
    "factoring": FACTORING,
    "linear_algebra": LINEAR_ALGEBRA,
    "gauss": [gauss_jordan],
    "eigen": [eigenvalues_2x2],
    "det": [determinant_3x3],
    "systems": [lambda: system("2x2"), lambda: system("3x3")],
}
_TOPICS["random"] = FACTORING + LINEAR_ALGEBRA

_MENU_CHOICES = {
    "1": "factoring",
    "2": "systems",
    "3": "gauss",
    "4": "eigen",
    "5": "det",
    "r": "random",
}

_MENU = """Choose a topic:
  1  factoring            (GCF, squares, trinomials, grouping)
  2  systems             (2x2 and 3x3, incl. no/infinite solutions)
  3  gauss               (row reduction)
  4  eigen               (eigenvalues and eigenvectors)
  5  det                 (3x3 determinants)
  r  random              (anything)
  q  quit
"""


def _pick(pool: list) -> dict:
    return random.choice(pool)()


def _show(p: dict, reveal: bool) -> None:
    print()
    print(f"--- {p['kind']} " + "-" * max(0, 58 - len(p['kind'])))
    print(p["problem"])
    if reveal:
        print(f"\n  ANSWER:  {p['answer']}")
        print("  STEPS:")
        for s in p["steps"]:
            for line in s.splitlines():
                print(f"    * {line}")
    print()


def _interactive(p: dict) -> bool:
    """Grade one attempt. Returns True if correct."""
    _show(p, reveal=False)
    print(f"  hint: {p['hint']}")
    try:
        raw = input("  your answer> ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    if raw.lower() in {"h", "hint"}:
        print(f"  {p['hint']}\n")
        return False
    if raw.lower() in {"s", "skip"}:
        print("  skipped.\n")
        return False
    if raw.lower() in {"a", "ans", "answer"}:
        _show(p, reveal=True)
        return False
    ok, msg = p["check"](raw)
    print(f"  {'OK  ' if ok else 'NO  '} {msg}\n")
    if not ok:
        _show(p, reveal=True)
    return ok


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Algebra and linear algebra practice.")
    ap.add_argument("topic", nargs="?", default="menu",
                    help="factoring | systems | gauss | eigen | det | random | menu")
    ap.add_argument("-n", "--count", type=int, default=5, help="how many problems")
    ap.add_argument("-s", "--seed", type=int, help="reproducible seed")
    ap.add_argument("--practice", action="store_true", help="grade your answers")
    args = ap.parse_args(argv)
    if args.seed is not None:
        random.seed(args.seed)

    key = args.topic.lower()
    if key in {"menu", "m", ""}:
        while True:
            print(_MENU)
            try:
                c = input("> ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                return 0
            if c in {"q", "quit", "exit", ""}:
                return 0
            topic = _MENU_CHOICES.get(c, c)          # accept 1-5 or the name
            pool = _TOPICS.get(topic)
            if pool is None:
                print("  pick 1-5, r or q")
                continue
            if args.practice:
                _drill_loop(pool)
            else:
                for _ in range(args.count):
                    _show(_pick(pool), reveal=True)
        return 0

    pool = _TOPICS.get(key)
    if pool is None:
        if key in {"random", "r"}:
            pool = FACTORING + LINEAR_ALGEBRA
        else:
            ap.error(f"unknown topic {key!r}; try: {', '.join(sorted(_TOPICS))}, random, menu")
    if args.practice:
        return _drill_loop(pool)
    for _ in range(args.count):
        _show(_pick(pool), reveal=True)
    return 0


def _drill_loop(pool: list) -> int:
    right = wrong = 0
    while True:
        p = _pick(pool)
        if _interactive(p):
            right += 1
        else:
            wrong += 1
        print(f"  score: {right} right, {wrong} not yet\n")
        try:
            if input("  another? (y/n) ").strip().lower().startswith("n"):
                break
        except (EOFError, KeyboardInterrupt):
            print()
            break
    print(f"final: {right} right, {wrong} not yet")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
