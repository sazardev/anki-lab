# Algebra Rules Bible — expanded

Everything you need before linear algebra, in the order you actually need it.
The original was missing the decision procedures — *which method do I use?* —
which is the part that makes factoring feel arbitrary. That is section 2.

---

## 1. The one-page core

### Order of operations

$$\text{Parentheses} \to \text{Exponents} \to \text{Mult/Div} \to \text{Add/Sub}$$

$$3+2(5^2-4) = 3+2(25-4) = 3+42 = 45$$

### Signs

| | |
|---|---|
| $(+) (+)$ | $+$ |
| $(-)(-)$ | $+$ |
| $(+)(-)$ | $-$ |
| $(-)(+)$ | $-$ |

Same signs → positive. Different → negative. **Division follows multiplication.**

### Combine like terms

Only terms with the **same variable and same exponent**:

$$3x + 5x = 8x \qquad 7x^2 - 2x^2 = 5x^2$$

$$3x + 4y \;\text{cannot combine} \qquad 3x^2 + 4x \;\text{cannot combine}$$

### The distributive property

$$a(b+c) = ab + ac \qquad a(b-c) = ab - ac$$

The negative sign distributes to **every** term:

$$-(x+3) = -x-3 \qquad -(x-3) = -x+3$$

### Exponent rules

| Rule | |
|---|---|
| multiply | $x^a x^b = x^{a+b}$ |
| divide | $\dfrac{x^a}{x^b} = x^{a-b}$ |
| power of power | $(x^a)^b = x^{ab}$ |
| power of product | $(xy)^n = x^n y^n$ |
| zero | $x^0 = 1$ |
| negative | $x^{-n} = \dfrac{1}{x^n}$ |

> **Trap:** adding exponents happens in a *product*. `2x² + x³` is already simplified.

### Three identities — memorise

$$\boxed{(a+b)^2 = a^2 + 2ab + b^2}$$
$$\boxed{(a-b)^2 = a^2 - 2ab + b^2}$$
$$\boxed{(a+b)(a-b) = a^2 - b^2}$$

---

## 2. Which factoring method? (the decision tree)

This is the part that was missing. Walk it top to bottom.

```
Start
  │
  ├─ Is there a common factor in EVERY term?   → GCF        (§3.1)
  │     (numbers, and lowest power of each variable)
  │
  ├─ Is it a difference of squares a²−b²?     → §3.2
  │     (both terms perfect squares, MINUS between)
  │
  ├─ Is it a perfect square trinomial?         → §3.3
  │     a² ± 2ab + b²   (first & last are squares,
  │                      middle is exactly ±2ab)
  │
  ├─ Is it 3 terms with leading 1?  x²+bx+c   → §3.4
  │
  ├─ Is it 3 terms, leading ≠ 1?  ax²+bx+c   → §3.5 (the ac trick)
  │
  ├─ Is it 4+ terms?                           → grouping   (§3.6)
  │
  ├─ Is it a sum/difference of cubes?          → §3.7
  │
  └─ Is the variable inside a power?           → substitution (§3.8)
```

**Order matters.** GCF first, always. Factoring `9x⁴−4x²` by squares first gives
`x²(3x−2)(3x+2)`… which is right, but doing GCF first is what keeps you from
forgetting the `x²`.

---

## 3. Factoring — the six methods

### 3.1 Greatest common factor

Take the GCF of the **numbers** and the **lowest power of each variable**.

$$12x^3 + 18x^2 = \mathbf{6x^2}(2x + 3)$$

$$15x^4y^2 + 10x^2y = \mathbf{5x^2y}(3x^2y + 2)$$

> **Check:** after dividing, the bracket must have **no** common factor. If it
> does, you didn't finish.

### 3.2 Difference of squares

$$a^2 - b^2 = (a-b)(a+b)$$

