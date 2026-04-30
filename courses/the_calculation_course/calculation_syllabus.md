# Calculation Course — A 10-Week Syllabus for Mathematical Economics & Planning

*Central source document. Everything you need to execute the plan is linked from here.*

---

## How to use this document

This is a 10-week mathematical-economics bootcamp designed to get you from multivariable calculus to the point where you can read Michio Morishima's *Marx's Economics: A Dual Theory of Value and Growth* (1973) and Cockshott/Cottrell's planning literature with full mathematical comprehension. Each week has the same structure:

1. **One-sentence framing** — why this week exists in the arc
2. **Learning objectives** — what you can do by Sunday night
3. **Core concepts** — the actual math, stated precisely
4. **Resource schedule** — a day-by-day pacing with linked videos and readings
5. **Mini project** — a concrete Python deliverable that locks the concepts in
6. **Self-check** — questions you should be able to answer without notes
7. **Bridge** — how this week feeds into the next

Budget **10–15 hours per week**. Videos alone take 3–5 hours; the project and self-check take another 5–8. If you have a heavier week at work, skip the extra-depth material at the bottom of each week, never the core.

The end-state after Week 10: you crack open Morishima's Chapter 1 and think "I know exactly what this matrix is doing." We end with a post-course reading ladder that walks you into Morishima and the planning literature.

---

## Master resource list (linked once here, referenced by shorthand throughout)

### Primary video courses

- **MIT 18.02SC Multivariable Calculus** (Auroux, Fall 2010 — Scholar edition, designed for independent learners): <https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/>
- **MIT 18.06 Linear Algebra** (Gilbert Strang, Spring 2005, the canonical version): course page <https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2005/> · YouTube playlist <https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8>
- **MIT 18.03SC Differential Equations** (Mattuck/Miller, Fall 2011 — Scholar edition): <https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/>
- **3Blue1Brown — Essence of Calculus** (13 videos, ~3h total, visual intuition): <https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr>
- **3Blue1Brown — Essence of Linear Algebra** (15 videos, ~3h total): <https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab>

### QuantEcon lectures (the computational-economics backbone)

- **Linear Programming** (intro): <https://intro.quantecon.org/lp_intro.html>
- **Input-Output Models**: <https://intro.quantecon.org/input_output.html>
- **The Solow-Swan Growth Model**: <https://intro.quantecon.org/solow.html>
- **Dynamics in One Dimension** (useful for Week 10 stability intuition): <https://intro.quantecon.org/scalar_dynam.html>
- Full undergraduate series landing page: <https://intro.quantecon.org/intro.html>

### Planning-economics primary texts (free, legal PDFs)

- **Cockshott & Cottrell, *Towards a New Socialism*** (1993, 2000 edition — author-hosted PDF): <https://users.wfu.edu/cottrell/socialism_book/new_socialism.pdf>
- **"Mathematics to Plan an Economy"** (cibcom.org, Cockshott-tradition introduction to cyber-socialist calculation): <https://cibcom.org/wp-content/uploads/2022/06/Mathematics_to_plan_an_economy_.pdf>
- **Cockshott, "Returning to Kantorovich"** (a full LP planning tutorial with lp_solve code): <https://paulcockshott.wordpress.com/returning-to-kantorovich/>
- **Morishima, *Marx's Economics: A Dual Theory of Value and Growth*** (1973 — Internet Archive scan): <http://digamo.free.fr/morishimarx.pdf> · Archive.org mirror: <https://archive.org/details/marxseconomicsdu0000mori>

### Books worth buying if you want the full-depth version

- **Alpha C. Chiang & Kevin Wainwright, *Fundamental Methods of Mathematical Economics* (4th ed., McGraw-Hill 2005)** — the canonical math-econ textbook. This is the book graduate programs use for their "math camp" before first-year theory sequences. Written in a patient, economist-motivated style: each technique is introduced, worked through, then immediately shown doing economic work. It's the natural companion across Weeks 2–9, but especially Weeks 5–6 (Ch 9, 11, 12, 13 on unconstrained, multi-variable, equality-constrained, and Kuhn-Tucker optimization) and Week 9 (Ch 15–17 on differential equations). Worth owning; used copies of the 4th edition are cheap.
- **Gilbert Strang, *Introduction to Linear Algebra* (6th ed.)** — the 18.06 companion. Strang's prose is as good as the lectures.
- **Morishima, *Theory of Economic Growth* (1969)** and **Morishima, *Equilibrium, Stability and Growth* (1964)** — the other two volumes of the "Morishima trilogy". The 1973 *Marx's Economics* is written assuming you've read these; you haven't, but you'll get most of it anyway.
- **Barro & Sala-i-Martin, *Economic Growth* (2nd ed., MIT Press)** — the standard graduate growth-theory reference. Read selectively for Week 10.

### Extra tools

- **IBM CPLEX LP Tutorial** (good, hands-on LP walk-through): <https://ibmdecisionoptimization.github.io/tutorials/html/Linear_Programming.html>
- **Brad DeLong's Solow notebook** (a Jupyter version of the QuantEcon Solow model): <https://nbviewer.jupyter.org/github/braddelong/LS2019/blob/master/2019-08-08-Sargent-Stachurski.ipynb>
- **Paul Cockshott's YouTube lectures** (Marx, materialism, mathematics and computing): search the channel for "Cockshott Lecture 1" — a full Fall 2021 course you can sample.

### Python environment (do this once, before Week 1)

```bash
python -m venv morishima-env
source morishima-env/bin/activate
pip install numpy scipy sympy matplotlib jupyter pulp cvxpy networkx pandas
pip install quantecon quantecon_book_networks
```

You own a MacBook Pro M1 Max with 32GB RAM — more than enough. Use VS Code with the Jupyter and Python extensions, or plain JupyterLab, whichever you already prefer.

---

## Week 1 — Multivariable Calculus

**Framing.** Before you can formalize a consumer choosing a bundle or a planner choosing an output vector, you need to be fluent in functions of several variables: surfaces, level sets, gradients, and chain rules.

**Learning objectives.** By Sunday, you can: take partial and directional derivatives by hand and symbolically; read and draw contour maps of a 2-variable function; compute and interpret a gradient geometrically as "the direction of steepest ascent, perpendicular to the level set"; write out and use the multivariable chain rule; assemble a Hessian and know what it represents.

**Core concepts.** Functions f: ℝⁿ → ℝ and their graphs as surfaces. Level sets {x : f(x) = c} and contour plots. Partial derivatives ∂f/∂xᵢ, the gradient vector ∇f, and directional derivatives Dᵥf = ∇f · v̂. The tangent plane and linearization f(x) ≈ f(x₀) + ∇f(x₀)·(x - x₀). The multivariable chain rule in matrix form: if x = x(t), then df/dt = ∇f · x'(t). The Hessian matrix of second partials.

**Resource schedule (roughly 6 study days).**

- Day 1–2: 3Blue1Brown *Essence of Calculus* Chapters 1–7 (refresher on the single-variable story — derivatives, chain rule, integration). This is fast and visual; treat it as priming.
- Day 3–4: MIT 18.02SC, Unit 2 — "Partial Derivatives" sessions. Work the session videos plus at least two recitation problems each on partials, gradients, and directional derivatives.
- Day 5: MIT 18.02SC sessions on tangent planes and linearization + the Chain Rule session.
- Day 6: The Hessian. No single great video here; read Evan Chen's Fall 2024 MIT notes on second-derivative tests: <https://ocw.mit.edu/courses/res-18-016-multivariable-calculus-recitation-notes-fall-2024/>

**Mini project — Utility surface and contour map.** Pick a Cobb-Douglas utility function u(x, y) = x^α · y^(1-α) with α = 0.4. Using matplotlib, produce three linked plots: (1) a 3D surface plot of u over [0, 10] × [0, 10]; (2) a contour plot at the same domain with 10 level curves; (3) the contour plot overlaid with gradient vectors on a grid, computed from the analytic formula ∇u = (α·y/x · u, (1-α)·x/y · u) — equivalently just (∂u/∂x, ∂u/∂y). Visually verify: gradients are perpendicular to level curves. Then change α to 0.5 and to 0.2 and commit in-line notes on how the contour shape changes. This is the same object that becomes an "indifference curve" in Week 2.

**Self-check.** State the definition of ∇f in one sentence, then draw why ∇f ⊥ level set. Take f(x, y) = x² + 3xy — compute the Hessian. If g(x, y, z) = ln(x) + ln(y) + ln(z) and (x, y, z) = (t, t², t³), compute dg/dt two ways (direct substitution and chain rule) and check they agree.

**Bridge.** Everything here stays with you. In Week 2 the level set becomes a budget constraint, and the gradient's relationship to it becomes the first-order condition of constrained optimization.

---

## Week 2 — Constrained Optimization

**Framing.** Economics is almost never unconstrained. The method of Lagrange multipliers is the workhorse: it's how you get from "maximize utility" to "marginal rate of substitution equals price ratio" — and the multiplier itself turns out to be a shadow price, the economic meaning that makes the whole machinery sing.

**Learning objectives.** You can set up and solve a constrained max/min problem with one equality constraint by Lagrange multipliers; state and apply the bordered-Hessian second-order condition for whether a critical point is a local max, min, or saddle; interpret the multiplier λ as the sensitivity of the optimum value to a relaxation of the constraint (i.e., a shadow price); do basic comparative statics via the implicit function theorem.

**Core concepts.** The Lagrangian L(x, y, λ) = f(x, y) - λ·(g(x, y) - c). First-order conditions ∇f = λ·∇g — geometrically, "at the optimum, the level set of the objective is tangent to the constraint." Interpretation of λ: d(max value)/dc = λ. Second-order conditions and the bordered Hessian. Extension to multiple constraints. Implicit function theorem for comparative statics: if F(x, p) = 0 pins down x as a function of p, then dx/dp = -(∂F/∂x)⁻¹ (∂F/∂p). Envelope theorem as a cleaner statement of the same thing.

**Resource schedule.**

- **Companion reading: Chiang Ch 12 ("Optimization with Equality Constraints").** If you have the book, read this alongside the MIT videos. Chiang's treatment of the bordered Hessian and the envelope theorem is clearer than most, and his worked examples (utility maximization with Cobb-Douglas, cost minimization, output maximization subject to a cost constraint) are exactly the problems you'll meet in the mini project.
- Day 1–2: MIT 18.02SC Unit 2, Part C sessions on Lagrange multipliers. Work the session problems and recitation videos. The Auroux lecture on Lagrange is especially clean.
- Day 3: Khan Academy multivariable calculus section on constrained optimization (supplementary, visual). Search "Khan Academy Lagrange multipliers" on YouTube; the playlist is by Grant Sanderson (same person as 3B1B).
- Day 4: The shadow-price interpretation. Read Simon & Blume (if you can get a copy) Chapter 19 — the envelope theorem section. If not, read Preston McAfee's free *Introduction to Economic Analysis* <http://www.mcafee.cc/Introecon/> on consumer choice; it does this exposition in clean, applied language.
- Day 5: Implicit function theorem. MIT 18.02SC "Non-independent variables" session + Mattuck's supplementary note *N* on the 18.02 Fall 2007 page: <https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/pages/readings/supp_notes/>
- Day 6: Project work.

**Mini project — Constrained utility max in SymPy.** Using the same Cobb-Douglas u(x, y) = x^0.4 · y^0.6 from Week 1, set up the consumer problem max u subject to p₁·x + p₂·y = M, with p₁ = 2, p₂ = 3, M = 100. Solve it symbolically with SymPy: define variables, the Lagrangian, and use `sp.solve` on the three FOCs. Print out x*, y*, λ*, and the value u*. Then reproduce the *graphical* story: plot the budget line, three or four indifference curves, and the optimum point where the highest feasible indifference curve is tangent to the budget line. Finally, do an envelope-theorem check: re-solve with M = 101 and verify numerically that (new u*) − (old u*) ≈ λ*.

**Self-check.** Why is λ called a "shadow price"? State the envelope theorem in words. At a Cobb-Douglas optimum, what is the relationship between the share parameter α and the fraction of income spent on good x? (Answer: α itself — derive it.) Geometrically, what is the bordered Hessian doing?

**Bridge.** You've now used linear algebra informally — gradients, Jacobians. Week 3 steps back and builds the linear-algebraic apparatus properly, so that by Week 4 eigenvalues let you analyze large-scale economic systems.

---

## Week 3 — Linear Algebra Basics

**Framing.** The economics from Week 7 onward is fundamentally matrix economics: every sector is a row, every good is a column, and the relationships are linear. This week you make sure you can read a matrix as a transformation and not just a grid of numbers.

**Learning objectives.** Fluent matrix-vector and matrix-matrix multiplication, including the "row picture" and "column picture" interpretations. Solve Ax = b by row reduction by hand on small cases. Compute rank and determinant of small matrices. Know when an inverse exists and what "linear independence" means geometrically. Read Ax = b as "find the combination of columns of A that equals b."

**Core concepts.** Vectors in ℝⁿ as points and as arrows. Linear combinations, span, linear independence, basis. Matrix multiplication as composition of linear transformations. Row reduction / Gaussian elimination to RREF. Rank, column space, null space. Inverse matrices and when they exist (square + full rank). Determinant as "signed volume scaling factor of the transformation." Transpose and its geometric meaning (subtly: not "the inverse in disguise").

**Resource schedule.**

- Day 1: 3Blue1Brown *Essence of Linear Algebra* Chapters 1–4 (vectors, linear combinations, span, linear transformations, matrix multiplication). Watch these before everything else — the mental model you gain here compounds.
- Day 2: Strang MIT 18.06 Lectures 1–3 (geometry of linear equations, elimination, multiplication and inverses). Strang's "row picture vs column picture" framing is the clearest in mathematics.
- Day 3: 3Blue1Brown Chapters 5–8 (three-dimensional transforms, determinant, inverse, nonsquare matrices, dot products).
- Day 4: Strang Lecture 4–5 (A = LU factorization, transposes, permutations) — watch lightly, you'll revisit if needed.
- Day 5–6: Strang Lectures 9–10 on independence, basis, dimension; Lecture 6–7 on column space and null space. This is where abstract and concrete fuse. Work at least five exercises by hand from Strang's textbook Ch. 3 (a PDF copy is in most university libraries; the official book link is <https://math.mit.edu/linearalgebra/>).

**Mini project — Solve a 3-sector mini-IO system in NumPy.** Build a 3×3 technical-coefficients matrix A (rows = sectors, columns = sectors) where A[i,j] = the amount of sector-i output needed to produce one unit of sector-j output. Make up plausible numbers, e.g. A = [[0.1, 0.2, 0.1], [0.3, 0.1, 0.2], [0.1, 0.3, 0.1]]. Pick a final-demand vector d = [100, 50, 80]. Compute x that solves (I − A)·x = d using three different methods — `np.linalg.solve`, explicit `np.linalg.inv(I − A) @ d`, and by implementing row reduction yourself using elementary row ops on the augmented matrix [I − A | d]. Verify they all agree. This is the baby version of the Leontief inverse you'll meet properly in Week 7.

**Self-check.** What is the rank of a 3×5 matrix with three linearly independent columns? What does it mean geometrically that det(A) = 0? If Ax = b has no solution, what does that say about b relative to the column space of A? Why is `np.linalg.solve(A, b)` preferred over `np.linalg.inv(A) @ b` numerically?

