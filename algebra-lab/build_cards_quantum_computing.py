#!/usr/bin/env python3
"""Builds cards_quantum_computing.json -- qubits, gates, algorithms, errors.

Source of truth is this file; the JSON is generated. r"" strings keep single
backslashes; json.dumps escapes them. HTML tags stay OUTSIDE \\( ... \\).
"""

from cards_lib import write_json

DECKS: dict[str, list[dict]] = {}


def card_to(deck_name: str, front: str, back: str, *tags: str) -> None:
    DECKS.setdefault(deck_name, []).append(
        {"f": front, "b": back, "t": " ".join(tags)})


# ============================================================ Qubits
F = "QC::Qubits"

card_to(F, "What is a qubit?",
        "A two-level quantum system, the abstract equivalent of a classical bit. Its state is a "
        r"unit vector \\(|\\psi\\rangle = \\alpha|0\\rangle + \\beta|1\\rangle\\) with "
        r"\\(|\\alpha|^2 + |\\beta|^2 = 1\\).",
        "q::what", "qc::qubit")

card_to(F, "Why does a qubit hold more information than a bit?",
        "A bit is 0 or 1; a qubit is a <b>superposition</b>, and it can be in any of infinitely many "
        "states. That is not more classical information, though: measurement still returns only one "
        "bit, and the gain shows up only in interference and entanglement.",
        "q::why", "qc::qubit")

card_to(F, "How many classical bits does n qubits represent?",
        r"Exactly \\(2^n\\). So 10 qubits = 1024 amplitudes, 20 qubits = about a million, 50 qubits "
        "exceeds the memory of a supercomputer. The <b>state</b> is exponential even though a single "
        "measurement is not.",
        "q::what", "qc::qubit")

card_to(F, "What does measuring a qubit give?",
        r"0 or 1, with probabilities \\(|\\alpha|^2\\) and \\(|\\beta|^2\\). After measurement the "
        "state is \\(|0\\rangle\\) or \\(|1\\rangle\\) respectively: one bit, and the phase is gone.",
        "q::what", "qc::measurement")

card_to(F, "What is the Bloch sphere?",
        r"Every pure qubit state maps to a point on the unit sphere, with amplitudes "
        r"\\[ \\alpha = \\cos\\frac{\\theta}{2}, \\qquad \\beta = e^{i\\varphi}\\sin\\frac{\\theta}{2} \\]"
        "<br>Two angles, so the state has two real parameters, as it should. The sphere is <b>not</b> "
        "a 3D physical space: distance on it is meaningless.",
        "q::what", "qc::bloch")

card_to(F, "Where are the computational basis states on the Bloch sphere?",
        r"\\(|0\\rangle\\) is the north pole and \\(|1\\rangle\\) the south pole; the equator is the "
        r"whole equator. Measuring along axis \\(\\hat n\\) returns 0 or 1 with probability "
        r"\\((1 \\pm \\hat r\\cdot\\hat n)/2\\).",
        "q::how", "qc::bloch")

card_to(F, "What is the X gate, and what does it do?",
        r"Not \\(X\\)-rotation (that is \\(R_x\\)). The Pauli \\(X\\) is the <b>NOT</b> gate: it flips "
        r"\\(|0\\rangle \\leftrightarrow |1\\rangle\\), is its own inverse, and is the bit-flip. It "
        r"swaps the Bloch sphere's \\(\\pm z\\) and \\(\\pm x\\) axes.",
        "q::what", "qc::gates")

card_to(F, "What is the Z gate?",
        r"The <b>phase flip</b>: \\(|0\\rangle \\to |0\\rangle\\), \\(|1\\rangle \\to -|1\\rangle\\). It "
        r"leaves populations untouched, so it is invisible in computational-basis measurement, but it "
        r"shifts phase and therefore interferes.",
        "q::what", "qc::gates")

