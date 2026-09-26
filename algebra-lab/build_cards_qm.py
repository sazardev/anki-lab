#!/usr/bin/env python3
"""Builds cards_qm.json -- quantum mechanics, beginner to advanced.

Source of truth is this file; cards_qm.json is generated. Use r"" strings so
backslashes stay single, and let json.dumps escape them. Keep HTML tags OUTSIDE
\\( ... \\): MathJax silently drops math that contains them.
"""

from cards_lib import write_json

DECKS: dict[str, list[dict]] = {}


def card_to(deck_name: str, front: str, back: str, *tags: str) -> None:
    DECKS.setdefault(deck_name, []).append(
        {"f": front, "b": back, "t": " ".join(tags)})


# ============================================================ Foundations
F = "QM::Foundations"

card_to(F, "What is quantum mechanics?",
        "The theory of matter at atomic scales, where <b>classical</b> quantities like energy and "
        "angular momentum take only <b>discrete</b> values, and states are described by a vector "
        "in an abstract vector space rather than by position and momentum.",
        "q::what", "qm::foundations")

card_to(F, "State the five postulates of quantum mechanics.",
        "1. A state is a ray in a Hilbert space \\(|\\psi\\rangle\\).<br>"
        "2. Observables are self-adjoint (Hermitian) operators.<br>"
        "3. Possible outcomes are the eigenvalues; a measurement returns one of them.<br>"
        r"4. Probabilities are \\(P(a) = |\\langle a|\\psi\\rangle|^2\\) (Born rule)." + "<br>"
        r"5. Between measurements, \\(|\\psi\\rangle\\) evolves by \\(|\\psi(t)\\rangle = U(t)|\\psi(0)\\rangle\\), with \\(U\\) unitary.",
        "q::what", "qm::foundations", "qm::postulates")

card_to(F, "What does the wavefunction actually represent?",
        "Not a material wave. It encodes the <b>amplitude</b> for every possible measurement "
        "outcome; only its <b>squared magnitude</b> is directly observable. The complex phase is "
        "unobservable on its own but matters through interference.",
        "q::pitfall", "qm::foundations")

card_to(F, "What is the Born rule?",
        r"The probability of measuring outcome \\(a\\) is \\(P(a) = |\\langle a|\\psi\\rangle|^2\\)."
        "<br>Probabilities of mutually exclusive outcomes add, so amplitudes add only when states "
        "are superposed.",
        "q::what", "qm::born-rule")

card_to(F, "How is a wavefunction normalised?",
        r"Require \\(\\int |\\psi(\\mathbf{x},t)|^2 d^3x = 1\\). For a normalised state this equals "
        r"\\(\\langle \\psi|\\psi\\rangle = 1\\).", "q::how", "qm::normalisation")

card_to(F, "What is superposition?",
        r"A linear combination of states: \\(|\\psi\\rangle = c_1|1\\rangle + c_2|0\\rangle\\) with "
        r"\\(|c_1|^2 + |c_2|^2 = 1\\).", "q::what", "qm::superposition")

card_to(F, "What happens on measurement?",
        "The state collapses (projects) onto the eigenstate of the operator measured, with "
        "probability given by the Born rule. Immediately after, the system is again in a definite "
        "state.",
        "q::what", "qm::measurement")

card_to(F, "Does measurement destroy every correlation?",
        "No. <b>Local</b> entanglement is destroyed, but a <b>global</b> correlation survives; that "
        "is the whole basis of Bell tests and quantum teleportation.",
        "q::pitfall", "qm::measurement")

card_to(F, "State the uncertainty principle.",
        r"For any two observables \\(A\\) and \\(B\\): "
        r"\\[ \\Delta A\\,\\Delta B \\geq \\frac{1}{2}\\big|\\langle [A,B] \\rangle\\big| \\]"
        "<br>For position and momentum this is "
        r"\\[ \\Delta x\\,\\Delta p \\geq \\frac{\\hbar}{2} \\]",
        "q::what", "qm::uncertainty")

card_to(F, "Where does the uncertainty principle come from?",
        "Not measurement disturbance. It is a property of the algebra: a state with a definite "
        "value of \\(A\\) is not also a state with a definite value of \\(B\\), because "
        r"\\(\\Delta A\\,\\Delta B\\) is bounded by the commutator.",
        "q::how", "qm::uncertainty")

card_to(F, "Is the uncertainty principle a limit on measurement accuracy?",
        "No. It is a limit on how <b>sharply</b> a state can be prepared with respect to two "
        "incompatible quantities, independent of how good the instrument is.",
        "q::pitfall", "qm::uncertainty")

card_to(F, "What is complementarity?",
        "Certain pairs of properties (position/momentum, polarisation paths) cannot both be "
        "assigned definite values to the same system. Which one is sharp is decided by the "
        "measurement you choose.",
        "q::what", "qm::complementarity")

card_to(F, "Planck's quantum hypothesis",
        "Energy is exchanged in discrete quanta \\(E = h\\nu\\), not continuously. This is what "
        "blackbody radiation forced, and it is the seed of the whole theory.",
        "q::what", "qm::foundations")

