#!/usr/bin/env python3
"""Builds cards_computing.json -- algorithms, data structures, PL, OS, networks,
databases, security, ML.

Source of truth is this file; the JSON is generated. r"" strings keep single
backslashes; json.dumps escapes them. HTML tags stay OUTSIDE \\( ... \\).
"""

from cards_lib import write_json

DECKS: dict[str, list[dict]] = {}


def card_to(deck_name: str, front: str, back: str, *tags: str) -> None:
    DECKS.setdefault(deck_name, []).append(
        {"f": front, "b": back, "t": " ".join(tags)})


# ============================================================ Complexity
F = "CS::Complexity"

card_to(F, "What does big-O actually assert?",
        "An asymptotic <b>upper</b> bound: \\(f(n) = O(g(n))\\) if there are constants \\(C, n_0\\) with "
        r"\\(f(n) \\leq C\\,g(n)\\) for all \\(n \\geq n_0\\). It says nothing about a lower bound, and "
        "it says nothing for the specific inputs you happen to have.",
        "q::what", "cs::big-o")

card_to(F, "Why is big-O a poor predictor of real speed?",
        "It ignores constants, and in practice constants dominate. Insertion sort is "
        r"\\(O(n^2)\\) and merge sort \\(O(n\\log n)\\), yet for \\(n\\) under about 20 insertion sort "
        "wins because of cache behaviour and low overhead. Use \\(\\Theta\\) when you care about the "
        "true growth.",
        "q::pitfall", "cs::big-o")

card_to(F, "State the common complexity classes.",
        "| class | shape | example |<br>|"
        "|---|---|---|<br>"
        "| \\(O(1)\\) | constant | array index, hash lookup |<br>"
        "| \\(O(\\log n)\\) | logarithmic | binary search, balanced-tree descent |<br>"
        "| \\(O(n)\\) | linear | scan |<br>"
        "| \\(O(n\\log n)\\) | sorting | merge sort, heap sort |<br>"
        "| \\(O(n^2)\\) | quadratic | bubble sort, naive all-pairs |<br>"
        "| \\(O(2^n)\\), \\(O(n!)\\) | exponential, factorial | exhaustive search, TSP |",
        "q::what", "cs::big-o")

card_to(F, "What is a P versus NP problem?",
        "P is the set of decision problems solvable in polynomial time. NP is the set whose solutions "
        "are verifiable in polynomial time. \\(P \\stackrel{?}{=} NP\\) asks whether every easily "
        "verified problem is also easily solved. It is a question about <b>verifiability</b> versus "
        "<b>findability</b>.",
        "q::what", "cs::complexity-classes")

card_to(F, "What is NP-hardness, and why is it the right notion of hard?",
        "A problem is NP-hard if every problem in NP reduces to it in polynomial time, so a fast "
        "solver for it would collapse the hierarchy. It is the standard certificate of intractability, "
        "and it is what makes SAT, travelling salesman and knapsack hard.",
        "q::what", "cs::complexity-classes")

card_to(F, "How do you show a problem is NP-hard?",
        "By exhibiting a polynomial-time reduction from a known NP-hard problem, and proving both "
        "directions of the equivalence. Restating the problem in different words is not a proof, and "
        "exponential-looking brute force is not evidence of hardness.",
        "q::how", "cs::complexity-classes")

card_to(F, "What is space complexity, and why does it surprise people?",
        "Space is the memory a computation needs, and a naive reading suggests more memory is always "
        "worse. But any \\(O(n^2)\\)-time algorithm can be made to run in \\(O(\\log n)\\) space by "
        "recomputing, and any polynomial-space problem has an exponential-time algorithm, so the two "
        "measures are not simply ordered.",
        "q::what", "cs::complexity-classes")

# ============================================================ Algorithms
F = "CS::Algorithms"

card_to(F, "When is divide and conquer appropriate?",
        "When the problem splits into <b>independent</b> subproblems of smaller size, and combining "
        "their solutions is cheap. The recurrence is \\(T(n) = aT(n/b) + f(n)\\), and the Master "
        "theorem reads off the result. Non-independent subproblems mean you need dynamic programming.",
        "q::how", "cs::algorithms")