card_to(F, "What is the H gate?",
        r"The <b>Hadamard</b>: \\(H = \\frac{1}{\\sqrt2}\begin{pmatrix}1 & 1\\ 1 & -1"
        r"\end{pmatrix}\\). It is its own inverse and rotates \\(\\pi\\) about the axis between \\(x\\) "
        r"and \\(z\\). It turns \\(|0\\rangle\\) into the \\(+\\) superposition and is how you create "
        r"superposition from a classical bit.",
        "q::what", "qc::gates")

card_to(F, "What is the S gate?",
        r"A quarter-turn phase flip: \\(|0\\rangle \\to |0\\rangle\\), \\(|1\\rangle \\to i|1\\rangle\\). "
        r"\\(S^2 = Z\\). It is the discrete version of \\(R_z\\), and \\(S^\\dagger ZS = X\\), so "
        r"phase gates and X generate single-qubit Clifford operations.",
        "q::what", "qc::gates")

card_to(F, "How does a general single-qubit gate look?",
        r"Any one-qubit unitary is a rotation: \\(U = e^{i\\alpha}R_z(\\gamma)R_y(\\beta)R_z(\\delta)\\), "
        r"with three parameters for \\(2\\times2\\) unitaries modulo global phase. General rotations "
        r"need a non-Clifford gate such as \\(T = \\mathrm{diag}(1, e^{i\\pi/4})\\).",
        "q::what", "qc::gates")

card_to(F, "What is the T gate and why does it matter?",
        r"\\(T = \\mathrm{diag}(1, e^{i\\pi/4})\\), a \\(\\pi/4\\) phase. The Clifford group alone is "
        "not universal; adding \\(T\\) is, and \\(T\\) is <b>not</b> efficiently simulable classically. "
        "It is the source of essentially all the fault-tolerance cost.",
        "q::what", "qc::gates")

card_to(F, "What is a global phase, and why is it unphysical?",
        r"Multiplying \\(|\\psi\\rangle\\) by \\(e^{i\\theta}\\) changes no probabilities, since "
        r"\\(|e^{i\\theta}\\alpha|^2 = |\\alpha|^2\\). So global phases are dropped, and two operators "
        r"differing only by one act identically on states. Unitaries are equivalent up to this factor.",
        "q::what", "qc::qubit")

# ============================================================ Multi-qubit & entanglement
F = "QC::Entanglement"

card_to(F, "What is entanglement?",
        "Two or more qubits in a joint state that <b>cannot</b> be written as a product "
        r"\\(|\\psi\\rangle_{AB} = |a\\rangle_A \\otimes |b\\rangle_B\\). Measurement outcomes are "
        "correlated beyond anything classical local variables can reproduce.",
        "q::what", "qc::entanglement")

card_to(F, "List the two Bell states.",
        r"\\[ |\\Phi^+\\rangle = \\frac{|00\\rangle + |11\\rangle}{\\sqrt2}, \\qquad "
        r"|\\Phi^-\\rangle = \\frac{|00\\rangle - |11\\rangle}{\\sqrt2} \\]"
        r"<br>and the other pair, \\(|\\Psi^\\pm\\rangle = \\frac{|01\\rangle \\pm |10\\rangle}"
        r"{\\sqrt2}\\). They are maximally entangled, with zero local information.",
        "q::what", "qc::entanglement")

card_to(F, "How do you prepare a Bell pair in one step?",
        r"Start from \\(|00\\rangle\\), apply \\(H\\) to the first qubit, then \\(\\mathrm{CNOT}\\) with "
        r"the first as control: \\(CNOT\\cdot(H\\otimes I)|00\\rangle = |\\Phi^+\\rangle\\). "
        "The pattern <b>H then CNOT</b> is the standard entangler.",
        "q::how", "qc::entanglement")

card_to(F, "What correlation do Bell states show?",
        r"Measuring in the same basis on both qubits gives <b>perfectly identical</b> outcomes for "
        r"\\(\\Phi^\\pm\\) and <b>perfectly opposite</b> for \\(\\Psi^\\pm\\), always. No local hidden "
        r"variable theory reproduces all four; that is Bell's theorem, tested to loophole-free standard.",
        "q::what", "qc::entanglement")