**Bridge.** Week 4 takes the matrix as transformation and asks: what are the special vectors that it just *scales* rather than rotates? Those are eigenvectors, and the scaling factors are eigenvalues — and they turn out to be the key to stability analysis, growth rates, and the Perron-Frobenius theorem that sits at the heart of Leontief economics.

---

## Week 4 — Eigenvalues and Systems

**Framing.** Eigenvalues are how we detect whether a dynamical system converges or blows up, and how we identify the "natural directions" of a linear process. In economics, the largest (Perron-Frobenius) eigenvalue of a nonnegative matrix is the maximal balanced growth rate, and the condition for a Leontief economy to be viable is that this eigenvalue be less than one.

**Learning objectives.** Compute eigenvalues and eigenvectors of 2×2 and 3×3 matrices by hand via det(A − λI) = 0, and in NumPy for larger. Diagonalize a matrix when possible. State the Perron-Frobenius theorem for nonnegative matrices. Understand how eigenvalues of the Jacobian determine local stability of a fixed point — this is foreshadowing Week 10.

**Core concepts.** The eigenvalue equation Av = λv. Characteristic polynomial det(A − λI) = 0. Eigenspaces. Diagonalization A = PDP⁻¹ when A has n linearly independent eigenvectors. Spectral theorem: symmetric matrices have real eigenvalues and orthogonal eigenvectors. **Perron-Frobenius theorem**: a nonnegative irreducible matrix has a positive real eigenvalue λ_PF that dominates all others in absolute value, with a strictly positive eigenvector. Stability: if all eigenvalues of a discrete-time system A satisfy |λᵢ| < 1, zero is a stable fixed point; for a continuous-time system ẋ = Ax, the condition is Re(λᵢ) < 0.

**Resource schedule.**

- Day 1: 3Blue1Brown *Essence of Linear Algebra* Chapters 13–14 (change of basis, eigenvectors and eigenvalues). Watch twice — the geometric intuition is the whole game.
- Day 2: Strang 18.06 Lectures 21–22 (eigenvalues and diagonalization).
- Day 3: Strang 18.06 Lectures 23–24 (Markov matrices, Fourier series as eigen-decomposition — the Markov piece is directly analogous to stability in economic dynamics).
- Day 4: Perron-Frobenius. Read QuantEcon's lecture on it: <https://intro.quantecon.org/eigen_I.html> and <https://intro.quantecon.org/eigen_II.html> (one of these covers PF in detail).
- Day 5: Connection to dynamics. Read 3B1B's video on matrix exponentials (if available) or its text companion. Preview MIT 18.03SC's session on "Linear Systems of ODEs" — full depth comes in Week 9, but seeing how eigenvalues classify phase portraits now will pay off.
- Day 6: Project.

**Mini project — Eigenstructure of an input-output matrix.** Take the matrix A from Week 3's project. Compute its eigenvalues and eigenvectors with `np.linalg.eig`. Identify the Perron-Frobenius eigenvalue (the largest in absolute value, which for a nonnegative matrix is real and positive). Verify it has a positive eigenvector. Check whether the matrix is "productive": we need the PF eigenvalue to be strictly less than 1 for (I − A)⁻¹ to exist as a nonnegative matrix. Then deliberately construct a *non*-productive A (scale yours up by 2) and watch what goes wrong — (I − A)⁻¹ still exists numerically but contains negative entries, meaning the economy can't meet any positive final demand without producing negative amounts somewhere. Explain this in three sentences in your notebook.

**Self-check.** Why does det(A − λI) = 0 find eigenvalues? For a 2×2 matrix A = [[a, b], [c, d]], what are the eigenvalues in terms of trace and determinant? If A has eigenvalues 0.5, 0.8, 1.2 and you iterate xₜ₊₁ = Axₜ, what happens long-run and why? What's the Perron-Frobenius eigenvalue of the identity matrix? (Hint: any positive vector is an eigenvector with eigenvalue 1 — so I is on the boundary between productive and non-productive.)

**Bridge.** You now have linear algebra and calculus both at a working level. Week 5 combines them into the formal theory of optimization under constraints, which is the precondition for linear programming in Week 6.

---

## Week 5 — Economic Optimization

**Framing.** Where Week 2 dealt with equality constraints and smooth interiors, the economics of planning and trade involves *inequality* constraints ("we have at most X units of steel"), non-negativity ("you can't produce −5 tons of wheat"), and corner solutions. Kuhn-Tucker conditions are Lagrange multipliers generalized to this world — and they're the theoretical bridge to linear programming.

**Learning objectives.** Set up and analyze unconstrained optimization with second-order conditions for multivariable functions. State and apply the Kuhn-Tucker (KKT) conditions for inequality-constrained problems. Understand convexity and why convex problems have unique global optima. Write and solve a consumer or firm problem in Python using scipy.optimize or cvxpy.

**Core concepts.** Unconstrained optimization: ∇f = 0, Hessian negative-definite for maximum. Convex sets and convex functions: epigraph, convex combination. Why convex problems are "easy" — any local optimum is global. The KKT conditions: stationarity of Lagrangian, primal feasibility, dual feasibility (λ ≥ 0 for ≤ constraints), complementary slackness (λᵢ·gᵢ(x) = 0 — either the constraint binds or its multiplier is zero). Constraint qualifications (you can mostly ignore these but should know they exist).

**Resource schedule.**