card_to(F, "State the Master theorem cases.",
        r"For \\(T(n) = aT(n/b) + O(n^d)\\), with \\(a \\geq 1, b > 1\\):<br>"
        r"• \\(d > \\log_b a \\): \\(T(n) = O(n^d)\\) -- the work at the leaves dominates.<br>"
        r"• \\(d = \\log_b a \\): \\(T(n) = O(n^d \\log n)\\).<br>"
        r"• \\(d < \\log_b a \\): \\(T(n) = O(n^{\\log_b a})\\) -- recursion dominates.<br>"
        "Merge sort is the classic borderline case.",
        "q::what", "cs::algorithms")

card_to(F, "What does the Master theorem not cover?",
        r"Recurrences with subtraction, with irregular branching, or with \\(f(n) = O(n^d \\log^k n)\\). "
        r"Also \\(T(n) = 2T(n/2) + O(n)\\) (merge sort) is exactly borderline and needs the "
        r"logarithmic factor, which a careless reading misses.",
        "q::pitfall", "cs::algorithms")

card_to(F, "When does greedy work?",
        "Only when the locally best choice is provably extendable to a global optimum, which is "
        "certified by the <b>exchange argument</b> or <b>stays-ahead</b>. Interval scheduling, "
        "Huffman coding and MST are greedy and correct; most interval-scheduling-looking problems "
        "with weights are not.",
        "q::how", "cs::algorithms")

card_to(F, "What is dynamic programming good for?",
        "Overlapping subproblems plus an optimal substructure, where a table of smaller answers can be "
        "reused. Longest common subsequence, shortest paths, knapsack, optimal BST. The cost is "
        "usually polynomial space, and the win comes from reuse.",
        "q::how", "cs::algorithms")

card_to(F, "What is the difference between recursion and dynamic programming?",
        "Recursion re-solves the same subproblem many times, e.g. naive Fibonacci in "
        r"\\(O(\\varphi^n)\\) with an exponential call tree. Memoising or bottom-up tabulation makes it "
        r"linear. The structure is identical; only the reuse differs.",
        "q::pitfall", "cs::algorithms")

card_to(F, "What is the 0/1 knapsack recurrence, and why is it 0/1?",
        r"\\[ dp[i][w] = \\max\\big(dp[i-1][w],\\; v_i + dp[i-1][w-w_i]\\big) \\]"
        "<br>The \\(i-1\\) index forces each item to be used at most once. Unbounded knapsack instead "
        r"uses \\(dp[w]\\) on both sides, which allows repeats. Cost is \\(O(nW)\\), pseudo-polynomial "
        "in the capacity.",
        "q::how", "cs::algorithms")

card_to(F, "Why is knapsack called pseudo-polynomial?",
        "Because \\(O(nW)\\) is polynomial in the numeric value of \\(W\\), but \\(W\\) may be encoded "
        "in \\(\\log W\\) bits, so in the input size it is exponential. Knapsack is therefore only "
        "weakly NP-complete, and is exactly where dynamic programming and a greedy-like approach can "
        "still be useful.",
        "q::pitfall", "cs::algorithms")

card_to(F, "How does Dijkstra's algorithm work, and what is its limitation?",
        r"Repeatedly finalises the closest unvisited vertex, relaxing its edges: \\(O((V+E)\\log V)\\) "
        r"with a binary heap. It requires <b>non-negative</b> edge weights. With negative edges a "
        r"closer vertex may still improve later, and the algorithm silently gives wrong answers; use "
        r"Bellman-Ford (no negativity needed) when weights may be negative.",
        "q::how", "cs::algorithms")

card_to(F, "What is the A* algorithm?",
        r"A* is Dijkstra guided by an admissible heuristic \\(h\\): "
        r"\\[ f(n) = g(n) + h(n) \\]"
        r"<br>Admissible means \\(h\\) never overestimates the true remaining cost, which guarantees "
        r"optimality. With \\(h=0\\) it reduces to Dijkstra, so A* is a generalisation.",
        "q::what", "cs::algorithms")

card_to(F, "What is memoization versus bottom-up tabulation?",
        "Memoization adds caching to top-down recursion, computing only reachable states. Bottom-up "
        "fills a table in dependency order, computing all states but with no recursion overhead and no "
        "stack risk. They produce the same table; the choice is recursion depth versus wasted work.",
        "q::pitfall", "cs::algorithms")

# ============================================================ Data structures
F = "CS::DataStructures"

