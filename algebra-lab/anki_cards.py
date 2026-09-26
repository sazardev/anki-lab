#!/usr/bin/env python3
"""Build the Algebra Lab Anki decks.

Card design
-----------
Every card asks exactly one question and answers it in as few words as
possible. Three question types, taggable so you can drill one kind at a time:

    q::what   what IS this?      (concept, definition, notation)
    q::do     what does it DO?   (purpose, when to reach for it)
    q::how    how do I USE it?   (procedure, worked micro-example)

Topic tags are hierarchical, so Anki's tag search works as a tree:

    algebra::fractions::add
    algebra::factoring::trinomial
    la::eigenvalues

Math is written for Anki's built-in MathJax: \\( ... \\) inline, \\[ ... \\]
for display. The editor shortcut is Ctrl+M.

Idempotent: re-running syncs the decks instead of duplicating notes.
"""

from __future__ import annotations

import sys
from pathlib import Path

DECK = "Algebra Lab"
COLLECTION = Path.home() / ".local/share/Anki2/User 1/collection.anki2"


def m(s: str) -> str:
    """Inline math for MathJax."""
    return "\\(" + s + "\\)"


def d(s: str) -> str:
    """Display math."""
    return "\\[" + s + "\\]"


def A(s: str) -> str:
    """A worked answer on its own line."""
    return d(s)


CARDS: list[tuple[str, str, str]] = []


def C(tags: str, front: str, back: str) -> None:
    CARDS.append((tags, front.strip(), back.strip()))


# =====================================================================
# 1. ARITHMETIC
# =====================================================================

C("q::what arithmetic::fractions",
  "What is a fraction's denominator?",
  "The <b>bottom</b> number. It tells you <i>how many equal parts</i> the whole "
  "is split into. " + m(r"\frac{3}{4}") + " means 3 parts out of 4.")

C("q::what arithmetic::fractions",
  "What does " + m(r"\frac{a}{b}") + " actually <i>mean</i>?",
  A(r"\frac{a}{b} = a \div b")
  + "For " + m(r"\frac{3}{4}") + " it is <b>3 divided by 4</b>, or <i>3 out of 4</i>. "
  "It is <b>not</b> a division waiting to happen &mdash; it is a number.")

C("q::how arithmetic::fractions::reduce",
  "Reduce to lowest terms: " + m(r"\frac{18}{24}"),
  A(r"\frac{18\div 6}{24\div 6} = \mathbf{\frac{3}{4}}")
  + "Divide both by the GCF. Always check the answer multiplies back.")

C("q::how arithmetic::fractions::reduce",
  "Reduce to lowest terms: " + m(r"\frac{45}{60}"),
  A(r"\frac{45\div 15}{60\div 15} = \mathbf{\frac{3}{4}}")
  + "GCF is 15, not 5 &mdash; check both are still divisible by 3.")

C("q::do arithmetic::fractions::reduce",
  "How do you reduce a fraction to lowest terms?",
  "Divide <b>both</b> numerator and denominator by their GCF. "
  "Never subtract. Never divide only one.")

C("q::how arithmetic::fractions::compare",
  "Which is bigger: " + m(r"\frac{3}{4}") + " or " + m(r"\frac{5}{8}") + "?",
  A(r"\frac{3}{4} = \frac{6}{8} > \frac{5}{8}")
  + "<b>Never</b> compare by eyeballing the numbers. Get a common denominator first.")

C("q::how arithmetic::fractions::compare",
  "Which is bigger: " + m(r"\frac{7}{10}") + " or " + m(r"\frac{2}{3}") + "?",
  A(r"\frac{7}{10} = \frac{21}{30}, \qquad \frac{2}{3} = \frac{20}{30}")
  + m(r"\frac{21}{30} > \frac{20}{30}") + ", so " + m(r"\mathbf{\frac{7}{10}}") + " is bigger.")

C("q::how arithmetic::fractions::add",
  m(r"\frac{1}{2} + \frac{1}{3}"),
  A(r"\frac{3}{6} + \frac{2}{6} = \mathbf{\frac{5}{6}}")
  + "Same denominator? Add numerators. Different? Make them the same first.")

C("q::how arithmetic::fractions::add",
  m(r"\frac{2}{3} + \frac{1}{4}"),
  A(r"\frac{8}{12} + \frac{3}{12} = \mathbf{\frac{11}{12}}")
  + "LCD of 3 and 4 is 12.")

C("q::how arithmetic::fractions::add",
  m(r"\frac{3}{4} - \frac{5}{6}"),
  A(r"\frac{9}{12} - \frac{10}{12} = \mathbf{-\frac{1}{12}}")
  + "A negative answer is fine. Do not panic and flip it.")

C("q::how arithmetic::fractions::add",
  m(r"1\frac{2}{3} + 2\frac{1}{4}"),
  A(r"\frac{5}{3} + \frac{9}{4} = \frac{20}{12} + \frac{27}{12} = \mathbf{\frac{47}{12}} = 3\frac{11}{12}")
  + "Convert the mixed numbers to improper fractions <b>first</b>.")

C("q::how arithmetic::fractions::multiply",
  m(r"\frac{3}{4} \times \frac{5}{7}"),
  A(r"\frac{3\cdot 5}{4\cdot 7} = \mathbf{\frac{15}{28}}")
  + "Multiply straight across, then reduce. <b>Never</b> cross-cancel first "
  "unless you want an easier time.")

C("q::how arithmetic::fractions::multiply",
  m(r"\frac{2}{3} \div \frac{4}{5}"),
  A(r"\frac{2}{3} \times \frac{5}{4} = \mathbf{\frac{5}{6}}")
  + "Division by a fraction means <b>multiply by its reciprocal</b>.")

C("q::do arithmetic::fractions::multiply",
  "What is <b>cross-cancelling</b> and when is it useful?",
  "Cancelling a factor across the " + m(r"\times") + " before multiplying.<br>"
  + m(r"\frac{2\cdot 9}{3\cdot 4} = \frac{2\cdot 3}{3\cdot 4} = \frac{1}{2}")
  + "Use it when the numbers are ugly. It never changes the answer.")

C("q::what arithmetic::fractions",
  m(r"\frac{a}{b} + \frac{c}{d}"),
  "The rule that makes fraction addition possible:<br>"
  + A(r"\frac{ad}{bd} + \frac{bc}{bd} = \mathbf{\frac{ad+bc}{bd}}")
  + "Multiply <b>up</b> and <b>across</b>.")

C("q::do arithmetic::fractions::add",
  "How do you add fractions with different denominators?",
  "1. Find the LCD (least common denominator)<br>"
  "2. Rewrite each fraction over the LCD &mdash; multiply top and bottom<br>"
  "3. Add the numerators, keep the denominator<br>"
  "4. Reduce<br>"
  + "<b>Never</b> add the denominators.")

C("q::what arithmetic::percent",
  "What does " + m(r"x\%") + " mean and how do you get the number back?",
  A(r"x\% = \frac{x}{100}, \qquad x = y\% \iff y = x \cdot \frac{p}{100}")
  + "To find " + m(r"p\%") + " <b>of</b> something, multiply by " + m(r"\frac{p}{100}") + ".")

C("q::how arithmetic::percent",
  "What is 15% of 80?",
  A(r"80 \times \frac{15}{100} = 12")
  + "Multiply, then divide by 100 &mdash; or move the decimal two places left.")

C("q::how arithmetic::percent",
  "You scored 18 of 25 questions. What percent is that?",
  A(r"\frac{18}{25}\times 100 = 72\%")
  + "The word <b>of</b> always means multiply. " + m(r"\frac{18}{25}") + " is the "
  "fraction; " + m(r"72\%") + " is the answer.")

C("q::how arithmetic::percent",
  "A price rises 20% then falls 20%. Is it back to the original?",
  "<b>No.</b><br>" + A(r"100 \to 120 \to 120\cdot 0.8 = 96")
  + "Percent changes do not cancel unless the percentages match exactly. "
  "A rise and fall of the <i>same</i> percent always lands below the start.")

C("q::what arithmetic::order",
  "State the order of operations.",
  A(r"\textbf{Parentheses} \to \textbf{Exponents} \to \textbf{Mult/Div} \to \textbf{Add/Sub}")
  + "Say it as a phrase: <b>Please Excuse My Dear Aunt Sally</b>.")

C("q::how arithmetic::order",
  "Evaluate: " + m(r"2 + 3 \times 4^2 - 6 \div 2"),
  A(r"2 + 3\cdot 16 - 3 = 2 + 48 - 3 = \mathbf{47}")
  + "Exponent, then the two multiplications, then left to right.")

C("q::pitfall arithmetic::order",
  "Which is right: " + m(r"-4^2") + " or " + m(r"(-4)^2") + "?",
  A(r"-4^2 = -16 \qquad (-4)^2 = 16")
  + "An exponent grabs only what is immediately to its left. The sign is not "
  "part of the base unless brackets say so.")

C("q::pitfall arithmetic::order",
  "Someone writes " + m(r"2 + 3 = 5^2 = 25") + " as a chain. What is wrong?",
  "In algebra " + m(r"=") + " means <b>is exactly equal to</b>, not <i>becomes</i>.<br>"
  + m(r"2+3 = 5") + " is true. " + m(r"5 = 25") + " is false, so the chain is broken.<br>"
  "To chain steps, start a <b>new line</b> with the variable: "
  + m(r"x = 2+3") + "<br>" + m(r"x = 5") + ".")

C("q::what arithmetic::signs",
  "The four sign rules for multiplication, in one line.",
  A(r"(+)(+) = + \quad (-)(-) = + \quad (+)(-) = - \quad (-)(+) = -")
  + "Same signs give positive. Different give negative. Division follows the same rule.")

C("q::how arithmetic::signs",
  "Compute: " + m(r"(-3)^4 - (-2)^3"),
  A(r"81 - (-8) = \mathbf{89}")
  + m(r"(-3)^4") + " is positive (even power), " + m(r"(-2)^3") + " is negative (odd).")

C("q::how arithmetic::signs",
  "Compute: " + m(r"-3^4 + (-3)^4"),
  A(r"-81 + 81 = \mathbf{0}")
  + "Same number, different meaning. A great trap.")

C("q::do arithmetic::signs",
  "How do you handle the negative sign in " + m(r"-(x + 5)") + "?",
  "Distribute it to <b>every</b> term: " + A(r"-(x+5) = -x - 5")
  + "The sign does not stop at the bracket.")

# =====================================================================
# 2. EXPRESSIONS
# =====================================================================

C("q::what algebra::terms",
  "What is a <b>term</b>?",
  "A single piece separated by <b>+</b> or " + m(r"\pm") + " signs.<br>"
  + m(r"3x^2 - 5y + 7") + " has <b>three</b> terms: " + m(r"3x^2") + ", " + m(r"-5y") + ", " + m(r"7") + ".")

C("q::what algebra::like",
  "What makes two terms <b>like terms</b>?",
  "The <b>same variable part</b> &mdash; same letters, same powers.<br>"
  + m(r"3x") + " and " + m(r"5x") + " are like. " + m(r"3x") + " and " + m(r"3x^2") + " are not.")

C("q::do algebra::like",
  "Can you combine " + m(r"3x^2") + " and " + m(r"4x") + "?",
  "<b>No.</b> Different powers, so they are not like terms. "
  + m(r"3x^2 + 4x") + " is already fully simplified.")

C("q::how algebra::like",
  "Simplify: " + m(r"5x - 3x + 2 + 7x - 1"),
  A(r"(5-3+7)x + (2-1) = \mathbf{9x + 1}")
  + "Collect the " + m(r"x") + " terms, then the constants.")

C("q::do algebra::distribute",
  "What does the distributive property let you do?",
  A(r"a(b+c) = ab + ac")
  + "Multiply one factor by a <b>sum</b> by multiplying each term inside. "
  "It is the definition of multiplication &mdash; it lets you remove brackets.")

C("q::how algebra::distribute",
  "Expand: " + m(r"4(2x - 3y + 5)"),
  A(r"8x - 12y + \mathbf{20}")
  + "The 4 multiplies <b>every</b> term, including the constant.")

C("q::how algebra::distribute",
  "Expand: " + m(r"-(3x - 2)"),
  A(r"\mathbf{-3x + 2}")
  + "The leading minus multiplies everything. " + m(r"-x+2") + ", not " + m(r"-x-2") + ".")

C("q::how algebra::distribute",
  "Expand: " + m(r"-2(3 - 4x)"),
  A(r"\mathbf{4x - 6}")
  + m(r"-2\cdot 3 = -6") + " and " + m(r"-2\cdot(-4x) = 8x") + ". Two sign flips.")

C("q::how algebra::distribute",
  "Expand: " + m(r"x(2x - 3)(x + 1)"),
  A(r"x(2x^2 - x - 3) = \mathbf{2x^3 - x^2 - 3x}")
  + "Multiply the binomials first, then distribute. Fewer terms to track.")