card_to(F, "What is monogamy of entanglement?",
        "If A and B are maximally entangled, A cannot be entangled with C at the same time. This is "
        "why entanglement is a resource, and it is the security argument behind quantum key distribution.",
        "q::what", "qc::entanglement")

card_to(F, "What is entanglement entropy?",
        r"For a bipartite pure state, \\(S_A = S_B = -\\mathrm{Tr}(\\rho_A \\log \\rho_A)\\) and the "
        r"total entropy is zero: you can measure A perfectly only by destroying A's link to B. "
        r"For \\(|\\Phi^+\\rangle\\) the reduced state is \\(\\mathbb{1}/2\\), so \\(S = \\ln 2\\).",
        "q::what", "qc::entanglement")

card_to(F, "Can you clone a qubit?",
        r"No. For unitary \\(U\\) and any unknown state, \\(U(|0\\rangle|0\\rangle + |1\\rangle|0\\rangle)"
        r"= U|0\\rangle|0\\rangle + U|1\\rangle|0\\rangle\\) cannot equal "
        r"\\(|0\\rangle|0\\rangle + |1\\rangle|1\\rangle\\), since the first summand forces "
        r"\\(U = I\\). No-cloning holds even for imperfect copying (no-cloning with noise).",
        "q::what", "qc::entanglement")

card_to(F, "Can you broadcast an unknown qubit to two receivers?",
        r"No. Broadcasting requires cloning. The two no-go results differ in strength: "
        "no-cloning forbids copying regardless of entanglement, no-broadcast forbids distributing to "
        r"several parties even if they <b>start entangled</b>.",
        "q::pitfall", "qc::entanglement")

card_to(F, "What is the controlled-Z gate used for?",
        r"It applies \\(Z\\) to the target only if the control is 1, and it is symmetric in the two "
        r"qubits. With Hadamards on both qubits it produces a <b>phase</b> kickback: "
        r"\\(\\mathrm{CZ}(H\\otimes H)|+\\rangle|-\\rangle = |-\\rangle|-\\rangle\\). That converts a "
        r"phase into a measurable bit, and is how \\(Z\\) and CNOT are built from \\(H\\) and CNOT.",
        "q::how", "qc::gates")

card_to(F, "What is phase kickback?",
        "Apply a gate to the target conditioned on a control, and the phase of the <b>control</b> "
        "state encodes information about the target. E.g. \\(\\mathrm{CNOT}\\) sends "
        r"\\(|a\\rangle|-\\rangle \\to |a\\rangle|-a\\rangle\\). It is the standard trick for computing "
        "a function into the phase.",
        "q::what", "qc::gates")

card_to(F, "Which two-qubit gates are CNOT and CZ, and are they related?",
        r"CNOT is a bit flip on the target, CZ a phase flip; both are symmetric under interchange. "
        r"\\[ \\mathrm{CZ} = (I\\otimes H)\\,\\mathrm{CNOT}\\,(I\\otimes H) \\]"
        "<br>so any symmetric entangling gate gives both. CZ is the usual choice in trapped-ion and "
        "neutral-atom hardware; CNOT in superconducting and photonic.",
        "q::what", "qc::gates")

card_to(F, "How do you get a Toffoli gate, and why do you care?",
        r"\\(\\mathrm{CCX} = (I\\otimes H)\\,\\mathrm{CNOT}\\,(I\\otimes H)\\,\\mathrm{CNOT}\\). "
        r"It is the <b>universal</b> classical gate: any reversible Boolean function is a composition "
        r"of Toffoli and single-qubit gates, which is what makes quantum simulation of chemistry "
        r"possible.",
        "q::what", "qc::gates")

# ============================================================ Circuits
F = "QC::Circuits"

card_to(F, "What is a quantum circuit?",
        "A network of gates acting on a register, read left to right or right to left depending on "
        "convention, ending in measurements. It is a compact description of a unitary followed by a "
        "measurement, and it is <b>not</b> reversible after measurement.",
        "q::what", "qc::circuits")