card_to(F, "Compare array, linked list, and dynamic array.",
        "| structure | random access | insert at front | memory |<br>|"
        "|---|---|---|---|<br>"
        "| static array | \\(O(1)\\) | \\(O(n)\\) | contiguous, no pointers |<br>"
        "| linked list | \\(O(n)\\) | \\(O(1)\\) given a cursor | scattered, per-node overhead |<br>"
        "| dynamic array | \\(O(1)\\) | \\(O(n)\\) | contiguous, amortised \\(O(1)\\) append |<br>"
        "In practice dynamic arrays win almost everywhere because of cache locality.",
        "q::what", "cs::data-structures")

card_to(F, "Why is dynamic-array append amortised O(1)?",
        r"On reaching capacity, double it and copy. A run of \\(n\\) appends performs \\(O(\\log n)\\) "
        r"resizes totalling \\(1+2+4+\\dots < 2n\\) copies, so the cost is \\(O(n)\\) over \\(n\\) "
        r"operations. Growth by a <b>constant</b> factor instead would make append \\(O(n)\\) "
        r"amortised in the worst case.",
        "q::how", "cs::data-structures")

card_to(F, "What is the invariant of a binary heap?",
        "Every node is at least as large as its children (max-heap), so the maximum is always at the "
        "root. It gives \\(O(1)\\) find-max, \\(O(\\log n)\\) insert and remove-max, and the linear-time "
        "heapify (\\(\\Theta(n)\\), from the last internal node downwards) needed to build from an array.",
        "q::what", "cs::data-structures")

card_to(F, "How good is a hash table, and what is the weak point?",
        r"Average \\(O(1)\\) insert, lookup and delete, but worst case \\(O(n)\\) when every key "
        r"collides. Adversarial keys can force this, so production tables randomise the hash. Also "
        r"load factor above about 0.7 degrades linearly, and iteration order is <b>unordered</b>.",
        "q::pitfall", "cs::data-structures")

card_to(F, "What is a B-tree and why do databases use it?",
        "A balanced tree with many keys per node, so it is very shallow. A node sized to a 16 KB "
        "disk page holds about 1000 keys, so the fanout is ~1000: depth 2 stores about "
        "\\(10^6\\) keys and depth 3 about \\(10^9\\). A binary search tree would need depth 20 and "
        "\\(20\\) random reads for the same \\(10^6\\) keys. The node size is chosen to match the "
        "disk page, which is why the structure is disk-friendly.",
        "q::what", "cs::data-structures")

card_to(F, "What is a B-tree versus a B+ tree?",
        "A B+ tree stores data only in leaves and links them in order, so range scans are a simple "
        "sequential walk. A B tree stores data in every node, gaining one level of capacity but "
        "losing ordered-leaf scanning. Databases mostly use B+ trees.",
        "q::pitfall", "cs::data-structures")

card_to(F, "What are the trade-offs of quicksort?",
        r"In-place and \\(O(n\\log n)\\) on average with excellent cache behaviour, but \\(O(n^2)\\) "
        r"on sorted or reverse-sorted input with a naive pivot. Median-of-three or introsort (which "
        r"switches to heapsort when recursion gets too deep) removes the worst case. Mergesort is "
        r"stable and \\(O(n\\log n)\\) worst case but needs \\(O(n)\\) extra space.",
        "q::pitfall", "cs::data-structures")

card_to(F, "What is a graph adjacency list versus adjacency matrix?",
        "Adjacency list is \\(O(V+E)\\) space and takes \\(O(\\deg(v))\\) to list neighbours, so it is "
        "the right choice for sparse graphs (almost all real ones). A matrix is \\(O(V^2)\\) space but "
        "gives \\(O(1)\\) edge lookup, which only pays off for dense graphs or repeated membership "
        "tests.",
        "q::what", "cs::data-structures")

# ============================================================ PL
F = "CS::PL"

card_to(F, "What is the difference between a compiled and interpreted language?",
        "Compilation translates the whole program before running, so errors surface early and loops "
        "can be optimised; interpretation executes statement by statement, so it starts instantly and "
        "is easy to debug. Most modern languages are <b>hybrid</b>: e.g. V8 compiles JS to bytecode, "
        "JIT-compiles hot functions, and Java bytecode is interpreted or JIT-compiled per method.",
        "q::what", "cs::languages")