- **Primary text for this week and next: Chiang & Wainwright Ch 9, 11, 12, 13.** If you own the book, Chapter 9 (unconstrained optimization, one and n variables, second-order conditions), Chapter 11 (multi-variable maxima with economic applications — profit-max, cost-min), Chapter 12 (equality-constrained optimization with a clean treatment of the bordered Hessian that's better than most), and Chapter 13 (the KKT conditions and quasi-concavity) are the most direct path through this material in the whole literature. The examples are all economic — firms, consumers, production functions — which makes the mathematics feel earned rather than imposed. Work at least a dozen exercises across these four chapters; they are where the understanding actually settles.
- Day 1: Convexity. The most accessible resource is Stephen Boyd's Stanford EE364a (Convex Optimization) Lecture 1–2 on YouTube: <https://www.youtube.com/playlist?list=PL3940DD956CDF0622>. Watch at 1.5× and don't try to absorb everything — you're building intuition.
- Day 2: Boyd Lecture 3–4 (convex functions, operations that preserve convexity).
- Day 3: KKT conditions. Boyd Lecture 9–10 covers duality and KKT. Also read Section 5.5 of the Boyd & Vandenberghe textbook, *Convex Optimization*, free PDF: <https://web.stanford.edu/~boyd/cvxbook/>. Then read Chiang Ch 13 alongside — Chiang's exposition of KKT is specifically aimed at economists and will stick better.
- Day 4: Application to consumer theory. Read McAfee's *Introduction to Economic Analysis* Chapter 12 (consumer theory) and Chapter 14 (producer theory), free at <http://www.mcafee.cc/Introecon/>. Watch how corner solutions and non-negativity naturally produce KKT-style conditions.
- Day 5: cvxpy. Do the cvxpy getting-started tutorial: <https://www.cvxpy.org/tutorial/intro/index.html>
- Day 6: Project.

**Mini project — Firm cost-minimization with cvxpy.** A firm produces a good with the Cobb-Douglas technology y = L^0.5 · K^0.5. Wage is w = 20, rental rate is r = 10. The firm wants to produce y = 100 at minimum cost, with L, K ≥ 0. Solve this three ways: (1) analytically using Lagrange — derive the cost function C(y, w, r); (2) numerically with cvxpy, reading off the optimal L, K; (3) verify Shephard's lemma — that ∂C/∂w = L* at the optimum. Then add a second constraint: L ≤ 40 (union-imposed labor cap). Re-solve with cvxpy. Report which constraints bind, what the dual variables are, and interpret.

**Self-check.** What is the economic content of complementary slackness? Why is the sum of two convex functions convex, but not necessarily the product? State Jensen's inequality in your own words. When does the Lagrange method from Week 2 give you the KKT-correct answer without explicitly writing out the inequality constraints?

**Bridge.** When the objective and all constraints are linear, the KKT framework specializes to the beautifully clean world of linear programming — with its own celebrated duality theorem, which turns out to be *exactly* the price-system duality of economic theory. That's Week 6.

---

## Week 6 — Linear Programming and Duality

**Framing.** In 1939, Leonid Kantorovich — working on plywood-cutting optimization for a Soviet industry ministry — invented linear programming, and won the only Nobel Prize in economics ever given to a Soviet citizen. Every LP has a *dual* problem, and the duality theorem is the mathematical foundation of planning prices. This week you learn to use an LP solver, read the shadow-price output, and understand why Kantorovich's machinery is a direct answer to the Mises-Hayek calculation argument.

**Learning objectives.** Set up an LP in standard form. Solve LPs in Python using scipy's `linprog`, PuLP, or cvxpy. State and interpret the LP duality theorem. Read dual variables (shadow prices) off a solver output and explain what they mean in the original problem. Work the Kantorovich plywood example.

**Core concepts.** Standard form: min cᵀx s.t. Ax = b, x ≥ 0 (with inequality forms as variants). Feasible region = polytope = intersection of half-spaces. The simplex method traverses vertices. Every LP has a dual: max bᵀy s.t. Aᵀy ≤ c. **Weak duality** (primal objective ≥ dual objective always) and **strong duality** (when solutions exist, the two objectives are equal). Shadow prices = optimal dual variables = ∂(optimal value)/∂(constraint RHS). Complementary slackness in LP form.

**Resource schedule.**

- **Anchor reading: Chiang Ch 13 (sections on Kuhn-Tucker and quasi-concave programming) continues from Week 5 directly into LP territory.** If you worked through it last week, the transition is seamless — LP is the specialization of KKT where objective and constraints are all linear, and Chiang's exposition of how shadow prices emerge from the Lagrangian makes the economic interpretation of LP duals click without further explanation.
- Day 1: QuantEcon's LP introduction lecture (read + run the code): <https://intro.quantecon.org/lp_intro.html>. Work both of the example problems (production, investment).
- Day 2: IBM CPLEX Part 1 LP tutorial <https://ibmdecisionoptimization.github.io/tutorials/html/Linear_Programming.html>. Skip the CPLEX-specific syntax; read for the concepts: feasible region, extreme points, slack, degeneracy.
- Day 3: Duality. Watch Jim Dai or Ashwin Pananjady's LP duality lectures on YouTube (search "LP duality lecture"), or read Chapter 3 of Chvátal's *Linear Programming* if you have access. The clearest short treatment is in the QuantEcon "Optimal Transport" lecture: <https://python.quantecon.org/opt_transport.html> — pay attention to how the dual variables are interpreted as "ship-out values" and "ship-in values".
- Day 4: Read Cockshott's blog post *Returning to Kantorovich*: <https://paulcockshott.wordpress.com/returning-to-kantorovich/>. This works the original plywood example and then extends it to an economy-wide plan. This single post is the most important primary reading of Week 6.
- Day 5–6: Project.

**Mini project — Production LP with shadow-price analysis.** A factory produces two products, P1 and P2. P1 needs 2 units of material and 4 units of labor per unit; P2 needs 5 units of material and 2 units of labor. Revenues are \$3/unit (P1) and \$4/unit (P2). Material available: 30 units. Labor available: 20 units. Both products must be non-negative. (This is QuantEcon's first example.) Step 1: solve with PuLP *and* with scipy's `linprog`, compare. Step 2: print the optimal dual variables — read off the shadow prices of material and labor. Step 3: verify the shadow price story empirically — add 1 to the material constraint (31 units), re-solve, and check that the objective increases by approximately the material shadow price. Step 4: write 150 words in the notebook connecting what you just computed to the *planning* interpretation: these shadow prices are the "scarcity prices" that a planner in the Kantorovich tradition would use to coordinate decisions across the economy even without a market.

**Self-check.** If a constraint is non-binding at the optimum, what is its shadow price? Why? State the duality theorem in one sentence. Why can the simplex method be slow in the worst case but usually fast in practice? What is the dual of the dual?

**Bridge.** Week 7 applies exactly this LP machinery to an entire economy described as a matrix of input-output coefficients. That's Leontief's contribution — and it's the technical core of what Morishima and Cockshott both build on.

---

## Week 7 — Input-Output Analysis

**Framing.** Wassily Leontief won the 1973 Nobel Prize for showing how an economy's inter-industry structure can be represented as a single matrix A, where Aᵢⱼ is the amount of good i needed to produce one unit of good j. Every result in the first half of Morishima's *Marx's Economics* is a statement about the algebra of this matrix. If you understand (I − A)⁻¹, you understand the backbone of mathematical Marxian and planning economics.

**Learning objectives.** State the Leontief model. Compute the Leontief inverse L = (I − A)⁻¹ and interpret its entries (Lᵢⱼ = total — direct plus indirect — units of good i needed for one unit of *final demand* for good j). State the Hawkins-Simon productivity condition. Set up the dual price system pᵀ = pᵀA + vᵀ (where v is value added per unit, e.g. labor) and derive labor values. Simulate and interpret a demand shock.

**Core concepts.** The matrix A of technical coefficients. Gross output x, final demand d, intermediate consumption Ax. The fundamental identity: x = Ax + d, hence x = (I − A)⁻¹ d = Ld. Neumann series interpretation: L = I + A + A² + A³ + ... (first-round, second-round, ... effects). Hawkins-Simon condition: all leading principal minors of (I − A) are positive — equivalently, Perron-Frobenius eigenvalue of A is less than 1. Price-value duality: p = pA + v (row vector equation) gives p = v(I − A)⁻¹ — which, when v is a vector of unit labor requirements, gives a vector of *labor values* in the Marxian sense. Output multipliers as column sums of L.

**Resource schedule.**

- Day 1–2: QuantEcon's *Input-Output Models* lecture, all the way through: <https://intro.quantecon.org/input_output.html>. Run all the code. This lecture uses real US BEA data and builds up the full machinery.
- Day 3: Wikipedia's input-output model article, focus on the mathematical formulation and the extensions (dynamic IO, regional IO): <https://en.wikipedia.org/wiki/Input%E2%80%93output_model>
- Day 4: Morishima, *Marx's Economics*, Chapter 1 "Dual definition of value" and Chapter 3 "Quantitative determination of relative value". PDF: <http://digamo.free.fr/morishimarx.pdf>. You're going to read this slowly and with a notebook open. Morishima introduces value as a solution to a simultaneous linear system, which is exactly the dual price system you set up computationally.
- Day 5: Morishima Chapter 5 "Surplus value and exploitation" — the Fundamental Marxian Theorem (rate of exploitation > 0 iff rate of profit > 0) is stated in matrix form and proven in pages you can now follow. *Optional companion for critical reading*: alongside Morishima's Chapter 1 and 3, read Zhang's "Notes on Michio Morishima's Understanding of Marxian Economics" (*World Review of Political Economy* 10(3), 2019), open-access at <https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.10.3.0280>. Zhang — a Chinese Marxist economist at Sichuan University — gives Morishima real credit for the mathematization but argues that the core formalization choices (value-as-aggregation-tool, the wage-numeraire in price equations) inherit Smithian rather than Marxian value theory. You'll get the full weight of this argument in a short seminar between Controversies 5 and 6, but reading Zhang alongside Morishima now means the critical frame is in your head while you're doing the absorption.
- Day 6: Project.

**Mini project — Two-sector IO model and demand shock.** Build a 2-sector economy (say, "food" and "machines") with technical matrix A = [[0.2, 0.3], [0.4, 0.1]] and direct labor coefficients v = [0.5, 0.6] (hours per unit of output). Final demand d = [100, 50]. Compute: (1) required gross outputs x; (2) Leontief inverse L; (3) total labor embodied in each unit of final demand — equivalently, the labor values of the two goods, p = v(I − A)⁻¹; (4) total labor used in the economy, vᵀ x. Now impose a demand shock: a 20% increase in food demand (d_food: 100 → 120). Compute the new x, the *change* in x for each sector, and decompose it into direct effects (A applied once) versus indirect effects (higher-order). Make a bar chart.

**Self-check.** Why does the Leontief inverse capture both direct and indirect requirements? What's the economic meaning of the row sums versus column sums of L? In what sense is the labor-value vector p the "dual" of the output vector x? If A had a Perron-Frobenius eigenvalue greater than 1, what would (I − A)⁻¹ look like, and what would that mean for the economy?

**Bridge.** You've now done input-output analysis as an accounting exercise. Week 8 turns it into a *planning* exercise: given resources and a set of final-demand targets, find a feasible plan — and if multiple plans are feasible, find the best one using LP.

---

## Week 8 — Planning and Allocation

**Framing.** This is the keystone week. You combine LP (Week 6) with input-output analysis (Week 7) to formulate the full economic planning problem that Kantorovich and then Cockshott/Cottrell have worked on. Everything you've done feeds in here.

**Learning objectives.** Set up a multi-sector planning problem: given technology A, labor coefficients v, labor endowment L̄, and a desired composition of final demand, find the plan that maximizes scale (or utility of a final-demand bundle) subject to resource constraints. Compute planning prices as LP dual variables. Contrast quantity-targeting with price-targeting. Understand the Cockshott-Cottrell "labour-time" proposal and its difference from conventional shadow-price approaches. Understand why planning is computationally tractable at realistic scale.

**Core concepts.** The planning LP: max α s.t. (I − A)x ≥ α·d*, v·x ≤ L̄, x ≥ 0 (where d* is a desired basket and α is the scale). Dual variables — planning prices — are labor values when the constraint is labor. Von Neumann balanced growth: the maximal λ such that the economy can produce (λ · consumption-bundle) next period from this period's output. Marginal-substitution-free planning "in natura" (Cockshott). Iterative plan-adjustment algorithms. The calculation debate — why 20th-century arguments against planning (Mises, Hayek) are computational claims that modern hardware and algorithms refute.

**Resource schedule.**

- Day 1: Read *Mathematics to Plan an Economy* (cibcom.org PDF): <https://cibcom.org/wp-content/uploads/2022/06/Mathematics_to_plan_an_economy_.pdf>. This is a tight, mathematically explicit introduction to what we're about to build.
- Day 2: Cockshott & Cottrell, *Towards a New Socialism*, Chapter 3 (*Information and Economics*) and Chapter 9 (*Planning*). Free PDF: <https://users.wfu.edu/cottrell/socialism_book/new_socialism.pdf>. Read for the architecture of the proposal, not the polemics. Note in particular the argument about computational complexity being ~ N log N.
- Day 3: Re-read Cockshott's *Returning to Kantorovich* blog post — now the LP details are inside you. Run his three-sector example (energy, food, machines with labor, wind, river, fertile and highland land) in PuLP or cvxpy.
- Day 4: Paul Cockshott's YouTube lecture series *Marx, Materialism, Mathematics, and Computing* — Lectures 1 and 5 are especially relevant. Lecture 1: <https://www.youtube.com/watch?v=-u1IbJPdL0c>. Lecture 5: <https://www.youtube.com/watch?v=FcZGvmjI9Vw>.
- Day 5: Briefly read QuantEcon's *Von Neumann Growth Model* lecture: <https://python.quantecon.org/von_neumann_model.html>. This is the most general LP formulation of a growing economy and shadows Morishima's later chapters.
- Day 6: Project.

**Mini project — Three-sector planning model.** Build a three-sector economy (agriculture, industry, services) with a technical matrix A of your choosing (plausible positive entries, Perron-Frobenius eigenvalue < 1), labor coefficients v, and a total labor endowment of, say, 1000 hours. Specify a target final-demand composition d* = [0.5, 0.3, 0.2] (shares). Using cvxpy, solve the planning LP: maximize α subject to (I − A)x ≥ α·d*, v·x ≤ 1000, x ≥ 0. Report x*, α* (the scale of the standard basket you can deliver), and the dual variables on the labor constraint (= labor value in hours of one "unit of the standard basket"). Then do three things: (1) halve the technical coefficient A[1,2] (industry becomes 50% less agriculture-intensive) and re-solve; report how α* and the plan change. (2) Add a second resource constraint (say energy): w·x ≤ 500. Re-solve. (3) Change d* to favor services more heavily and comment on what happens.

**Self-check.** Why is this LP the computational equivalent of a market? What does the dual variable on the labor constraint represent, and why does it deserve the name "labor value"? What does the dual variable on a specific output constraint ((I − A)x ≥ αd*) represent? Cockshott argues the computational complexity of national planning is ~ N log N — where does this come from, and do you believe it?

**Bridge.** Everything so far has been static — a snapshot. Week 9 introduces dynamics via differential equations, so that by Week 10 you can talk about growth, stability, and how economies *change over time* — the core questions of Morishima's later work.

---

## Week 9 — Differential Equations

**Framing.** The economy moves. Capital accumulates, population grows, technology advances. The mathematics of continuous-time change is differential equations, and the specific tools you need for economics are: first-order linear ODEs (Solow model), systems of linear ODEs (Goodwin model, linearized growth), phase portraits (geometric understanding), and numerical simulation (when the equations aren't solvable by hand).

**Learning objectives.** Solve first-order linear and separable ODEs analytically. Solve 2×2 linear systems of ODEs by finding eigenvalues and eigenvectors of the system matrix. Classify equilibria of 2D systems (node, saddle, spiral, center) by the trace-determinant criterion. Simulate ODEs numerically with Euler's method and with `scipy.integrate.solve_ivp`. Draw and interpret a phase portrait.

**Core concepts.** First-order linear ODE: dy/dt = ay + f(t). Separable ODEs. Systems: ẋ = Ax. Solution via eigenvalue decomposition: if A = PDP⁻¹ then x(t) = P·e^(Dt)·P⁻¹·x(0). Phase plane: plot trajectories in (x, y) space. Fixed points (equilibria): where ẋ = 0. Linearization around an equilibrium: Jacobian J; local behavior classified by Re(λ(J)). Classification: two negative reals = stable node; one positive one negative = saddle (unstable); complex with negative real parts = stable spiral; etc. Euler method: xₙ₊₁ = xₙ + h·f(xₙ). Its numerical instability for large h.

**Resource schedule.**

- **Companion reading: Chiang Ch 15 ("Continuous Time: First-Order Differential Equations"), Ch 16 ("Higher-Order Differential Equations"), and Ch 17 ("Discrete Time: First-Order Difference Equations").** If you own the book, these three chapters are a clean parallel track to MIT 18.03SC, worked entirely with economic examples (debt dynamics, market-stability models, cobweb theorems). Chiang's treatment of the discrete-time case (Ch 17) is especially good — MIT 18.03 only covers continuous time, and a lot of the economics literature is discrete-time.
- Day 1: MIT 18.03SC Unit 1 — Introduction to ODEs, direction fields, separable and first-order linear equations. <https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/>
- Day 2: MIT 18.03SC Unit 2 — Second-order linear equations (skim) and Unit 3 — Fourier (skip; optional). Main event is next day.
- Day 3–4: MIT 18.03SC Unit 4 — "Linear Systems of First Order ODEs" — the whole unit. Phase portraits, eigenvalue-based classification, the trace-determinant plane. This is the conceptual core of the week.
- Day 5: Numerical simulation. Read the `scipy.integrate.solve_ivp` documentation and work the examples: <https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html>. Do a side-by-side comparison of Euler vs RK4 on a known equation.
- Day 6: Project.

**Mini project — Solow growth dynamics via Euler.** The Solow model in continuous time: dk/dt = s·f(k) − δ·k, with f(k) = A·k^α. Take A = 2, α = 0.3, s = 0.3, δ = 0.1. Find the steady state k* analytically. Then: (1) simulate the ODE using your own hand-coded Euler method with step size h = 0.1, starting from three different initial capital levels k₀ ∈ {0.5, 3, 10}, and plot all three trajectories converging to k* on the same axes. (2) Reduce h to 0.01 and re-run — comment on any differences. (3) Redo with `scipy.integrate.solve_ivp` using RK45 and compare. (4) Plot the "Solow diagram": s·f(k) and δ·k on the same axes, with the intersection at k*. The story is done — you've now written the software version of the foundational growth model in economics.

**Self-check.** For a 2D linear system ẋ = Ax, if trace(A) < 0 and det(A) > 0, what type of equilibrium is the origin? Why does the Solow model have a unique positive steady state when f is strictly concave? Why does Euler become unstable if h is too large, and what heuristic controls the safe step size? What's the relationship between the eigenvalues of the Jacobian and local stability?

**Bridge.** Week 10 closes the loop: you take everything you've built — IO matrices, LP planning, linear algebra, eigenvalues, ODEs — and apply it to the central dynamic questions of economics: when do economies converge to a steady state, when do they grow in balance, and when do they oscillate or crash. You'll end the course ready to read Morishima.

---

## Week 10 — Growth and Stability

**Framing.** This is synthesis week. You'll look at three classes of dynamic economic model — the Solow-Swan neoclassical model, the Goodwin growth-cycle model (inspired by predator-prey dynamics and the class struggle), and the von Neumann balanced growth model — and in each case you'll (a) write down the dynamics, (b) find equilibria, (c) analyze stability via linearization, and (d) simulate. By the end you have the vocabulary and the tools to read Morishima, Barro-Sala-i-Martin, and the modern planning literature with comprehension.

**Learning objectives.** Derive steady states of a growth model. Linearize around a steady state and use the Jacobian's eigenvalues to classify stability. Draw a phase plane for a 2D economic model, including nullclines, fixed points, and sample trajectories. Connect discrete-time stability (|λ| < 1) to continuous-time stability (Re(λ) < 0). Read and interpret the first chapters of Morishima's *Theory of Economic Growth*.

**Core concepts.** Balanced growth path: all variables grow at a constant rate, ratios stay fixed. Local vs global stability. Nullclines: curves where one state variable's time derivative is zero; they divide the phase plane into regions. The Goodwin model: two state variables (employment rate u, wage share v), nonlinear dynamics that produce closed-orbit *cycles* rather than convergence — a mathematical rendering of Marx's reserve-army-of-labor story. Turnpike theorems (mentioned, not mastered): optimal growth paths converge to a "turnpike" even if they deviate near the endpoints. Von Neumann balanced growth: the maximum λ such that λ·(input bundle) ≤ (output bundle) for some non-negative intensity vector — solved as an LP.

**Resource schedule.**

- Day 1: QuantEcon *Solow-Swan Growth Model*: <https://intro.quantecon.org/solow.html>. Work all examples. The stochastic Solow at the end is a nice preview of how noise enters the picture.
- Day 2: QuantEcon *Dynamics in One Dimension*: <https://intro.quantecon.org/scalar_dynam.html> — the 45-degree diagram treatment of the Solow-Swan model. This connects discrete-time dynamics to what you did in Week 9.
- Day 3: The Goodwin model. Read the Wikipedia article *Goodwin model (economics)*: <https://en.wikipedia.org/wiki/Goodwin_model_(economics)>. Supplement with Chapter 13 of Wolfgang Strobl's free *Dynamical Systems in Economics* notes, or with Desai's *Macroeconomics and Monetary Theory* if you have access. Goodwin took the Lotka-Volterra equations from biology and reinterpreted them: "rabbits" = workers (employment rate), "foxes" = capitalists (wage share). High employment → wages rise → profits fall → investment falls → employment falls. Beautiful.
- Day 4: Morishima, *Theory of Economic Growth* (1969), Chapters 1–2 — if you can access it; most university libraries will have it. Alternatively, Barro & Sala-i-Martin Chapter 1 (neoclassical growth), skimming the proofs, paying attention to the saddle-path stability story.
- Day 5–6: Project.

**Mini project — Phase-plane simulator for the Goodwin model.** Implement the Goodwin model: du/dt = (1/σ − ω − δ) − u (simplified; use the standard form from Wikipedia), dv/dt = (ρu − γ)v, where u is employment rate, v is wage share, and the parameters σ, δ, ρ, γ are calibrated (take from the Wikipedia article, or use Desai's values). (1) Find the non-trivial fixed point (u*, v*) analytically. (2) Simulate with `solve_ivp` from several initial conditions and plot trajectories in the (u, v) phase plane — you should see closed orbits around the fixed point (it's a *center*, not a stable spiral — this is the Lotka-Volterra property). (3) Plot the two nullclines (du/dt = 0 and dv/dt = 0) on the same figure, and sample direction-field arrows on a grid. (4) Linearize around (u*, v*) — compute the Jacobian symbolically with SymPy, evaluate at the fixed point, compute eigenvalues. Verify they are pure imaginary, consistent with closed orbits. (5) Write 200 words in the notebook on what the Goodwin model says economically: why does the economy oscillate rather than converge? What's the Marxian interpretation? What happens if you add a small damping term?

**Self-check.** In the Solow model, why is the steady state globally stable? In the Goodwin model, why does the fixed point have pure imaginary eigenvalues — and why is this structurally fragile (any perturbation would turn it into either a stable or unstable spiral)? What's the difference between *balanced growth* and *steady state*? Write the Solow steady-state condition in words, then as an equation, then interpret each term.

**Bridge.** You now have the full toolkit. The next step is not another week of math — it's reading Morishima, and letting the mathematical apparatus you've built get exercised against his arguments about labor values, exploitation, and growth.

---

## Post-course: reading Morishima and beyond

The 10 weeks were designed to get you to the point where you can open *Marx's Economics* and follow it. Here's the recommended reading order after Week 10:

1. **Morishima, *Marx's Economics: A Dual Theory of Value and Growth* (1973).** PDF: <http://digamo.free.fr/morishimarx.pdf>. Read Part I and Part II carefully (you have the tools). Part III (the transformation problem) is historically important but computationally dense; skim on first pass. Part IV (reproduction scheme) rewards careful reading; Part V (capital and value) is the peak.

2. **Cockshott & Cottrell, *Towards a New Socialism* (1993).** You already read Chapters 3 and 9 in Week 8. Now read the whole book. The critique of Soviet planning (Chapter 5), the treatment of labor tokens (Chapter 2), and the political-constitutional argument (Chapters 13–14) were only tangentially mathematical and you'll find you can engage with them at a new level having done the math.

3. **Morishima, *Theory of Economic Growth* (1969).** This is the middle volume of the Morishima trilogy and the systematic treatment of multi-sector growth, including Morishima's extensions of von Neumann. It's the bridge between Marxian and modern growth theory.

4. **Morishima, *Equilibrium, Stability and Growth* (1964).** The mathematical appendix of the trilogy — only dip in if you want to see the proofs.

5. **The Chinese critical canon on the Japanese School of Mathematical Marxian Economics.** Before concluding the Morishima trilogy is the last word, read the three-paper sequence of Xian Zhang's critique and positive program — "Notes on Michio Morishima's Understanding of Marxian Economics" (*WRPE* 10(3), 2019), "A Critical Deconstruction of the Okishio Theorem" with Yufeng Xue (*WRPE* 13(2), 2022), and "The Formalization of Marx's Economics" (*WRPE* 14(1), 2023) — plus Bin Yu's companion "Analysis of the Okishio Theorem" (*WRPE* 13(2), 2022). All open-access on ScienceOpen. You'll have hit some of this in the between-controversies seminar; the full sequence is worth the revisit in light of the trilogy.

6. **Barro & Sala-i-Martin, *Economic Growth* (2nd ed.).** The mainstream graduate growth theory textbook. Read Chapters 1–5 for the neoclassical backbone, Chapter 6 onward for endogenous growth.

7. **Cockshott, *How the World Works* (2019).** A more recent and more accessible Cockshott book — worth reading as a capstone.

8. **Paul Cockshott's YouTube channel** and academic papers — his *Computers and Economic Democracy* papers (co-authored with various Greek and Spanish economists in the 2010s) extend the planning LP machinery in directions your Week 8 project merely glimpsed.

If you find yourself wanting deeper math: **Boyd & Vandenberghe, *Convex Optimization*** (free PDF), and **Bertsimas & Tsitsiklis, *Introduction to Linear Optimization***, are the two standard references. **Acemoglu, *Introduction to Modern Economic Growth*** is the most mathematically rigorous modern growth textbook.

---

# Part II — Economic Controversies

These are post-course seminars. Each is a week-length unit that takes a live methodological debate in economics and runs you through it *using the mathematical apparatus you built in Weeks 1–10*. The pedagogical bet is that reproducing a controversy computationally — deriving the key result on paper, then coding the empirical demonstration yourself — locks in both the debate and the tools at once, in a way that passive reading never will.

Each controversy has the same structure as a regular week: framing, objectives, core concepts, resource schedule, mini project, self-check, bridge. Take one per week at whatever pace makes sense after the core 10-week arc is done.

---

## Controversy 1 — The Cobb-Douglas Critique

**Framing.** You have been happily using the Cobb-Douglas form throughout Weeks 1–9 as a teaching example: smooth, concave, closed-form everything. It turns out that one of the most famous papers in heterodox economics — Anwar Shaikh's 1974 "Humbug Production Function" — is a full-frontal demolition of the Cobb-Douglas production function's claim to be a *law of production*. Shaikh's argument, sitting on top of the older **Cambridge Capital Controversy** (Robinson 1953 → Sraffa 1960 → Samuelson's 1966 concession), was later extended by Jesus Felipe and John McCombie into a systematic attack on the entire aggregate-production-function empirical literature. This week you reproduce the Humbug result in Python, derive the accounting-identity trick on paper, and understand exactly why the Morishima/Cockshott tradition works in the disaggregated input-output framework of Week 7 rather than in aggregate Y = F(K, L) land.

**Learning objectives.** By the end of this week you can: (1) state Shaikh's argument in three sentences without notes; (2) derive the Y = A·Lᵅ·K¹⁻ᵅ "shape" from the accounting identity Y ≡ wL + rK plus constant factor shares, using total differentials from Week 1; (3) reproduce the humbug experiment computationally — generate nonsense data, regress it, and watch a Cobb-Douglas fit come out with high R²; (4) explain the Cambridge circularity argument (capital can't be measured without prices, prices depend on the rate of profit, the rate of profit is what the production function is meant to explain); (5) explain to a non-specialist why Morishima's multi-sector input-output apparatus is not just stylistic preference but a considered response to these critiques.

**Core concepts.** The national-accounts identity Y ≡ wL + rK as pure bookkeeping. Factor shares α ≡ wL/Y, 1−α ≡ rK/Y and the empirical regularity of their approximate constancy over long periods (this is the load-bearing assumption). Total differentiation of the identity and the algebraic maneuver that turns it into a growth-rate form. Solow's 1957 residual A(t) as the thing left over when you attribute growth to factor accumulation. The Humbug data construction: synthetic (K, Y) pairs whose scatter plot spells "HUMBUG." Capital aggregation: why valuing a stock of heterogeneous physical capital goods requires prices, which require a profit rate, which is supposed to fall out of the aggregate production function — the circularity. *Reswitching* and *capital reversing* (the Cambridge result that sunk Samuelson's "surrogate production function" defense): the same technique can be cost-minimizing at both a high and a low profit rate but not in between, which violates the monotonic substitution story neoclassicism needs. Why Leontief-style disaggregated IO sidesteps all of this: there's no scalar K, only a matrix A, and prices are derived from the structure of production rather than from marginal products of fictional aggregates.