card_to(F, "Why must quantum gates be unitary?",
        r"Unitarity gives \\(\\|\\psi\\|^2\\) constant in time, i.e. conservation of total probability, "
        r"and makes evolution reversible and norm-preserving. Non-unitary 'gates' (measurement, "
        r"amplitude damping) are legitimate but stochastic and irreversible, which is exactly why they "
        r"cannot be freely composed into a circuit.",
        "q::why", "qc::circuits")

card_to(F, "What does circuit depth mean?",
        "The longest path through the circuit, in layers of parallel gates. It matters because "
        "decoherence grows with depth: the shallower the circuit, the more gates fit before errors "
        "accumulate. Optimising for depth, not gate count, is the right target.",
        "q::what", "qc::circuits")

card_to(F, "What is the gate set {H, T, CNOT}?",
        "A <b>universal</b> set: every unitary on n qubits can be built from it to arbitrary accuracy. "
        "Clifford gates \\(\\{H,S,CNOT\\}\\) are not universal but are cheap and simulable, and "
        "everything outside the Clifford group is expensive.",
        "q::what", "qc::circuits")

card_to(F, "What is a quantum subroutine?",
        r"A block of gates reused many times. Without them, a linear-algebraic decomposition of a "
        r"1024-dimensional unitary has \\(\\sim 4^n\\) parameters, so you would need exponentially many "
        r"distinct gates; with a good ansatz (product states, low-depth layers) only polynomial.",
        "q::why", "qc::circuits")

card_to(F, "Why is compiling to a hardware basis hard?",
        "Because a single logical gate decomposes into many physical ones, and \\(T\\) and \\(S\\) "
        "have very different costs. Solovay-Kitaev gives \\(O(\\log^c(1/\\varepsilon))\\) overhead, but "
        "in practice phase-polynomial synthesis and the required *T-count* dominate.",
        "q::how", "qc::circuits")

card_to(F, "What is the Solovay-Kitaev algorithm?",
        "Approximates any single-qubit gate to accuracy \\(\\varepsilon\\) using a fixed finite gate "
        "set, with length \\(O(\\log^c(1/\\varepsilon))\\). Needed because hardware cannot implement "
        "arbitrary rotations exactly. The constants are still too large in practice, so the standard "
        "tool is phase-polynomial synthesis plus qubit-efficient routing.",
        "q::what", "qc::circuits")

card_to(F, "What is transpilation, and what does it optimise?",
        "Mapping a circuit onto a real device: choose the basis, route for connectivity, then optimise. "
        "The objective is \\(2n\\) SWAPs (or \\(3n\\) for a line) per long-range gate plus a big "
        "depth penalty, and the result is compared by expected cost, not gate count.",
        "q::how", "qc::circuits")

card_to(F, "What is circuit cutting, and when is it used?",
        "Partition a circuit so that each fragment is small enough to simulate classically, then "
        "reconstruct the expectation values from many fragment evaluations. The cost grows "
        "exponentially in the number of cuts, so it only pays for shallow circuits spread over many "
        "qubits -- the opposite regime from fault tolerance.",
        "q::how", "qc::circuits")

card_to(F, "What is the difference between a gate model and an annealer?",
        "A gate model is universal and exactly simulates quantum evolution, but needs error "
        "correction. An annealer (D-Wave) is a restricted Ising machine run adiabatically: far "
        "larger qubit counts, but it can only solve that one class of problem and is not universal.",
        "q::pitfall", "qc::circuits")

# ============================================================ Algorithms
F = "QC::Algorithms"

card_to(F, "What is the quantum Fourier transform?",
        r"\\[ \\mathrm{QFT}|x\\rangle = \\frac{1}{\\sqrt{N}}\\sum_{y=0}^{N-1} e^{2\\pi i xy/N}"
        r"|y\\rangle \\]<br>It is the quantum analogue of the FFT, and it maps phase information into "
        r"the amplitudes, which is the reverse of what the classical FFT exploits.",
        "q::what", "qc::qft")