card_to(F, "What is the difference between statically and dynamically typed languages?",
        "Static types are checked before running, and types are part of the program, so they are "
        "documented and refactorable. Dynamic types defer to runtime, giving flexibility. Note that "
        "static typing does not prevent memory unsafety: C is statically typed and has buffer "
        "overflows, because type safety and memory safety are different properties.",
        "q::what", "cs::types")

card_to(F, "What is memory safety?",
        "Guaranteeing that a program never dereferences an invalid or freed pointer, and that memory "
        "is freed exactly once. Rust gets it from ownership and borrowing checked at compile time; "
        "garbage-collected languages get it from a tracing collector; C and C++ do not, which is why "
        "use-after-free and buffer overflow account for a large share of security vulnerabilities.",
        "q::what", "cs::memory")

card_to(F, "What is manual memory management's core difficulty?",
        "Every allocation must be matched by exactly one free, on <b>every</b> path including errors, "
        "exceptions and early returns. A leak is a missed free; a double free is two; a "
        "use-after-free is reading memory that has been handed back. The three failures are one "
        "bookkeeping bug seen three ways.",
        "q::why", "cs::memory")

card_to(F, "What is the difference between heap and stack allocation?",
        "The stack holds locals and return addresses, is freed automatically on return, and is fast "
        "but small and LIFO. The heap is for dynamically sized objects, lives until explicitly freed "
        "or garbage-collected, and is larger. Allocating a large array on the stack is a real bug: it "
        "can smash the stack rather than growing it.",
        "q::what", "cs::memory")

card_to(F, "What is the difference between pass-by-value, pass-by-reference, and pass-by-pointer?",
        "Pass-by-value copies, so the callee cannot affect the caller's variable. Pass-by-reference "
        "passes an alias, so it can. Pass-by-pointer passes an address explicitly, so \\(nullptr\\) is "
        "possible and the callee can reassign the pointer. The commonest bug is expecting "
        "pass-by-value semantics and being surprised that the caller sees no change.",
        "q::what", "cs::functions")

card_to(F, "What is the difference between an interface and an abstract class?",
        "An interface specifies capabilities with no state; an abstract class may hold state and "
        "provide implementations. So multiple interfaces can be combined but only one class can be "
        "inherited from. The distinction is a design signal, not just syntax: use interfaces to "
        "describe roles, abstract classes to share implementation.",
        "q::what", "cs::paradigms")

# ============================================================ OS
F = "CS::OS"

card_to(F, "What is the difference between a process and a thread?",
        "A process is an address space plus resources; a thread is a stack and registers inside a "
        "process. Threads in one process share memory, so communication is cheap but a data race in "
        "one corrupts all. Processes are isolated, so a crash is contained but communication needs "
        "pipes or shared memory.",
        "q::what", "cs::processes")

card_to(F, "What is context switching, and why is it expensive?",
        "Saving one thread's registers, stack pointer and program counter, then loading another's. The "
        "cost is the bookkeeping plus <b>cache and TLB pollution</b>: the new thread runs against cold "
        "caches, which usually dominates. This is why reducing switches matters more than making them "
        "cheaper.",
        "q::why", "cs::processes")

card_to(F, "What is a race condition?",
        "Behaviour that depends on the unsynchronised interleaving of concurrent operations, so the "
        "result is not deterministic. Classic form: check-then-act, e.g. testing a counter, then "
        "incrementing it non-atomically. Fixes are mutual exclusion, atomics, or immutable data that "
        "removes the window.",
        "q::what", "cs::concurrency")

card_to(F, "What is the difference between a mutex and a semaphore?",
        "A mutex is mutual exclusion: one owner at a time, and only the owner may release. A "
        "semaphore is a counter of N permits with no ownership, so it can signal a different thread "
        "and can be used to count N resources. Using a semaphore of one as a lock is a common but "
        "lossy substitution, since release-by-another is then allowed.",
        "q::what", "cs::concurrency")

card_to(F, "What is a deadlock, and what are the four conditions?",
        "Two or more threads each waiting on the other, permanently blocked.<br>"
        "1. Mutual exclusion: a resource is held exclusively.<br>"
        "2. Hold and wait: a thread holds while requesting more.<br>"
        "3. No preemption: resources cannot be forcibly taken.<br>"
        "4. Circular wait: the wait-for graph has a cycle.<br>"
        "Break any one to prevent it, and the standard orderings (global lock order, or try-lock) "
        "target the last.",
        "q::what", "cs::concurrency")