card_to(F, "Classify the hydrogen spectrum into series, and give the Lyman limit.",
        r"Lyman \\(n\\to1\\) (UV), Balmer \\(n\\to2\\) (visible), Paschen \\(n\\to3\\) (IR).<br>"
        r"The Lyman series converges to \\(\\nu \\to \\frac{m e^4}{8\\varepsilon_0^2 h^3 c}\\), "
        "the series limit.",
        "q::what", "qm::spectrum")

card_to(F, "Why is classical physics recovered from quantum mechanics?",
        r"For actions \\(S \\gg \\hbar\\) the interference phase over a region is tiny, so amplitudes "
        "add to an ordinary classical integral. This is the <b>semiclassical</b> (correspondence) limit.",
        "q::what", "qm::correspondence")

# ============================================================ Math
F = "QM::Math"

card_to(F, "What is a Hilbert space?",
        "A complete inner-product space. The state space of a quantum system is a Hilbert space: "
        "a vector space where lengths and angles come from an inner product and all Cauchy sequences "
        "converge.",
        "q::what", "qm::hilbert")

card_to(F, "What does Dirac notation mean?",
        r"A ket \\(|\\psi\\rangle\\) is a vector; a bra \\(\\langle\\phi|\\) is its dual covector. "
        r"Their product \\(\\langle\\phi|\\psi\\rangle\\) is the inner product; it is linear in "
        "\\(|\\psi\\rangle\\) and conjugate-linear in \\(|\\phi\\rangle\\).",
        "q::what", "qm::dirac")

card_to(F, "What is a self-adjoint (Hermitian) operator?",
        r"\\(\\hat A = \\hat A^\\dagger\\), i.e. \\(\\langle\\psi|\\hat A|\\phi\\rangle = "
        r"\\langle\\phi|\\hat A^\\dagger|\\psi\\rangle\\). Only self-adjoint operators have an "
        "orthonormal set of real eigenvalues, so they are exactly the observables.",
        "q::what", "qm::operators")

card_to(F, "How do you compute an expectation value?",
        r"\\[ \\langle A \\rangle = \\langle\\psi|\\hat A|\\psi\\rangle \\]"
        "<br>In position space "
        r"\\[ \\langle A \\rangle = \\int \\psi^*(x)\\,\\hat A\\,\\psi(x)\\,dx \\]",
        "q::how", "qm::operators")

card_to(F, "What is a commutator?",
        r"\\[ [A,B] = \\hat A\\hat B - \\hat B\\hat A \\]"
        "<br>A non-zero commutator means the two observables cannot share eigenstates, so both "
        "cannot be sharp at once.",
        "q::what", "qm::commutators")

card_to(F, "Why must position and momentum not commute?",
        r"\\[ [\\hat x,\\hat p] = i\\hbar \\]"
        "<br>Position and momentum are conjugate, so no state is sharp in both. The value \\(i\\hbar\\), "
        "not zero, is what makes Planck's constant physical.",
        "q::what", "qm::commutators")

card_to(F, "What is the completeness relation?",
        r"\\[ \\sum_i |a_i\\rangle\\langle a_i| = \\mathbb{1} \\]"
        "<br>It is the resolution of the identity in terms of any orthonormal eigenbasis, and it is "
        "how you expand an arbitrary state.",
        "q::what", "qm::basis")

card_to(F, "What is a product state for two particles?",
        r"\\(|\\psi\\rangle = |a\\rangle_1 \\otimes |b\\rangle_2\\). Equivalently "
        r"\\(|a\\rangle|b\\rangle\\). The factorised form is what separability means.",
        "q::what", "qm::tensor")

card_to(F, "What is the trace, and what is it good for?",
        r"\\[ \\mathrm{Tr}(A) = \\sum_i \\langle i|A|i\\rangle = \\sum_i \\lambda_i \\]"
        "<br>It is basis-independent, invariant under cyclic permutations of operators, and a pure "
        "state has \\(\\mathrm{Tr}(\\rho^2) = 1\\).",
        "q::what", "qm::density")

card_to(F, "What is a density matrix?",
        r"\\(\\rho = \\sum_k p_k |\\psi_k\\rangle\\langle\\psi_k|\\) with \\(p_k \\geq 0\\) and "
        r"\\(\\mathrm{Tr}\\rho = 1\\). It describes states where you do not (or cannot) know which "
        "pure state was prepared.",
        "q::what", "qm::density")

card_to(F, "Pure or mixed? How do you tell?",
        r"Pure states have \\(\\mathrm{Tr}(\\rho^2) = 1\\); mixed states give a value strictly "
        r"less than 1, the <b>purity</b>. A maximally mixed state of dimension \\(d\\) has "
        r"\\(\\mathrm{Tr}(\\rho^2) = 1/d\\).",
        "q::how", "qm::density")

card_to(F, "Why must a density matrix be a density matrix?",
        "It must be Hermitian, positive semi-definite, and have unit trace. Hermiticity and trace one "
        "make probabilities real and normalised; positivity is what makes every "
        "\\(P(a) = \\mathrm{Tr}(\\rho\\,E_a)\\) non-negative.",
        "q::how", "qm::density")