**Resource schedule (~6 study days).**

- Day 1: Read Shaikh's original 1974 paper — it's only 6 pages, and you'll understand it now in a way you wouldn't have before Week 7. Hosted on Shaikh's own site: <http://anwarshaikhecon.org/index.php/publications/aggregate-production-functions/44-1974/87-laws-of-production-and-laws-of-algebra-the-humbug-production-function>. Also mirrored at <https://digitalcommons.bard.edu/as_archive/656/>.
- Day 2: Cohen & Harcourt, "Retrospectives: Whatever Happened to the Cambridge Capital Theory Controversies?" (*Journal of Economic Perspectives*, 2003). This is the standard mainstream retrospective — fair, historically careful, and it reveals just how much of the debate was conceded by the neoclassical side and then quietly forgotten. PDF: <http://piketty.pse.ens.fr/files/CohenHarcourt03.pdf>.
- Day 3: Felipe & McCombie — the modern extension. Read their 2005 paper "How sound are the foundations of the aggregate production function?" (*Eastern Economic Journal*) as an entry point, or skim their 2013 book *The Aggregate Production Function and the Measurement of Technical Change: "Not Even Wrong"* (Edward Elgar). An accessible short version: Felipe & McCombie (2014), "The Aggregate Production Function: 'Not Even Wrong'," *Review of Political Economy*, 26(1). For a free summary see Guerrien & Gun in *Real World Economics Review* 73: <https://www.paecon.net/PAEReview/issue73/GuerrienGun73.pdf>.
- Day 4: Root it. Read Joan Robinson's 1953–54 paper "The Production Function and the Theory of Capital" (*Review of Economic Studies* 21) if you can access it — it's the origin point. If not, the INET piece by Marc Lavoie gives a clean summary: <https://www.ineteconomics.org/perspectives/blog/what-even-famous-mainstream-economists-miss-about-the-cambridge-capital-controversies>.
- Day 5–6: Project.

**Mini project — Reproduce the Humbug, two parts.**

*Part A: Algebraic derivation (paper + SymPy verification).* Start from Y = wL + rK. Take the total differential: dY = w·dL + r·dK + L·dw + K·dr. Divide through by Y and rearrange using the share definitions α = wL/Y and 1−α = rK/Y. You should be able to get:

&nbsp;&nbsp;&nbsp;&nbsp;dY/Y = α·(dL/L) + (1−α)·(dK/K) + α·(dw/w) + (1−α)·(dr/r)

Now assume (the empirical regularity) that α is approximately constant over the sample period, and define A(t) such that dA/A ≡ α·(dw/w) + (1−α)·(dr/r). Integrate. You get:

&nbsp;&nbsp;&nbsp;&nbsp;ln Y = α·ln L + (1−α)·ln K + ln A(t)

which rearranges to Y = A(t)·Lᵅ·K¹⁻ᵅ — the exact Cobb-Douglas form, with no production theory whatsoever, just accounting plus constant shares. Write this out by hand, then verify the symbolic manipulation in SymPy. The moment you see the Cobb-Douglas fall out of pure bookkeeping is the moment the argument lands.

*Part B: Numerical humbug.* In a Jupyter notebook: (1) Construct 50 synthetic annual data points where the per-capita output y and per-capita capital k, when plotted as (ln k, ln y), trace out the letters of "HUMBUG" in a scatter — any reasonable letter-shape generation works, the point is that this data cannot have come from a well-behaved production function since the function (ln k → ln y) is non-monotonic and wiggly. (2) For each year, generate a labor share αₜ that is approximately constant — say α ≈ 0.7 with small noise. From this, a wage time series and a profit-rate time series that are consistent with y and k and α. (3) Apply the standard Solow growth-accounting decomposition to recover a "residual" A(t), then run the regression ln(y/A) = β·ln(k) + const and inspect the fitted β. Also try `statsmodels.api.OLS` on ln y vs ln k and ln L and a time trend. (4) Report: R², estimated coefficients, and how close the coefficient on ln k is to (1−α). It should fit beautifully despite the data being absurd — that's the whole point. (5) Write 200 words in the notebook explaining *why* this happened, tying it to Part A.