C("q::pitfall algebra::distribute",
  "Why is " + m(r"-(x-5) = -x-5") + " wrong?",
  A(r"-(x-5) = -x + \mathbf{5}")
  + "The minus flips the sign of the second term too. This is the most common "
  "sign error in all of algebra.")

C("q::how algebra::evaluate",
  "Evaluate " + m(r"3x^2 - 2x + 1") + " at " + m(r"x = -2"),
  A(r"3(4) - 2(-2) + 1 = 12 + 4 + 1 = \mathbf{17}")
  + "Brackets the negative first. " + m(r"x^2 = 4") + " but " + m(r"-2x = -4") + ".")

C("q::how algebra::evaluate",
  "Evaluate " + m(r"\frac{x^2 - 1}{x - 1}") + " at " + m(r"x = 5"),
  A(r"\frac{25-1}{5-1} = \frac{24}{4} = \mathbf{6}")
  + "Substitute straight in. (You can also cancel to " + m(r"x+1") + " first &mdash; "
  "but only if " + m(r"x \neq 1") + ".)")

C("q::pitfall algebra::evaluate",
  "You substitute " + m(r"x = -2") + " into " + m(r"x^2") + " and write " + m(r"-4") + ". Correct?",
  "<b>No.</b> " + A(r"(-2)^2 = +4")
  + "The exponent applies to " + m(r"-2") + " here because it is the base. "
  "Write the brackets.")

# =====================================================================
# 3. FRACTIONS IN ALGEBRA (deep)
# =====================================================================

C("q::what algebra::fractions::rational",
  "What is a <b>rational expression</b>?",
  "Any ratio of two polynomials, like " + m(r"\frac{x+2}{x-3}") + ".<br>"
  "The variables may appear in the denominator &mdash; that is the whole difference "
  "from arithmetic.")

C("q::do algebra::fractions::domain",
  "Why must you never set a denominator to zero?",
  m(r"\frac{1}{0}") + " is <b>undefined</b>, not infinity.<br>"
  "So " + m(r"\frac{x+2}{x-3}") + " has " + m(r"x \neq 3") + ".<br>"
  "The fraction is the <b>function</b> " + m(r"\frac{1}{x}") + " &mdash; it is a rule, "
  "and the rule has a hole where it breaks.")

C("q::how algebra::fractions::domain",
  "Find the domain of " + m(r"\frac{x+1}{x^2 - 4}") + ".",
  "Set the denominator to zero and exclude those:<br>"
  + A(r"x^2 - 4 = (x-2)(x+2) = 0 \;\Rightarrow\; x = 2,\; x = -2")
  + "Domain excludes " + m(r"\mathbf{x \neq 2, -2}") + ".")

C("q::how algebra::fractions::domain",
  "Find the domain of " + m(r"\frac{2}{x} + \frac{1}{x+1}") + ".",
  "<b>Both</b> denominators count, not just the first.<br>"
  + A(r"x \neq 0 \quad \textbf{and} \quad x \neq -1")
  + "A sum of fractions needs every denominator non-zero.")

C("q::do algebra::fractions::cancel",
  "What can be cancelled in a fraction?",
  "<b>Only factors.</b> " + m(r"\frac{3x}{x} = 3") + " because " + m(r"x") + " is a factor.<br>"
  + m(r"\frac{x+2}{x} \neq 2") + " because " + m(r"x+2") + " is a <b>sum</b>.<br>"
  "The cancellation test: does the expression split into a product at all?")

C("q::pitfall algebra::fractions::cancel",
  "Simplify " + m(r"\frac{x^2 - 4}{x - 2}") + ".",
  A(r"\frac{(x-2)(x+2)}{x-2} = \mathbf{x+2}")
  + "<b>But</b> only for " + m(r"x \neq 2") + ". At " + m(r"x = 2") + " the original is "
  + m(r"\frac{0}{0}") + " &mdash; undefined. Cancelling gives a <i>hole</i>, not a value.")

C("q::how algebra::fractions::cancel",
  "Simplify " + m(r"\frac{x^2 - 9}{x^2 + 6x + 9}") + ".",
  A(r"\frac{(x-3)(x+3)}{(x+3)^2} = \frac{x-3}{x+3}")
  + "One " + m(r"(x+3)") + " cancels, leaving one. Restriction: " + m(r"x \neq -3") + ".")

C("q::pitfall algebra::fractions::cancel",
  "Can you cancel " + m(r"x") + " in " + m(r"\frac{x^2 + 4x}{x}") + "?",
  "No &mdash; but you can factor first:<br>"
  + A(r"\frac{x(x+4)}{x} = \mathbf{x+4}")
  + "Cancelling is a <b>factoring</b> step. The numerator has to be a product before "
  "you may cancel anything.")

C("q::how algebra::fractions::add",
  "Simplify: " + m(r"\frac{1}{x} + \frac{1}{y}"),
  A(r"\frac{y}{xy} + \frac{x}{xy} = \mathbf{\frac{x+y}{xy}}")
  + "LCD here is " + m(r"xy") + ". Multiply up and across.")

C("q::how algebra::fractions::add",
  "Simplify: " + m(r"\frac{1}{x-1} + \frac{1}{x+1}"),
  A(r"\frac{x+1}{x^2-1} + \frac{x-1}{x^2-1} = \mathbf{\frac{2x}{x^2-1}}")
  + "The LCD is the product, but <b>factor it</b>: " + m(r"x^2-1 = (x-1)(x+1)") + ".")

C("q::how algebra::fractions::subtract",
  "Simplify: " + m(r"\frac{2}{x-2} - \frac{5}{x+3}"),
  A(r"\frac{2(x+3)}{x^2+x-6} - \frac{5(x-2)}{x^2+x-6} = \mathbf{\frac{-3x + 16}{x^2+x-6}}")
  + "Change the sign of <b>every</b> term in the second numerator, then combine.")

C("q::pitfall algebra::fractions::subtract",
  "In " + m(r"\frac{1}{x} - \frac{1}{y}") + ", what must you do to the second term?",
  "<b>Negate both</b> numerator and denominator:<br>"
  + A(r"\frac{1}{x} - \frac{1}{y} = \frac{1}{x} + \frac{-1}{y}")
  + "The minus in front applies to the <i>whole</i> fraction. Then use the addition rule.")

C("q::how algebra::fractions::complex",
  "Simplify: " + m(r"\frac{\frac{1}{x}}{\frac{2}{y}}"),
  A(r"\frac{1}{x} \times \frac{y}{2} = \mathbf{\frac{y}{2x}}")
  + "A fraction in a denominator means <b>multiply by the reciprocal</b>. Twice.")

C("q::how algebra::fractions::complex",
  "Simplify: " + m(r"\frac{1 - \frac{1}{x}}{1 + \frac{1}{x}}"),
  "Multiply top and bottom by " + m(r"x") + " to clear the inner fractions:<br>"
  + A(r"\frac{\frac{x-1}{x}}{\frac{x+1}{x}} = \frac{x-1}{x}\cdot\frac{x}{x+1} = \mathbf{\frac{x-1}{x+1}}")
  + "<b>Multiply both by the same thing.</b> That is the universal escape hatch.")

C("q::do algebra::fractions::complex",
  "You have nested fractions. What always works?",
  "<b>Multiply the top and bottom of the whole thing by the common denominator.</b> "
  "It is the one move that always clears every fraction at once.")

C("q::how algebra::fractions::mixed",
  "Write as an improper fraction: " + m(r"2\frac{3}{4}"),
  A(r"2\frac{3}{4} = \frac{2\cdot 4 + 3}{4} = \mathbf{\frac{11}{4}}")
  + "<b>Multiply</b> the whole part by the denominator, <b>add</b> the numerator.")

C("q::how algebra::fractions::mixed",
  "Write as a mixed number: " + m(r"\frac{23}{5}"),
  A(r"23 \div 5 = 4\text{ r }3 \;\Rightarrow\; \mathbf{4\frac{3}{5}}")
  + "Divide, keep the remainder over the original denominator.")

C("q::pitfall algebra::fractions::mixed",
  "Convert " + m(r"1\frac{2}{3}") + " to a fraction. Common wrong answer?",
  A(r"1\frac{2}{3} = \frac{1\cdot 3 + 2}{3} = \mathbf{\frac{5}{3}}")
  + "The wrong answer " + m(r"\frac{7}{3}") + " comes from <b>adding</b> instead of multiplying.")

# =====================================================================
# 4. EXPONENTS AND RADICALS
# =====================================================================

C("q::what algebra::exponents",
  "What is a <b>power</b>, and what do the parts mean?",
  A(r"a^n")
  + m(r"a") + " is the <b>base</b> (the thing being multiplied), "
  + m(r"n") + " is the <b>exponent</b> (how many copies).")

C("q::do algebra::exponents::multiply",
  "Rule for " + m(r"x^a \cdot x^b") + "?",
  A(r"x^a\cdot x^b = \mathbf{x^{a+b}}")
  + "<b>Add</b> the exponents. Only works for the <b>same base</b>.")

C("q::do algebra::exponents::divide",
  "Rule for " + m(r"\frac{x^a}{x^b}") + "?",
  A(r"\frac{x^a}{x^b} = \mathbf{x^{a-b}}")
  + "<b>Subtract</b>. Exponents follow the same signs as the terms.")

C("q::do algebra::exponents::power",
  "Rule for " + m(r"(x^a)^b") + "?",
  A(r"(x^a)^b = \mathbf{x^{ab}}")
  + "<b>Multiply</b> the exponents.")

C("q::pitfall algebra::exponents::power",
  "Is " + m(r"(x^2)^3") + " the same as " + m(r"x^{2^3}") + "?",
  "<b>No.</b><br>"
  + A(r"(x^2)^3 = x^{2\cdot 3} = x^6 \qquad x^{2^3} = x^8")
  + "Brackets mean multiply. A bare exponent means <i>evaluate the exponent first</i>.")

C("q::do algebra::exponents::product",
  "Rule for " + m(r"(ab)^n") + "?",
  A(r"(ab)^n = \mathbf{a^n b^n}")
  + "The power applies to <b>every</b> factor, not just the first.")

C("q::do algebra::exponents::fraction",
  "Rule for " + m(r"\left(\frac{a}{b}\right)^n") + "?",
  A(r"\left(\frac{a}{b}\right)^n = \mathbf{\frac{a^n}{b^n}}")
  + "Numerator and denominator are raised independently.")

C("q::what algebra::exponents",
  m(r"x^0"),
  A(r"x^0 = \mathbf{1}")
  + "Because " + m(r"\frac{x}{x} = 1") + " for any " + m(r"x \neq 0") + ". "
  "Holds for <b>any</b> base including negatives: " + m(r"(-5)^0 = 1") + ".")

C("q::what algebra::exponents",
  m(r"x^{-n}"),
  A(r"x^{-n} = \mathbf{\frac{1}{x^n}}")
  + "A negative exponent does not make a negative number &mdash; it puts the base "
  "on the bottom.")

C("q::how algebra::exponents::neg",
  "Simplify: " + m(r"\frac{x^4}{x^7}") + " and " + m(r"x^{-3}") + " rewritten",
  A(r"\frac{x^4}{x^7} = \mathbf{x^{-3}} = \mathbf{\frac{1}{x^3}}")
  + "Subtract to get a negative exponent, then flip it to the bottom.")

C("q::how algebra::exponents::expand",
  "Expand: " + m(r"(2x^3)^2 \cdot (4x)^3"),
  A(r"4x^6 \cdot 64x^3 = \mathbf{256x^9}")
  + "Raise each bracket, then multiply: coefficients multiply, exponents add.")

C("q::pitfall algebra::exponents",
  "Why can you not combine " + m(r"x^2 + x^3") + "?",
  "The exponent rules come from <b>multiplication</b>, not addition.<br>"
  + A(r"x^2\cdot x^3 = x^5 \quad\text{but}\quad x^2 + x^3 \neq x^5")
  + "There is no addition rule. " + m(r"x^2+x^3") + " is already simplified.")

C("q::what algebra::radicals",
  "What does " + m(r"\sqrt{x}") + " mean?",
  "The <b>principal square root</b>: the non-negative number whose square is "
  + m(r"x") + ".<br>" + m(r"\sqrt{9} = 3") + " and " + m(r"\sqrt{-9}") + " is <b>not</b> " + m(r"-3")
  + " &mdash; it is undefined over the reals.")

C("q::pitfall algebra::radicals",
  "Simplify " + m(r"\sqrt{x^2}") + ". What is the answer?",
  A(r"\sqrt{x^2} = \mathbf{|x|}")
  + "<b>Not</b> " + m(r"x") + " unless you know " + m(r"x \ge 0") + ". "
  "The square root is the <i>positive</i> one, so the absolute value is required.")

C("q::how algebra::radicals",
  "Simplify: " + m(r"\sqrt{72}"),
  A(r"\sqrt{72} = \sqrt{4\cdot 18} = 2\sqrt{18} = 2\sqrt{9\cdot 2} = \mathbf{2\cdot 3\sqrt{2} = 6\sqrt{2}}")
  + "Pull out perfect squares one at a time until nothing is left.")