card_to(F, "What is a memory barrier, and when is it needed?",
        "A fence that forbids the compiler or CPU from reordering or caching writes across it. It is "
        "needed for lock-free code publishing data: without a release barrier the data write can become "
        "visible after the flag write, so a reader can see the flag but not the data. An ordinary "
        "mutex implies the needed barriers, so you rarely write them yourself.",
        "q::what", "cs::concurrency")

card_to(F, "What is virtual memory?",
        "Giving each process its own address space and mapping it to physical frames on demand. It "
        "gives isolation, lets programs exceed physical memory via paging, and simplifies loading. The "
        "price is a page table (and TLB misses) plus the possibility of thrashing when working sets "
        "exceed physical memory.",
        "q::what", "cs::memory")

card_to(F, "What is paging versus swapping?",
        "Paging moves individual pages between RAM and disk as needed, so a process needs only its "
        "active pages resident; the virtual address space never has to fit anywhere whole. Swapping "
        "moves a whole process. Paging won, and \"swapping\" in modern systems usually means "
        "reclaiming anonymous pages rather than whole processes.",
        "q::what", "cs::memory")

card_to(F, "What is a file system journal?",
        "A log of intended metadata operations, written before they are applied, so a crash mid-update "
        "can be replayed or rolled back. It protects <b>metadata only</b>: after replay the directory "
        "structure is consistent, but a partially written file's contents are still whatever was "
        "flushed. ext4 and NTFS are journalling; FAT is not.",
        "q::what", "cs::filesystems")

# ============================================================ Networking
F = "CS::Networking"

card_to(F, "Where does each layer sit, and what does each do?",
        "Bottom to top: physical (bits, voltage), data link (frames, MAC, per-hop), network "
        "(packets, IP routing), transport (ports, reliability, TCP/UDP), application (HTTP, DNS, "
        "SMTP). Each layer adds a header and offers its service to the one above, using the services "
        "of the one below.",
        "q::what", "cs::networking")

card_to(F, "Why is TCP called end-to-end reliable, and what is its cost?",
        "Because reliability is implemented in the hosts, not in routers, so it works across any "
        "unreliable path. The cost is latency, head-of-line blocking, and the handshake plus "
        "acknowledgement traffic. It also means the network core can drop or reorder packets without "
        "breaking correctness, which is why NAT and firewalls can be stateless.",
        "q::why", "cs::networking")

card_to(F, "What is the three-way handshake, and why not two?",
        r"1. Client sends SYN.<br>2. Server replies SYN+ACK.<br>3. Client sends ACK.<br>"
        "Two messages would leave an ambiguity: a delayed first SYN could make the server keep a "
        "half-open connection it will never hear about. The third message confirms both sides agree, "
        "which is also what lets the client report its initial receive window.",
        "q::how", "cs::networking")

card_to(F, "What causes the Nagle algorithm to hurt latency?",
        "Nagle withholds a small segment until an in-flight one is acknowledged, to avoid wasting "
        "bandwidth. Combined with delayed ACK it can add hundreds of milliseconds to interactive "
        "traffic. Modern stacks often set both off (TCP_NODELAY) and rely on application-level "
        "batching instead.",
        "q::pitfall", "cs::networking")

card_to(F, "What is a subnet mask for, and how do you tell network from host bits?",
        "It marks which part of an IP address identifies the network and which the host, so a router "
        "knows what to forward. The host part is not all zeros (this network) or all ones "
        "(broadcast). CIDR \\(192.168.1.0/24\\) gives 24 network bits and 8 host bits, so 254 usable "
        "addresses.",
        "q::how", "cs::networking")

card_to(F, "What is a DNS record, and how does resolution work?",
        "Names map to records. A resolver walks the hierarchy: root, then TLD, then authoritative "
        "nameserver, using referrals plus recursion, and caches the answer with a TTL. Records you meet "
        "in practice: A/AAAA for addresses, CNAME for aliases, MX for mail, TXT for verification and "
        "policy, NS for delegation.",
        "q::what", "cs::networking")