*Optional Part C (extra depth):* Do the same experiment using a genuine Leontief input-output economy — build a 5-sector IO system (using Week 7's machinery), generate time series of aggregate output and "capital" (the value of the sectoral output bundle) as the technology matrix A changes over time in some nonsense way, and fit a Cobb-Douglas to the aggregates. You'll get another good fit. You've now demonstrated Shaikh's point on data that comes from a specific, disaggregated, Leontief-admissible production structure with no aggregate production function at all.

**Self-check.** Why does the empirical constancy of factor shares *make* the Cobb-Douglas fit work, rather than the Cobb-Douglas fit *explaining* the constancy of factor shares? What's the difference between an accounting identity and an economic law? State the Cambridge circularity argument in one sentence — there's a simultaneity of measurement and explanation at its heart. Why do Morishima and Cockshott both sidestep this entire problem? If the Cobb-Douglas is "only" an accounting identity, why does it continue to be used throughout macroeconomics, growth theory, and RBC models? (Cynical answer is fine, but also: is there a charitable answer?) And — to tie back to your own syllabus — does the Shaikh critique invalidate your use of Cobb-Douglas utility functions in Weeks 1 and 2? Why or why not?

**Bridge.** The Cambridge-Shaikh critique pushed serious heterodox theorists away from aggregate marginal-productivity stories and toward the classical-Marxian tradition of treating the economy as a linear system of interdependent sectors — which is where the second great 20th-century controversy in economics lives. That's the **socialist calculation debate** (Mises → Hayek → Lange → Robbins → Dobb → Mises again → Kantorovich → Cockshott), and it's Controversy 2.

---

## Controversy 2 — The Socialist Calculation Debate

**Framing.** This is the longest-running and most politically consequential methodological debate in 20th-century economics. It opens in 1920 with Ludwig von Mises's claim that rational economic calculation under socialism is strictly *impossible*; it runs through Oskar Lange's 1936 "market socialist" reply, Friedrich Hayek's 1945 reformulation of the argument in informational terms, Don Lavoie's 1985 Austrian revival, and Cockshott & Cottrell's computational counter-argument from the early 1990s onward. For you — someone whose technical work is precisely in the territory of "can we use modern information systems to run better economic coordination" — this is the debate where your politics and your tooling meet. By the end of this week you will have implemented both sides: the one-shot central planning LP (Kantorovich-Cockshott) and the iterative Lange-Lerner tâtonnement, and you will know from the inside which of the classical arguments survive modern computing and which don't.

**Learning objectives.** You can state Mises's 1920 impossibility claim precisely (note: it's narrower than it's usually presented — it's specifically about the *means of production*, not consumer goods, and it's a calculation claim, not an information claim). You can state Lange's market-socialist response and the tâtonnement procedure he proposes. You can state Hayek's 1945 reformulation — *the knowledge problem* — and explain why it's a genuinely different argument from Mises's. You can state Cockshott's computational response, including the N log N complexity claim, and know what it depends on. You can implement a small multi-sector economy both ways (LP and tâtonnement) in Python and empirically compare convergence, information flow, and robustness. Finally, you can say in specific technical terms *which parts of the Austrian argument survive modern computing and which don't*, without either hero-worshipping or strawmanning the Austrians.

**Core concepts.** Mises's calculation argument: without private ownership of the means of production, no exchange of them, therefore no market-clearing prices for capital goods, therefore no common unit in which to compare alternative production plans. (Consumer goods can still have prices even under socialism — this distinction matters and is often lost in popular retellings.) Lange's market socialism: planners play Walrasian auctioneer — announce prices, firms told to produce where marginal cost equals price, planners adjust prices in proportion to excess demand. Known as *Lange-Lerner pricing* or socialist tâtonnement. Hayek's 1945 reformulation: the hard problem isn't calculation, it's *knowledge* — specifically "knowledge of the particular circumstances of time and place," dispersed across millions of actors, tacit, local, partly non-articulable. The price system is valuable primarily as an information-aggregation and coordination mechanism, not primarily as a computational one. Post-1970s mechanism design (Hurwicz, Maskin): formalizes this as the question of what institutions minimize communication costs for implementing desired allocations. Cockshott's computational response: input-output planning has complexity O(N log N) in the number of goods N (using iterative methods that exploit the sparsity of real technology matrices), which is tractable for N ~ 10⁸ on a modern laptop — and the national accounts of a real economy have that many line items or fewer. Dapprich's 2022 extension: modern LP solvers handle choice *between* technologies, so the argument that planners need to know all feasible production methods in advance is also defused.

**Resource schedule (~7 study days, this one's a bit heavier).**

- Day 1: Mises, "Economic Calculation in the Socialist Commonwealth" (1920). Free PDF at Mises Institute: <https://cdn.mises.org/Economic%20Calculation%20in%20the%20Socialist%20Commonwealth_Vol_2_3.pdf>. It's 50 pages in the Salerno edition. Read it the way you'd read any primary source you disagree with: charitably, looking for the strongest version of the argument. The core of the claim sits in the middle of the essay (sections on calculation without money-prices for the means of production) — give that section two passes.
- Day 2: Hayek, "The Use of Knowledge in Society" (*American Economic Review* 1945). University of Chicago PDF: <https://home.uchicago.edu/~vlima/courses/econ200/spring01/hayek.pdf>. Alternative copy at <https://kysq.org/docs/Hayek_45.pdf>. Twelve pages; read twice. This is one of the most influential economics papers ever written — and the argument is *not* the same as Mises's, though it's often conflated with it.
- Day 3: Lange's side of the debate. If you can find a copy, read Lange's 1936 paper "On the Economic Theory of Socialism" (*Review of Economic Studies* 4). It's paywalled but available through most university libraries. For a free modern summary, read the *Socialist Calculation Debate* Wikipedia article's "Lange model" section: <https://en.wikipedia.org/wiki/Socialist_calculation_debate>. And for a clean exposition of the tâtonnement mechanism Lange borrowed from Walras, the QuantEcon lecture *Equalizing Difference* and its neighbours on market equilibrium are good priming material.
- Day 4: Cockshott & Cottrell, "Information and Economics: A Critique of Hayek" (1997). PDF at Glasgow: <https://www.dcs.gla.ac.uk/~wpc/reports/hayek/hayek.pdf>; mirror at Wake Forest: <https://users.wfu.edu/cottrell/socialism_book/hayek_critique.pdf>. This is the paper that applies Shannon-style information theory to Hayek's argument and shows where it breaks down as a *specifically* informational claim. For the companion paper on Mises, read Cottrell & Cockshott's "Calculation, Complexity and Planning" (*Review of Political Economy* 1993).
- Day 5: The state of the debate. Read Dapprich & Greenwood, "Cybersocialism and the Future of the Socialist Calculation Debate" (*Studies in Political Economy*, 2024), free PDF: <https://westminsterresearch.westminster.ac.uk/download/9a880fc75c3050f2def2f72fa685b90c8d5db4734bef96d7801677306bed3e50/191339/17-1-art-4.pdf>. This is a fair, recent academic summary that treats both sides seriously. Then for the contemporary Austrian counter-position, read Boettke & Candela (2023), "On the Feasibility of Technosocialism" (*Journal of Economic Behavior & Organization* 205) — it's paywalled but findable, and it's the sharpest recent formulation of why some Austrians still think Cockshott's program fails even granting modern computing.
- Day 6–7: Project.

**Mini project — Planning LP vs Lange-Lerner tâtonnement.** Set up a 5-sector economy: technology matrix A (5×5 nonnegative, Perron-Frobenius eigenvalue < 1), labor coefficients v (5-vector), labor endowment L = 1000 hours, and a consumer demand system D(p) that maps prices to final-good demands — use a Cobb-Douglas demand system with budget share vector β and total consumer income wL (so d_i(p) = β_i · wL / p_i, where w is the wage and p is the price of consumer good i).

*Version A — Central Planning LP (the Cockshott-Kantorovich way).* Formulate as: given β (known preferences) and L (known endowment), find x such that (I − A)x ≥ d, v·x ≤ L, x ≥ 0, maximizing a social-welfare objective (e.g., maximize the scale factor α such that d = α·β). Solve once with cvxpy. Record: optimal x*, the dual variables on each constraint (these are your "planning prices"), and the wall-clock time.

*Version B — Lange-Lerner Tâtonnement (the market-socialist way).* Don't assume the planner knows A or v. Instead, implement the iterative procedure:
1. Planners announce a price vector p_t and wage w_t.
2. Firms (each knowing only their own column of A and their own v_j) solve: produce x_j to match the demand signal they receive.
3. Consumers generate demand d_i(p_t) = β_i · w_t L / p_{t,i}.
4. Compute excess demand: ED_t = d − (I − A)x.
5. Update: p_{t+1,i} = p_{t,i} · (1 + η · ED_{t,i}) for some step size η, and normalize. Repeat until ‖ED‖ < ε.

Now do five things: (1) Run both versions on the same economy, plot the tâtonnement's price trajectory, check it converges to the LP's dual prices. (2) Count iterations and total number of floating-point operations for each; compare. (3) Vary η — too small is slow, too large diverges, find the stability region. (4) *Hayek's scenario* — perturb a single column of A by 5% only on the firm's side; re-run tâtonnement. Does it still converge? How quickly? Can it track a slowly-varying A(t)? (5) *Cockshott's scenario* — scale the problem up to 50 sectors, then 500 sectors; time both approaches; check the N log N complexity claim empirically. Write 500 words interpreting the results with explicit reference to the readings. Does your experiment support Mises? Hayek? Cockshott? Where do they each have a point?

**Self-check.** Why does Mises's argument specifically target means of production rather than consumer goods? (If you can't answer this in a sentence, re-read the Mises.) What exactly does Lange's tâtonnement assume about planners' information, and is that assumption realistic? State Hayek's knowledge problem as an information-theoretic claim — where specifically does Cockshott & Cottrell's reply say Hayek is wrong, and where does it concede that Hayek has a point? What does Cockshott's N log N complexity claim actually depend on — sparsity of A, some algebraic structure of the iterative solver, something else? Is your empirical simulation consistent with the claim? What happens to Mises's argument if you accept that consumer goods can have markets within a planned economy (which both Lange and Cockshott explicitly allow)?

**Bridge.** You now have a concrete, experimentally-tested sense of the socialist calculation debate — probably a sharper sense than 95% of people who opine about it. Controversy 3 examines the internal consistency of the Marxian value theory that underlies the entire Cockshott program. If Marx's labor theory of value is *internally incoherent* — as was argued throughout the 20th century under the heading of the **Transformation Problem** — then the labor-hour-pricing apparatus of Cockshott/Cottrell loses its theoretical anchor. The math you'll need is entirely in your toolkit from Week 7.

---

## Controversy 3 — The Transformation Problem

**Framing.** This is the most famous internal-consistency charge against Marx's value theory, and it has been the central technical dispute inside Marxian economics for over a century. In *Capital* Vol. III, Ch. 9, Marx attempts to "transform" labor values into competitive prices of production (prices at which profit rates equalize across sectors), and claims that two aggregate identities hold: sum of prices = sum of values, and sum of profits = sum of surplus values. Bortkiewicz in 1907 pointed out that Marx's algorithm transformed outputs but not inputs — incomplete. When the full transformation is done (simultaneous equations for prices and rate of profit), *generically only one of the two aggregate identities can be preserved by choice of numeraire*. Whether this breaks Marx or merely revises him has divided the Marxian tradition ever since: Morishima and Seton rescued the core proposition with their Fundamental Marxian Theorem; Steedman in *Marx After Sraffa* argued values are "redundant"; Kliman and the Temporal Single-System Interpretation (TSSI) argue the whole "problem" is an artifact of simultaneist interpretation and disappears under temporal valuation. All the math you need is in your Week 7 toolkit.

**Learning objectives.** State the transformation problem precisely. Compute the value system and the price-of-production system for a three-sector economy. Show which of Marx's two aggregate identities holds and which fails in a Bortkiewicz-style simultaneous solution, and watch how the answer depends on the choice of numeraire. Prove (computationally) the Morishima-Seton Fundamental Marxian Theorem: rate of profit is positive iff rate of exploitation is positive. Implement the TSSI temporal alternative and see what changes. Come away with a clear view of what's really at stake: what parts of Marx survive the critique, what parts don't, and what this means — or doesn't — for Cockshott's planning program.

**Core concepts.** Value system: λ = λA + l (where l is unit labor requirements per sector), solved as λ = l(I − A)⁻¹. Price of production system: p = (1 + r)(pA + wl), with w the wage and r the uniform rate of profit — n equations in n+2 unknowns (n prices, r, w), so we fix a numeraire and one distribution parameter. Marx's two aggregate identities: Σpᵢxᵢ = Σλᵢxᵢ and Σπᵢ = Σsvᵢ. Bortkiewicz's result: choose the numeraire such that one identity holds, the other generically fails. Morishima-Seton Fundamental Marxian Theorem: r > 0 iff exploitation rate e > 0, regardless of whether the two aggregate identities hold — this is what rescues the core Marxian proposition. Steedman's position (*Marx After Sraffa*, 1977): labor values are formally redundant — you can compute p and r from (A, l) and the real wage directly via Sraffa's machinery (Controversy 4), so why bother with the value system at all? The TSSI (Kliman, Freeman, McGlone): drop simultaneist valuation, interpret Marx temporally — inputs valued at prior-period prices, outputs at current prices — and both identities can be made to hold.

**Resource schedule (~6 days).**

- Day 1: Marx, *Capital* Vol. III, Ch. 9 ("Formation of a General Rate of Profit and Transformation of Commodity Values into Prices of Production"). Free at marxists.org: <https://www.marxists.org/archive/marx/works/1894-c3/ch09.htm>. This is the primary source of everything that follows. Read slowly, work his numerical example by hand.
- Day 2: Morishima, *Marx's Economics*, Part III ("The Transformation Problem"), Chapters 6–7 — the mathematical statement. You already have the PDF: <http://digamo.free.fr/morishimarx.pdf>.
- Day 3: Steedman's critique. *Marx After Sraffa* (1977) is widely available through libraries. The short version is Steedman's 1977 paper "Marx on the Rate of Profit" in *Capital and Class*. For a free summary from the critical perspective, Robert Vienneau's blog has good exposition: <http://robertvienneau.blogspot.com>.
- Day 4: The TSSI response. Kliman, *Reclaiming Marx's Capital: A Refutation of the Myth of Inconsistency* (2007), selected chapters — especially Ch. 6 on the transformation problem. If you don't have access, Kliman's papers are partially free on the Marxist-Humanist Initiative site.
- Day 5: Shaikh's defense via iterative transformation: "Marx's Theory of Value and the Transformation Problem" (1977, in *The Subtle Anatomy of Capitalism*, Jesse Schwartz ed.). Also relevant is Shaikh's more recent *Capitalism: Competition, Conflict, Crises* (Oxford 2016), Chapter 9.
- Day 6: Project.

**Mini project — Transform a three-sector economy three ways.** Set up the classic three-sector example: Sector I (means of production), Sector II (wage goods), Sector III (luxury goods). Use Marx's original numerical values from *Capital* Vol. III Ch. 9 (constant capital, variable capital, surplus value per sector). (1) Compute the value vector λ from λ = l(I − A)⁻¹. Verify that total value equals Marx's "value of product." (2) Attempt Marx's own (incomplete) transformation — transform output values at the average rate of profit, see what breaks. (3) Implement the proper Bortkiewicz-style simultaneous transformation: solve p = (1 + r)(pA + wl) together with a chosen numeraire. Show that, with the standard numeraire (say, sum of prices = sum of values), the aggregate profit identity fails by a small amount; switch to the alternative numeraire (sum of profits = sum of surplus values), show the price-value identity now fails. Report both. (4) Implement the Morishima-Seton FMT numerically: vary the real wage across a range, compute r and the exploitation rate e at each wage, plot both, and verify they change sign together. (5) Implement the TSSI temporal version: two-period model where t=0 prices value inputs into t=1 outputs, compute period-by-period profits, show how both identities can be preserved. (6) Write 400 words: does the transformation problem actually undermine Cockshott's program? (Main point: probably not — Cockshott uses labor values *directly* for planning, doesn't claim they equal prices of production, so the transformation problem is about an internal debate in interpretive Marxism rather than a load-bearing element of planning theory. But the debate matters for whether "exploitation" remains a coherent category.)

**Self-check.** State Marx's two aggregate identities. Why can both not generically hold simultaneously in the Bortkiewicz solution? State the Morishima-Seton Fundamental Marxian Theorem in one sentence. What does TSSI *concede* to Bortkiewicz and what does it *reject*? What does Steedman's "redundancy" critique amount to — is he denying labor values exist, or denying they're *necessary* for determining prices? Does the transformation problem matter for Cockshott's planning apparatus? Why or why not?

**Bridge.** Steedman's critique points directly forward: he argues that since Sraffa showed you can determine prices and distribution from (A, l) and one distribution parameter without reference to values, the Marxian value system is redundant. Controversy 4 is the serious study of that Sraffian apparatus — which turns out to have devastating independent implications for neoclassical theory too, as the Cambridge Capital Controversy already hinted.

---

## Controversy 4 — Sraffa vs. Marginalist Value Theory

**Framing.** Piero Sraffa's 1960 book *Production of Commodities by Means of Commodities: Prelude to a Critique of Economic Theory* is 99 pages of dense algebra, forty years in the writing, and arguably the most influential short book in 20th-century political economy outside Keynes. Its achievement: a complete theory of prices and income distribution derived from the technical structure of production plus *one* distributional parameter (wage or profit rate), with no reference to marginal utility, subjective preferences, or aggregate production functions. It provides the formal machinery that sank Samuelson's "surrogate production function" defense in the Cambridge Capital Controversy (via the reswitching paradox), offers a clean alternative to Marxian value theory for determining prices (Steedman's case in Controversy 3), and reconstructs a classical (Ricardo-Marx) tradition of price theory that had been dormant since the marginalist revolution. For your purposes, Sraffa is the keystone that connects the input-output machinery of Week 7 to the distributional questions at the center of political economy.

**Learning objectives.** Set up and solve Sraffa's price equation for a multi-sector economy. Compute and plot the wage-profit frontier. Construct the "standard commodity" and understand why it matters (the frontier is linear in its units). Demonstrate reswitching on a two-technique example — this is the computational exhibit that ended the Cambridge Capital Controversy in Cambridge UK's favor. Explain what Sraffa's framework shares with Leontief (Week 7) and where it diverges. Understand why Sraffian prices don't require marginal productivity theory and what that means for the neoclassical story of factor returns.

**Core concepts.** Sraffa's price equation: p = (1 + r)(pA + wl), where A is the technology matrix, l the labor coefficients, w the wage, r the uniform rate of profit, and p the price row-vector. n+2 unknowns, n equations — fix a numeraire and one of (r, w). Wage-profit frontier: as r ranges from 0 to its maximum r_max (the Perron-Frobenius eigenvalue of A in a particular normalization), w traces out a downward-sloping curve. The **standard commodity**: Sraffa's construction of a composite commodity in whose units the wage-profit relationship is *linear* — w = 1 − r/r_max. This is connected to the right eigenvector of A at the PF eigenvalue: the standard commodity has the same value composition as the economy's input structure. **Reswitching**: for two available techniques (A₁, l₁) and (A₂, l₂), technique 1 can be cost-minimizing at both r = 0 and r = r_high while technique 2 dominates at intermediate r. This violates the neoclassical story that lower interest rates always induce more "capital-intensive" production. The Cambridge critique of aggregate capital (Controversy 1) gets its sharpest mathematical form here: there is no well-defined "quantity of capital" that monotonically substitutes for labor as interest rates change. Ricardian invariable measure of value: what the standard commodity provides, solving a problem Ricardo wrestled with for his last years. Marx connection: Sraffian prices = prices of production from Controversy 3, reached without any detour through labor values.

**Resource schedule (~6 days).**

- Day 1–2: Sraffa, *Production of Commodities by Means of Commodities* (Cambridge University Press, 1960). Ninety-nine pages. Read slowly with pen and paper. Sraffa's examples are small — work them out by hand before moving on. Widely available through university libraries; out of print in some editions but easy to find secondhand.
- Day 3: Pasinetti, *Lectures on the Theory of Production* (Columbia University Press, 1977), Chapters 4–5 — the cleanest pedagogical presentation of Sraffa's apparatus.
- Day 4: Kurz & Salvadori, *Theory of Production: A Long-Period Analysis* (Cambridge 1995) — the modern comprehensive reference. Chapter 4 on single-product systems, Chapter 5 on joint production.
- Day 5: Reswitching. Samuelson's 1966 *Quarterly Journal of Economics* "Summing Up" piece is the famous concession: read the final few pages. For worked reswitching examples in detail, Robert Vienneau's blog has dozens: <http://robertvienneau.blogspot.com>. For the definitive modern treatment of reswitching and capital reversing, see Petri's *General Equilibrium, Capital and Macroeconomics* (Elgar, 2004).
- Day 6: Project.

**Mini project — Sraffian prices, wage-profit frontier, and reswitching.** (1) Set up a two-sector Sraffian economy: technology matrix A (2×2 nonnegative, PF eigenvalue < 1), labor coefficient vector l. Compute the maximum rate of profit r_max as 1/(PF eigenvalue of A) − 1, using linalg machinery from Week 4. (2) For twenty values of r ∈ [0, r_max], solve for the corresponding wage w(r) with the numeraire "price of sector 1 = 1", and plot the wage-profit frontier. (3) Construct the standard commodity: find the right eigenvector of A corresponding to r_max, normalize, use as the numeraire. Re-plot the wage-profit relationship in standard-commodity units. Verify it's linear: w = 1 − r/r_max. Marvel. (4) Build a reswitching example: two techniques (A₁, l₁) and (A₂, l₂) chosen such that the cost functions cross twice as r varies. For each technique compute the wage-profit frontier; on a single plot show both frontiers and mark the switching points; annotate the reswitching region. (5) Compare with Marxian values: using the same A and l, compute the labor-value vector λ from Week 7. Check — are Sraffian prices at r = 0 (maximum wage) equal to labor values? (Yes.) Are they proportional to values at positive r? (Only if organic compositions are uniform across sectors — generally not.) (6) Write 300 words: what does your reswitching plot *mean* in plain English about the neoclassical story of factor returns? What does it say about the Cambridge Capital Controversy (Controversy 1)?

**Self-check.** What role does marginal utility play in Sraffian price theory? (Answer: none.) What's the economic content of the standard commodity — why does Sraffa bother constructing it? Why is the wage-profit frontier always downward-sloping for a given technique? State the reswitching phenomenon in one sentence. What does Sraffa's framework share with the Leontief input-output framework (Week 7), and where does it diverge? Is the Sraffian framework compatible with the Marxian one? (Yes — they compute the same prices of production — though Sraffians tend to treat values as optional.)

**Bridge.** Controversy 5 is the famous late-Marx claim that Sraffa's apparatus most directly endangers: the tendential fall in the rate of profit. If Sraffa lets you compute r directly from (A, l, w) with no reference to organic composition or values, then *what is Marx's LTFRP a claim about*, exactly? Okishio's 1961 theorem sharpens this into a counter-claim: productivity-enhancing technical change must *raise*, not lower, the rate of profit. The TSSI response challenges the foundation. The empirical evidence is real and contested.

---

## Controversy 5 — The Falling Rate of Profit and Okishio's Theorem

**Framing.** Marx's "law of the tendential fall in the rate of profit" (LTFRP), laid out in *Capital* Vol. III Part III, is one of the most politically consequential claims in his system: it's the theoretical engine of his prediction that capitalism is prone to recurrent crisis. The argument: as capitalists accumulate, the organic composition of capital (ratio of constant capital to variable capital) rises, and so the rate of profit r = S/(C + V) tends to fall despite rising labor productivity. In 1961 the Japanese Marxian economist Nobuo Okishio proved a theorem that appeared to demolish this: if a new technique is cost-reducing at current prices and the real wage is held constant, then the rate of profit at the new equilibrium prices *must rise*. Provable, clean, and for thirty years taken as settled — if you wanted a theory of falling profits you had to look elsewhere. Then, starting in the 1990s, the TSSI school (Kliman, Freeman, McGlone) challenged not Okishio's theorem as a theorem but its relevance to Marx: they argued the theorem assumes simultaneist valuation, which misrepresents what Marx was doing. The debate is fully live. And the empirical evidence — Dumenil & Levy, Shaikh, Moseley, Kliman, Roberts — finds genuine falling profit rates in post-WWII OECD economies, though the interpretation is contested.

**Learning objectives.** State the LTFRP precisely as Marx made it. State Okishio's theorem precisely and understand why it's mathematically unassailable *given its assumptions*. Implement both Okishio's result and the TSSI temporal alternative in the same economy, and see the same underlying technical change produce a *rising* profit rate under one interpretation and a *falling* one under the other. Know the empirical record: what do real-world profit rates actually do, and what methodological choices matter for the answer? Understand this as a debate about interpretation as much as about economics.

**Core concepts.** Rate of profit in value terms: r = S/(C + V). Rate of profit in price terms: r = π/K, aggregate profits over aggregate capital stock. Organic composition of capital: C/V. Marx's informal argument: accumulation → rising C/V → falling r, assuming rate of exploitation is held constant. Okishio's theorem (1961): let technique j produce the same output as technique j' at lower unit cost when evaluated at current prices p. Then when the economy adopts j' and prices adjust to the new equilibrium p' (again satisfying p' = (1+r')(p'A' + wl')), the new profit rate r' ≥ r. Proof is by simultaneous perturbation of the price equation from Controversy 4. Critical assumption: *simultaneous* valuation — the prices used to evaluate input costs are the same as the prices at which output is sold. TSSI objection: in reality, inputs are purchased at past prices and outputs sold at current (falling, due to productivity rise) prices. Capital stock evaluated at historical cost is *larger* than capital stock evaluated at current replacement cost. Hence the denominator of r is bigger temporally than simultaneously, which can make r fall even as simultaneously-computed r rises. Critics of TSSI (Mohun-Veneziani, Mongiovi): this is an ad hoc rescue; Marx was not an adherent of historical-cost accounting. The empirical question: Shaikh's 2016 book *Capitalism* presents strong evidence for a long-run decline in US profit rates since the 1940s; so do Dumenil-Levy. But exactly how to measure r — which capital concept, which deflator, which sectoral coverage — changes the answer.

**Ergodicity sidebar.** There's a third methodological axis in this debate that's worth flagging even though it's not yet part of the mainstream Marxian literature: the empirical profit-rate work you'll read on Day 5 is methodologically *ensemble-averaging* — averaging rates across firms at a point in time, or averaging aggregate rates across time periods, and treating the two operations as interchangeable. Ole Peters and Alexander Adamou's ergodicity-economics program raises a specific worry: if firm-level profit dynamics are multiplicative (which Minsky-Keen leverage dynamics, which you'll meet in Controversy 6, suggests they are), then ensemble averages and time averages diverge, and the aggregate "falling rate of profit" you compute may be quite different from what a representative firm actually experiences. This doesn't resolve the Okishio-TSSI debate — it adds a third methodological axis to it. If you want to push this thread, see Peters & Adamou, *An Introduction to Ergodicity Economics* (Cambridge 2025), especially their treatment of multiplicative processes and non-ergodicity, and Peters's 2019 *Nature Physics* review "The Ergodicity Problem in Economics."

**Resource schedule (~7 days — this one rewards care).**

- Day 1: Marx, *Capital* Vol. III, Chapters 13–15 (Part III, "The Law of the Tendential Fall in the Rate of Profit"). Free: <https://www.marxists.org/archive/marx/works/1894-c3/ch13.htm>. Three chapters; read all three. Chapter 14 on "counteracting factors" is important and often neglected.
- Day 2: Okishio's 1961 paper "Technical Changes and the Rate of Profit" (*Kobe University Economic Review* 7) if accessible. Easier: the clean textbook exposition in John Roemer's *Analytical Foundations of Marxian Economic Theory* (1981), Chapter 3. Roemer is an analytic-Marxist who takes Okishio as essentially decisive — useful as the "standard academic" position.
- Day 3: Kliman, *Reclaiming Marx's Capital* (2007), Chapter 7 ("The Falling Rate of Profit Controversy"). This is the canonical TSSI statement on Okishio. Kliman also has papers on the Marxist-Humanist Initiative site.
- Day 4: Critics of TSSI: Mohun & Veneziani, "The Incoherence of the TSSI: A Reply to Kliman and Freeman" (*Capital and Class* 31, 2007). Gary Mongiovi, "Vulgar Economy in Marxian Garb" (*Review of Radical Political Economics* 34, 2002). These are harsh but substantive.
- Day 5: Empirical record. Shaikh, *Capitalism: Competition, Conflict, Crises* (Oxford 2016), Chapter 16 on profit-rate trends. Michael Roberts's blog for ongoing empirical work: <https://thenextrecession.wordpress.com>. Dumenil & Levy, *The Crisis of Neoliberalism* (Harvard 2011), Chapters on profit-rate measurement.
- Day 6–7: Project.

**Mini project — Okishio vs TSSI, side by side.** (1) Set up a two-sector economy at a stationary equilibrium: technology A₀, labor l₀, wage w, compute prices p₀ and the profit rate r₀ using Sraffa's equation from Controversy 4. (2) Introduce a cost-reducing technique in Sector 1: A₁ has a lower unit cost at prices p₀ than A₀ does. Solve for the new equilibrium prices p₁ and profit rate r₁ holding the real wage constant. Verify Okishio's theorem: r₁ ≥ r₀. (3) Now simulate the *same* technical change temporally: at t=0, capital inputs are valued at p₀ (historical cost); at t=1, output is sold at the new prices p₁. Compute the TSSI profit rate r_TSSI = (p₁·q − p₀·A₁·q − w·l₁·q) / (p₀·A₁·q + w·l₁·q). Show that r_TSSI < r₀ is possible even when r₁ > r₀ under simultaneist valuation. (4) Iterate: run the sequence for 20 periods with steady productivity growth in Sector 1, plot both r and r_TSSI trajectories. They diverge — one rises, one falls. (5) Empirical exercise: download US BEA data (corporate profits, fixed capital stock) for 1947–2020, compute a rough "profit rate on fixed capital" series, and plot it. Experiment with current-cost vs historical-cost valuation; see how the answer changes. (6) Write 500 words: does the TSSI successfully save Marx? What has each side actually conceded? Is the empirical record consistent with LTFRP, and on whose interpretation? What does this controversy mean for Cockshott's program (which uses labor values directly, and so doesn't itself depend on a working LTFRP)?