C("q::do algebra::radicals::product",
  "Rule for " + m(r"\sqrt{ab}") + "?",
  A(r"\sqrt{ab} = \mathbf{\sqrt{a}\,\sqrt{b}}")
  + "True for " + m(r"a, b \ge 0") + ". This is how you <b>simplify</b>: split and pull squares out.")

C("q::do algebra::radicals::quotient",
  "Rule for " + m(r"\sqrt{\frac{a}{b}}") + "?",
  A(r"\sqrt{\frac{a}{b}} = \mathbf{\frac{\sqrt{a}}{\sqrt{b}}}")
  + "Same idea, top and bottom separately.")

C("q::how algebra::radicals::rationalise",
  "Rationalise: " + m(r"\frac{3}{\sqrt{5}}"),
  A(r"\frac{3}{\sqrt{5}}\cdot\frac{\sqrt{5}}{\sqrt{5}} = \mathbf{\frac{3\sqrt{5}}{5}}")
  + "Multiply by 1 in the form " + m(r"\frac{\sqrt{5}}{\sqrt{5}}") + " to push the root up.")

C("q::how algebra::radicals::rationalise",
  "Rationalise: " + m(r"\frac{1}{1+\sqrt{2}}"),
  "Multiply by the conjugate " + m(r"\frac{1-\sqrt{2}}{1-\sqrt{2}}") + ":<br>"
  + A(r"\frac{1-\sqrt{2}}{1-\sqrt{2}} = \mathbf{\frac{1-\sqrt{2}}{1-2} = \sqrt{2} - 1}")
  + "The conjugate always cancels the middle term.")

C("q::do algebra::radicals::conjugate",
  "What is the <b>conjugate</b> and why does it work?",
  "Flip the sign on the second term: " + m(r"a+b \to a-b") + ".<br>"
  + A(r"(a+b)(a-b) = a^2-b^2")
  + "The middle terms cancel, leaving no radical. Use it to rationalise "
  "denominators with two terms.")

C("q::how algebra::radicals::equations",
  "Solve: " + m(r"\sqrt{x+3} = 4"),
  A(r"x + 3 = 16 \;\Rightarrow\; x = \mathbf{13}")
  + "Square both sides. Always <b>check</b>: " + m(r"\sqrt{13+3} = 4") + " &check;")

C("q::pitfall algebra::radicals::equations",
  "You solve " + m(r"\sqrt{2x-1} = x-3") + " and get two answers. What must you do?",
  "Square both sides (getting " + m(r"x = 4") + " and " + m(r"x = -2") + "), then "
  "<b>substitute both back</b>.<br>" + m(r"x = -2") + " is <b>extraneous</b> because "
  "the right side is negative while a square root never is. "
  "Squaring can create false answers.")

# =====================================================================
# 5. LOGARITHMS
# =====================================================================

C("q::what algebra::logs",
  "What does " + m(r"\log_b(x)") + " mean?",
  A(r"\log_b(x) = y \iff b^y = x")
  + "The <b>exponent</b> you need. " + m(r"\log_2 8 = 3") + " because " + m(r"2^3 = 8") + ".")

C("q::do algebra::logs",
  "How do you convert a logarithm into an exponential form?",
  "Swap the base and the answer for the exponent:<br>"
  + A(r"\log_b(x) = y \iff b^y = x")
  + "Everything on the right of the " + m(r"=") + " goes to the left as the base.")

C("q::how algebra::logs",
  "Solve " + m(r"\log_2(x) = 5") + ".",
  A(r"2^5 = x \;\Rightarrow\; x = \mathbf{32}")
  + "Rewrite in exponential form, then evaluate.")

C("q::how algebra::logs",
  "Solve " + m(r"\log_x(27) = 3") + ".",
  A(r"x^3 = 27 \;\Rightarrow\; x = \mathbf{3}")
  + "A common answer is 9 (squaring) &mdash; read the exponent carefully.")

C("q::do algebra::logs::product",
  "Rule for " + m(r"\log_b(xy)") + "?",
  A(r"\log_b(xy) = \mathbf{\log_b x + \log_b y}")
  + "<b>Products become sums.</b> This is the same as " + m(r"x^2\cdot x^3 = x^5") + " "
  "after applying " + m(r"b^{(\ )}") + ".")

C("q::do algebra::logs::quotient",
  "Rule for " + m(r"\log_b\!\left(\frac{x}{y}\right)") + "?",
  A(r"\log_b\!\left(\frac{x}{y}\right) = \mathbf{\log_b x - \log_b y}")
  + "Division becomes subtraction.")

C("q::do algebra::logs::power",
  "Rule for " + m(r"\log_b(x^n)") + "?",
  A(r"\log_b(x^n) = \mathbf{n\log_b x}")
  + "The exponent comes out in front as a multiplier.")

C("q::do algebra::logs::change",
  "How do you change bases?",
  A(r"\log_b(x) = \mathbf{\frac{\log_c(x)}{\log_c(b)}}")
  + "Use any base you like, typically 10 or " + m(r"e") + ". "
  "You need the log of the old base too.")

C("q::pitfall algebra::logs",
  m(r"\log(xy) \neq \log x \cdot \log y") + ". Why not?",
  "The rule is a <b>sum</b>, not a product. It comes from the product rule for "
  "exponents.<br>" + m(r"\log(2\cdot 3) = \log 6") + " but "
  + m(r"\log 2 \cdot \log 3 = \log 2.58") + " &mdash; nonsense.")

C("q::pitfall algebra::logs",
  "What is undefined: " + m(r"\log_b(0)") + " and " + m(r"\log_b(-5)") + "?",
  "<b>Both.</b><br>"
  + A(r"b^y > 0 \text{ always} \;\Rightarrow\; 0 \text{ and negatives have no log}")
  + "No power of a positive base ever reaches 0 or goes negative.")

C("q::how algebra::logs::equations",
  "Solve " + m(r"\log_2(x) + \log_2(x-1) = 3") + ".",
  A(r"\log_2\bigl(x(x-1)\bigr) = 3 \;\Rightarrow\; x^2 - x = 8 \;\Rightarrow\; x^2-x-8=0")
  + "Combine with the product rule, convert to exponential, then you have a "
  "<b>quadratic</b>. Check both roots against the domain.")

# =====================================================================
# 6. FACTORING
# =====================================================================

C("q::do factoring::method",
  "List the factoring methods in the order you should try them.",
  "1. <b>GCF</b> &mdash; always first<br>"
  "2. <b>Difference of squares</b> " + m(r"a^2-b^2") + "<br>"
  "3. <b>Perfect square trinomial</b> " + m(r"a^2\pm2ab+b^2") + "<br>"
  "4. <b>Monic trinomial</b> " + m(r"x^2+bx+c") + "<br>"
  "5. <b>Trinomial</b> " + m(r"ax^2+bx+c") + " via the " + m(r"ac") + " trick<br>"
  "6. <b>Grouping</b> &mdash; four or more terms<br>"
  "7. <b>Cubes</b> " + m(r"a^3\pm b^3") + "<br>"
  "8. <b>Substitution</b> &mdash; variable sits inside a power")

C("q::do factoring::method",
  "How do you <b>choose</b> a method rather than guess?",
  "Read the <b>shape</b>:<br>"
  "4+ terms &rarr; grouping<br>"
  "2 terms, both squares, minus &rarr; difference of squares<br>"
  "3 terms, first and last are squares &rarr; perfect square trinomial<br>"
  "3 terms, leading 1 &rarr; two-number method<br>"
  "3 terms, leading not 1 &rarr; the " + m(r"ac") + " trick<br>"
  "2 terms, both cubes &rarr; cubes<br>"
  "variable inside a power &rarr; substitution")

C("q::what factoring::what",
  "What is factoring, conceptually?",
  "Running <b>multiplication backwards</b>.<br>"
  + A(r"3(x+2) = 3x+6 \quad\Longleftrightarrow\quad 3x+6 = 3(x+2)")
  + "Every technique here is just distributing, inverted.")

C("q::do factoring::gcf",
  "How do you find the GCF of a polynomial?",
  "1. GCF of the <b>numbers</b><br>"
  "2. <b>Lowest</b> power of each variable present<br>"
  + "Multiply them. " + m(r"12x^3 + 18x^2") + " gives " + m(r"6") + " and " + m(r"x^2") + ".")

C("q::how factoring::gcf",
  "Factor completely: " + m(r"12x^3 + 18x^2"),
  A(r"\mathbf{6x^2}(2x+3)")
  + "The bracket has no common factor, so you are done.")

C("q::how factoring::gcf",
  "Factor completely: " + m(r"15x^4y^2 + 10x^2y"),
  A(r"\mathbf{5x^2y}(3x^2y + 2)")
  + "Numbers: 5. Lowest powers: " + m(r"x^2, y") + ".")

C("q::pitfall factoring::gcf",
  "You factored " + m(r"8x^2 - 4x") + " as " + m(r"4x(2x - 1)") + ". Correct?",
  A(r"8x^2 - 4x = \mathbf{4x}(2x-1)")
  + "Yes. But always re-check the bracket &mdash; here " + m(r"2x-1") + " shares nothing.")

C("q::do factoring::squares",
  "When does the difference-of-squares rule apply?",
  A(r"a^2 - b^2 = (a-b)(a+b)")
  + "Both pieces must be <b>perfect squares</b>, joined by a <b>minus</b>. "
  "If it is a plus with no middle term, it does not factor.")

C("q::how factoring::squares",
  "Factor: " + m(r"x^2 - 49"),
  A(r"\mathbf{(x-7)(x+7)}"))

C("q::how factoring::squares",
  "Factor: " + m(r"4x^2 - 25"),
  A(r"\mathbf{(2x-5)(2x+5)}")
  + "Take the square root of the 4 first &mdash; " + m(r"4 = 2^2") + ".")

C("q::how factoring::squares",
  "Factor: " + m(r"9x^4 - 4x^2"),
  A(r"x^2(9x^2-4) = \mathbf{x^2(3x-2)(3x+2)}")
  + "<b>GCF first</b> (" + m(r"x^2") + "), then the bracket is a difference of squares.")

C("q::pitfall factoring::squares",
  "Can you factor " + m(r"9x^2 + 4") + "?",
  "<b>No.</b> " + m(r"(a+b)^2") + " needs a middle term " + m(r"2ab") + " and there is none. "
  "It is <b>irreducible</b> over the integers. " + m(r"9x^2-4") + " factors; "
  + m(r"9x^2+4") + " does not.")

C("q::how factoring::square-trinomial",
  "Factor: " + m(r"x^2 + 10x + 25"),
  A(r"\mathbf{(x+5)^2}")
  + "First and last are squares; the middle is " + m(r"+2(x)(5)") + ", so it is "
  + m(r"(a+b)^2") + ".")

C("q::how factoring::square-trinomial",
  "Factor: " + m(r"x^2 - 14x + 49"),
  A(r"\mathbf{(x-7)^2}")
  + "Negative middle term means " + m(r"(a-b)^2") + ".")

C("q::do factoring::square-trinomial",
  "How do you test for a perfect square trinomial?",
  "Square the first term, square the last, and check the middle is exactly "
  + m(r"\pm 2ab") + ".<br>" + m(r"x^2+6x+9") + ": " + m(r"2(1)(3)=6") + " yes. "
  + m(r"x^2+5x+9") + ": " + m(r"2(1)(3)=6 \neq 5") + " no.")

C("q::do factoring::monic",
  "State the two-number method for " + m(r"x^2+bx+c") + ".",
  A(r"m+n = b \quad\text{and}\quad mn = c")
  + "Find two numbers that <b>multiply</b> to " + m(r"c") + " and <b>add</b> to " + m(r"b")
  + ", then write " + m(r"(x+m)(x+n)") + ".")

C("q::do factoring::monic",
  "How do you pick the right signs for " + m(r"m, n") + "?",
  m(r"c > 0") + " means " + m(r"m, n") + " share a sign &mdash; use the sign of " + m(r"b") + ".<br>"
  + m(r"c < 0") + " means <b>opposite</b> signs, and the bigger one matches the sign of " + m(r"b") + ".")

C("q::how factoring::monic",
  "Factor: " + m(r"x^2 + 5x + 6"),
  A(r"mn = 6,\; m+n = 5 \;\Rightarrow\; 2,3 \;\Rightarrow\; \mathbf{(x+2)(x+3)}"))

C("q::how factoring::monic",
  "Factor: " + m(r"x^2 - 5x + 6"),
  A(r"\mathbf{(x-2)(x-3)}")
  + m(r"c>0") + " so same signs; " + m(r"b<0") + " so both negative.")

C("q::how factoring::monic",
  "Factor: " + m(r"x^2 + x - 6"),
  A(r"mn = -6 \;\Rightarrow\; \text{opposite signs} \;\Rightarrow\; \mathbf{(x+3)(x-2)}"))