$$x^2 - 49 = (x-7)(x+7)$$
$$4x^2 - 25 = (2x-5)(2x+5)$$
$$9x^4 - 4x^2 = x^2(3x-2)(3x+2)$$

> **Trap:** $a^2 + b^2$ does **not** factor. `4x² + 25` is already complete.
> The $+$ form has no middle term to supply.

### 3.3 Perfect square trinomial

$$a^2 \pm 2ab + b^2 = (a \pm b)^2$$

$$x^2 + 10x + 25 = (x+5)^2 \qquad x^2 - 14x + 49 = (x-7)^2$$

Test it: is the middle term exactly $\pm 2ab$? `x² − 2x + 1` → yes. `x² + 2x + 1` → yes.

### 3.4 Trinomial $x^2 + bx + c$ — find two numbers

You need $m, n$ with:

$$m + n = b \qquad mn = c$$

| $c$ | $b$ | signs | example |
|---|---|---|---|
| $+$ | $+$ | both $+$ | $x^2+5x+6 \to (x+2)(x+3)$ |
| $+$ | $-$ | both $-$ | $x^2-5x+6 \to (x-2)(x-3)$ |
| $-$ | any | opposite | $x^2+x-6 \to (x+3)(x-2)$ |

*Why it works:* $(x+m)(x+n) = x^2 + (m+n)x + mn$. The expansion **forces** both
conditions. If no pair satisfies both, it does not factor.

### 3.5 Trinomial $ax^2 + bx + c$ — the $ac$ trick

1. Compute $a \cdot c$.
2. Find two numbers with **that product** and with **sum $b$**.
3. Split the middle term into those two.
4. Group, factor each group.

$$6x^2 + 11x + 3$$

$$ac = 6\cdot3 = 18 \qquad \text{product }18,\ \text{sum }11 \;\Rightarrow\; 9 \text{ and } 2$$

$$6x^2 + \underbrace{9x + 2x}_{9+2=11} + 3 = 3x(2x+3) + 1(2x+3) = (3x+1)(2x+3)$$

More:

$$2x^2+7x+3:\ ac=6,\ \{6,1\} \Rightarrow 2x(x+3)+1(x+3) = (2x+1)(x+3)$$
$$3x^2-10x+8:\ ac=24,\ \{-6,-4\} \Rightarrow 3x(x-2)-4(x-2) = (3x-4)(x-2)$$

> **Trap:** splitting $b$ arbitrarily. `4x² + 4x − 3` has $ac = -12$ and $b = 4$,
> so the split is $6 + (-2)$, **not** $1 + 3$. Always list the pairs of $ac$.

*Why $ac$ works:* splitting $b$ into $m+n$ only produces a factorable quadratic
when $mn = ac$.

### 3.6 Grouping (four or more terms)

$$x^3 + 5x^2 + 2x + 10 = x^2(x+5) + 2(x+5) = (x^2+2)(x+5)$$
$$2x^3 - 8x^2 - 5x + 20 = 2x^2(x-4) - 5(x-4) = (x-4)(2x^2-5)$$

> **Rule:** pair $x^3$ with $x^2$, and $x$ with the constant. Pairing $x^3$ with
> the constant shares nothing.

### 3.7 Sum and difference of cubes

$$a^3 + b^3 = (a+b)(a^2 - ab + b^2)$$
$$a^3 - b^3 = (a-b)(a^2 + ab + b^2)$$

The signs **inside** are opposite to the sign **outside**.

$$x^3 - 27 = (x-3)(x^2+3x+9)$$
$$8x^3 + 125 = (2x+5)(4x^2-10x+25)$$

### 3.8 Substitution

If the variable sits inside a power, let the power be the new variable.

$$x^4 - 10x^2 + 9$$

Let $u = x^2$, so $u^2 - 10u + 9 = (u-1)(u-9)$.

Substitute back:

$$= (x^2-1)(x^2-9) = (x-1)(x+1)(x-3)(x+3)$$