# ============================================================ Schrodinger
F = "QM::Schrodinger"

card_to(F, "State the time-dependent Schrodinger equation.",
        r"\\[ i\\hbar \\frac{\\partial}{\\partial t}|\\psi\\rangle = \\hat H |\\psi\\rangle \\]"
        "<br>In position space it is a first-order PDE in time and second order in space.",
        "q::what", "qm::schrodinger")

card_to(F, "What is a stationary state?",
        r"A state of definite energy: \\(\\hat H|\\psi_n\\rangle = E_n|\\psi_n\\rangle\\). It only "
        r"acquires a phase, \\(|\\psi_n(t)\\rangle = e^{-iE_nt/\\hbar}|\\psi_n\\rangle\\), so every "
        "measurable probability is time independent.",
        "q::what", "qm::stationary")

card_to(F, "What is the time-independent Schrodinger equation?",
        r"\\[ \\hat H\\psi = E\\psi \\]<br>Equivalently, for a potential that does not depend on time, "
        r"\\(\\left[-\\frac{\\hbar^2}{2m}\\nabla^2 + V(\\mathbf{x})\\right]\\psi = E\\psi\\). "
        "Finding the spectrum means solving this eigenvalue problem.",
        "q::what", "qm::schrodinger")

card_to(F, "How do you separate the Schrodinger equation?",
        r"Assume \\(|\\psi(\\mathbf{x},t)\\rangle = \\phi(\\mathbf{x})T(t)\\). Substitution gives "
        r"\\(T\\hat H\\phi = \\phi \\hat H T\\), so both must equal the same constant \\(E\\). Then "
        r"\\(T = e^{-iEt/\\hbar}\\) and \\(\\hat H\\phi = E\\phi\\).",
        "q::how", "qm::separation")

card_to(F, "Which operators represent x, p and H?",
        r"\\[ \\hat x = x, \\qquad \\hat p = -i\\hbar\\nabla, \\qquad "
        r"\\hat H = -\\frac{\\hbar^2}{2m}\\nabla^2 + V(\\mathbf{x}) \\]",
        "q::what", "qm::operators")

card_to(F, "State the energy-time uncertainty principle.",
        r"\\[ \\Delta H\\,\\Delta t \\geq \\frac{\\hbar}{2} \\]"
        "<br>Unlike the \\(x\\)–\\(p\\) case, \\(t\\) is not an operator, so this is not a statement "
        "about commutators; it says short-lived states have broad energy spread.",
        "q::what", "qm::uncertainty")

card_to(F, "What is the probability current?",
        r"\\[ \\mathbf{j} = \\frac{\\hbar}{m}\\mathrm{Im}\\left(\\psi^*\\nabla\\psi\\right) \\]"
        r"<br>It satisfies the continuity equation \\(\\partial_t |\\psi|^2 + \\nabla\\cdot\\mathbf{j} = 0\\), "
        "so probability is locally conserved.",
        "q::what", "qm::current")

card_to(F, "What is the physical difference between a global and an energy measurement?",
        "An energy measurement returns a <b>time average</b> because the phase drops out; a "
        "measurement of a general observable can be instantaneous. Energy is the only observable "
        "commuting with \\(\\hat H\\).",
        "q::pitfall", "qm::measurement")

card_to(F, "How do you solve a Schrodinger problem numerically?",
        "Discretise space on a grid, replace \\(\\nabla^2\\) by a finite-difference stencil, and build "
        "a symmetric tridiagonal Hamiltonian. Then diagonalise it (Lanczos, or sparse methods for "
        "large grids) to get the spectrum and eigenvectors.",
        "q::how", "qm::numerics")

card_to(F, "What is a wave packet, and why do we need it?",
        "A localised superposition of energy eigenstates, "
        r"\\(|\\psi\\rangle = \\int dE\\,\\tilde\\psi(E)|E\\rangle\\). Plane waves are delocalised and "
        "useless for particles with a definite position, so free particles are described by packets "
        "that spread with time.",
        "q::what", "qm::wavepackets")

card_to(F, "How fast does a free Gaussian packet spread?",
        r"For initial width \\(\\Delta x_0\\), after time \\(t\\): "
        r"\\[ \\Delta x(t) = \\Delta x_0\\sqrt{1 + \\left(\\frac{\\hbar t}{2m\\Delta x_0^2}\\right)^2} \\]"
        "<br>The spreading time \\(2m\\Delta x_0^2/\\hbar\\) is why macroscopic superpositions look classical.",
        "q::how", "qm::wavepackets")

# ============================================================ Potentials
F = "QM::Potentials"

card_to(F, "Energies of a particle in a one-dimensional infinite well.",
        r"For a well of width \\(L\\) on \\([0,L]\\):"
        r"\\[ E_n = \\frac{n^2\\pi^2\\hbar^2}{2mL^2}, \\qquad n = 1,2,3,\\dots \\]"
        "<br>The ground state is \\(n=1\\), never \\(n=0\\): a zero-energy wavefunction is not normalisable.",
        "q::what", "qm::infinite-well")