C("q::pitfall factoring::monic",
  "Factor " + m(r"x^2 + 4x + 4") + " and be careful.",
  A(r"\mathbf{(x+2)^2}")
  + "It is a <b>perfect square</b>, not " + m(r"(x+2)(x+4)") + ". "
  + m(r"2\cdot 4 = 8 \neq 4") + " for the pair 2 and 4, but 2 and 2 gives product 4 and sum 4.")

C("q::do factoring::ac-trick",
  "Why multiply " + m(r"a") + " by " + m(r"c") + " in " + m(r"ax^2+bx+c") + "?",
  "Because splitting " + m(r"b") + " into " + m(r"m+n") + " only lets you factor when "
  + m(r"mn = ac") + ".<br>In " + m(r"(mx+p)(nx+q)") + " the middle term is " + m(r"mq+np")
  + ", so forcing that to equal " + m(r"b") + " needs <b>both</b> "
  + m(r"m+n=b") + " and " + m(r"mn=ac") + ".")

C("q::how factoring::ac-trick",
  "Factor: " + m(r"6x^2 + 11x + 3"),
  A(r"ac = 18,\; m+n = 11 \;\Rightarrow\; 9,2")
  + A(r"6x^2+9x+2x+3 = 3x(2x+3)+1(2x+3) = \mathbf{(3x+1)(2x+3)}"))

C("q::how factoring::ac-trick",
  "Factor: " + m(r"2x^2 + 7x + 3"),
  A(r"ac = 6,\; 6+1 = 7 \;\Rightarrow\; 6x^2+6x+x+3 = 2x(x+3)+1(x+3) = \mathbf{(2x+1)(x+3)}"))

C("q::how factoring::ac-trick",
  "Factor: " + m(r"3x^2 - 10x + 8"),
  A(r"ac = 24,\; -6+(-4) = -10")
  + A(r"3x^2-6x-4x+8 = 3x(x-2)-4(x-2) = \mathbf{(3x-4)(x-2)}"))

C("q::pitfall factoring::ac-trick",
  "You split " + m(r"4x^2 + 4x - 3") + " as " + m(r"4x^2 + 1x + 3x - 3") + ". Wrong. Fix it.",
  m(r"ac = -12") + ", so list the pairs: " + m(r"\pm 1,\pm 12") + " and " + m(r"\pm 2,\pm 6")
  + " and " + m(r"\pm 3,\pm 4") + ".<br>Only " + m(r"6 + (-2) = 4") + " works:<br>"
  + A(r"4x^2+6x-2x-3 = 2x(2x+3)-1(2x+3) = \mathbf{(2x-1)(2x+3)}"))

C("q::do factoring::grouping",
  "When is grouping the right method?",
  "When there are <b>four or more terms</b>, no GCF, and it is not a trinomial. "
  "You are looking for two groups that share a common binomial.")

C("q::how factoring::grouping",
  "Factor: " + m(r"x^3 + 5x^2 + 2x + 10"),
  A(r"x^2(x+5) + 2(x+5) = \mathbf{(x^2+2)(x+5)}"))

C("q::how factoring::grouping",
  "Factor: " + m(r"2x^3 - 8x^2 - 5x + 20"),
  A(r"2x^2(x-4) - 5(x-4) = \mathbf{(x-4)(2x^2-5)}")
  + "The hidden 2 and 5 come out of the groups.")

C("q::do factoring::grouping",
  "Which terms pair up when grouping?",
  "Always " + m(r"x^3") + " with " + m(r"x^2") + ", and " + m(r"x") + " with the constant.<br>"
  + m(r"x^3 + 10") + " shares nothing; " + m(r"x^3 + 10x^2") + " shares " + m(r"x^2") + ".")

C("q::do factoring::cubes",
  "State the two cube identities.",
  A(r"a^3 + b^3 = (a+b)(a^2-ab+b^2)")
  + A(r"a^3 - b^3 = (a-b)(a^2+ab+b^2)")
  + "The signs inside are <b>opposite</b> to the sign outside.")

C("q::how factoring::cubes",
  "Factor: " + m(r"x^3 - 27"),
  A(r"\mathbf{(x-3)(x^2+3x+9)}")
  + "Difference of cubes, " + m(r"x^3 - 3^3") + ".")

C("q::how factoring::cubes",
  "Factor: " + m(r"8x^3 + 125"),
  A(r"\mathbf{(2x+5)(4x^2-10x+25)}")
  + "Take the cube root of <b>each</b>: " + m(r"\sqrt[3]{8x^3} = 2x") + ", "
  + m(r"\sqrt[3]{125} = 5") + ".")

C("q::pitfall factoring::cubes",
  "Factor " + m(r"x^3 - 8") + ". What is the trap?",
  A(r"\mathbf{(x-2)(x^2+2x+4)}")
  + "The trap is stopping at " + m(r"(x-2)") + ", or expanding to " + m(r"x^2-2x+4")
  + " &mdash; the signs are " + m(r"a^2 \mathbf{+} ab + b^2") + " here.")

C("q::do factoring::substitution",
  "What is substitution factoring?",
  "When the variable sits <b>inside a power</b>, promote that power to be the new "
  "variable, factor, then substitute back.<br>"
  "It is the same trinomial method in disguise &mdash; and it is exactly what you do "
  "when diagonalising a matrix.")

C("q::how factoring::substitution",
  "Factor: " + m(r"x^4 - 10x^2 + 9"),
  A(r"u = x^2 \;\Rightarrow\; u^2-10u+9 = (u-1)(u-9)")
  + A(r"\mathbf{(x^2-1)(x^2-9) = (x-1)(x+1)(x-3)(x+3)}"))

C("q::how factoring::substitution",
  "Factor: " + m(r"x^6 - 9x^3 + 8"),
  A(r"u = x^3 \;\Rightarrow\; u^2-9u+8 = (u-1)(u-8)")
  + A(r"\mathbf{(x^3-1)(x^3-8)} = \mathbf{(x-1)(x^2+x+1)(x-2)(x^2+2x+4)}"))

C("q::what factoring::complete",
  "What does <b>fully factor</b> mean?",
  "Every factor is <b>irreducible</b> &mdash; no further factoring is possible over "
  "the integers, and no GCF remains outside the brackets.<br>"
  "So " + m(r"4x^2(2x+3)^2") + " is fully factored, but " + m(r"4x^2(2x+3)") + " is not.")

C("q::pitfall factoring::mistakes",
  "The three most common factoring mistakes.",
  "1. <b>Forgetting the GCF</b> and leaving one inside the bracket<br>"
  "2. <b>Cancelling a sum</b> &mdash; " + m(r"\frac{x+2}{x} \neq 2") + "<br>"
  "3. <b>Dropping the middle term</b> when expanding " + m(r"(a\pm b)^2"))

# =====================================================================
# 7. QUADRATICS
# =====================================================================

C("q::what quadratics::what",
  "What is a quadratic equation?",
  A(r"ax^2 + bx + c = 0, \quad a \neq 0")
  + "The " + m(r"x^2") + " term is what makes it quadratic. " + m(r"a \neq 0") + " or it is not one.")

C("q::how quadratics::discriminant",
  "Compute the discriminant and say what it tells you: " + m(r"2x^2+3x-5=0"),
  A(r"\Delta = 3^2 - 4(2)(-5) = 9 + 40 = \mathbf{49}")
  + m(r"\Delta > 0") + " &rarr; two real roots &middot; "
  + m(r"\Delta = 0") + " &rarr; one repeated root &middot; "
  + m(r"\Delta < 0") + " &rarr; no real roots, two complex.")

C("q::how quadratics::formula",
  "Solve with the formula: " + m(r"3x^2 - 5x - 2 = 0"),
  A(r"x = \frac{5 \pm \sqrt{25 + 24}}{6} = \frac{5\pm 7}{6}")
  + A(r"x = \mathbf{2} \quad\text{or}\quad x = \mathbf{-\frac{1}{3}}")
  + "Check both in the original equation.")

C("q::how quadratics::complete-square",
  "Solve by completing the square: " + m(r"x^2 + 6x + 5 = 0"),
  A(r"x^2+6x+9 = 9-5 \;\Rightarrow\; (x+3)^2 = 4")
  + A(r"x+3 = \pm 2 \;\Rightarrow\; x = \mathbf{-1},\; \mathbf{-5}")
  + "Half the coefficient of " + m(r"x") + ", squared: " + m(r"(6/2)^2 = 9") + ".")

C("q::do quadratics::complete-square",
  "How do you complete the square for " + m(r"x^2+bx+c=0") + "?",
  "1. " + m(r"\frac{b}{2}") + ", squared &rarr; " + m(r"\left(\frac{b}{2}\right)^2") + "<br>"
  "2. <b>Add it to both sides</b>, and subtract it inside the bracket<br>"
  "3. Left side is now " + m(r"\left(x+\frac{b}{2}\right)^2") + "<br>"
  "4. Take square roots of both sides<br>"
  "This is the <b>same move</b> as orthogonal projection in linear algebra.")

C("q::do quadratics::vieta",
  "Without solving, what is the sum and product of the roots of " + m(r"2x^2-7x+3=0") + "?",
  A(r"\text{sum} = \frac{7}{2}, \qquad \text{product} = \frac{3}{2}")
  + "Vieta: sum " + m(r"= -\frac{b}{a}") + ", product " + m(r"= \frac{c}{a}") + ". "
  "Instantly checks your answer.")

C("q::do quadratics::roots",
  "What is the relationship between the roots and the graph of " + m(r"y = ax^2+bx+c") + "?",
  "The <b>roots are the x-intercepts</b>.<br>"
  + m(r"\Delta > 0") + " &rarr; 2 intercepts &middot; " + m(r"\Delta = 0") + " &rarr; touches the axis once &middot; "
  + m(r"\Delta < 0") + " &rarr; no intercepts.<br>Vertex at " + m(r"x = -\frac{b}{2a}") + ".")

C("q::pitfall quadratics::formula",
  "You use the quadratic formula and divide by " + m(r"2a") + " with " + m(r"a = 0") + ". Problem?",
  "Yes &mdash; then it is <b>not a quadratic</b>. Solve it as a linear equation. "
  "The formula requires " + m(r"a \neq 0") + ".")

C("q::pitfall quadratics::formula",
  "Common sign slip in the quadratic formula?",
  m(r"x = \frac{\mathbf{-b} \pm \sqrt{b^2-4ac}}{2a}") + "<br>"
  "The " + m(r"-b") + " is essential. In " + m(r"x^2-7x+10=0") + " that is "
  + m(r"\frac{7\pm 3}{2}") + " giving 5 and 2 &mdash; not negatives.")

# =====================================================================
# 8. SYSTEMS
# =====================================================================

C("q::what systems::what",
  "What does a <b>system</b> of equations mean?",
  "A set of equations that must <b>all</b> hold <b>at the same time</b>.<br>"
  + A(r"\begin{cases}2x+3y=7\\4x-y=5\end{cases}")
  + "The solution is the one point satisfying every equation.")

C("q::do systems::substitution",
  "What is the substitution method?",
  "Solve one equation for one variable, then <b>replace</b> that variable in the "
  "other equation. Produces a single-variable equation you already know how to solve.")

C("q::how systems::substitution",
  "Solve: " + A(r"\begin{cases}2x+3y=7\\4x-y=5\end{cases}"),
  A(r"y = 4x-5 \quad\text{(from eq 2)}")
  + A(r"2x + 3(4x-5) = 7 \;\Rightarrow\; 14x = 22 \;\Rightarrow\; x = \tfrac{11}{7}")
  + A(r"y = \tfrac{9}{7} \qquad \boxed{(\tfrac{11}{7},\;\tfrac{9}{7})}")
  + "Check in eq 1: " + m(r"\frac{22}{7}+\frac{27}{7} = 7") + " &check;")

C("q::do systems::elimination",
  "What is the elimination method?",
  "Multiply equations so a column matches, then <b>add</b> to cancel that column. "
  "Keeps both variables, so no substitution back is needed.")

C("q::how systems::elimination",
  "Solve by elimination: " + A(r"\begin{cases}2x+3y=7\\4x-y=5\end{cases}"),
  A(r"R_2 \to R_2 - 2R_1 \;\Rightarrow\; \begin{cases}2x+3y=7\\0x-7y=-9\end{cases}")
  + A(r"y = \tfrac{9}{7}, \quad x = \tfrac{11}{7}"))

C("q::what systems::cases",
  "How many solutions can a linear system have, and how do you tell?",
  "<b>Three cases</b>, decided by the reduced matrix:<br>"
  + m(r"0 = 0") + " row, other rows give values &rarr; <b>infinitely many</b> (dependent)<br>"
  + m(r"0 = k,\; k \neq 0") + " row &rarr; <b>no solution</b> (inconsistent)<br>"
  + "pivot in every variable column &rarr; <b>unique</b>")

C("q::do systems::graph",
  "Two lines have no solution. What does that look like?",
  "They are <b>parallel</b> &mdash; same slope, different intercepts. "
  "Infinitely many means they are the <b>same line</b>. One solution means they cross.")