card_to(F, "What is congestion control, and what is it trying to do?",
        "Adjust the sending rate to keep the network just below capacity, without central knowledge. "
        "Reno and CUBIC grow the window until packet loss or delay signals congestion, then halve it; "
        "BBR instead uses delay and throughput as signals. It is a control problem run in the "
        "endpoints, so it has to be conservative.",
        "q::what", "cs::networking")

# ============================================================ Databases
F = "CS::Databases"

card_to(F, "What are the ACID properties?",
        "<b>Atomicity</b>: all or nothing, via rollback.<br>"
        "<b>Consistency</b>: constraints hold at commit.<br>"
        "<b>Isolation</b>: concurrent transactions behave as if serial.<br>"
        "<b>Durability</b>: committed data survives a crash.<br>"
        "Durability costs a write to stable storage on every commit; isolation costs concurrency.",
        "q::what", "cs::databases")

card_to(F, "Which isolation level prevents what?",
        "Read uncommitted can see dirty data; read committed prevents that but can re-read a different "
        "value in one transaction; repeatable read prevents that but can show phantoms; serializable "
        "prevents phantoms too, at the greatest cost. The levels are ordered by anomalies prevented, "
        "and higher levels buy correctness with locks or multi-version concurrency control.",
        "q::what", "cs::databases")

card_to(F, "What do the normal forms fix, and what is the point of 3NF?",
        "1NF: atomic values, no repeating groups. 2NF: no partial dependency on a composite key. 3NF: "
        "no transitive dependency of non-key attributes on the key. The goal is not tidiness but that "
        "each fact is stored once, which is what makes anomalies (update, insertion, deletion) "
        "impossible rather than merely handled.",
        "q::what", "cs::databases")

card_to(F, "Why does an index help, and when does it not?",
        r"B-trees let a lookup skip most rows, turning \\(O(n)\\) scans into \\(O(\\log n)\\) plus a "
        r"random read. It does not help when the predicate is not selective, when it is applied to a "
        r"function of the column, or on small tables where a sequential scan wins. Every index also "
        r"costs write amplification and space.",
        "q::how", "cs::databases")

card_to(F, "What is a database index, and what are the two main kinds?",
        "A redundant structure mapping column values to row locations, maintained on write. "
        "<b>B-tree</b> for range and equality, compact and log-structured. <b>Hash</b> for equality "
        "only, constant time but no ordering. The planner picks based on the query.",
        "q::what", "cs::databases")

card_to(F, "What is write-ahead logging, and why is it correct?",
        "Log the changes <b>before</b> they are applied to the data pages, so after a crash you replay "
        "the log to reach a consistent state. It is correct because the log is ordered, and because "
        "replaying a prefix of committed operations cannot lose a committed transaction.",
        "q::how", "cs::databases")

# ============================================================ Security
F = "CS::Security"

card_to(F, "What is the difference between symmetric and public-key cryptography?",
        "Symmetric uses one shared secret for both directions and is fast, but key distribution is "
        "the hard part. Public-key uses a mathematically linked pair: a private key you keep and a "
        "public key you publish, so no shared secret has to be delivered. In practice TLS and SSH use "
        "both: public-key to establish a secret, symmetric for the data.",
        "q::what", "cs::security")

card_to(F, "What properties does a hash need for cryptographic use?",
        r"Preimage resistance, second-preimage resistance, and <b>collision resistance</b>. MD5 was "
        r"collision-broken in 2004 and SHA-1 in 2017 (SHAttered), so both are unusable for signatures "
        r"and certificates. SHA-256 and SHA-3 are <b>not</b> collision-broken. A plain hash is also "
        r"not a password store: that needs a slow KDF plus a per-user salt.",
        "q::pitfall", "cs::security")

card_to(F, "Why salt a password, and what does it protect against?",
        r"A per-user random salt makes identical passwords hash differently, so one rainbow table "
        r"cannot attack the whole database, and it stops a precomputation working across accounts. "
        r"With a slow KDF such as Argon2 or scrypt plus a salt, a stolen database is not trivially "
        r"crackable offline.",
        "q::why", "cs::security")

card_to(F, "What is the TLS handshake protecting, and in what order?",
        r"1. Client hello with a cipher suite list and a random nonce.<br>"
        r"2. Server hello, certificate, and its own nonce.<br>"
        r"3. Client verifies the certificate chain against a trusted root and the hostname, then "
        r"derives the symmetric session keys.<br>"
        r"The certificate is the only thing authenticating the server; the nonces are what prevent "
        r"replay.",
        "q::how", "cs::security")