**Self-check.** State Okishio's theorem precisely including its assumption about valuation. Why is it mathematically unassailable? What does the TSSI concede and what does it reject? If you accept TSSI, does LTFRP become a trivial accounting consequence of temporal valuation, or does it still require a substantive argument about organic composition? What's the difference between a *tendency* and a *law* in Marx's own language, and why does Chapter 14 on counteracting factors matter? Based on your empirical exercise, does profit-rate behavior in your series depend on the measurement choices you made?

**Bridge.** Before moving from production to money, there's a short seminar worth taking. Controversies 3 and 5 have walked you through the two internal Marxian debates over Morishima's apparatus (the transformation problem and the Okishio theorem) as they're usually framed in the Anglophone literature. But there's a third voice you haven't heard yet — a coordinated Chinese Marxist engagement with the whole Japanese School of Mathematical Marxian Economics — that takes a substantially different methodological view of what went wrong and proposes its own reconstruction. Read it before the monetary controversy. It's short.

---

## Seminar — The Chinese Critique of the Japanese School of Mathematical Marxian Economics

**Framing.** This is a seminar, not a full controversy — three open-access papers, a day or two of reading, a 500-word reflection, and you move on. But the position is distinctive enough and sufficiently underrepresented in Anglophone debates to deserve its own stop on the tour. Since roughly the 2010s, a coordinated cluster of Chinese Marxist economists — centered on Sichuan University, the Chinese Academy of Social Sciences' Academy of Marxism, and the World Association for Political Economy's *World Review of Political Economy* journal — has been developing a systematic critique of the Japanese School of Mathematical Marxian Economics (Morishima, Okishio, Seton). The Anglophone transformation-problem debate you met in Controversy 3 (Morishima vs Steedman vs Kliman-TSSI) and the Okishio debate in Controversy 5 (Okishio vs TSSI vs empirical school) largely operate within the same mathematical framework they argue about — they disagree about interpretation, timing, or valuation within a shared input-output/wage-normalized apparatus. The Chinese school you're about to read argues that the shared apparatus itself inherits Smithian rather than Marxian value theory, and that a different formalization is both possible and already underway. Whether you find this convincing is your call — but having it in your head before the money chapter sharpens your sense of what "formalization" can and cannot do.

**Learning objectives.** Understand the specific technical claim the Chinese critique makes about Morishima's wage-numeraire construction (p_{i,w} = p_i/w collapses into Adam Smith's labor-commanded value theory, not Marx's labor-consumed value theory). Understand how this same objection applies to Okishio's proof and why the Chinese critique treats it as an independent third position rather than a variant of TSSI. Know the positive program Zhang is building in his 2023 paper — what it preserves from Marx's Vol I apparatus, what mathematical tools it adds (game theory, probability, cybernetic control) beyond the linear-algebra toolkit you used in Weeks 3-4, and where it's still incomplete. Situate this within the Chinese-Marxist institutional ecosystem (WAPE, WRPE, CASS Academy of Marxism) and understand why a Chinese-language critical tradition engages Morishima and Okishio differently than the Anglophone one.

**Core concepts.** *The wage-numeraire objection*: Morishima and Okishio both normalize prices by the wage rate (p_{i,w} = p_i/w) to achieve dimensional commensurability between value and price calculations. Zhang argues this makes the resulting "value" = labor purchased, which is Smith's concept, not Marx's labor expended. The argument has force because once you accept the wage-numeraire move, the apparent contradictions in the transformation problem and the apparent soundness of Okishio's theorem both follow — but both are artifacts of the smuggled Smithian concept. *Value as unity of quality and quantity*: Zhang's core objection to Morishima is that he reduces Marx's concept of value to its quantitative dimension (labor-time magnitudes that aggregate outputs) and erases the qualitative dimension (value as social relation between producers under conditions of private division of labor). *The positive program*: Zhang 2023 works through *Capital* Vol I and constructs a formalization that uses the mapping f: A → w (labor → value) as primary; that distinguishes between socially-necessary-labor-time-per-unit (Vol I sense) and socially-necessary-labor-time-for-a-demand (Vol III sense) rather than conflating them; that introduces game-theoretic payoff matrices for producer competition as a prisoner's dilemma; that treats labor complexity via the coefficient h(t) rather than wage-proportional conversion; and that explicitly models wage-payment as end-of-period (means-of-payment function). *Institutional context*: WAPE was founded in 2004, WRPE in 2010. Editorial office at the Academy of Marxism, CASS. This is not a fringe tradition — it is a significant fraction of how Chinese academic Marxian economics organizes itself.

**Resource schedule (~2 days).**

- Day 1: Zhang, "Notes on Michio Morishima's Understanding of Marxian Economics" (*WRPE* 10(3), 2019). Open access: <https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.10.3.0280>. You've already read this — re-read with the positive program in mind now that you know it's coming. Then Zhang & Xue, "A Critical Deconstruction of the Okishio Theorem" (*WRPE* 13(2), 2022). Open access: <https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.13.2.0154>. This is the Okishio-specific version of the same methodological argument — independent of TSSI and arguably sharper as a technical matter.
- Day 2: Zhang, "The Formalization of Marx's Economics: A Summary Attempt Taking as an Example the First Volume of Capital" (*WRPE* 14(1), 2023). Open access: <https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0004>. This is the positive reconstruction — what a Marx-faithful mathematization of Vol I looks like in Zhang's program. Read with attention to what mathematical tools Zhang uses beyond linear algebra. For a second Chinese-school voice making a related Okishio critique from a different angle, also read Bin Yu, "Analysis of the Okishio Theorem" (*WRPE* 13(2), 2022): <https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.13.2.0192>. Yu is the founder of the "Engels School of China" at the CASS Academy of Marxism — a separate institutional voice reaching similar conclusions.