C("q::do systems::geom",
  "What does each system look like in the plane?",
  m(r"3x + 2y = 6 \to \text{line}") + " (a boundary)<br>"
  + m(r"x > 2 \to \text{half-plane}") + " (shade one side)<br>"
  + m(r"x = 2 \to \text{vertical line}") + "<br>"
  + m(r"x^2+y^2 = 9 \to \text{circle}") + " &mdash; curves, not just lines.")

C("q::how systems::word",
  "A pen costs $3, a notebook $2. You buy " + m(r"p") + " and " + m(r"n")
  + " for $22, and " + m(r"p + n = 8") + ". Set up the system.",
  A(r"\begin{cases}3p + 2n = 22 \\ p + n = 8\end{cases}")
  + "Translate <b>each</b> sentence into one equation.<br>"
  + "Double the second, then subtract: "
  + m(r"\tfrac{3p+2n=22}{2p+2n=16} \Rightarrow p = 6")
  + ", so " + m(r"\mathbf{n = 2}") + ".<br>"
  + "Check: " + m(r"3(6) + 2(2) = 22") + " and " + m(r"6 + 2 = 8") + " &check;")

C("q::do systems::word",
  "You keep getting 'no solution' on a word problem. What is wrong?",
  "Usually the two sentences are <b>mutually exclusive</b> &mdash; e.g. "
  "\"at least 20\" and \"at most 15\". Re-read and check they can hold together.")

C("q::how systems::3x3",
  "How do you solve a 3x3 system?",
  "Augment with a bar and <b>row reduce</b>: get a 1 in the top-left, clear the "
  "column below it, move right, repeat.<br>"
  + A(r"\left[\begin{array}{ccc|c}1&1&1&6\\2&3&1&11\\1&2&5&20\end{array}\right]")
  + A(r"\;\Rightarrow\;\left[\begin{array}{ccc|c}1&0&0&1\\0&1&0&2\\0&0&1&3\end{array}\right]")
  + "Every variable ends with a leading 1 and all others 0. Read the last column: "
  + m(r"x = 1,\; y = 2,\; z = 3") + ".<br>"
  + "<b>Sanity check:</b> if the last row is " + m(r"0 = k") + " with " + m(r"k \neq 0")
  + ", there is <b>no</b> solution.")

C("q::do systems::rowops",
  "Which three row operations are legal, and why are they safe?",
  "1. <b>Swap</b> two rows<br>2. <b>Scale</b> a row by a nonzero number<br>"
  "3. <b>Add</b> a multiple of one row to another<br>"
  "All three are invertible, so they <b>preserve the solution set</b>. "
  "Column operations do not.")

C("q::do systems::rowops",
  "Why can you not divide a row by a variable expression in a matrix?",
  "Because " + m(r"\frac{1}{x}") + " can be zero, which would not be invertible &mdash; "
  "and the system may have no " + m(r"x \neq 0") + " condition.<br>"
  "In <b>Gauss-Jordan</b> you may only divide by a <b>number</b>.")

C("q::do systems::sub",
  "When is substitution <i>better</i> than elimination?",
  "When one variable already has coefficient " + m(r"\pm 1") + ", or already appears "
  "alone.<br>" + m(r"3x + 4y = 10,\; x = 2") + " &rarr; substitute straight in. "
  "Elimination otherwise &mdash; it avoids the round trip.")

# =====================================================================
# 9. INEQUALITIES AND ABSOLUTE VALUE
# =====================================================================

C("q::do inequalities::overview",
  "State the inequality rules for multiplication and division.",
  "By a <b>positive</b> number: direction <b>unchanged</b>.<br>"
  "By a <b>negative</b> number: direction <b>reversed</b>.<br>"
  + A(r"x > 3 \Rightarrow x + 2 > 5 \qquad x > 3 \Rightarrow -x < -3")
  + "Adding a number never flips. Multiplying by a negative always does.")

C("q::how inequalities::linear",
  "Solve: " + m(r"-2x > 6"),
  A(r"-2x > 6 \;\Rightarrow\; x < \mathbf{-3}")
  + "Divide by " + m(r"-2") + " and <b>flip</b>.")

C("q::how inequalities::linear",
  "Solve: " + m(r"3(x-1) \le 2x + 5"),
  A(r"3x - 3 \le 2x + 5 \;\Rightarrow\; x \le \mathbf{8}")
  + "Expand first, then collect. Do not split a " + m(r"\times") + " across a "
  + m(r"\pm") + " blindly.")

C("q::how inequalities::linear",
  "Solve: " + m(r"\frac{x}{-3} > 2"),
  A(r"x < \mathbf{-6}")
  + "Flipped because the divisor is negative.")

C("q::do inequalities::compound",
  "How do you write " + m(r"x > 5") + " <b>and</b> " + m(r"x < 10") + " as a double inequality?",
  A(r"5 < x < 10")
  + "<b>And</b> = <i>between</i> = a chain. <b>Or</b> = two separate pieces, "
  "drawn as two rays on a number line.")

C("q::how inequalities::abs",
  "Solve: " + m(r"|x - 3| < 4"),
  A(r"-4 < x - 3 < 4 \;\Rightarrow\; \mathbf{-1 < x < 7}")
  + m(r"|u| < c") + " means " + m(r"-c < u < c") + ". Two-sided.")

C("q::how inequalities::abs",
  "Solve: " + m(r"|2x + 1| \ge 5"),
  A(r"2x+1 \le -5 \;\textbf{or}\; 2x+1 \ge 5")
  + A(r"x \le -3 \;\textbf{or}\; x \ge 2")
  + m(r"|u| \ge c") + " means " + m(r"u \le -c") + " <b>or</b> " + m(r"u \ge c")
  + " &mdash; the <i>outside</i>, not the inside.")

C("q::do inequalities::abs",
  "What does " + m(r"|x - a|") + " represent?",
  "The <b>distance</b> from " + m(r"x") + " to " + m(r"a") + " on a number line.<br>"
  + A(r"|x| < c \;\Rightarrow\; a \text{ point is within } c \text{ of } a")
  + m(r"|x| \ge c") + " means outside that window &mdash; always <b>or</b>, never and.")

# =====================================================================
# 10. FUNCTIONS
# =====================================================================

C("q::what functions::what",
  "What is a function?",
  "A rule that assigns <b>exactly one</b> output to each input.<br>"
  + m(r"f : A \to B")
  + "The word <b>exactly one</b> is the whole definition. " + m(r"y = x^2")
  + " defines a function of " + m(r"x") + "; " + m(r"x^2 + y^2 = 4")
  + " does <b>not</b>, because it gives " + m(r"y = \pm 2") + " for " + m(r"x=0") + ".")

C("q::what functions::what",
  "What is the difference between " + m(r"y = 2x + 1") + " and " + m(r"f(x) = 2x + 1") + "?",
  m(r"y = 2x+1") + " is an <b>equation</b>: a relation between two variables.<br>"
  + m(r"f(x) = 2x+1") + " says " + m(r"f") + " is a <b>function</b>, and "
  + m(r"x") + " is the <b>input</b> (domain), " + m(r"f(x)") + " the output. "
  "You can <b>substitute</b> into it, compose it, invert it.")

C("q::do functions::domain",
  "How do you find the domain of " + m(r"\frac{\sqrt{x}}{x-2}") + "?",
  "Two conditions:<br>"
  + m(r"x \ge 0") + " (root needs a non-negative argument)<br>"
  + m(r"x \neq 2") + " (denominator)<br>"
  + "Domain: " + m(r"\mathbf{[0,2) \cup (2,\infty)}"))

C("q::how functions::domain",
  "Domain of " + m(r"\frac{1}{(x-3)^2} + \sqrt{x+1}") + "?",
  m(r"x \neq 3") + " and " + m(r"x \ge -1") + " &rarr; " + m(r"\mathbf{[-1,3)\cup(3,\infty)}"))

C("q::do functions::range",
  "What is <b>range</b>?",
  "All possible <b>outputs</b>. The mirror of domain.<br>"
  + m(r"f(x) = x^2") + " has domain all reals but range " + m(r"[0,\infty)")
  + " &mdash; the output can never be negative.")

C("q::do functions::composition",
  "What does " + m(r"(f \circ g)(x)") + " mean?",
  A(r"(f \circ g)(x) = f\bigl(g(x)\bigr)")
  + "Apply " + m(r"g") + " <b>first</b>, then feed the result to " + m(r"f") + ". "
  "Right to left. Order matters: " + m(r"f \circ g \neq g \circ f") + ".")

C("q::how functions::composition",
  m(r"f(x) = x+1") + ", " + m(r"g(x) = 2x") + ". Find " + m(r"(f\circ g)(x)") + " and " + m(r"(g\circ f)(x)") + ".",
  A(r"(f\circ g)(x) = f(2x) = \mathbf{2x+1}")
  + A(r"(g\circ f)(x) = g(x+1) = \mathbf{2x+2}")
  + "Different answers &mdash; composition is <b>not</b> commutative.")

C("q::do functions::inverse",
  "What is an <b>inverse</b> function and what makes it exist?",
  A(r"f^{-1}(f(x)) = x")
  + "It undoes " + m(r"f") + ". It exists as a <i>function</i> only when " + m(r"f")
  + " is <b>one-to-one</b> &mdash; no horizontal line test failures.")

C("q::how functions::inverse",
  "Find the inverse of " + m(r"f(x) = 3x - 5") + ".",
  A(r"y = 3x-5 \;\Rightarrow\; x = \tfrac{y+5}{3} \;\Rightarrow\; \mathbf{f^{-1}(x) = \tfrac{x+5}{3}}")
  + "Swap " + m(r"x") + " and " + m(r"y") + ", then solve for " + m(r"y") + ". "
  "Check: " + m(r"f^{-1}(f(2)) = f^{-1}(1) = 2") + " &check;")

C("q::how functions::transform",
  "Describe the transformations of " + m(r"f(x) = (x-3)^2 + 2") + " from " + m(r"f(x) = x^2") + ".",
  "Right " + m(r"3") + " &rarr; <b>shift left</b><br>"
  "Up " + m(r"2") + " &rarr; shift up<br>"
  "Order: <b>horizontal first</b>, then vertical &mdash; inside the brackets is reversed, "
  "outside is not.<br>"
  "Vertex: " + m(r"(3, 2)") + ". Domain all reals, range " + m(r"[2,\infty)") + ".")

C("q::do functions::transform",
  "Quick reference: what does each change to " + m(r"f(x)") + " do?",
  m(r"f(-x) \to \text{reflect in the } y\text{-axis}") + "<br>"
  + m(r"-f(x) \to \text{reflect in the } x\text{-axis}") + "<br>"
  + m(r"f(x) + k \to \text{up } k") + " &middot; " + m(r"f(x) - k \to \text{down } k") + "<br>"
  + m(r"af(x) \to \text{vertical stretch }(a>1)") + " / <b>flip</b> " + m(r"(a<0)") + " / "
  + m(r"(|a|<1)") + " squash<br>"
  + m(r"f(bx) \to \text{horizontal squash by } 1/b")
  + "&nbsp;&nbsp;(the <b>opposite</b> of the coefficient outside)")

C("q::do functions::poly",
  "Which polynomials are even and which are odd?",
  m(r"f(-x) = f(x) \Rightarrow \textbf{even}") + " &mdash; symmetric about the "
  + m(r"y") + "-axis: " + m(r"x^2, x^4, 1") + "<br>"
  + m(r"f(-x) = -f(x) \Rightarrow \textbf{odd}") + " &mdash; symmetric about the origin: "
  + m(r"x, x^3, 5x") + "<br>Everything else is <b>neither</b>.")

C("q::do functions::linear",
  m("f(x) = 2x + 1"),
  "A <b>linear</b> function: " + m(r"mx + b") + ".<br>Straight line, slope " + m(r"m")
  + ", " + m(r"y") + "-intercept " + m(r"b") + ", " + m(r"x") + "-intercept "
  + m(r"-\frac{b}{m}") + ".<br>Domain and range are <b>all real numbers</b>.")

C("q::do functions::types",
  "Name five important function types and their shapes.",
  "<b>Linear</b> " + m(r"mx+b") + " &middot; <b>Quadratic</b> " + m(r"ax^2+bx+c")
  + " &middot; <b>Cubic</b> " + m(r"ax^3+\dots") + " &middot; "
  + "<b>Exponential</b> " + m(r"ab^x") + " &middot; <b>Logarithmic</b> " + m(r"a\log_b x")
  + "<br>Each is the inverse of the pair next to it: exponential&harr;log, "
  + "quadratic&harr;square root.")

# =====================================================================
# 11. GEOMETRY AND GRAPHS
# =====================================================================

C("q::what geometry::slope",
  "What does the <b>slope</b> mean geometrically?",
  A(r"m = \frac{y_2 - y_1}{x_2 - x_1}")
  + "<b>Rate of change</b> &mdash; rise over run. Also the tangent of the angle "
  "the line makes with the " + m(r"x") + "-axis.")