card_to(F, "How many gates does the QFT need?",
        r"\\(O(n^2)\\) for \\(n\\) qubits, because the Hadamards and controlled phase rotations at "
        r"different distances cannot all run in parallel. It is cheap to apply but its output is "
        r"scrambled, so reading it needs many measurements.",
        "q::how", "qc::qft")

card_to(F, "What is the Deutsch-Jozsa algorithm?",
        "Shows a genuine quantum advantage on a promise problem: a function "
        r"\\(\\{0,1\\}^n \\to \\{0,1\\}\\) known to be either constant or balanced. One query suffices "
        r"versus \\(2^{n-1}\\) classically, via interference. It is the simplest witness that quantum "
        r"computing changes asymptotics, though the problem is contrived.",
        "q::what", "qc::algorithms")

card_to(F, "State Grover's algorithm and its cost.",
        r"Searching \\(N = 2^n\\) unsorted items for a marked one takes "
        r"\\(O(\\sqrt{N}) = 2^{n/2}\\) queries with probability near 1, versus \\(O(N)\\) classically. "
        r"The trick is amplitude amplification: about \\((\\pi/4)\\sqrt{N}\\) reflections about the "
        r"mean and the marked state.",
        "q::what", "qc::grover")

card_to(F, "What is the optimality caveat on Grover?",
        r"The \\(\\sqrt{N}\\) is optimal: BBBV proves any quantum search needs \\(\\Omega(\\sqrt{N})\\). "
        r"It is a square-root, not exponential, speedup, so it only wins for enormous \\(N\\) -- and "
        r"not against structured search problems that classical algorithms already handle in poly time.",
        "q::pitfall", "qc::grover")

card_to(F, "Why does Grover need multiple qubits?",
        "Diffusion is an \\(n\\)-qubit operation, so a search over \\(2^n\\) items needs an oracle "
        "acting on all \\(n\\) plus the extra ancilla for the phase oracle: about \\(n+1\\) qubits. "
        "Search for \\(N\\) items therefore needs \\(\\log_2 N + 1\\) qubits, not \\(N\\).",
        "q::pitfall", "qc::grover")

card_to(F, "State Shor's factoring algorithm and its cost.",
        r"Factors \\(N\\) in \\(O((\\log N)^3)\\) time, versus the best classical sub-exponential "
        r"(general number field sieve, roughly \\(e^{O((\\log N)^{1/3}(\\log\\log N)^{2/3})}\\)). The "
        r"exponential-in-input-size gap is the real result, not the \\(O(n^3)\\) itself.",
        "q::what", "qc::shor")

card_to(F, "How does Shor's algorithm turn factoring into a period problem?",
        r"Pick \\(a\\) coprime to \\(N\\), compute \\(a^r \\bmod N\\). Fermat's little theorem says "
        r"\\(a^r = 1\\) for some \\(r\\) dividing \\(\\varphi(N)\\), so \\(r\\) is a period. QFT of "
        r"\\(|a^x \\bmod N\\rangle\\) reveals \\(r\\) by finding peaks near \\(kN'/r\\), and \\(\\gcd\\) "
        r"gives a factor. The exponential speedup is in <b>period finding</b>.",
        "q::how", "qc::shor")

card_to(F, "What is quantum simulation, and why is it expected to win first?",
        "Simulating another quantum system (chemistry, materials, lattice QCD) with a quantum "
        "computer. The output is a state that is generically exponential to describe, and the "
        "Hamiltonians are local and structured, so natural ansätze work. This needs no speedup "
        "argument at all: the problem itself is quantum.",
        "q::why", "qc::algorithms")

card_to(F, "What is HHL, and why is it often dismissed?",
        r"Linear-system solve in \\(O(\\log^2 N)\\) given a good condition number and an efficient "
        r"state-preparation/measurement oracle. The input preparation and readout are exponentially "
        r"costly, so the honest end-to-end complexity is often worse than classical. It demonstrates "
        r"a query-model speedup, not a practical one.",
        "q::pitfall", "qc::algorithms")

# ============================================================ Resources
F = "QC::Resources"