> This is the same $x^2+bx+c$ method wearing a disguise. It appears constantly in
> linear algebra (diagonalisation), so learn it now.

---

## 4. Rational expressions

**Cancel factors, never sums.**

$$\frac{3x}{x} = 3 \qquad\qquad \frac{x+2}{x} \neq 2$$

$$\frac{x^2+4}{x^2} = 1 + \frac{4}{x^2}$$

Simplify by splitting numbers and variables:

$$\frac{12x^5y^3}{4x^2y} = \frac{12}{4}\cdot x^{5-2} y^{3-1} = 3x^3y^2$$

$$\frac{2x^3y^2}{4xy^5} = \frac{x^2}{2y^3}$$

**Multiplying and dividing:**

$$\frac{a}{b}\cdot\frac{c}{d} = \frac{ac}{bd} \qquad
\frac{a}{b}\div\frac{c}{d} = \frac{a}{b}\cdot\frac{d}{c}$$

**Rationalising** (getting rid of a radical denominator):

$$\frac{1}{\sqrt2}\cdot\frac{\sqrt2}{\sqrt2} = \frac{\sqrt2}{2}$$

---

## 5. Radicals and absolute value

$$\sqrt{ab} = \sqrt a\,\sqrt b \qquad \sqrt{25x^2} = 5|x|$$

> The $|x|$ is not optional. $\sqrt{x^2} = x$ is **false** for $x<0$.

$$\sqrt{12} = 2\sqrt3 \qquad \sqrt{50} = 5\sqrt2$$

$$|x| = \text{distance from } 0 \qquad |5| = 5 \qquad |-5| = 5$$

$$|x| = 5 \;\Rightarrow\; x = 5 \text{ or } x = -5$$

---

## 6. Logarithms

$$\log_b(x) = y \iff b^y = x$$

$$\log_b(xy) = \log_b x + \log_b y \qquad
\log_b\!\left(\frac{x}{y}\right) = \log_b x - \log_b y \qquad
\log_b(x^n) = n\log_b x$$

---

## 7. Solving equations

| type | move |
|---|---|
| $3x+5=20$ | subtract 5, divide 3 |
| $2(x-3)=4x+8$ | expand first, then collect |
| $\dfrac{x+2}{3}=\dfrac{2x-1}{5}$ | cross-multiply: $5(x+2)=3(2x-1)$ |
| $-2x > 6$ | dividing by a negative **flips** the inequality |

**Quadratic formula** (when factoring fails):

$$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a} \qquad \Delta = b^2-4ac$$

$\Delta > 0$ two roots, $=0$ one root, $<0$ no real roots.

---

## 8. Completing the square — the bridge to linear algebra

Worth learning now because it is *the* idea behind orthogonal projection and
least squares later.

$$x^2 + 6x + 5$$

Complete: take half the coefficient of $x$, square it, add and subtract.

$$= \left(x^2 + 6x + 9\right) - 9 + 5 = (x+3)^2 - 4 = 0$$

$$(x+3)^2 = 4 \;\Rightarrow\; x = -3 \pm 2 \;\Rightarrow\; x = -1 \text{ or } -5$$

> You have seen this before: "completing the square" is the same move as
> "finding the $R$ in $QR$ decomposition", i.e. orthogonalisation.

---

## 9. Systems of linear equations

### The three cases

| condition | result | looks like |
|---|---|---|
| $\det(A)\neq 0$ | **unique** solution | pivots in every column |
| $\det(A)=0$, consistent | **infinitely many** | a $0=0$ row |
| $\det(A)=0$, inconsistent | **no** solution | a $0=k$, $k\neq0$ row |

Geometrically: lines **cross once**, are the **same line twice**, or are
**parallel**.

### Substitution

$$\begin{cases} 2x + 3y = 7 \\ 4x - y = 5 \end{cases}$$

From (2): $y = 4x-5$. Into (1):