C("q::how geometry::slope",
  "Slope through " + m(r"(1, 2)") + " and " + m(r"(4, 11)") + "?",
  A(r"m = \frac{11-2}{4-1} = \frac{9}{3} = \mathbf{3}")
  + "Always subtract in the <b>same order</b> in both fractions.")

C("q::what geometry::slope",
  "What is a vertical line's slope, and why?",
  "<b>Undefined.</b> " + A(r"x = c \to m \text{ does not exist}")
  + "Run is " + m(r"0") + ", and dividing by zero is not allowed. It is still a line "
  "&mdash; just not a function of " + m(r"x") + ".")

C("q::what geometry::slope",
  "What is a horizontal line's slope?",
  A(r"m = \mathbf{0} \quad (y = c)")
  + "It <b>is</b> a function: exactly one output per input, always the same one.")

C("q::do geometry::lines",
  m("y = 3x - 2") + ". Give the slope, the " + m(r"y") + "-intercept, the "
  + m(r"x") + "-intercept, and the standard form.",
  "slope " + m(r"\mathbf{3}") + " (the coefficient of " + m(r"x") + ")<br>"
  + m(r"y") + "-intercept " + m(r"\mathbf{(0,-2)}") + "<br>"
  + m(r"x") + "-intercept " + m(r"(\tfrac{2}{3}, 0)") + "<br>"
  + "standard: " + m(r"\mathbf{3x - y = 2}"))

C("q::do geometry::lines",
  "Put " + m(r"2x + 3y = 12") + " into slope-intercept form.",
  A(r"3y = -2x + 12 \;\Rightarrow\; y = \mathbf{-\tfrac{2}{3} x + 4}")
  + "Solve for " + m(r"y") + ". Slope " + m(r"-\frac{2}{3}") + ", intercept " + m(r"4") + ".")

C("q::do geometry::lines",
  "Are " + m(r"y = 2x + 1") + " and " + m(r"y = 2x - 5") + " parallel or identical?",
  "<b>Parallel.</b> Same slope " + m(r"2") + ", different intercepts. "
  "No solutions. Identical would need the same intercept too.")

C("q::do geometry::parallel",
  "What is the condition for two lines to be parallel?",
  A(r"m_1 = m_2 \quad \text{(and } y_1 \neq y_2\text{)}")
  + "Same slope. If the intercepts also match they are the <b>same line</b>.")

C("q::do geometry::distance",
  "Distance between " + m(r"(1,2)") + " and " + m(r"(4,6)") + "?",
  A(r"d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9+16} = \mathbf{5}"))

C("q::do geometry::midpoint",
  "Midpoint of " + m(r"(1,2)") + " and " + m(r"(5,8)") + "?",
  A(r"M = \left(\tfrac{1+5}{2}, \tfrac{2+8}{2}\right) = \mathbf{(3,5)}")
  + "Average each coordinate separately.")

C("q::how geometry::circles",
  "Put " + m(r"x^2 + y^2 = 25") + " in standard form and read off the centre and radius.",
  "Already standard: " + m(r"(x-0)^2 + (y-0)^2 = 5^2") + "<br>"
  "Centre " + m(r"\mathbf{(0,0)}") + ", radius " + m(r"\mathbf{5}") + ".<br>"
  "General: " + m(r"(x-h)^2 + (y-k)^2 = r^2") + " &mdash; centre " + m(r"(h,k)") + ".")

C("q::do geometry::parabola",
  "For " + m(r"y = 2(x-3)^2 + 1") + ", where is the vertex and what opens up?",
  "Vertex " + m(r"\mathbf{(3, 1)}") + ", opens <b>up</b> because "
  + m(r"a = 2 > 0") + ".<br>Axis of symmetry " + m(r"\mathbf{x = 3}") + ". "
  "Range " + m(r"[1,\infty)") + ", domain all reals.")

# =====================================================================
# 12. SEQUENCES AND SERIES
# =====================================================================

C("q::what sequences::what",
  "What is an arithmetic sequence?",
  "A sequence with a <b>constant difference</b>: " + m(r"a, a+d, a+2d, \dots") + "<br>"
  + A(r"a_n = a_1 + (n-1)d")
  + "Example: " + m(r"3, 7, 11, 15") + " has " + m(r"d = 4") + ".")

C("q::what sequences::what",
  "What is a geometric sequence?",
  "A sequence with a <b>constant ratio</b>: " + m(r"a, ar, ar^2, \dots") + "<br>"
  + A(r"a_n = a_1 r^{n-1}")
  + "Example: " + m(r"2, 6, 18, 54") + " has " + m(r"r = 3") + ".")

C("q::how sequences::arith",
  "Arithmetic: " + m(r"a_1 = 5, d = 3") + ". Find " + m(r"a_{20}") + ".",
  A(r"a_{20} = 5 + 19\cdot 3 = \mathbf{62}")
  + m(r"(n-1)") + ", not " + m(r"n") + " &mdash; the first term is " + m(r"n=1") + " already.")

C("q::how sequences::arith",
  "Arithmetic sum: " + m(r"a_1 = 2, d = 3, n = 10") + ".",
  A(r"S_{10} = \tfrac{n}{2}(2a_1 + (n-1)d) = 5(4 + 27) = \mathbf{155}"))

C("q::how sequences::geom",
  "Geometric: " + m(r"a_1 = 3, r = 2") + ". Find " + m(r"a_8") + ".",
  A(r"a_8 = 3\cdot 2^{7} = \mathbf{384}")
  + m(r"n-1 = 7") + " factors, again because of the " + m(r"n-1") + ".")

C("q::do sequences::geom",
  "When does a geometric series converge?",
  "Only when " + m(r"|r| < 1") + ", and then its sum is " + A(r"S_\infty = \frac{a_1}{1-r}")
  + "Otherwise it <b>diverges</b> &mdash; the terms never shrink to zero.")

# =====================================================================
# 13. VECTORS
# =====================================================================

C("q::what vectors::what",
  "What is a vector?",
  A(r"\mathbf{v} = \begin{bmatrix}3\\2\end{bmatrix}")
  + "An <b>arrow</b>: it has magnitude <b>and</b> direction.<br>"
  + m(r"\begin{bmatrix}3\\2\end{bmatrix} \neq \begin{bmatrix}2\\3\end{bmatrix}")
  + " &mdash; the second is a different arrow, pointing elsewhere.")

C("q::do vectors::add",
  "How do you add and scale vectors?",
  A(r"\begin{bmatrix}a\\b\end{bmatrix} + \begin{bmatrix}c\\d\end{bmatrix} = \begin{bmatrix}a+c\\b+d\end{bmatrix}")
  + "Componentwise. " + m(r"k\mathbf{v}") + " multiplies each component. "
  "Addition is commutative; scalar multiplication is not.")

C("q::how vectors::add",
  "Add " + m(r"\begin{bmatrix}1\\2\\3\end{bmatrix}") + " and " + m(r"\begin{bmatrix}4\\-1\\2\end{bmatrix}") + ".",
  A(r"\begin{bmatrix}5\\1\\5\end{bmatrix}")
  + "Three components, three additions. Straight down the columns.")

C("q::do vectors::length",
  "What is the magnitude of a vector?",
  A(r"\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots}")
  + "Pythagoras. " + m(r"\|\begin{bmatrix}3\\4\end{bmatrix}\| = \sqrt{9+16} = 5")
  + " &mdash; the 3-4-5 triangle.")

C("q::do vectors::dot",
  "What does the <b>dot product</b> do, and what does it mean geometrically?",
  A(r"\mathbf{u}\cdot\mathbf{v} = u_1v_1 + u_2v_2 + \cdots = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta")
  + "It gives the <b>scaled projection</b> of one onto the other.<br>"
  + m(r"= 0") + " means <b>orthogonal</b> (perpendicular).<br>"
  + m(r"< 0") + " means the angle is obtuse.")

C("q::how vectors::dot",
  "Dot product of " + m(r"\begin{bmatrix}1\\2\\-1\end{bmatrix}") + " and " + m(r"\begin{bmatrix}3\\-1\\4\end{bmatrix}") + "?",
  A(r"3 - 2 - 4 = \mathbf{-3}")
  + "Multiply matching positions, then add. Negative means obtuse.")

C("q::do vectors::projection",
  "What is the projection of " + m(r"\mathbf{u}") + " onto " + m(r"\mathbf{v}") + "?",
  A(r"\text{proj}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{v}\|^2}\,\mathbf{v}")
  + "The <b>shadow</b> " + m(r"\mathbf{u}") + " casts along " + m(r"\mathbf{v}") + ". "
  + m(r"\|\mathbf{v}\|^2 = \mathbf{v}\cdot\mathbf{v}") + " &mdash; not " + m(r"\|\mathbf{v}\|") + ".")

C("q::do vectors::lincomb",
  "What is a linear combination?",
  A(r"a\mathbf{v}_1 + b\mathbf{v}_2 + \cdots")
  + "Any sum of scaled vectors. <b>Span</b> of a set = <i>every</i> linear combination of it. "
  "In " + m(r"\mathbb{R}^2") + " two non-parallel vectors span everything.")

C("q::do vectors::indep",
  "What does <b>linear independence</b> mean?",
  A(r"a\mathbf{v}_1 + b\mathbf{v}_2 = \mathbf{0} \;\Rightarrow\; a = b = 0")
  + "No vector is a combination of the others. It means scaling and adding can only "
  "reach the zero vector in the trivial way.")

C("q::do vectors::basis",
  "What is a <b>basis</b>?",
  "A set that is both <b>independent</b> and <b>spans</b>.<br>"
  "Every " + m(r"\mathbb{R}^n") + " has a basis of " + m(r"\mathbf{n}") + " vectors. "
  "That " + m(r"n") + " is the <b>dimension</b>. Change the basis, keep the number.")

C("q::do vectors::subspace",
  "What makes a subset a <b>subspace</b> of " + m(r"\mathbb{R}^n") + "?",
  "It must contain " + m(r"\mathbf{0}") + " and be <b>closed</b> under:<br>"
  "1. vector addition &nbsp;&nbsp; 2. scalar multiplication<br>"
  + "Then " + m(r"\mathbf{u} - \mathbf{v}") + " is automatically in it too.<br>"
  + A(r"\text{span}(\mathbf{v}_1,\dots,\mathbf{v}_k)")
  + " is always a subspace; a bare set of points usually is not.")

# =====================================================================
# 14. MATRICES
# =====================================================================

C("q::what matrices::what",
  "What is a matrix?",
  "A rectangular array of numbers. The entry in row " + m(r"i") + ", column " + m(r"j")
  + " is " + m(r"a_{ij}") + ".<br>" + A(r"\begin{bmatrix}2&1\\1&3\end{bmatrix}")
  + "It is a <b>linear transformation</b> in disguise: multiply a column vector by it.")

C("q::do matrices::multiply",
  "How do you multiply two matrices?",
  "Row-by-column: each entry is a dot product of a row of the first with a column "
  "of the second.<br>"
  + A(r"\begin{bmatrix}a&b\\c&d\end{bmatrix}\begin{bmatrix}e&f\\g&h\end{bmatrix} = \begin{bmatrix}ae+bg & af+bh\\ce+dg & cf+dh\end{bmatrix}")
  + "The inner dimensions must match: " + m(r"(m\times n)(n\times p)") + " is " + m(r"(m\times p)") + ".")

C("q::pitfall matrices::multiply",
  "Is " + m(r"AB = BA") + "?",
  "<b>No, not in general.</b> " + m(r"AB") + " has shape " + m(r"(m\times n)(n\times p)")
  + " while " + m(r"BA") + " may not even exist. Matrix multiplication is "
  "<b>not</b> commutative &mdash; unlike ordinary numbers.")

C("q::do matrices::transpose",
  "What does transposing do, and what is it good for?",
  "Flips rows and columns: " + A(r"(A^T)_{ij} = A_{ji}")
  + m(r"(AB)^T = B^TA^T") + " &mdash; <b>order reverses</b>.<br>"
  + "Used to turn a column vector into a row vector so you can multiply, and to "
  "rewrite dot products as matrix products.")

C("q::what matrices::what",
  "What is the identity matrix and what does it do?",
  A(r"I = \begin{bmatrix}1&0\\0&1\end{bmatrix}")
  + m(r"AI = IA = A") + ". It is the identity for multiplication, like 1 for numbers. "
  "Diagonal 1s, zeros elsewhere.")

C("q::do matrices::inverse",
  "What is an <b>inverse</b>, and when does one exist?",
  A(r"A^{-1}A = AA^{-1} = I")
  + "Exists <b>iff</b> " + m(r"\det(A) \neq 0") + " &mdash; then " + m(r"A")
  + " is <b>invertible</b> / non-singular. If " + m(r"\det = 0") + " it is <b>singular</b>: "
  "no inverse, and " + m(r"A\mathbf{x} = \mathbf{b}") + " has no unique solution.")