card_to(F, "What are the main quantum resource costs?",
        "<b>Qubit count</b> (memory, the hardest to scale), <b>two-qubit gate count</b> (the real "
        "time cost), <b>T-count</b> (the fault-tolerance cost), and <b>depth</b> (the decoherence "
        "budget). Optimising a circuit means trading these off, not minimising gate count.",
        "q::what", "qc::resources")

card_to(F, "Why are T gates the expensive ones?",
        "Fault tolerance needs a code that can correct both bit and phase errors, which forces a "
        "large overhead. Within a surface code, each logical T gate costs roughly a few thousand "
        "physical gates, while Clifford gates are much cheaper. So <b>T-count</b> is the number that "
        "predicts hardware time, not the total gate count.",
        "q::why", "qc::resources")

card_to(F, "What is qubit overhead in a fault-tolerant scheme?",
        "Roughly a factor \\(d^2\\) physical qubits per logical qubit, where \\(d\\) is the code "
        "distance. With \\(d \\sim 25\\)-30 and thousands of logical qubits needed, that is millions "
        "of physical qubits, which is the main reason useful FTQC is out of reach today.",
        "q::what", "qc::resources")

card_to(F, "What is a NISQ device and what limits it?",
        "Noisy Intermediate-Scale Quantum: tens to thousands of qubits with two-qubit error rates "
        "around \\(10^{-3}\\), far above the roughly \\(10^{-10}\\) an unprotected algorithm needs. No "
        "long computations are possible without error correction, so NISQ-era value is in "
        "demonstration and in error mitigation.",
        "q::what", "qc::resources")

card_to(F, "What is zero-noise extrapolation, and what is its weakness?",
        "Run the circuit at several artificially amplified noise levels, fit the result against the "
        "noise parameter, and extrapolate back to zero. The weakness is that the extrapolation is a "
        "polynomial fit to a function that is not known to be polynomial, so it can be badly biased; "
        "it also costs a multiple of the circuit count.",
        "q::pitfall", "qc::resources")

card_to(F, "What is dynamical decoupling?",
        r"Inserting idle periods of \\(\\pi\\) pulses so that idle and gate noise partly cancel, "
        r"extending \\(T_2^*\\) toward \\(T_2\\). It suppresses \\(z\\)-type error and a little \\(xy\\), "
        r"but cannot remove gate errors, so it helps shallow circuits and not deep ones.",
        "q::how", "qc::resources")

card_to(F, "What is readout error, and how is it handled?",
        "State-preparation and measurement error: the reported bit is wrong for a small fraction of "
        "shots. It is measured by preparing a known state many times, and mitigated by calibration "
        "matrices or by changing the assignment of outcomes. It is a calibration problem, not a "
        "coherence problem, so it is comparatively cheap to fix.",
        "q::how", "qc::resources")

card_to(F, "What are T1 and T2?",
        r"\\(T_1\\) is energy relaxation: the \\(z\\)-component of Bloch vector decays as "
        r"\\(e^{-t/T_1}\\). \\(T_2\\) is dephasing, where the transverse component decays as "
        r"\\(e^{-t/T_2}\\). Always \\(T_2 \\leq 2T_1\\), and \\(T_2^*\\) is the even shorter observed "
        r"dephasing from inhomogeneous broadening.",
        "q::what", "qc::resources")

card_to(F, "What is quantum volume?",
        "A hardware benchmark: the largest square circuit an average-width device can run so that the "
        r"output distribution stays close to ideal. It counts qubits \\(n\\) and depth \\(d\\) as a "
        r"single number \\(2^d\\), and it is a best-case metric, not a measure of useful performance.",
        "q::what", "qc::resources")

card_to(F, "Which metric best predicts useful quantum advantage?",
        "Not qubits or volume, but <b>logical operations before failure</b>: how many error-corrected "
        "gates a device can sustain. A device with many noisy qubits is less useful than a small one "
        "with a small logical error rate, because advantage needs total error below a threshold "
        "across the whole computation.",
        "q::why", "qc::resources")

# ============================================================ Error correction
F = "QC::ErrorCorrection"