card_to(F, "Wavefunctions inside an infinite well.",
        r"\\[ \\psi_n(x) = \\sqrt{\\frac{2}{L}}\\sin\\!\\left(\\frac{n\\pi x}{L}\\right), \\quad 0<x<L, \\]"
        "<br>Zero outside. The sine is not arbitrary: the walls force \\(\\psi = 0\\) at the boundaries.",
        "q::what", "qm::infinite-well")

card_to(F, "Scaling rule for a particle in a box.",
        r"Halving \\(L\\) multiplies every energy by 4 (since \\(E \\propto L^{-2}\\)), and multiplies "
        "the momentum scale by 2. Conversely, doubling the mass has no effect on the energies at all.",
        "q::pitfall", "qm::infinite-well")

card_to(F, "Expectation value of x in the ground state of a well on [0,L].",
        r"The density is \\(2/L\\sin^2(\\pi x/L)\\), symmetric about \\(L/2\\), so "
        r"\\[ \\langle x\\rangle = L/2 \\]<br>yet \\(\\langle p\\rangle = 0\\): the particle is "
        "confined, not stationary.",
        "q::how", "qm::infinite-well")

card_to(F, "What is a delta-function potential?",
        r"\\(V = \\lambda\\,\\delta(x)\\). It is the cleanest non-smooth potential: a bound state "
        r"exists iff \\(\\lambda < 0\\), with \\(E = -m\\lambda^2/(2\\hbar^2)\\). Useful because it can "
        "be solved exactly and models a point defect.",
        "q::what", "qm::delta")

card_to(F, "What is tunnelling, qualitatively?",
        "A particle with energy below the barrier still has a non-zero amplitude on the far side, "
        "because the wavefunction decays as an exponential rather than stopping. Non-zero, but "
        "exponentially small, and it falls off hard with barrier width.",
        "q::what", "qm::tunnelling")

card_to(F, "Transmission through a rectangular barrier.",
        r"For \\(E < V_0\\), width \\(a\\):"
        r"\\[ T \\approx \\frac{16E(V_0-E)}{V_0^2} e^{-2\\kappa a}, \\qquad "
        r"\\kappa = \\frac{\\sqrt{2m(V_0-E)}}{\\hbar} \\]"
        "<br>The exponential is what makes tunnelling negligible in everyday mechanics but dominant "
        "in STM junctions and alpha decay.",
        "q::what", "qm::tunnelling")

card_to(F, "Derive alpha decay from tunnelling.",
        r"\\(\\kappa = \\sqrt{2m_\\alpha(V_0-E)/Q}\\), and the decay rate is a \\(\\kappa\\propto "
        r"\\sqrt{1/\\hbar}\\) barrier penetration. The Geiger-Nuttall law \\(T_{1/2} \\propto "
        r"1/Z^2\\)-ish exponential sensitivity is the empirical fingerprint.",
        "q::how", "qm::tunnelling")

card_to(F, "Energies of the quantum harmonic oscillator.",
        r"\\[ E_n = \\hbar\\omega\\left(n + \\tfrac{1}{2}\\right), \\qquad n = 0,1,2,\\dots \\]"
        "<br>Levels are <b>equally spaced</b> by \\(\\hbar\\omega\\), exactly like a classical "
        "oscillator. The ground state is \\(n=0\\) with energy \\(\\hbar\\omega/2\\).",
        "q::what", "qm::harmonic-oscillator")

card_to(F, "What are the ladder operators, and what do they do?",
        r"\\[ a = \\sqrt{\\frac{m\\omega}{2\\hbar}}\\left(\\hat x + \\frac{i\\hat p}{m\\omega}\\right),"
        r"\\qquad a^\\dagger = \\sqrt{\\frac{m\\omega}{2\\hbar}}\\left(\\hat x - \\frac{i\\hat p}{m\\omega}\\right) \\]"
        r"<br>\\(a|n\\rangle = \\sqrt{n}\\,|n-1\\rangle\\) and \\(a^\\dagger|n\\rangle = "
        r"\\sqrt{n+1}\\,|n+1\\rangle\\). They step through the ladder, which is why the spectrum is linear in \\(n\\).",
        "q::how", "qm::harmonic-oscillator")

card_to(F, "Why can the number operator not be negative?",
        r"\\(n = a^\\dagger a \\geq 0\\) because \\(\\|a|\\psi\\rangle\\|^2 \\geq 0\\). The state "
        r"\\(|n=-1\\rangle\\) is killed by \\(a\\), i.e. it is the zero vector, so negative indices simply do not exist.",
        "q::pitfall", "qm::harmonic-oscillator")

card_to(F, "Does the harmonic oscillator have a zero-energy state?",
        "No. The ground state has \\(E_0 = \\hbar\\omega/2\\), the <b>zero-point energy</b>, which is "
        "the minimum permitted by the uncertainty relation \\(\\Delta x\\,\\Delta p \\geq \\hbar/2\\). "
        "This has real consequences: \\({}^4\\mathrm{He}\\) stays liquid at 0 K.",
        "q::pitfall", "qm::harmonic-oscillator")