**Mini reflection (no coding).** Write 500–800 words in a notebook answering three questions. (1) Is the wage-numeraire objection (Zhang's core technical claim) convincing? Specifically: when Morishima writes p_{i,w} = p_i/w and treats this as a dimensional-unification device, is he committing Zhang's charged Smithian move, or is the objection overreaching? (2) How does Zhang's critique of Okishio relate to TSSI? They're both anti-Okishio, they arrive at related conclusions, but the route is different — where does TSSI concede something Zhang doesn't, or vice versa? Is it possible to hold both positions, or do they conflict? (3) Zhang's positive program (2023 paper) brings in game theory and probability tools you have from your broader toolkit. Does adding these to the apparatus genuinely capture something Morishima missed, or does it just re-decorate the same input-output framework? No right answer required — this is a reflection exercise to clarify your own view before moving on.

**Self-check.** State the wage-numeraire objection in one sentence without jargon. Why does the Chinese school treat this as an independent third position rather than a variant of TSSI? What does Zhang 2023 add, mathematically, to the Morishima toolkit — is it just new flavor, or a genuinely different formalization? What institutional setting does WRPE sit in, and why does that matter when reading the critique? If Zhang's critique is correct, how much damage does it do to Cockshott's planning program? (Note: Cockshott uses labor values directly in-kind — no wage-numeraire — so the attack lands on Morishima and Okishio but not directly on Cockshott, which is a point worth thinking through explicitly.)

**Bridge.** All six treatments of the production side — five controversies plus this seminar — have now been completed. The Sraffa-Steedman-TSSI-Chinese debate takes money for granted, which, as heterodox economists have been pointing out for decades, is exactly where modern capitalism does its most interesting and destabilizing work. Controversy 6 confronts the monetary side head-on, and then — this is the payoff you've been building toward — asks how money, credit, and finance enter a *planned* economy. This is the capstone.

---

## Controversy 6 — Monetary Theory of Production, Endogenous Money, and Money in a Planned Economy

**Framing.** The 20th-century Marxian tradition inherited Sraffa's neglect of money. Modern mainstream macroeconomics has a theory of money that is demonstrably wrong about how banks actually work (it's been admitted by the Bank of England itself, in a now-famous 2014 paper). In parallel, a heterodox tradition — post-Keynesian, circuitist, Minskyan — has developed the **monetary theory of production**, centered on the claim that money is endogenously created by banks through the act of lending, and that this monetary circuit is essential to how capitalism actually functions. Key figures: Wynne Godley and Marc Lavoie, who gave us stock-flow consistent (SFC) modeling; Augusto Graziani and the Italian circuitists; Hyman Minsky and his intellectual heir Steve Keen. This controversy is the direct answer to a question your Week 8 project merely gestured at: once you have a planned-economy LP, how do *investment*, *intertemporal coordination*, and *transition from capitalism* work? The Cockshott-Cottrell proposal uses labor tokens (IOUs for consumer goods, non-circulating, redeemable in consumption); Dapprich's 2023 extension lets token prices on consumer goods adjust toward market-clearing rates. This is the capstone. Everything connects.

**Learning objectives.** State the endogenous vs exogenous money debate precisely and know why endogenous is now the empirically settled position. Understand Graziani's monetary circuit as a distinct theoretical framework from both mainstream monetarism and traditional Marxism. Build a stock-flow consistent macroeconomic model from scratch and use it to show why "loans create deposits, not the other way round." Understand Minsky-Keen debt-dynamic models as genuine nonlinear systems that can endogenously produce crises. Know what functions money serves in a capitalist economy and, for each function, know the specific institutional substitute proposed in the Cockshott-Cottrell-Dapprich tradition. Finally: have *computationally verified* that a planned economy can coordinate investment without money, using your Week 8 planning LP extended intertemporally.

**Core concepts.** *Endogenous money*: banks create deposits when they make loans; the central bank accommodates reserve demand; the "money multiplier" of textbooks has the causality reversed. Empirically established: BoE 2014 paper. *Monetary theory of production* (Graziani): production takes time; firms need monetary finance *before* they can sell output; banks create the money that starts the productive cycle; M → M' is the fundamental circuit. *Profit paradox*: if firms collectively borrow M to pay wages and then sell output for M', where does the "extra" M' − M come from? Resolution (Lavoie, Godley): through credit expansion and stock-flow accounting, interest payments, and multi-period dynamics. *Stock-flow consistent (SFC) modeling* (Godley-Lavoie): every flow is a change in some stock; every financial asset is someone else's liability; no accounting black holes. The "three balances" identity: government balance + private balance + foreign balance = 0. *Minsky-Keen financial instability*: debt dynamics are endogenous; the economy moves through hedge, speculative, and Ponzi financing regimes; crisis is internally generated. *Relevance to planning*: in a market economy, money coordinates (a) spot exchange, (b) unit of account, (c) store of value, (d) means of financing production across time. In a planned economy, physical allocation replaces (a) and (d) directly; unit of account (b) can be labor-hours or physical units; store of value (c) can be a consumer-goods claim (labor tokens). *Cockshott-Cottrell labor tokens*: issued in exchange for hours worked, redeemable at labor-content prices of consumer goods, explicitly non-circulating (no firm-to-firm tokens). *Dapprich extension* (2023): token prices of consumer goods are adjusted to clear markets, not fixed at labor content — a concession to the argument that labor content alone doesn't reflect intensity of preference. *Intertemporal planning*: replace the interest rate with a social time-preference discount factor in a multi-period LP.