C("q::do matrices::inverse",
  "What is the inverse of a " + m(r"2\times 2") + " matrix?",
  A(r"\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}")
  + "Swap the diagonal, negate the off-diagonal, divide by the determinant. "
  "Only valid for " + m(r"2\times 2") + ".")

C("q::do matrices::inverse",
  "How do you solve " + m(r"A\mathbf{x} = \mathbf{b}") + " when " + m(r"A") + " is invertible?",
  A(r"\mathbf{x} = \mathbf{A^{-1}}\mathbf{b}")
  + "Multiply both sides by " + m(r"A^{-1}") + ". With a 3x3 or larger matrix, "
  "<b>row reduction is easier</b> than finding the inverse by hand.")

C("q::do matrices::rank",
  "What is the <b>rank</b> of a matrix?",
  "The number of pivots in its row echelon form &mdash; equivalently the number of "
  "linearly independent rows (or columns).<br>"
  + m(r"\text{rank}(A) = n") + " means invertible. " + m(r"\text{rank}(A) < n")
  + " means the system cannot have a unique solution.")

C("q::do matrices::rref",
  "What does RREF look like, and how do you read a solution from it?",
  "Every leading entry is " + m(r"1") + ", each is the only non-zero in its column, "
  "and pivots move rightward.<br>"
  "In " + m(r"\left[\begin{array}{cc|c}1&0&3\\0&1&-1\end{array}\right]") + " the "
  "last column gives " + m(r"\mathbf{x = (3,\,-1)^T}") + " directly.")

# =====================================================================
# 15. LINEAR ALGEBRA
# =====================================================================

C("q::what la::transition",
  "What is the conceptual jump from elementary algebra to linear algebra?",
  "Elementary asks <b>what is " + m(r"x") + "?</b> Linear algebra asks "
  "<b>what happens to a whole space</b> under an operation.<br>"
  "From manipulating equations to thinking about <b>vectors, spaces and "
  "transformations</b>.")

C("q::what la::transformation",
  "What is a <b>linear transformation</b>?",
  A(r"T(\mathbf{u}+\mathbf{v}) = T(\mathbf{u})+T(\mathbf{v}), \qquad T(c\mathbf{u}) = c\,T(\mathbf{u})")
  + "Preserves addition and scaling. Equivalently " + m(r"T(\mathbf{0}) = \mathbf{0}")
  + " and straight lines stay straight.<br>"
  "Every linear map on " + m(r"\mathbb{R}^n") + " <b>is</b> multiplication by a matrix.")

C("q::do la::transformation",
  "What is the <b>matrix of a transformation</b>?",
  "The standard basis images as columns: " + A(r"[T] = \begin{bmatrix} | & | \\ T(e_1) & T(e_2) \\ | & | \end{bmatrix}")
  + "A transformation is fully described by where it sends " + m(r"\mathbf{e}_1, \mathbf{e}_2") + ".")

C("q::how la::transformation",
  "Matrix of the map " + m(r"T(x,y) = (2x + y,\; x - y)") + "?",
  m(r"T(e_1) = (2, 1)") + ", " + m(r"T(e_2) = (1, -1)") + ", so"
  + A(r"[T] = \begin{bmatrix}2&1\\1&-1\end{bmatrix}"))

C("q::what la::eigenvalues",
  "What is an <b>eigenvalue</b>?",
  A(r"A\mathbf{v} = \lambda\mathbf{v}")
  + "A scalar " + m(r"\lambda") + " and a direction " + m(r"\mathbf{v}") + " where the "
  "transformation only <b>scales</b>. " + m(r"\mathbf{v} \neq \mathbf{0}") + ".<br>"
  "The eigenvector is the one direction that does not rotate or shear.")

C("q::do la::eigenvalues",
  "How do you find eigenvalues?",
  A(r"\det(A - \lambda I) = \mathbf{0}")
  + "Build " + m(r"A - \lambda I") + ", expand the determinant, solve the polynomial. "
  "Use " + m(r"- \lambda I") + ", never " + m(r"+ \lambda I") + ".")

C("q::how la::eigenvalues",
  "Eigenvalues of " + m(r"\begin{bmatrix}2&1\\0&3\end{bmatrix}") + "?",
  m(r"A - \lambda I = \begin{bmatrix}2-\lambda&1\\0&3-\lambda\end{bmatrix}")
  + A(r"\det = (2-\lambda)(3-\lambda) = 0 \;\Rightarrow\; \mathbf{\lambda = 2,\; 3}")
  + "A triangular matrix's eigenvalues are its <b>diagonal entries</b>.")

C("q::do la::eigenvalues",
  "How do you find the eigenvector for an eigenvalue?",
  A(r"(A - \lambda I)\mathbf{v} = \mathbf{0}")
  + "Row reduce " + m(r"A - \lambda I") + " and read the free variable. Any nonzero "
  "multiple is valid &mdash; " + m(r"\mathbf{v}") + " is only defined up to scale.")

C("q::how la::eigenvalues",
  "Eigenvector for " + m(r"\lambda = 2") + " of " + m(r"\begin{bmatrix}2&1\\0&3\end{bmatrix}") + "?",
  m(r"A - 2I = \begin{bmatrix}0&1\\0&1\end{bmatrix}")
  + A(r"\Rightarrow\; v_2 = 0, \quad \mathbf{v} = \begin{bmatrix}1\\0\end{bmatrix}")
  + "Every nonzero multiple works.")

C("q::do la::eigenvalues::geom",
  "What does a negative eigenvalue mean geometrically?",
  "That direction is scaled and <b>flipped</b> &mdash; rotated " + m(r"180^\circ")
  + ". A " + m(r"\lambda = 0") + " direction collapses to the origin.")

C("q::what la::eigenvalues::repeated",
  "What if an eigenvalue repeats?",
  "You may get only <b>one</b> independent eigenvector. Then the matrix is "
  "<b>not diagonalisable</b> &mdash; you cannot build an eigenbasis.<br>"
  "Check the dimension of the null space of " + m(r"A - \lambda I") + ".")

C("q::do la::diagonalisation",
  "What is diagonalisation, and when can you do it?",
  A(r"A = PDP^{-1} \quad\text{iff } P^{-1}AP = D")
  + m(r"D") + " is diagonal (eigenvalues on the diagonal), " + m(r"P")
  + " holds the eigenvectors as columns.<br>"
  "Possible <b>iff</b> " + m(r"A") + " has " + m(r"n") + " linearly independent eigenvectors.")

C("q::do la::diagonalisation",
  "Why bother diagonalising?",
  "Powers become trivial: " + A(r"A^k = PD^kP^{-1}, \qquad D^k = \begin{bmatrix}\lambda_1^k & \\ & \ddots\end{bmatrix}")
  + "So " + m(r"A^{100}") + " is instant instead of hopeless. This is how you analyse "
  "long-term growth and Markov chains.")

C("q::what la::determinant",
  "What does the determinant <i>mean</i>, not just how to compute it?",
  "It <b>scales volume</b>. " + m(r"|\det A|") + " is the factor by which "
  + m(r"A") + " stretches space.<br>"
  + m(r"\det = 0") + " means space is <b>flattened</b> &mdash; vectors become dependent.<br>"
  + m(r"\det < 0") + " means the map also <b>flips orientation</b>.")

C("q::do la::determinant",
  "Expand a 3x3 determinant along the first row. What are the signs?",
  A(r"+ \;\; - \;\; +")
  + m(r"\det = a_{11}M_{11} - a_{12}M_{12} + a_{13}M_{13}")
  + "Alternating. Getting these wrong is the most common determinant error.")

C("q::do la::determinant",
  "What does " + m(r"\det(A) = 0") + " tell you? Three things.",
  "1. " + m(r"A") + " is <b>singular</b>, no inverse<br>"
  "2. Rows/columns are <b>linearly dependent</b><br>"
  "3. " + m(r"A\mathbf{x}=\mathbf{b}") + " has <b>no unique</b> solution<br>"
  + m(r"\text{volume factor} = 0"))

C("q::do la::matrix::det-properties",
  "How does the determinant behave under multiplication?",
  A(r"\det(AB) = \det(A)\det(B)")
  + "So " + m(r"\det(A^{-1}) = \frac{1}{\det A}") + ", and "
  + m(r"\det(A^2) = (\det A)^2") + ".")

C("q::what la::inner-product",
  "What is an <b>inner product</b>?",
  A(r"\langle \mathbf{u},\mathbf{v}\rangle = \mathbf{u}\cdot\mathbf{v}")
  + "It turns a pair of vectors into a <b>number</b> measuring alignment. "
  "The standard one on " + m(r"\mathbb{R}^n") + " is the dot product.")

C("q::do la::orthogonal",
  "What does it mean for vectors to be <b>orthogonal</b>, and why care?",
  A(r"\mathbf{u}\cdot\mathbf{v} = \mathbf{0}")
  + "They are perpendicular. Orthogonal vectors are automatically <b>linearly "
  "independent</b> &mdash; so an orthogonal set is a <b>basis</b>. They are also "
  "easiest to work with: no redundancy, and projections stay simple.")

C("q::do la::orthogonal",
  "How do you orthogonalise a set? Gram-Schmidt in one line each.",
  A(r"\mathbf{w}_1 = \mathbf{v}_1")
  + A(r"\mathbf{w}_2 = \mathbf{v}_2 - \frac{\langle \mathbf{v}_2,\mathbf{w}_1\rangle}{\langle \mathbf{w}_1,\mathbf{w}_1\rangle}\mathbf{w}_1")
  + "<b>Subtract the projection</b> onto what you already have. Repeat. "
  "The " + m(r"\mathbf{w}") + " are mutually orthogonal and span the same space.")

C("q::do la::least-squares",
  "Why is <b>least squares</b> the right problem when there is no exact solution?",
  "A least-squares fit minimises the <b>sum of squared residuals</b> "
  + m(r"\|\mathbf{b} - A\mathbf{x}\|^2") + ".<br>"
  "This is the orthogonal projection of " + m(r"\mathbf{b}") + " onto "
  + m(r"\operatorname{col}(A)") + " &mdash; the closest point in the column space. "
  "Squaring punishes big errors, which is exactly what you want.")

C("q::do la::orthogonal-complement",
  "What is the orthogonal complement?",
  A(r"W^{\perp} = \{\mathbf{w} \in \mathbb{R}^n : \mathbf{w}\cdot\mathbf{v} = 0 \;\forall \mathbf{v} \in W\}")
  + "The directions <b>perpendicular</b> to everything in " + m(r"W") + ".<br>"
  + A(r"\dim W + \dim W^\perp = n")
  + " and " + A(r"\mathbb{R}^n = W \oplus W^\perp")
  + " &mdash; every vector splits uniquely into a part in " + m(r"W") + " and a part "
  "in " + m(r"W^\perp") + ".")

C("q::do la::symmetric",
  "What is special about a <b>symmetric</b> matrix?",
  m(r"A^T = A")
  + " &mdash; mirror image across the diagonal.<br>"
  "Its eigenvalues are always <b>real</b>, and it can be orthogonally diagonalised: "
  + m(r"A = QDQ^T") + ".<br>Real symmetric matrices are the <i>good</i> ones: "
  "always orthogonally diagonalisable, never defective.")

# =====================================================================
# 16. TRICKS
# =====================================================================

C("q::how tricks::quick",
  "A number is divisible by 3 &mdash; how do you know instantly?",
  "Sum the <b>digits</b>. If the sum is divisible by 3, so is the number.<br>"
  + m(r"2+4+7+1 = 14") + " &rarr; not divisible by 3. Divisible by 9? " + m(r"14") + " isn't either.")

C("q::how tricks::quick",
  "A number is divisible by 4 &mdash; how do you know instantly?",
  "Look at the <b>last two digits</b> only.<br>"
  + m(r"7316") + " &rarr; " + m(r"16") + " is divisible by 4, so " + m(r"7316") + " is. "
  "For 8, use the last <b>three</b> digits.")

C("q::how tricks::quick",
  "Multiply " + m(r"(x + 2)(x + 3)") + " fast, by hand.",
  "Middle terms via " + m(r"3+2 = 5") + ": " + A(r"x^2 + 5x + 6")
  + "But first ask: do the numbers multiply to 6 and add to 5? "
  "If yes, <b>factor</b> instead of expanding &mdash; that is the real trick.")

C("q::how tricks::quick",
  "Compute " + m(r"(2x + 5)(2x + 5)") + " without expanding.",
  "Recognise " + m(r"(a+b)^2 = a^2+2ab+b^2") + " with " + m(r"a = 2x, b = 5") + ": "
  + A(r"4x^2 + 20x + 25")
  + "Or even better: recognise " + m(r"(2x+5)^2") + " and use "
  + m(r"a^2 - b^2") + " if it shows up inside something.")

C("q::how tricks::quick",
  "Simplify " + m(r"\frac{x^2 - 4}{x^2 - 6x + 8}") + " without a calculator.",
  "Factor both: " + A(r"\frac{(x-2)(x+2)}{(x-2)(x-4)} = \frac{x+2}{x-4}")
  + "Restrictions " + m(r"x \neq 2, 4") + ". Factoring beats expanding every time.")