card_to(F, "What does the classical limit of the oscillator look like?",
        r"For large \\(n\\), the spacing \\(\\hbar\\omega\\) is negligible against \\(E_n \\approx "
        r"\\hbar\\omega n\\), so the ladder becomes a continuum. The probability density then tends to "
        r"the classical distribution \\(\\propto 1/\\sqrt{E - E_{\\min}}\\).",
        "q::pitfall", "qm::harmonic-oscillator")

card_to(F, "How many states lie below a given energy?",
        r"The number of states with \\(E_n \\leq E\\) is \\(n+1 \\leq 1 + E/(\\hbar\\omega) - 1/2 = "
        r"E/(\\hbar\\omega) + 1/2\\). This counting is the seed of statistical mechanics and the "
        "Planck blackbody result.",
        "q::how", "qm::harmonic-oscillator")

# ============================================================ Angular momentum
F = "QM::AngularMomentum"

card_to(F, "What is the eigenvalue equation of L squared?",
        r"\\[ \\hat L^2 |l,m\\rangle = \\hbar^2 l(l+1)|l,m\\rangle, \\qquad l = 0,1,2,\\dots \\]"
        "<br>Because of the \\(l(l+1)\\) factor, angular momentum never has a sharp magnitude and a "
        "sharp component at the same time.",
        "q::what", "qm::angular-momentum")

card_to(F, "Eigenvalues of Lz and their degeneracy.",
        r"\\[ \\hat L_z |l,m\\rangle = \\hbar m|l,m\\rangle, \\qquad m = -l,-l+1,\\dots,l \\]"
        "<br>So \\(m\\) has \\(2l+1\\) values, and each eigenvalue is degenerate in \\(l\\).",
        "q::what", "qm::angular-momentum")

card_to(F, "What are the allowed values of l, and what is each called?",
        "Integers \\(l = 0,1,2,3,\\dots\\) are called s, p, d, f, g, h. The letters are only labels, "
        "not values: an f electron has \\(l=3\\).",
        "q::what", "qm::quantum-numbers")

card_to(F, "Give the four quantum numbers for an atomic electron.",
        r"\\(n = 1,2,\\dots\\); \\(l = 0,\\dots,n-1\\); \\(m = -l,\\dots,l\\); "
        r"\\(m_s = \\pm \\tfrac12\\). The count \\(\\sum 2(2l+1) = 2n^2\\) gives the shell capacity.",
        "q::what", "qm::quantum-numbers")

card_to(F, "What are spherical harmonics?",
        r"Eigenfunctions of \\(\\hat L^2\\) and \\(\\hat L_z\\): "
        r"\\[ Y_l^m(\\theta,\\varphi) \\propto P_l^m(\\cos\\theta)\\,e^{im\\varphi} \\]"
        "<br>They are the angular part of the hydrogen wavefunction, and \\(|Y_l^m|^2\\) is the "
        "probability of finding the electron at those angles.",
        "q::what", "qm::angular-momentum")

card_to(F, "What is spin half, and what are its states?",
        r"Intrinsic angular momentum with \\(s = \\tfrac12\\), so "
        r"\\(\\hat S^2 = \\frac{3}{4}\\hbar^2\\) and \\(m_s = \\pm \\tfrac12\\). It is <b>not</b> a "
        "tiny spinning ball: it has no classical counterpart and appears even in a stationary particle.",
        "q::what", "qm::spin")

card_to(F, "Give the spin-1/2 operators as matrices.",
        r"\\[ S_x = \\frac{\\hbar}{2}\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}, \\quad "
        r"S_y = \\frac{\\hbar}{2}\begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}, \\quad "
        r"S_z = \\frac{\\hbar}{2}\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix} \\]"
        "<br>These are the Pauli matrices times \\(\\hbar/2\\).",
        "q::what", "qm::spin")

card_to(F, "Give the spin-up and spin-down states in Dirac notation.",
        r"\\[ |\\uparrow\\rangle = \begin{pmatrix}1\\0\end{pmatrix} = "
        r"|\\tfrac12, +\\tfrac12\\rangle, \\qquad |\\downarrow\\rangle = "
        r"\begin{pmatrix}0\\1\end{pmatrix} = |\\tfrac12, -\\tfrac12\\rangle \\]",
        "q::what", "qm::spin")

card_to(F, "What are the singlet and triplet states of two spin-1/2 particles?",
        r"Symmetric (triplet, \\(S=1\\)): "
        r"\\(|\\uparrow\\uparrow\\rangle, |\\uparrow\\downarrow\\rangle + |\\downarrow\\uparrow\\rangle, "
        r"|\\downarrow\\downarrow\\rangle\\).<br>"
        r"Antisymmetric (singlet, \\(S=0\\)): "
        r"\\(|\\uparrow\\downarrow\\rangle - |\\downarrow\\uparrow\\rangle\\).",
        "q::what", "qm::spin")