**Ergodicity sidebar.** The Minsky-Keen debt dynamics you'll implement in Version 3 are a textbook example of what Peters and Adamou (ergodicity economics) call *non-ergodic multiplicative processes*: interest compounds, leverage evolves multiplicatively, and any individual firm's (or household's) trajectory has a time-average growth rate that can diverge sharply from the ensemble average computed across all firms. This provides the mathematical language for why Keen-style crises look benign in aggregate statistics and catastrophic for individual actors — the aggregate ensemble-average tells you the average of survivors weighted by survivor size, not the representative individual experience. If you want to push Version 3 further after building it, add a simple extension: rather than a single representative firm, simulate a distribution of N firms with idiosyncratic leverage shocks, plot both the ensemble-average debt-to-income trajectory and a fan-chart of individual trajectories, and watch ensemble averaging hide most of the fragility until catastrophic. This is a natural and short follow-up experiment if you're curious. Primary reference: Peters & Adamou, *An Introduction to Ergodicity Economics* (Cambridge 2025), with Peters's 2019 *Nature Physics* review "The Ergodicity Problem in Economics" as a free shorter alternative.

**Resource schedule (~8 days — this one is longer and it earns the space).**

- Day 1: Endogenous money orthodoxy. Bank of England Quarterly Bulletin 2014 Q1, "Money Creation in the Modern Economy" by McLeay, Radia, Thomas. Free: <https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy>. Short and authoritative; shorter than a *New Yorker* article. This is a central bank admitting the textbooks are wrong.
- Day 2: Lavoie, *Introduction to Post-Keynesian Economics* (Palgrave 2006), Chapter 3 on money and credit. A clean pedagogical overview.
- Day 3: Graziani, *The Monetary Theory of Production* (Cambridge, 2003). A short book, ~150 pages. The core of the circuitist tradition.
- Day 4–5: Godley & Lavoie, *Monetary Economics: An Integrated Approach to Credit, Money, Income, Production and Wealth* (Palgrave 2007). Free PDF: <http://digamo.free.fr/godleylavoie7.pdf>. Read Chapter 2 (accounting) and Chapter 3 (the SIM model) carefully. Chapter 4 (PC model) for portfolio choice. This is the methodology you'll implement.
- Day 6: SFC survey. Nikiforos & Zezza, "Stock-Flow Consistent Macroeconomic Models: A Survey," Levy Institute Working Paper 891 (2017). Free: <https://www.levyinstitute.org/pubs/wp_891.pdf>. A modern overview of where the field has gone.
- Day 7: Keen on financial instability. *Can We Avoid Another Financial Crisis?* (Polity 2017) for the accessible version. Keen's academic papers for the math — especially his derivation of endogenous debt dynamics from a simple set of accounting identities.
- Day 8: Money in a planned economy. Dapprich, "Tokens Make the World Go Round: Socialist Tokens as an Alternative to Money" (*Review of Evolutionary Political Economy* 4, 2023). Open access: <https://link.springer.com/article/10.1007/s43253-022-00091-6>. Plus Dapprich & Cockshott, "Input-Output Planning and Information" (*Journal of Economic Behavior & Organization* 205, 2023). Finally, Cockshott & Cottrell's chapters on labor tokens in *Towards a New Socialism* (Chapter 2 especially).
- Days 9–10: The capstone project.

**Mini project — From a capitalist SFC model to a planned economy, in four versions.** This is the capstone. All six Controversies, all ten Weeks, all your tooling — cashed out into a single coherent notebook. Build it incrementally.

*Version 1 — Baseline SIM.* Implement the Godley-Lavoie SIM model (Chapter 3 of their book): three sectors (households, firms, government), no banks, pure government-money economy. Simulate the stationary state. Perturb: increase government spending by 20%, trace the dynamic response over 100 periods. Verify stock-flow consistency at every time step (no accounting leaks).

*Version 2 — Add endogenous bank credit.* Extend to include a banking sector that creates deposits when it makes loans to firms. Firms borrow to finance wage payments; workers spend wages on consumer goods; firms receive revenue, repay loans (with interest); deposits are extinguished. Simulate a credit-financed expansion. Confirm Graziani's circuit: money originates in bank lending, is validated by production and sale, is destroyed by repayment. Address the profit paradox computationally: show that in a multi-period model with growing credit, aggregate monetary profits are reconciled.

*Version 3 — Minsky-Keen financial fragility.* Extend again: households borrow to finance consumption; debt-to-income ratios rise; investment responds to the valuation ratio (Tobin's q); monetary expansion initially looks healthy but eventually debt-servicing costs crowd out demand. Reproduce a Keen-style endogenous crisis: no external shock, the system produces instability from its own dynamics. Plot the collapse trajectory.

*Version 4 — THE PLANNED-ECONOMY TRANSFORMATION.* Replace the banking sector with the Cockshott-Cottrell-Dapprich apparatus. Investment decisions are made by a planning LP (the Week 8 machinery), extended intertemporally — multi-period horizon, explicit social-time-preference discount factor δ instead of a market interest rate. Labor is compensated in tokens. Tokens are redeemable for consumer goods at prices adjusted (à la Dapprich) toward market-clearing rates, without circulating between firms. Run on the same underlying technology and preferences as Version 3. Compare: (a) stability — does the planned economy avoid the endogenous crisis of the Keen-Minsky version? (b) investment allocation — does it differ systematically? (c) consumption trajectories for households; (d) response to a negative productivity shock, compared across all four versions.

Write 1,000 words (notebook markdown) interpreting the results. What roles did money play in Versions 1–3? Which of those roles persist in Version 4 in transmuted form? What genuinely goes away? What new coordination problems appear — and how does the LP solve them? Where, specifically, do you *not* trust your Version 4? What would the Boettke-Candela Austrian critique (from Controversy 2) point to as failure modes of your Version 4 that your simulation cannot detect?

**Self-check.** State the endogenous money thesis. Why does the textbook "loanable funds" story get the causality backwards? State Graziani's profit paradox and explain how a multi-period SFC framework resolves it. Why does stock-flow consistency discipline macroeconomic modeling in a way that DSGE models typically do not? What specific roles does money play in a capitalist economy, and which of these persist in the Cockshott-Dapprich token proposal? In your Version 4, how did you handle intertemporal coordination without an interest rate — and does the social time-preference discount factor feel like a first-class substitute, or a hack? After all four versions: do you believe a planned economy can coordinate investment at scale? What did the computation teach you that the reading alone did not?

**Bridge.** There's one more controversy worth attending to before you step away from this framework and apply it — because the single most politically urgent use case for the whole Cockshott-Cottrell-Dapprich planning program is climate. Controversy 7 is where the tools stop being just mathematically interesting and start being a serious candidate for how humanity might actually organize the decarbonization transition. It's the capstone-after-the-capstone.

---

## Controversy 7 — Climate-Constrained Planning

**Framing.** In October 2022 Cockshott, Cottrell, and Dapprich published *Economic Planning in an Age of Climate Crisis* — the trio's argument that the climate transition cannot be accomplished through carbon pricing and market incentives, and requires explicit economy-wide planning of the sort they have been theorizing for thirty years. This is the book where the planning apparatus you've now built in Python gets pointed at the crisis that will define the 21st century. The argument is serious, and it has received serious heterodox critical attention — Michael Roberts is broadly sympathetic; the Cosmonaut review ("How (Not) to Economically Plan in the Age of Climate Crisis") is sharply critical while engaging the substance. For a closing controversy this is the right one because it (a) synthesizes every piece of the prior arc — input-output, LP duality, Morishima-style multi-sector reasoning, labor tokens from Controversy 6, climate as a set of hard physical constraints — into a single concrete application, and (b) puts the whole tradition on trial against a real-world task with a deadline.

**Learning objectives.** Formulate a climate-constrained planning LP: standard multi-sector planning with the addition of CO₂ emission coefficients and a hard emissions cap that tightens over time. Understand why carbon pricing *alone* cannot accomplish the scale of transition required, and what the planning alternative adds. Know the historical precedent the authors lean on (UK wartime planning 1939–1945 and its continuation into the early postwar period). Be able to critique the book's proposal using tools from Controversies 2 (Austrian critique), 3 (transformation problem — does labor-plus-CO₂ dual accounting hold together?), and 6 (money and investment). Have computationally executed a three-decade decarbonization plan for a toy economy and seen, concretely, how the planner's choices trade off output, consumption, emissions, and investment in green capacity.

**Core concepts.** Dual accounting: every commodity has both a labor-time cost (as in Weeks 7–8) and a CO₂-emissions cost, with the emissions cost computed by a parallel Leontief inverse on the emissions matrix E. Planning objective: maximize welfare (output scale of a standard consumption basket) subject to labor endowment, resource endowments, *and* a time-varying emissions cap C(t) that falls toward zero. Shadow price of the emissions constraint: the LP's dual variable on the emissions cap is the planning equivalent of a carbon price — but unlike a market carbon price, it's computed self-consistently with the physical plan rather than emerging from a fiscal policy decision. The wartime-planning precedent: the UK from 1939 through the early 1950s ran what was in effect an input-output planning system (rationing, direction of labor, Board of Trade controls, sectoral priorities), and it worked well enough to win a total war and rebuild afterward. The authors' claim: the climate transition is a wartime-scale mobilization, and wartime-scale mobilizations have historically been done through planning, not markets. The critical response (Cosmonaut review, arbeitszeit.noblogs analysis): the book's novelty over *Towards a New Socialism* is limited; the ecological sections are thinner than the economic sections; and the relationship between labor-time and CO₂ as parallel accounting units needs more theoretical work than it receives. The Austrian response (implicit, derivable from Boettke-Candela lines): the emissions-abatement pathway requires *discovery* of technologies that don't yet exist, which is exactly where Hayekian knowledge arguments have their strongest footing.

**Resource schedule (~7 days).**

- Day 1–2: The book itself. Cockshott, Cottrell & Dapprich, *Economic Planning in an Age of Climate Crisis* (Amazon self-published, 2022, ISBN 9798357728739). Not available as a free legal PDF — it's cheap on Kindle ($10 or so). Chapters 1–3 (climate science and combat), 6–7 (theory of optimal planning, planning tractability), and 8 (planning and value) are the core for your purposes. The wartime-planning chapters (4–5) are worth reading as historical evidence that economy-wide planning has actually worked at scale under duress. Appendix A describes their software tools.
- Day 3: The sympathetic critical review. Michael Roberts, "Planning and the Climate," *The Next Recession* (Dec 2022): <https://thenextrecession.wordpress.com/2022/12/15/planning-and-the-climate/>. Roberts is a Marxist economist who broadly agrees with the planning tradition but has real critiques; this is the most useful single secondary source.
- Day 4: The harsh critical review. *Cosmonaut*, "How (Not) to Economically Plan in the Age of Climate Crisis" (July 2023): <https://cosmonautmag.com/2023/07/how-not-to-economically-plan-in-the-age-of-climate-crisis/>. From within the planning-sympathetic left, argues that the book is substantially weaker than *Towards a New Socialism* and that the ecological apparatus is underdeveloped. Read this even if you're sympathetic to the authors — especially if you're sympathetic.
- Day 5: The left counter-proposal worth knowing. Troy Vettese & Drew Pendergrass, *Half-Earth Socialism* (Verso, 2022). Different framework (explicitly anti-market, more radical on degrowth and land-use rewilding, uses GAMS-style LP), same political space. Read at least the introduction and the planning chapter. Interactive simulation at <https://half.earth>.
- Day 6: Background — the economics of climate mitigation in the mainstream. Nicholas Stern's 2006 *Stern Review* executive summary, for a sense of what the "carbon pricing + growth" orthodoxy looks like. Then William Nordhaus's Nobel lecture (available free). The point is to know the mainstream position you're arguing against before you throw your planning LP at the problem.
- Day 7: Project.

**Mini project — A thirty-year decarbonization LP for a toy economy.** Take your planning LP machinery from Week 8 and Controversy 6 Version 4. Extend to include climate constraints and run a full transition scenario.

*Setup.* Build a 6-sector economy: (1) fossil electricity, (2) renewable electricity, (3) heavy industry, (4) agriculture, (5) consumer manufacturing, (6) services. Pick plausible technical coefficients A (6×6, Perron-Frobenius eigenvalue < 1) and labor coefficients l. Critically: build an emissions-coefficient vector e, where eᵢ is direct CO₂ emissions per unit of sector-i output. Fossil electricity is by far the largest — say 10× any other sector. Renewable electricity is near zero. Heavy industry is moderately high. Agriculture is moderately high (methane, fertilizer). Consumer manufacturing and services are low. Compute *embodied* emissions per unit of final demand: ε = e(I − A)⁻¹, analogous to labor values.

*Part A: The status quo.* Solve the standard planning LP (maximize consumption scale, subject to labor endowment) with no emissions constraint. Report the associated emissions level per capita. This is the "unplanned baseline" — or equivalently, the emission level of a planner who doesn't care about climate.

*Part B: Hard-cap mitigation.* Add a constraint: total emissions ≤ C. Start with C equal to the baseline, solve; then reduce C by 5% each period over 30 periods (years), re-solving each time and tracking: (a) feasibility — does the LP remain feasible? (b) the shadow price of the emissions constraint — your endogenous "carbon price"; (c) sectoral output composition — how does the plan reallocate from fossil toward renewable as C tightens? (d) consumption scale — how much does welfare fall, and when (if ever) does it recover as green capacity grows?

*Part C: Green investment dynamics.* Extend to multi-period with explicit capital accumulation: green electricity capacity K_R(t) grows according to investment decisions; productive capacity of sector 2 is bounded by K_R. Same for fossil sector — K_F(t) doesn't grow but depreciates. Solve the planning problem as an intertemporal LP: 30-period horizon, endogenous investment allocation, the emissions cap C(t) falling linearly to zero by t=30. This is now a real decarbonization plan. Plot emissions, renewable capacity, fossil capacity, consumption, labor allocation across all sectors over the 30 years.

*Part D: Compare with carbon pricing.* Implement the "mainstream" alternative: keep the plan as the baseline but add a Pigouvian carbon tax τ on emissions, adjust τ until total emissions equal the planned trajectory. Compare the two allocations — where do they diverge? What does the tax fail to do that the plan does, and vice versa? (Typical finding: the plan coordinates *timing* of capacity expansion in ways a tax alone struggles with; the tax is more robust to planner mistakes about future technology costs.)

*Part E: Stress-test the critical arguments.* (1) Boettke-Candela Austrian critique: randomize the emissions coefficients e by ±20% to simulate the planner being wrong about emissions intensities. Re-run Part C. How much does the plan degrade? (2) Cosmonaut critique: the labor-plus-CO₂ dual accounting — does it actually produce coherent shadow prices, or are the two constraints pulling in ways that create internal contradictions? Experiment. (3) Dapprich token extension: add consumer demand that responds to token prices. Does the plan still converge?

Write 1,500 words in the notebook. Address: does your computational exercise support the Cockshott-Cottrell-Dapprich position? Where does carbon pricing look better and where does planning? What did the 30-year trajectory teach you that the equations alone did not? What would you tell someone in actual climate-policy circles who asked whether this kind of planning is feasible at national scale?

**Self-check.** Why can't a pure carbon price accomplish what the planning LP does? Why can the planning LP not accomplish what a carbon price does? What does the shadow price on the emissions cap mean, and why is it a more defensible "carbon price" than one set by political negotiation? State the Austrian critique of your Part E results, in its strongest form. What specifically does *Economic Planning in an Age of Climate Crisis* add beyond *Towards a New Socialism* — and what does the Cosmonaut review argue it fails to add? Is the wartime-planning historical precedent actually a good analogy for the climate transition? Where does it break down?

**Bridge.** You're out of controversies. What you've built, if you've done this seriously, is a working computational model of the climate transition under planned-economy assumptions, grounded in thirty years of heterodox-economic theory and stress-tested against the best critical arguments. That is a deliverable. Not many people anywhere have that.

---

## Where this lands

If you've worked through the full arc — ten weeks of mathematical foundation plus seven deep controversies — you're holding something genuinely rare. A Jupyter notebook that contains: a working Leontief input-output economy, a working Sraffian price system, a full transformation-problem implementation in three different valuation conventions, a stock-flow consistent capitalist macro model with endogenous money and financial fragility, a stock-flow consistent *planned* economy with labor tokens and intertemporal LP investment, and a thirty-year decarbonization plan with explicit emissions constraints and endogenous carbon shadow prices. Plus, underneath, a grasp of why this tradition of thought — input-output analysis, Sraffa-Pasinetti-Kurz price theory, Morishima's mathematical Marxism, Cockshott-Cottrell-Dapprich cyber-socialism, Godley-Lavoie stock-flow modeling, and climate-constrained planning — belongs together rather than being six separate niches.

From here, the natural next steps are: publishing (your SemPKM project is already adjacent to economic-knowledge infrastructure, and a heterodox-computational-economics replication notebook is a natural extension); direct modeling work with one of the Marxian computational-economics groups (Cogliano-Veneziani-Yoshihara at Queen Mary; the Cockshott circle at Glasgow; Dapprich at Potsdam); or — most interesting given your FreeCell platform and infrastructure-automation background — building actual planning and climate-transition software tooling that Left organising ecosystems could use. The tools are now yours.

---

## 201 — Placeholder for a Computational Reconstruction of Zhang's Marxian Formalization Program

**This is a placeholder, not a syllabus.** It exists so the thread isn't lost. The full 201 course should be written *after* the seminar in the 101 course (between Controversies 5 and 6), because until you've read Zhang 2023 carefully and sat with it, neither you nor I can design a sequel course properly. The time to expand this placeholder is when you have actual views about what you want from a 201, not before.

### Why this course exists

Zhang's 2023 paper ("The Formalization of Marx's Economics: A Summary Attempt Taking as an Example the First Volume of Capital," *WRPE* 14(1): 4–33) sketches a mathematical formalization of Marx's Vol I apparatus that is explicitly not Morishima's. Where Morishima and the Japanese School formalize using non-negative matrix theory and input-output analysis, Zhang brings in a wider toolkit: game theory (producer competition as a prisoner's dilemma), probability theory (commodity realization as a random variable with a distribution over successful/partial/failed outcomes), cybernetic control systems (the labor process as a feedback-regulated system), and continuous-time differential equations (unemployment-rate dynamics, capital accumulation). Zhang writes these equations down but does not implement them. To the best of what can be established from a literature search, nobody has. A computationally rigorous companion to Zhang 2023 — a Jupyter notebook or small library that actually runs each of the models he sketches — would be a genuine scholarly contribution and a plausible methodology paper for *WRPE* or a similar venue.

### What the course would cover, in broad strokes

Roughly eight to ten weeks, parallel in structure to the 101 controversies (framing, objectives, concepts, resources, project, self-check, bridge per week). The natural chapter divisions follow Zhang's 2023 paper structure:

- *Value theory formalization.* The mapping f: A → w, socially-necessary-labor-time in both the Vol I and Vol III senses, the fundamental theorem of the labor theory of value (W inversely proportional to labor productivity), labor complexity via h(t). Project: implement Zhang's value system and demonstrate numerically that his distinction between the two senses of SNLT produces different results than Morishima's conflated version. Compare with your Week 7 input-output value calculations.

- *Competition as a dynamic game.* The prisoner's-dilemma payoff matrix for technology adoption, the mixed-strategy and repeated-game extensions Zhang sketches but doesn't fully develop. Project: build a multi-agent simulation of N producers with heterogeneous technologies, each choosing to adopt or not, and track the emergence of Zhang's claimed dynamics (technology generalization, excess-return disappearance, value decline). This is where you'd be *extending* Zhang, not just implementing him.

- *Realization uncertainty and crisis probability.* The distribution F(s) = P(S ≤ s) over commodity-realization outcomes, the means-of-payment function and debt-crisis probability. Project: a simple stochastic simulation of a multi-period commodity economy with realization failures, tracking how crisis propagates through the payment system. This connects directly to the SFC work in Controversy 6 and to the ergodicity sidebar.

- *The labor process as a cybernetic system.* Zhang's equation y = x · S/(1−SR) from his "labor as cybernetic process" section. This is the sketchiest part of his program. Project: actually build the control-theoretic model of the labor process as Zhang implies it should work, using `scipy.signal` or similar, and see whether it produces the qualitative results Zhang claims (the "expansion capacity of capital," the quality-weighted production function).

- *Unemployment dynamics.* Zhang's differential equation da_u/dt = λ_u(1−a_u) − λ_e·a_u and its solution for the steady-state unemployment rate. Project: simulate under different transition probabilities; compare with BEA/BLS unemployment time series; examine the relative-surplus-population claim empirically.

- *Capital accumulation and the LTRPF.* Zhang's reformulation of the Okishio debate — the "prisoner's dilemma" route to a falling rate of profit as compound result of individual capital pursuing excess returns. This is the piece that extends most directly from 101-Controversy-5. Project: implement Zhang's game-theoretic LTRPF mechanism as an N-agent simulation; compare trajectories with Okishio's simultaneist rate and TSSI's temporal rate on the same underlying economy.

- *The primitive accumulation / deprivation process.* Zhang's stochastic deprivation function N_b = t·R^F·N_a. This is interesting and almost nobody works on it formally. Project: historical calibration exercise.

- *Putting it together.* A unified computational framework that runs through Zhang's Vol I formalization end-to-end, tied to a single running economy (probably a calibrated toy with 3-5 sectors).

### Outside sources that would pair naturally

- Bin Yu's Engels School work on Okishio and value theory (*WRPE* 13(2), 2022 and beyond — search the WRPE back catalog).
- Zhang's Chinese-language corpus (Zhang 2009, 2011, 2018) — these are in *Teaching and Research* and *Studies on Marxism* and would need translation, machine or otherwise.
- Cogliano, Veneziani, and Yoshihara, "Computational Methods and Classical-Marxian Economics" (*Journal of Economic Surveys* 36(2), 2022) — the QMUL group's survey of computational approaches to classical-Marxian theory.
- Duncan Foley and Ernesto Screpanti work on formal interpretations of Marx.
- The China Political Economy journal (Emerald) for adjacent work.

### Where this could actually go

Three plausible endpoints if the course succeeds:

1. **A methodology paper submitted to WRPE** presenting the computational companion to Zhang 2023, co-authored with Zhang himself if he's interested (his email is in the papers: zxscu@126.com). This is the most ambitious endpoint and not the obvious one to start with.

2. **An open-source library** — `marxecon` or similar — that implements the Morishima-Okishio framework, the TSSI framework, and the Zhang framework as alternative backends against the same economy object. This would let any future researcher do side-by-side comparison numerically rather than just rhetorically, which currently they can't. This is probably the highest-leverage endpoint given your infrastructure-engineering background.

3. **A direct contribution to the Cockshott / Dapprich planning tradition** — Dapprich's 2023 consumer-feedback planning paper already has code (in *Review of Political Economy*). A Zhang-compatible version of Dapprich's apparatus would be interesting work. Dapprich is at Potsdam and reachable.

### Pre-course prerequisites, when it's time

You'll already have most of what's needed from the 101 course. Additional prerequisites that would help:

- A game theory refresher: Osborne and Rubinstein's *A Course in Game Theory* (free PDF) or Fudenberg and Tirole for the more advanced material. A week's reading.
- Basic stochastic processes / Markov chains: the relevant chapters of Grinstead and Snell's *Introduction to Probability* (free CC PDF).
- Control theory at an introductory level: Åström and Murray's *Feedback Systems* (free PDF).
- Agent-based modeling: the *Mesa* Python library has a good tutorial; one afternoon's work to get oriented.

None of these are massive investments individually. The 201 course would thread them in as needed rather than frontloading them.

### When to come back to this

After the seminar between Controversies 5 and 6 in the 101 course. By then you'll have read all three of Zhang's English WRPE papers plus Bin Yu's companion piece, you'll know whether the critique lands for you and whether the positive program holds water, and you'll have real views about what the sequel course should look like. If at that point you still want to build 201, come back to this placeholder and expand it into a full syllabus. If by then you've decided Zhang's program is more promising as a future research contribution than as a second course of study, the placeholder still served its purpose — it named the thing so you could find it again.

Whatever version of 201 actually gets written: the deliverable should be concrete, public, and citable. That's what separates this from another year of reading.

---

## Appendix A — Pre-course checklist

- [ ] Python environment set up with the packages listed in the Master Resource section.
- [ ] Jupyter or VS Code+Jupyter working.
- [ ] A dedicated notebook per week, committed somewhere (GitHub private repo recommended given your setup).
- [ ] Calendar blocks for the week — 2–3 hour sessions × 4 per week is a workable pattern.
- [ ] Accept that you will fall behind at least once. That's fine. Don't skip weeks; slow down and catch up on the weekend.

## Appendix B — If you have extra time or want deeper depth

- Work selected exercises from Strang's *Introduction to Linear Algebra* textbook each week.
- Re-derive Morishima's Chapter 3 results on your own after Week 7 before checking against his text.
- Read Kantorovich's 1939 *Mathematical Methods of Organizing and Planning Production* (English translation available in *Management Science*, 1960) after Week 6 for historical context.
- Implement a proper simplex method from scratch (not just calling a solver) as an extra Week 6 exercise.

## Appendix C — Signs you're actually absorbing it

- You start seeing level sets everywhere (indifference curves, isoquants, production possibility frontiers are all the same geometric object).
- You stop thinking "inverse of a matrix" and start thinking "undo the linear transformation."
- The LP dual stops being a computational curiosity and starts being where the economic interpretation *lives*.
- When you read an economics paper with matrix notation, you immediately picture what each matrix is *doing* rather than what its entries literally are.
- You can explain why Cockshott's "economic planning is ~ N log N" claim is plausible to a non-specialist.

That last one is roughly the test of whether this course worked.