$$2x + 3(4x-5) = 7 \;\Rightarrow\; 14x = 22 \;\Rightarrow\; x = \tfrac{11}{7},\quad y = \tfrac{9}{7}$$

### Elimination

Multiply rows to make a column match, then add (or subtract) to kill it.

$$\begin{cases} 2x + 3y = 7 \\ 4x - y = 5 \end{cases}
\;\xrightarrow{\;R_2 \to R_2 - 2R_1\;}\;
\begin{cases} 2x + 3y = 7 \\ 0x - 7y = -9 \end{cases}
\;\Rightarrow\; y = \tfrac97,\; x = \tfrac{11}{7}$$

### Cramer's rule (2×2 only)

$$x = \frac{\begin{vmatrix} b_1 & a_{12} \\ b_2 & a_{22}\end{vmatrix}}{\det A}
\qquad
y = \frac{\begin{vmatrix} a_{11} & b_1 \\ a_{21} & b_2\end{vmatrix}}{\det A}$$

Only valid when $\det A \neq 0$.

---

## 10. Matrices — the basics you need first

### What a matrix *is*

A rectangular array of numbers. Nothing more. Row $i$, column $j$ is the entry $a_{ij}$.

$$A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$$

### Matrix multiplication

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{bmatrix} e & f \\ g & h \end{bmatrix}
=
\begin{bmatrix} ae+bg & af+bh \\ ce+dg & cf+dh \end{bmatrix}$$

Row-by-column. Not commutative: $AB \neq BA$ in general.

### Transpose

$$A^T = \begin{bmatrix} a & c \\ b & d \end{bmatrix}
\quad\text{iff}\quad
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$

$$(AB)^T = B^TA^T \qquad (A^T)^T = A$$

### Identity and inverse

$$I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\qquad AI = IA = A$$

$$A^{-1} = \frac{1}{\det A}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
\quad\text{(2×2 only)}$$

$A$ is invertible **iff** $\det A \neq 0$.

### Row reduction

Augment with a bar, then only these three moves (all preserve the solution set):

1. swap two rows
2. multiply a row by a nonzero scalar
3. add a multiple of one row to another

$$\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 2 & -1 & 3 \end{array}\right]
\xrightarrow{R_2 - 2R_1}
\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & -5 & -7 \end{array}\right]
\xrightarrow{-\frac{1}{5}R_2}
\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & 1 & \tfrac{7}{5} \end{array}\right]
\xrightarrow{R_1 - 2R_2}
\left[\begin{array}{cc|c} 1 & 0 & \tfrac{1}{5} \\ 0 & 1 & \tfrac{7}{5} \end{array}\right]$$

Read the solution off the last column: $x = \tfrac{1}{5}$, $y = \tfrac{7}{5}$.

> **You may swap and scale rows, never columns.** Row operations preserve the
> solution set; column operations change the problem.

---

## 11. Vectors

$$\mathbf{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$$

An **arrow**: magnitude *and* direction. Order matters —
$\begin{bmatrix}3\\2\end{bmatrix} \neq \begin{bmatrix}2\\3\end{bmatrix}$.

| | |
|---|---|
| magnitude | $\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots}$ |
| dot product | $\mathbf{u}\cdot\mathbf{v} = u_1v_1 + u_2v_2 + \cdots$ |
| orthogonal | $\mathbf{u}\cdot\mathbf{v} = 0$ |
| linear combination | $a\mathbf{v}_1 + b\mathbf{v}_2$ |
| span | all linear combinations |

$$\begin{bmatrix}3\\2\end{bmatrix}\cdot\begin{bmatrix}4\\-6\end{bmatrix} = 12 - 12 = 0$$

### Span, independence, basis, dimension

- **Span** of a set: every linear combination of them.
- **Independent**: no vector in the set is a combination of the others.
- **Basis**: $n$ independent vectors in $\mathbb{R}^n$.
- **Dimension**: size of a basis — always $n$ in $\mathbb{R}^n$.