card_to(F, "What is the total spin of two spin-1/2 particles?",
        r"\\(\\hat{\\mathbf S}_1\\cdot\\hat{\\mathbf S}_2\\) has eigenvalues \\(\\frac{\\hbar^2}{4}(S(S+1) - 3)\\), "
        r"so \\(S=0\\) gives \\(-\\frac{3}{4}\\hbar^2\\) and \\(S=1\\) gives \\(+\\frac{1}{4}\\hbar^2\\). "
        "Ferromagnetism comes from choosing the triplet.",
        "q::how", "qm::spin")

card_to(F, "How do you add two angular momenta?",
        r"\\(|j_1-j_2| \\leq j \\leq j_1 + j_2\\) in integer steps, so for two spin-1/2, "
        r"\\(j = 0\\) or 1. The Clebsch-Gordan coefficients give the weights of each product state in the coupled basis.",
        "q::how", "qm::angular-momentum")

card_to(F, "What is the Zeeman effect?",
        "A magnetic field \\(B\\) along \\(z\\) splits a level by "
        r"\\[ \\Delta E = \\mu_B B\\,g\\,m_j, \\qquad \\mu_B = \\frac{e\\hbar}{2m_e} \\]"
        "<br>Weak fields: the anomalous effect includes the Landé factor \\(g_J\\) from the total angular momentum.",
        "q::what", "qm::zeeman")

# ============================================================ Atoms
F = "QM::Atoms"

card_to(F, "The hydrogen Hamiltonian and potential.",
        r"A proton and electron separated by \\(r = |\\mathbf{x}|\\):"
        r"\\[ \\hat H = -\\frac{\\hbar^2}{2m_e}\\nabla^2 - \\frac{\\hbar^2}{2m_p}\\nabla_p^2 "
        r"- \\frac{e^2}{4\\pi\\varepsilon_0 r} \\]"
        "<br>Separating the centre of mass leaves a relative motion with reduced mass "
        r"\\(\\mu = m_em_p/(m_e+m_p) \\approx 0.9995\\,m_e\\).",
        "q::what", "qm::hydrogen")

card_to(F, "Energy levels of hydrogen.",
        r"\\[ E_n = -\\frac{\\mu e^4}{2(4\\pi\\varepsilon_0)^2\\hbar^2 n^2} "
        r"= -\\frac{13.6\\ \\mathrm{eV}}{n^2} \\]"
        "<br>Bound states have \\(n \\geq 1\\); the continuum is \\(E \\geq 0\\). The negative sign "
        "is what makes ionisation cost energy.",
        "q::what", "qm::hydrogen")

card_to(F, "What is the Bohr radius?",
        r"\\[ a_0 = \\frac{4\\pi\\varepsilon_0\\hbar^2}{\\mu e^2} = 0.529\\ \\text{\u00c5} \\]"
        "<br>It is the most probable distance of the electron from the proton in the ground state, "
        "and it sets the size of every hydrogen-like atom.",
        "q::what", "qm::hydrogen")

card_to(F, "How does the hydrogen energy scale with nuclear charge?",
        r"\\(E_n \\propto -Z^2/n^2\\) for a hydrogen-like ion. So \\(\\mathrm{He}^+\\) has four times "
        "the binding energy of \\(\\mathrm{H}\\), and \\(\\mathrm{Fe}^{25+}\\) is X-ray scale. This is "
        "the basis of X-ray spectroscopy.",
        "q::pitfall", "qm::hydrogen")

card_to(F, "Hydrogen wavefunctions and their labels.",
        r"\\[ \\psi_{nlm}(\\mathbf{r}) = R_{nl}(r)\\,Y_l^m(\\theta,\\varphi) \\]"
        "<br>Labels: \\(1s\\) is \\(n=1,l=0\\); \\(2s\\) is \\(n=2,l=0\\); \\(2p\\) is \\(n=2,l=1\\). "
        "Angular momentum and magnetic moment are conserved, so \\(l\\) and \\(m\\) do not mix.",
        "q::what", "qm::hydrogen")

card_to(F, "Why is hydrogen degenerate in l?",
        "In a pure Coulomb field, the potential is rotationally symmetric, so all \\(l\\) with the same "
        "\\(n\\) have the same energy. The degeneracy is lifted by fine structure, spin-orbit coupling "
        "and the Lamb shift.",
        "q::why", "qm::hydrogen")

card_to(F, "State the electric-dipole selection rules.",
        r"\\((\\Delta l = \\pm 1)\\), \\((\\Delta m = 0, \\pm 1)\\), and spin must be conserved "
        r"\\((\\Delta s = 0)\\). Parity changes. So \\(1s \\to 1s\\) and \\(1s \\to 2s\\) are "
        "<b>forbidden</b> by electric dipole, even though 2s lies below 2p.",
        "q::what", "qm::selection-rules")

card_to(F, "Why does effective nuclear charge replace Z in multi-electron atoms?",
        "Inner electrons shield the outer ones, so an outer electron feels roughly "
        r"\\[ Z_{\\text{eff}} = Z - \\sigma \\]<br>with \\(\\sigma\\) close to the number of core "
        "electrons. This is why the periodic table is built from a modified hydrogen.",
        "q::what", "qm::many-electron")