card_to(F, "Why is quantum error correction hard?",
        "You cannot measure an error without collapsing the state, and you cannot copy the state to "
        "compare. The fix is <b>redundancy in entangled subspaces</b>, plus a rule that errors take a "
        "known, recoverable form. Knill-Laflamme: \\(PEQ^\\dagger P = c_{ab}E_a^\\dagger E_b\\).",
        "q::what", "qc::qec")

card_to(F, "What does the Knill-Laflamme condition say?",
        r"For a code correcting errors \\(E_a\\), it requires "
        r"\\(PEQ^\\dagger P = c_{ab}E_a^\\dagger E_b\\). For a code that corrects an error exactly, "
        r"\\(P E_a^\\dagger E_b P = c_{ab}P\\): products of two errors act as scalars on the code "
        r"space, so syndromes are computable without learning the logical state.",
        "q::what", "qc::qec")

card_to(F, "What is a syndrome, and why is measuring it safe?",
        r"Correlate the error with an auxiliary system and measure that. The logical state is "
        r"untouched because the error operators act trivially on the code space: "
        r"\\(|\\psi\\rangle_L |0\\rangle \\to E_a|\\psi\\rangle_L|a\\rangle\\). You learn <b>which</b> "
        r"error occurred without learning anything about the encoded amplitudes.",
        "q::how", "qc::qec")

card_to(F, "Does the 3-qubit bit-flip code correct phase errors?",
        r"No. It corrects a single \\(X\\) (bit flip) because \\(|000\\rangle\\) and "
        r"\\(|111\\rangle\\) are the logical basis and both syndromes are distinct, but a single \\(Z\\) "
        r"acts as a logical phase and is <b>undetectable</b>. You need at least three qubits to detect "
        r"anything at all, since two errors are indistinguishable from one error plus a global phase.",
        "q::pitfall", "qc::qec")

card_to(F, "How does the Shor 9-qubit code correct arbitrary single-qubit errors?",
        "Concatenate three 3-qubit phase-flip codes, one per physical qubit, so a phase flip becomes a "
        "bit flip at the outer level, and correct that with the 3-qubit bit-flip code. Arbitrary "
        "errors decompose into \\(X\\), \\(Y\\), \\(Z\\) components, so this covers everything.",
        "q::how", "qc::qec")

card_to(F, "What does the threshold theorem say?",
        "If physical error rates are below a threshold, arbitrarily long computations are possible "
        "with a polylogarithmic overhead in the ideal circuit size, by encoding with a growing code "
        "distance and concatenating. The threshold for surface codes is roughly \\(10^{-2}\\) to "
        "\\(10^{-3}\\) with good hardware and fast decoding.",
        "q::what", "qc::qec")

card_to(F, "What is the surface code?",
        "A 2D topological code defined on a square lattice of qubits, with stabilizers "
        r"\\(A_v = X^{u_1}X^{u_2}X^{u_3}X^{u_4}\\) on vertices and "
        r"\\(A_p = Z^{v_1}Z^{v_2}Z^{v_3}Z^{v_4}\\) on faces, plus a global constraint. Its great "
        "virtue is locality: with only nearest-neighbour coupling you can still do universal "
        "computation via lattice surgery.",
        "q::what", "qc::qec")

card_to(F, "What is lattice surgery?",
        "Merging and splitting logical qubits by stabiliser measurement instead of moving them "
        "physically. It avoids the extra ancilla and routing of code deformation, and the space cost "
        "is \\(d\\) rows of ancilla, which is why surface-code schedules are dominated by the \\(d^2\\) "
        "overhead.",
        "q::how", "qc::qec")

card_to(F, "What is magic state distillation?",
        "Distil noisy \\(|T\\rangle\\) states into cleaner ones by running a code on the encoded "
        "state, improving fidelity at the cost of more qubits and time. This is the standard way to "
        "reduce the T-count overhead, and it is what determines whether a fault-tolerant T gate is "
        "affordable.",
        "q::how", "qc::qec")


def main() -> None:
    write_json("cards_quantum_computing", DECKS)


if __name__ == "__main__":
    main()