C("q::how tricks::quick",
  "How do you divide polynomials? Long division vs factoring?",
  "<b>Factoring first</b> is almost always faster.<br>"
  + m(r"\frac{x^3 - 8}{x - 2}") + " &rarr; difference of cubes &rarr; "
  + m(r"\frac{(x-2)(x^2+2x+4)}{x-2} = x^2+2x+4")
  + "Long division is the fallback.")

C("q::how tricks::quick",
  "Solve " + m(r"x^2 = 5x") + " without a formula.",
  A(r"x^2 - 5x = 0 \;\Rightarrow\; x(x-5) = 0 \;\Rightarrow\; x = \mathbf{0} \text{ or } 5")
  + "Get everything on one side, then <b>factor</b>. " + m(r"x = 0") + " is easy to lose "
  "&mdash; it is the answer people forget.")

C("q::how tricks::quick",
  "Evaluate " + m(r"2^{10}") + " without counting.",
  A(r"1024")
  + "Or " + m(r"2^{10} = (2^5)^2 = 32^2") + ". Powers of 2 and 10 are worth memorising "
  "for speed, not for the exam.")

C("q::how tricks::quick",
  "Estimate " + m(r"\frac{0.999^2}{1.001}") + " without computing.",
  "The numerator is just under 1, the denominator just over 1, so the answer is "
  "<b>slightly under 1</b>. Order-of-magnitude checks catch errors fast.")

C("q::do tricks::common",
  "Three shortcuts that always work.",
  "1. <b>Zero is a root</b>: if " + m(r"c = 0") + " then " + m(r"x = 0")
  + " is a solution. Check it first.<br>"
  "2. <b>Look for a nice root</b>: try " + m(r"x = 1, -1, 2, -2") + " before the formula.<br>"
  "3. <b>Factor instead of expanding</b>, always.")

C("q::do tricks::common",
  "You must choose between the quadratic formula and completing the square. When does each win?",
  "Perfect square, or " + m(r"b = 0") + " &rarr; <b>factor</b> or take a root. Instant.<br>"
  + m(r"b = 0") + " generally &rarr; " + A(r"x = \pm\sqrt{\frac{c}{a}}")
  + " &mdash; the formula collapses to a square root.<br>"
  "Otherwise: the formula, unless the numbers suit completing the square.")

C("q::how tricks::common",
  "If " + m(r"f(2) = 3") + " and " + m(r"f(2x) = 5") + ", what is " + m(r"f(4)") + "?",
  m(r"f(2x) = 5") + " means: at input " + m(r"2\cdot 2 = 4") + " the output is 5.<br>"
  + A(r"\mathbf{f(4) = 5}")
  + "Read " + m(r"f(2x)") + " as \"5 when the input is 2x\". Substituting "
  + m(r"2x = 4") + " is the whole trick.")

# =====================================================================
# 17. PITFALLS
# =====================================================================

C("q::pitfall algebra::cancel",
  m(r"\frac{x+2}{x} = 2") + " &mdash; correct?",
  "<b>No.</b> " + A(r"\frac{x+2}{x} = 1 + \frac{2}{x}")
  + "Only <b>factors</b> cancel, never sums. This is the single most common "
  "algebra error there is.")

C("q::pitfall algebra::perfect-squares",
  m(r"(x+2)^2 = x^2 + 4") + " &mdash; correct?",
  "<b>No.</b> " + A(r"x^2 + \mathbf{4x} + 4")
  + "Squaring means multiplying by itself, and the cross terms double up: "
  + m(r"2x\cdot 2 = 4x") + ".")

C("q::pitfall algebra::perfect-squares",
  m(r"\sqrt{x^2} = x") + " &mdash; correct?",
  "Only for " + m(r"x \ge 0") + ". In general " + A(r"\sqrt{x^2} = |x|")
  + "The square root is the <b>non-negative</b> one.")

C("q::pitfall algebra::exponents",
  m(r"x^2 + x^3 = x^5") + " &mdash; correct?",
  "<b>No.</b> Exponents combine by multiplication, not addition.<br>"
  + m(r"x^2\cdot x^3 = x^5") + " is true. The sum is already simplified.")

C("q::pitfall algebra::coefficient",
  m(r"3x^2 - x = 2x") + " &mdash; what is wrong?",
  A(r"3x^2 - x = 2x \;\Rightarrow\; 3x^2 = 3x \;\Rightarrow\; 3x(x-1) = 0 \;\Rightarrow\; x = \mathbf{0} \text{ or } \mathbf{1}")
  + "Common error: dividing by " + m(r"x") + " and losing " + m(r"x = 0") + ".<br>"
  "Move everything to one side and <b>factor</b>. "
  + m(r"\tfrac{3x^2}{3x} = x") + " is only valid when " + m(r"x \neq 0") + ", which is "
  "exactly the case you threw away.<br>"
  "<b>Never divide by a variable</b> &mdash; it might be zero.")

C("q::pitfall systems::rowops",
  "You swap two <i>columns</i> while row reducing. What breaks?",
  "The <b>solution</b> &mdash; you have permuted which variable is which.<br>"
  "Row operations preserve solutions; column operations change the problem. "
  "Only swap columns when you swap <b>both</b> rows and columns and track it.")

C("q::pitfall la::eigenvalues",
  "You set " + m(r"\det(A + \lambda I) = 0") + " for eigenvalues. Wrong sign?",
  m(r"\det(A+\lambda I) = \det\bigl(A-(-\lambda)I\bigr)")
  + ", so its roots are " + m(r"\mathbf{-\lambda_i}") + " &mdash; the <b>negatives</b> of "
  "the eigenvalues, <b>not</b> the same values.<br>"
  "Example: " + m(r"A = \begin{bmatrix}2&1\\0&3\end{bmatrix}") + " has eigenvalues "
  + m(r"2, 3") + ", but " + m(r"\det(A+\lambda I) = \lambda^2+5\lambda+6") + " gives "
  + m(r"\lambda = -2, -3") + ".<br>"
  "Standard convention is " + m(r"A - \lambda I") + ". If you use " + m(r"A + \lambda I")
  + ", remember to negate at the end.")

C("q::pitfall la::inverse",
  "Does " + m(r"(A+B)^{-1} = A^{-1} + B^{-1}") + "?",
  "<b>No.</b> " + A(r"(A+B)^{-1} \neq A^{-1}+B^{-1}")
  + "Matrices are not like fractions here. The false rule comes from treating "
  + m(r"\frac{1}{a+b}") + " like " + m(r"\frac{1}{a}+\frac{1}{b}") + " &mdash; which is also wrong.")

C("q::pitfall la::matrix-multiplication",
  "Is " + m(r"A(B\mathbf{x}) = (AB)\mathbf{x}") + " true?",
  "<b>Yes</b> &mdash; associativity holds.<br>"
  "What fails is commutativity: " + m(r"A(B\mathbf{x}) \neq B(A\mathbf{x})")
  + " in general. Same split for column vectors, but not for sums in a different order.")

C("q::pitfall geometry::slope",
  "Slope of the line through " + m(r"(1,2)") + " and " + m(r"(2,1)") + "?",
  A(r"m = \frac{1-2}{2-1} = -1")
  + "The trap is mixing the order: " + m(r"\frac{2-1}{1-2} = 1") + " is <b>wrong</b> "
  "&mdash; it is the slope of the perpendicular. Keep both subtractions in the "
  "same order top-to-bottom.")

C("q::pitfall functions::inverse",
  "The inverse of " + m(r"f(x) = 2x") + " is " + m(r"f^{-1}(x) = 2x") + ". Wrong how?",
  A(r"f^{-1}(x) = \mathbf{\frac{x}{2}}")
  + m(r"f^{-1}") + " means <b>reciprocal function</b>, not " + m(r"\frac{1}{f(x)}") + ". "
  "It is the function that undoes " + m(r"f") + ".")

# =====================================================================
# 18. NOTATION GLOSSARY
# =====================================================================

C("q::what notation::glossary", "What does " + m(r"\frac{d}{dx}") + " mean?",
  "Take the <b>derivative</b>: the rate of change, the slope of the tangent.<br>"
  + A(r"\frac{d}{dx}(x^3) = 3x^2")
  + "Notation matters: " + m(r"\frac{d}{dx}") + " and " + m(r"\frac{dy}{dx}") + " mean "
  "different things.")

C("q::what notation::glossary", "What is the difference between " + m(r"\in") + " and " + m(r"\subset") + "?",
  m(r"a \in S") + ": " + m(r"a") + " is an <b>element</b> of the set " + m(r"S") + "<br>"
  + m(r"A \subset B") + ": " + m(r"A") + " is <b>contained in</b> " + m(r"B")
  + " (proper subset &mdash; strictly smaller)<br>"
  + m(r"A \subseteq B") + " allows equality. " + m(r"A \in B") + " means " + m(r"A")
  + " is itself an element &mdash; a different level entirely.")

C("q::what notation::glossary", "What does " + m(r"\mathbb{R}^2") + " mean?",
  "All pairs of real numbers: " + m(r"\{(x,y) : x,y \in \mathbb{R}\}") + ".<br>"
  "It is a <b>2-dimensional space</b> &mdash; a flat plane. " + m(r"\mathbb{R}")
  + " is a line, " + m(r"\mathbb{R}^3") + " is space. The superscript is the dimension.")

C("q::what notation::glossary", "What is the difference between " + m(r"\mathbb{R}^n") + " and " + m(r"\mathbb{R} \times \mathbb{R}") + "?",
  "Nothing, in this case &mdash; but " + m(r"\mathbb{R}^2") + " is a <b>vector space</b> "
  "and " + m(r"\mathbb{R}\times\mathbb{R}") + " is a set. You can add vectors and "
  "scale them; you cannot do either to bare ordered pairs without saying so.")

C("q::what notation::glossary", "What is a <b>linear map</b> again, in one line?",
  A(r"T(a\mathbf{u}+b\mathbf{v}) = a\,T(\mathbf{u}) + b\,T(\mathbf{v})")
  + "One condition instead of two. It bundles addition and scalar multiplication "
  "together and is the definition to memorise.")

C("q::what notation::glossary", "What do these symbols mean: " + m(r"\propto") + ", " + m(r"\equiv") + ", " + m(r"\approx") + "?",
  m(r"\propto") + " &nbsp; proportional to<br>"
  + m(r"\equiv") + " &nbsp;identical / defined as<br>"
  + m(r"\approx") + " &nbsp;approximately equal<br>"
  + m(r"\neq") + " &nbsp;not equal &nbsp;&middot;&nbsp; " + m(r"\pm") + " &nbsp;plus or minus &nbsp;&middot;&nbsp; "
  + m(r"\Rightarrow") + " &nbsp;implies")

C("q::what notation::glossary", "What is a <b>field</b>?",
  "A set where you can add, subtract, multiply, and divide (except by zero), and "
  "all of it behaves as you expect.<br>"
  + m(r"\mathbb{R}") + " and " + m(r"\mathbb{C}") + " are fields. "
  + m(r"\mathbb{Z}") + " (integers) is <b>not</b> &mdash; " + m(r"\frac{1}{2}") + " is missing. "
  + m(r"\mathbb{Z}_6") + " is not &mdash; " + m(r"2\cdot 3 = 0") + " has no inverse.")

C("q::what notation::glossary", "What is a <b>vector space</b>?",
  "A set of vectors with addition and scalar multiplication that behaves like "
  + m(r"\mathbb{R}^n") + ": axioms for associativity, commutativity, a zero, and "
  "inverses. Matrices and polynomials are both vector spaces.")


# =====================================================================
# build
# =====================================================================

def main() -> int:
    if not COLLECTION.parent.parent.exists():
        print(f"error: no Anki profile at {COLLECTION.parent.parent}", file=sys.stderr)
        return 1

    from anki.collection import Collection

    col = Collection(str(COLLECTION))
    try:
        deck_id = col.decks.id(DECK)
        model = col.models.by_name("Basic")
        if model is None:
            print("error: no 'Basic' note type in the collection", file=sys.stderr)
            return 1

        existing: dict[str, int] = {}
        for nid in col.find_notes(f'"deck:{DECK}"'):
            existing.setdefault(col.get_note(nid)["Front"], nid)

        added = updated = 0
        for tags, front, back in CARDS:
            if front in existing:
                old = col.get_note(existing[front])
                if old["Back"] != back or set(old.tags) != set(tags.split()):
                    old["Back"] = back
                    old.tags = tags.split()
                    col.update_note(old)
                    updated += 1
                continue
            note = col.new_note(model)
            note["Front"] = front
            note["Back"] = back
            note.tags = tags.split()
            col.add_note(note, deck_id)
            existing[front] = 1
            added += 1

        print(f"deck '{DECK}': {added} new, {updated} updated ({len(CARDS)} in file)")
        print(f"cards in deck: {col.decks.card_count(deck_id, include_subdecks=True)}")
        return 0
    finally:
        col.close()


if __name__ == "__main__":
    raise SystemExit(main())