card_to(F, "State the Aufbau order of orbital filling.",
        "1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, 7s, 5f, 6d, 7p.<br>"
        "It follows the Madelung rule \\(n + l\\) with ties broken by smaller \\(n\\): fill every "
        "\\((n+l)\\) combination before moving to the next, so 4s fills before 3d.",
        "q::what", "qm::many-electron")

card_to(F, "Why does the Madelung rule really work?",
        "Because 4s and 3d overlap in energy, and in a many-electron atom 3d electrons shield weakly. "
        "Quantum-mechanically the order is a many-body result, not a one-electron fact; the rule is a "
        "very good approximation, not a theorem.",
        "q::pitfall", "qm::many-electron")

card_to(F, "State Hund's rules.",
        "1. Fill degenerate orbitals singly with parallel spins before pairing.<br>"
        "2. If the subshell stays half full or fully full it is especially stable.<br>"
        "3. For a subshell with less than half filling, the term with the <b>smallest</b> \\(J\\) is lowest; "
        "with more than half filling, the <b>largest</b> \\(J\\).",
        "q::what", "qm::hund")

card_to(F, "What is exchange energy?",
        r"Two electrons of opposite spin in overlapping orbitals have wavefunctions that partly cancel "
        r"between the nuclei, which <b>raises</b> the energy. Placing them in different orbitals "
        "avoids this, so parallel-spin pairs in different orbitals are preferred. It is the origin of "
        "the \\(\\mathrm{H}_2\\) bond and of Hund's first rule.",
        "q::what", "qm::exchange")

card_to(F, "Compare the magnitude of exchange splitting.",
        "Exchange is a <b>correction</b>, not a competitor: splittings run from a fraction of an "
        r"electronvolt to a few eV, against hartree-scale (\\(\\approx 27\\) eV) electrostatic "
        r"repulsion and similar orbital energies. So exchange refines a result you already had, and in "
        r"Hund's rule it sets the sign of a small splitting between nearly degenerate states.",
        "q::pitfall", "qm::exchange")

# ============================================================ Identical particles
F = "QM::IdenticalParticles"

card_to(F, "What is exchange symmetry?",
        "Permuting identical particles is a symmetry of the Hamiltonian, so the wavefunction is an "
        "eigenfunction of the exchange operator: either symmetric (bosons) or antisymmetric "
        "(fermions). No other option exists for a scalar symmetry.",
        "q::what", "qm::identical")

card_to(F, "What does antisymmetry imply physically?",
        r"Two fermions cannot share all quantum numbers, because the symmetric part of their common "
        r"orbital must vanish. That single fact produces the periodic table, atomic stability, and the "
        r"\\(\\varepsilon_0\\) in the hydrogen problem.",
        "q::why", "qm::pauli")

card_to(F, "Write the symmetric and antisymmetric combinations of two states.",
        r"\\[ |\\psi_\\pm\\rangle = \\frac{1}{\\sqrt{2}}\\left(|ab\\rangle \\pm |ba\\rangle\\right) \\]"
        "<br>Plus for bosons, minus for fermions.",
        "q::how", "qm::identical")

card_to(F, "What is degeneracy pressure?",
        "Exclusion forces fermions into higher momentum states at \\(T \\to 0\\), generating pressure "
        r"without any thermal motion, \\(P \\sim n^{5/3}\\). It is what keeps white dwarfs and neutron "
        "stars from collapsing, and it is why helium needs pressure to freeze.",
        "q::what", "qm::degeneracy")

card_to(F, "What is Bose-Einstein condensation?",
        "Below a critical temperature, an ideal Bose gas accumulates a macroscopic population in the "
        r"ground state, \\(\\mu \\to 0\\) and \\(n_0/N \\to 1\\). The condensate has no classical "
        "analogue and is a macroscopic quantum state.",
        "q::what", "qm::bec")

card_to(F, "Compare chemical potentials at zero temperature.",
        r"Fermions: \\(\\mu \\to E_F > 0\\), the Fermi energy, which is where the sea is full.<br>"
        r"Bosons: \\(\\mu \\to 0\\) from below, because the ground state is degenerate and can be filled "
        "without limit.",
        "q::pitfall", "qm::bec")

card_to(F, "Why is exchange a large effect in a solid but a small one in free atoms?",
        "In a free atom the same spatial orbital already forbids two electrons in it, so exchange only "
        "reshuffles states within a shell. In a solid, orbitals from many atoms overlap, so the "
        "occupied combination is a coherent superposition and exchange gains a macroscopic factor, "
        "setting the observed bonding in noble-gas solids.",
        "q::why", "qm::exchange")

# ============================================================ Approximation
F = "QM::Approximation"

card_to(F, "State the variational principle.",
        r"For any trial state \\(|\\psi\\rangle\\),"
        r"\\[ E_{\\text{GS}} \\leq \\langle\\psi|\\hat H|\\psi\\rangle \\]"
        "<br>Equality only for a true eigenstate, so minimising the energy over a family of trial "
        "states always approaches the ground energy from above and never below it.",
        "q::what", "qm::variational")