### Linear transformation

Preserves addition and scalar multiplication:

$$T(\mathbf{u}+\mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})
\qquad T(c\mathbf{u}) = c\,T(\mathbf{u})$$

Every linear map on $\mathbb{R}^n$ **is** multiplication by a single matrix. The
matrix is the transformation.

---

## 12. Determinants

Expand along a row. For $3\times3$, expand along the first row — signs alternate:

$$+ \;\; - \;\; +$$

$$\det\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}
= a(ei-fh) - b(di-fg) + c(dh-eg)$$

$\det = 0$ means: **singular**, rows/columns linearly dependent, not invertible,
and $A\mathbf{x}=\mathbf{b}$ has no unique solution.

---

## 13. Eigenvalues and eigenvectors

**Eigenvalues** come from the determinant:

$$\det(A - \lambda I) = 0 \qquad \text{use } A-\lambda I, \text{ not } A+\lambda I$$

**Eigenvectors** come from the null space:

$$(A - \lambda I)\mathbf{v} = \mathbf{0}$$

Row reduce $A-\lambda I$ and read off the free variable. Any nonzero multiple
works.

**Geometrically:** $A\mathbf{v} = \lambda\mathbf{v}$ means $\mathbf{v}$ is only
**scaled** — the direction is unchanged. Every other direction gets rotated or
sheared. A negative $\lambda$ flips that direction $180°$.

A repeated eigenvalue may give only one independent eigenvector — then the
matrix is **not diagonalisable**.

---

## 14. The bridge

This is the conceptual jump that trips everyone.

| | Elementary algebra | Linear algebra |
|---|---|---|
| question | what is $x$? | what happens to a whole space? |
| object | a number | a vector, a subspace |
| notation | $3x+5=20$ | $A\mathbf{x}=\mathbf{b}$ |
| method | manipulate one equation | transform $\mathbb{R}^n$ |
| answer | a value | a mapping |

The path:

```
arithmetic
  → variables, equations
    → systems of equations          ← 2 unknowns now
      → matrices                     ← store the coefficients
        → row reduction              ← solve many systems at once
          → vectors & subspaces      ← the objects themselves
            → linear transformations ← matrices as actions
              → eigenvalues          ← the directions that survive
```

You do **not** need to master all of mathematics first. You need: arithmetic →
elementary algebra → functions → coordinate geometry. Then this sheet is enough.

---

## 15. Error table — the ones that actually happen

| what you did | why it's wrong | instead |
|---|---|---|
| $\frac{x+2}{x} = 2$ | you cancelled a sum | $1 + \frac{2}{x}$ |
| $(x+2)^2 = x^2+4$ | dropped the middle term | $x^2+4x+4$ |
| $\sqrt{x^2} = x$ | only true for $x \ge 0$ | $5\|x\|$ style: $\sqrt{25x^2}=5\|x\|$ |
| $2x^2 + x^3 = 3x^5$ | added exponents in a sum | leave it; it's simplified |
| $-(x-3) = -x-3$ | minus didn't distribute | $-x+3$ |
| $-2x > 6 \Rightarrow x > -3$ | didn't flip | $x < -3$ |
| $\frac{2x^3}{4x^2} = \frac{x^2}{2}$ | mixed up which way | $x^{3-2}\cdot\frac{2}{4} = \frac{x}{2}$ |
| split $b$ as $1+3$ when $ac=-12$ | arbitrary split | list the pairs of $ac$ |

---

## 16. Where to practise

| what | where |
|---|---|
| infinite problems, graded, worked steps | `./run.sh` in `~/Work/algebra-lab` |
| same thing in the terminal | `./run.sh factoring --practice` |
| rules under time pressure | Anki, deck `Algebra Lab` |
| see what a matrix *does* | GeoGebra, menu → Math |

Start at section 2 and work down. Drill section 3 until the decision tree is
automatic — that is the whole game.