card_to(F, "What is SQL injection, and what prevents it?",
        "Building a query by concatenating user input lets an attacker insert SQL syntax, so "
        r"\\(1=1\\) or a trailing drop can change the query's meaning. The fix is <b>parameterised "
        r"queries</b>, where input is bound as data and never parsed as code. Escaping is fragile; "
        r"binding is not. Object-relational mappers usually parameterise, which is another reason to use them.",
        "q::what", "cs::security")

card_to(F, "What is a buffer overflow, and why is it still common?",
        "Writing past the end of a buffer into adjacent memory, which can corrupt a pointer or a return "
        "address. It persists because C and C++ do not check bounds, and copy functions trust caller "
        "lengths. Mitigations: ASLR, stack canaries, and non-executable stacks, which raise the bar "
        "rather than removing the bug.",
        "q::what", "cs::security")

card_to(F, "What is a race condition-to-privilege escalation in setuid programs?",
        "Setuid binaries run with the file owner's privileges, so if such a program operates on a file "
        "in a world-writable directory, an attacker can swap the file between the permission check and "
        "the use (a TOCTOU bug) and get the privileged code to act on their file. The lesson is that "
        "privileged code must do its checks atomically.",
        "q::what", "cs::security")

# ============================================================ ML
F = "CS::ML"

card_to(F, "What is overfitting, and how do you detect it?",
        "Fitting the noise in the training set, so training error falls while held-out error rises. "
        "It is detected by the gap between training and validation curves, and reduced with more data, "
        "regularisation, or simpler models. Testing on data used for tuning is not a held-out estimate.",
        "q::what", "cs::ml")

card_to(F, "Why is a single train/test split often misleading?",
        "One split is one sample, and a lucky split can differ a lot. Use k-fold cross-validation and "
        "report the spread across folds, not just the mean. Keep a final test set that is touched once, "
        "or the reported number is optimistically biased by model selection.",
        "q::how", "cs::ml")

card_to(F, "What is the bias-variance tradeoff?",
        "Underfitting is high bias: the model is too simple to capture the pattern. Overfitting is high "
        "variance: it captures noise. Total error is bias squared plus variance plus irreducible noise, "
        "so the goal is a model complex enough for the signal but not for the noise; validation error "
        "is what tells you where you are.",
        "q::what", "cs::ml")

card_to(F, "What is gradient descent, and what are its two failure modes?",
        r"\\[ \\theta \\leftarrow \\theta - \\eta\\,\\nabla_\\theta L(\\theta) \\]"
        "<br>Fails with too large a step (oscillation or divergence) and too small a step (too slow, "
        "and it can stall in a narrow valley rather than a minimum). Adaptive methods such as Adam and "
        "RMSProp scale the step per parameter, and momentum and second-order methods handle the valleys.",
        "q::how", "cs::ml")

card_to(F, "What does the chain rule give for backpropagation?",
        "Compute gradients by walking the computational graph backwards, reusing the local derivatives "
        "already computed in the forward pass, so each parameter gradient costs one pass. It is exact, "
        "not an approximation, and O(params) instead of the exponential cost of symbolic differentiation.",
        "q::how", "cs::ml")

card_to(F, "What are the layers of a feedforward network for, and what is its universal approximation limit?",
        "Layers of affine maps plus a nonlinearity compose nonlinear functions, and a single sufficiently "
        "wide hidden layer can approximate any continuous function on a compact domain. In practice "
        "depth matters more than width, and this theorem says nothing about how many samples you need "
        "or how hard optimisation is, which is why it overstates the practical result.",
        "q::pitfall", "cs::ml")

card_to(F, "What is the difference between regularisation methods?",
        r"L1 (lasso) penalises \\(\\|\\theta\\|_1\\) and can zero coefficients, giving feature selection. "
        r"L2 (ridge) penalises \\(\\|\\theta\\|_2^2\\) and shrinks, staying dense. Both are convex, which "
        r"is a real advantage. Dropout and early stopping are different in kind: they perturb training "
        r"rather than constrain the objective.",
        "q::what", "cs::ml")


def main() -> None:
    write_json("cards_computing", DECKS)


if __name__ == "__main__":
    main()