card_to(F, "Why does the variational principle hold?",
        r"Expanding any state in the energy basis, \\(\\langle H\\rangle = \\sum_n w_n E_n\\) with "
        r"\\(w_n \\geq 0\\) and \\(\\sum w_n = 1\\), so it is a weighted average of the spectrum and "
        r"can never fall below its smallest value.",
        "q::how", "qm::variational")

card_to(F, "What is the Born-Oppenheimer approximation?",
        r"Electrons are so much lighter than nuclei (\\(\\sim 1/1836\\)) that the nuclear kinetic "
        r"energy is negligible on the electronic timescale. Solve for \\(\\psi(\\mathbf{x};\\mathbf{R})\\) "
        r"with nuclei frozen at \\(\\mathbf{R}\\), then treat the resulting electronic energy as a "
        r"potential surface for nuclear motion.",
        "q::what", "qm::born-oppenheimer")

card_to(F, "Beyond Born-Oppenheimer: what is a PES?",
        r"The electronic energy \\(E_{\\text{el}}(\\mathbf{R})\\) is a potential energy surface for the "
        r"nuclei. Minima give equilibrium geometries, transition states are saddle points, and chemical "
        r"reaction dynamics is nuclear motion on these surfaces.",
        "q::what", "qm::born-oppenheimer")

card_to(F, "State first-order non-degenerate perturbation theory.",
        r"For \\(\\hat H = \\hat H_0 + \\lambda\\hat V\\) with unperturbed states \\(|n\\rangle\\):"
        r"\\[ E_n \\approx E_n^{(0)} + \\lambda\\langle n|\\hat V|n\\rangle \\]"
        r"<br>Corrections are second order in the small parameter, so the first-order shift is the "
        "expectation value in the unperturbed state.",
        "q::what", "qm::perturbation")

card_to(F, "First-order correction to the wavefunction.",
        r"\\[ |n\\rangle \\approx |n^{(0)}\\rangle + \\lambda\\sum_{m \\neq n} "
        r"\\frac{\\langle m|\\hat V|n\\rangle}{E_n^{(0)} - E_m^{(0)}} |m\\rangle \\]"
        "<br>It mixes in states of <b>different</b> symmetry only, since the matrix element vanishes otherwise.",
        "q::how", "qm::perturbation")

card_to(F, "What must change in degenerate perturbation theory?",
        r"If the unperturbed level is degenerate, diagonalise the perturbation <b>inside</b> the "
        r"degenerate subspace. Any basis choice outside it is arbitrary, and the naive expectation "
        r"value \\(\\langle n|\\hat V|n\\rangle\\) is basis dependent.",
        "q::what", "qm::perturbation")

card_to(F, "What does WKB quantisation give?",
        r"In classically allowed and forbidden regions solve \\(\\psi \\sim e^{\\pm "
        r"\\frac{1}{\\hbar}\\int\\sqrt{2m(E-V)}\\,dx}\\), then impose smoothness: the action across a "
        r"full oscillation cycle is quantised, \\(\\oint p\\,dq = 2\\pi\\hbar(n + \\tfrac12)\\) (Maslov).",
        "q::what", "qm::wkb")

card_to(F, "When is WKB valid?",
        r"Only where the wavelength is short compared to the scale on which the potential varies, "
        r"i.e. \\(|\\kappa'^{-1}| \\ll |\\kappa^{-1}|\\) with \\(\\kappa = \\sqrt{2m(E-V)}/\\hbar\\). "
        "It recovers the harmonic oscillator only if the Maslov index \\(1/2\\) is included, and it is "
        "what explains the hydrogen \\(n\\) degeneracy and the radial quantum number \\(l+1\\).",
        "q::pitfall", "qm::wkb")

card_to(F, "What is the tight-binding (LCAO) model?",
        "Replace an extended orbital by orbitals localised on each site and let them combine: "
        r"\\(|\\psi_k\\rangle = \\sum_j e^{ikx_j}|j\\rangle\\). This gives a band, a dispersion, and "
        "band gaps, which is why it describes metals, insulators and semiconductors qualitatively.",
        "q::what", "qm::tight-binding")

card_to(F, "What is the Hubbard model?",
        r"\\(\\hat H = -t\\sum\\langle ij\\rangle c^\\dagger_i c_j + U\\sum_i n_i(n_i-1)\\) with \\(t\\) "
        "hopping and \\(U\\) repulsion. It is minimal but captures the competition between kinetic and "
        "potential energy that drives Mott insulators, and it is the standard starting point for "
        "strongly correlated electrons.",
        "q::what", "qm::strong-correlation")

card_to(F, "What is Lindblad's equation?",
        r"\\(\\frac{d\\rho}{dt} = -\\frac{i}{\\hbar}[H,\\rho] + \\sum_k \\gamma_k "
        r"\\left(L_k\\rho L_k^\\dagger - \\tfrac12\\{L_k^\\dagger L_k,\\rho\\}\\right)\\)"
        "<br>Unitary evolution conserves purity; the dissipative terms do not, and are required to model "
        "decoherence and open quantum systems.",
        "q::what", "qm::open-systems")


def main() -> None:
    write_json("cards_qm", DECKS)


if __name__ == "__main__":
    main()
