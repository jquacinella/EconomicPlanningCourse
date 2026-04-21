# EconomicPlanningCourse

10 week syllabus to become an ecomomic planning expert.

## Convo that started it all

### Human (Apr 21, 2026, 1:15 AM):

can you read this learning path plan crated by another ai for me to learn economic modeling and planning and using subagents, create a detailed outline for each week? the end goal is to have a detailed syllabus for every week that will be my central source for me, plus links to the actual books I need, to all the videos, and fill in any blanks.

---

### Claude:

I've got the plan - a 10-week arc building from multivariable calculus through to Morishima-style economic planning. Before I dive in, quick note on scope: I'm in the web chat, so I can't literally dispatch subagents (that's a Claude Code feature), but I can do the equivalent — batch the research across resources and assemble a single master syllabus document for you. That'll serve the "central source" goal better than multiple files anyway.

Let me verify the actual resources first so the links are real, not hallucinated. Starting with the foundational courses.Excellent. I have enough verified to build this. I found the "Mathematics to plan an economy" reference (it's a Cockshott-tradition cyber-socialist calculation intro from cibcom.org — paired with his own Kantorovich blog post, it's the best free long-form treatment of planning math). I also confirmed Morishima's three growth books form a trilogy, which gives us a natural post-syllabus reading order.

Let me build the syllabus document now.Here's what you've got — a single ~48KB markdown file, 10 weeks, designed to be your central source.

A few decisions I made you should know about so you can push back:

**The "Mathematics to plan an economy" reference** in your CSV was slightly ambiguous. I traced it to a specific Cockshott-tradition PDF at cibcom.org and paired it with his *Returning to Kantorovich* blog post for Week 8 — those two together are the best free long-form planning-math treatment I could find. If the AI that made your plan meant something else (there's also a Cockshott-adjacent ebook floating around with a similar name), tell me and I'll swap it.

**The Morishima ending is explicit.** Your CSV stops at Week 10 with "Barro-Sala-i-Martin companion" but the filename tells me the real target is Morishima. So I ended Week 7 by having you read Morishima Chapters 1 and 3 against the IO machinery you just built — that's where the mathematical apparatus finally touches the destination — and then gave you a post-course reading ladder: *Marx's Economics* (free PDF linked) → *Towards a New Socialism* (full read after your Chapter 3+9 sample) → the other Morishima volumes → Barro-Sala-i-Martin → Cockshott's later work.

**I added a Goodwin model to Week 10.** Your CSV said "phase plane plotter for growth system" generically. Given your Marxian interests (and the fact that you've already built the Marx-circuit React visualization), Goodwin — Lotka-Volterra applied to class struggle — is a much richer target than a plain Solow phase plane, and it lets you feel the math harder (pure-imaginary eigenvalues, closed orbits, structural fragility). Solow stays as the Week 9 project.

**Project specs are concrete.** Each mini-project lists exact parameter values, exact output artifacts, and at least one verification step (envelope-theorem numerical check; Perron-Frobenius positivity check; shadow-price sensitivity check). The point is you can open Jupyter and start.

If you want changes — more Cockshott, more Sraffa, different pacing, a companion cheat-sheet, or the whole thing converted to a Word doc for annotation — say the word.

---

### Human (Apr 21, 2026, 1:28 AM):

This is amazing. I have read a takedown of the Cobb-Douglas utility function as being basically circuluar logic. i do not recall who claimed this. can you dig into that?

---

### Claude:

The most likely candidate is Anwar Shaikh's "humbug production function" paper from 1974 — the single most famous "this is circular reasoning" attack — but there's a whole genealogy of this critique worth mapping. Let me verify the details before I explain.Let me find the Shaikh paper itself — it's been scanned and is available online.The takedown you're probably remembering is **Anwar Shaikh's 1974 "Humbug Production Function" paper** — the single most famous "this is circular reasoning" attack on the Cobb-Douglas form. It's in *Review of Economics and Statistics* 56(1), pages 115–120, and Shaikh hosts it free on his own site: <http://anwarshaikhecon.org/index.php/publications/aggregate-production-functions/44-1974/87-laws-of-production-and-laws-of-algebra-the-humbug-production-function>. Given your Marxian reading list it's almost certainly Shaikh you ran into — he's at the New School and is one of the most prominent living heterodox economists.

The argument is devastatingly clean. Start from the national-accounts identity — total value added equals wages plus profits, or Y ≡ wL + rK. That's a bookkeeping truth, not an economic theory. Now assume (as is roughly true empirically) that labor and capital shares are approximately constant over time. If you differentiate the identity and impose constant shares, a short bit of algebra turns it into something that looks exactly like a Cobb-Douglas production function with exponents equal to the factor shares, plus a residual "technical progress" term (Solow's famous *A(t)*). The Cobb-Douglas isn't describing how inputs get transformed into outputs — it's describing *the accounting identity itself*, in disguise.

The coup de grâce was his numerical demonstration. Shaikh generated fake capital-output data whose scatter-plot, when drawn on a coordinate plane, literally spelled the word HUMBUG. This data couldn't possibly come from any real production process — it's nonsense. He then ran the standard Solow-style regression on it and got a perfect Cobb-Douglas fit with a high R², realistic-looking factor-share coefficients, and all. Since the accounting identity holds for *any* dataset where factor shares are roughly stable, the regression will always "work" — it's fitting an identity, not a law. So every empirical "confirmation" of aggregate Cobb-Douglas that had been treated as evidence for marginal-productivity theory over the preceding forty years was, in his account, just a restatement of how national accounts are constructed.

The institutional sidelight is great: Solow was editor of the journal, got to publish a reply in the same issue, and as the price of getting his rebuttal in at all Shaikh had to agree *not* to write a rejoinder. That's why the paper didn't land as hard as it should have at the time.

Shaikh's argument sits on top of a deeper critique — the **Cambridge Capital Controversy** (roughly 1953–1966), which is where the "circular" charge was first pressed. Joan Robinson, in a 1953 *Review of Economic Studies* paper ("The Production Function and the Theory of Capital"), pointed out that to write Y = f(K, L) you need to measure K as a scalar, but capital is physically heterogeneous — machines, factories, inventories. To aggregate them you have to value them in money. To value them you need prices. Prices depend on the rate of profit. And the rate of profit is exactly what the marginal product of aggregate capital is supposed to *explain*. So the construction defines in its inputs the very thing it's meant to derive as output. Sraffa's 1960 *Production of Commodities by Means of Commodities* formalized this into a rigorous multi-sector price-and-distribution theory — input-output machinery, essentially, which is exactly the terrain Morishima, Pasinetti, and Cockshott work on. Samuelson eventually conceded the logical point in a 1966 *QJE* piece called "A Summing Up," then the profession basically went on as if the concession hadn't happened.

The modern extension of Shaikh is **Jesus Felipe and John McCombie's 2013 book** *The Aggregate Production Function and the Measurement of Technical Change: "Not Even Wrong"* (Edward Elgar). They take Shaikh's accounting-identity argument, apply it systematically to the entire empirical production-function literature (including CES and translog forms, not just Cobb-Douglas), and argue it's fatal.

Two notes on how this connects to your syllabus. **First**, the Cobb-Douglas that shows up in Week 1 (utility) and Week 5 (production) is being used as a *teaching tool* — it's a smooth, strictly concave, analytically tractable function that makes multivariable calculus and constrained optimization nicely solvable in closed form, and is therefore the universal first example in every undergrad textbook. That pedagogical role is independent of whether it describes anything real. You can't learn Lagrange multipliers without an example, and x^α·y^(1−α) is the cleanest one. **Second**, the critique is *especially* relevant to where you're heading. Morishima and Cockshott both work in the input-output/Leontief framework partly *because* the Cambridge-Shaikh critique discredits the aggregate production function as a foundation for value and distribution theory. The linear IO apparatus doesn't need to aggregate heterogeneous capital — it keeps the sectors disaggregated, and derives prices from the structure of production rather than from marginal products of mystical aggregates. So when you hit Morishima Chapter 1 in Week 7, the reason he doesn't touch Cobb-Douglas with a ten-foot pole isn't stylistic, it's the natural consequence of taking Shaikh and Sraffa seriously.

If you want one thing to read after Shaikh's original paper, I'd suggest the Cohen and Harcourt 2003 *Journal of Economic Perspectives* piece "Retrospectives: Whatever Happened to the Cambridge Capital Theory Controversies?" — it's a fair, mainstream-journal retrospective that situates all of this: <http://piketty.pse.ens.fr/files/CohenHarcourt03.pdf>.

---

### Human (Apr 21, 2026, 1:35 AM):

I would love for you to add to the syllabus another section called 'economic controversies' where we can list this cobb-douglas critique and review exactly what you have here but using the tools we learned in the syllabus. what you have above can be a whole week of a lesson with links to everything including the mainstream-journal retrospective. 

once we do that, we can add in the socialist calculation debate

---

### Claude:

Let me pull up the current syllabus file and add the new section before the appendices.Good, I see the right insertion point. Now I'll add a new "Part II — Economic Controversies" section with a full week on the Cobb-Douglas critique (structured identically to the regular weeks) and a placeholder for the socialist calculation debate.Done — syllabus updated with a new **Part II — Economic Controversies** section sitting between the post-course reading ladder and the appendices. A few design choices worth flagging:

**Structure matches the regular weeks exactly.** Same seven elements (framing, objectives, core concepts, resource schedule, mini project, self-check, bridge), so no cognitive switching cost when you get there.

**The mini project has three parts, ordered by depth.** Part A is the algebraic derivation — take Y ≡ wL + rK, total-differentiate it (Week 1 tool), impose constant shares (the empirical move), integrate, and watch Cobb-Douglas fall out of pure accounting. This is the moment the argument lands and it uses Week 1 skills directly. Part B is the numerical humbug — synthetic (ln k, ln y) data that literally traces the letters of "HUMBUG", fit a Cobb-Douglas, get a high R². Part C is optional extra depth: do it again with a genuine Leontief IO economy from Week 7, proving the critique isn't about data being pathological — it's about what regressions on accounting identities always do.

**Resource links verified.** Shaikh's paper is hosted free on his own New School-adjacent site and mirrored at Bard's digital archive. Cohen-Harcourt JEP retrospective is on Piketty's course server. Felipe-McCombie has a free summary in *Real World Economics Review* #73. Robinson's 1953 paper is paywalled but I linked Lavoie's INET summary as a fallback.

**The Socialist Calculation Debate placeholder is a commitment, not a stub.** I sketched out the trajectory I'd want to walk (Mises → Hayek → Lange → Kantorovich → Cockshott) and the project premise (planner's LP vs Lange-Lerner tâtonnement, head-to-head computational comparison on your M1 Max). When you're ready, just say "do Controversy 2" and I'll write it in the same slot. If there are other controversies you want queued — the Transformation Problem, the Sraffa vs Marginalist value theory debate, Keynes vs the Classics, Piketty's r > g framing, whatever — let me know and I'll add them to the list.

One substantive self-question I put in the self-check worth calling out: *does the Shaikh critique invalidate your use of Cobb-Douglas utility functions in Weeks 1 and 2?* The honest answer is no — Shaikh/Cambridge are about the **production function** (aggregating heterogeneous capital goods, explaining factor prices). Utility functions have their own separate critiques (preference axiom violations, incomparability issues) but not the accounting-identity one. Worth making sure that distinction is clean in your head before you go on to Morishima.

---

### Human (Apr 21, 2026, 1:40 AM):

do Controversy 2; can we also line up the Transformation Problem, the Sraffa vs Marginalist value theory debate but not fill it in too much for now.

---

### Claude:

Let me verify the key sources for the socialist calculation debate before I write it up — the classic Mises, Hayek, and Lange texts all have ideological-minefield hosting situations and I want the best free versions.All key sources verified. The Cockshott-Cottrell "Information and Economics: A Critique of Hayek" is hosted at both Glasgow and Wake Forest, and I found the best mainstream summary (Dapprich & Greenwood 2024) that fairly represents the state of the debate. Now let me update the document.Done. The file is now 71KB with the full Socialist Calculation Debate week plus placeholder stubs for Controversies 3 and 4. A few design decisions worth flagging:

**I was deliberately even-handed on the Austrian side.** Given your sympathies it would have been easy to caricature Mises and Hayek and then have you "destroy" them in the project. That would have been intellectually dishonest and actually harmful to your thinking — the Cockshott reply is most powerful when it responds to the strongest version of the Austrian argument, not the strawman. So I noted explicitly that Mises's 1920 argument is *narrower than usually presented* (it's about means of production, not consumer goods, which Lange and Cockshott both allow markets in), and that Hayek 1945 is a *different* argument from Mises 1920 (calculation vs knowledge), which is often conflated. I also pointed you at Boettke & Candela (2023) for the sharpest current Austrian counter-position to Cockshott specifically. Know the strongest version of the other side.

**The project is genuinely hard and genuinely interesting.** The head-to-head — planning LP (one-shot, centralized) vs tâtonnement (iterative, decentralized information) — on the *same* economy with the *same* Cobb-Douglas demand system and IO technology is something you can actually execute in a notebook, and it gives you empirical ground to stand on. The five sub-experiments are designed so that each of Mises, Hayek, and Cockshott has something that either vindicates or challenges them. The Hayek perturbation experiment (firms know their own column of A better than the planner does) is particularly pointed — this is exactly Hayek's "dispersed knowledge" scenario, translated into something computational.

**Controversy 3 (Transformation Problem) is sketched tightly because it flows naturally out of Week 7.** You'll have read Morishima's Chapter 7 in Week 7, which is where Morishima-Seton lives. So the Controversy 3 project is essentially "re-do Morishima's math yourself, with a computer, for a 3-sector economy, and watch where the identities hold and where they break." This is the internal Marxian economics controversy — it's about whether Marx's own value-price apparatus is coherent, which the Cockshott program quietly depends on.

**Controversy 4 (Sraffa vs. Marginalist) bridges backward to the Cambridge Capital Controversy in Controversy 1 and forward to a question Morishima wrestled with explicitly.** This is the one where the math is cleanest — Sraffa's book is basically linear algebra from cover to cover — but the implications are the most radical. I deliberately included reswitching here rather than under the Cobb-Douglas critique, because reswitching is where Sraffian theory gives a *positive* prediction (not just a critique), which distinguishes it from the Shaikh argument.

Two candidates to consider for Controversy 5 if you want to keep going: the **profit rate tendency debate** (does the rate of profit actually have a tendency to fall, and if so why — Okishio's theorem vs TSSI responses — directly continuous with Controversy 3), or the **monetary theory of production / endogenous money debate** (post-Keynesians vs mainstream, Keen, Graziani, Lavoie — which matters if you ever want to take your planning apparatus and ask how credit and money enter a non-market economy).

Just say the word when you want to fill in Controversies 3, 4, or queue up more.

---

### Human (Apr 21, 2026, 1:56 AM):

OK lets do both "does the rate of profit actually have a tendency to fall, and if so why — Okishio's theorem vs TSSI responses" and "monetary theory of production / endogenous money debate (post-Keynesians vs mainstream, Keen, Graziani, Lavoie)"
with a focus on taking your planning apparatus and ask how credit and money enter a non-market economy.

Once we do that, lets fill them all in

---

### Claude:

Let me do some targeted research to verify sources for each controversy before writing all four. I'll batch the searches.All sources verified. Let me view the current placeholder section to get the exact text I need to replace.Now replacing the two placeholders with four full controversies:Done. The document is now 555 lines / 102KB, with all six controversies filled in at full depth. Structural summary:

**Controversy 3 — Transformation Problem.** Marx Vol III Ch 9 (free at marxists.org), Morishima's own mathematical treatment in Part III of *Marx's Economics*, Steedman's "redundancy" critique, Kliman's TSSI defense, Shaikh's iterative rescue. Project: three-sector transformation with Marx's own numbers, Bortkiewicz simultaneous solution, Morishima-Seton Fundamental Marxian Theorem verification, TSSI temporal alternative. The self-check closes with the pragmatic question: *does any of this actually damage Cockshott's planning program?*

**Controversy 4 — Sraffa vs. Marginalist.** Sraffa directly (the 99 pages), Pasinetti's *Lectures*, Kurz & Salvadori's modern reference. Project: compute wage-profit frontier, construct the standard commodity, build a two-technique reswitching example, compare Sraffian prices to Marxian values. This is where the Cambridge Capital Controversy from Controversy 1 gets its sharpest mathematical edge — reswitching is where you can *see* the failure of monotonic capital-labor substitution.

**Controversy 5 — Falling Rate of Profit / Okishio.** Marx Vol III Ch 13-15 (free), Okishio's theorem via Roemer's clean exposition, Kliman's TSSI rebuttal, Mohun-Veneziani critics of TSSI, Shaikh-Roberts empirical work. Project: same technical change simulated under both simultaneist and temporal valuation, producing *opposite* profit-rate predictions from the same underlying economy. Then download BEA data and plot actual profit rates 1947-2020 with different methodological choices. The most rewarding sub-finding is usually: measurement choice matters enormously.

**Controversy 6 — Monetary Theory of Production & Money in a Planned Economy.** This is the capstone I was building toward. BoE 2014 paper (central bank admitting the textbooks are wrong), Graziani's *Monetary Theory of Production*, Godley & Lavoie's *Monetary Economics* (free PDF at digamo.free.fr), the Levy Institute SFC survey, Keen's Minsky work, Dapprich's open-access 2023 tokens paper. The project has four progressive versions of an SFC macroeconomic model: (1) baseline Godley-Lavoie SIM, (2) add endogenous bank credit and address Graziani's profit paradox, (3) add Minsky-Keen financial fragility and generate an endogenous crisis, (4) **THE PLANNED-ECONOMY TRANSFORMATION** — replace the banking sector with the Cockshott-Cottrell-Dapprich labor-token apparatus, use your Week 8 LP machinery extended intertemporally for investment, run head-to-head against the capitalist versions on the same underlying technology and preferences.

**Everything connects.** Controversy 6 imports the SFC methodology into *your own planning apparatus* and asks how investment, intertemporal coordination, and transition from capitalism actually work in non-market form. Dapprich 2023 is the contemporary frontier of that question, and it's open-access, so you can read it right now. The final bridge of Controversy 6 notes there's no next controversy — the arc is complete.

Two things worth calling out explicitly:

**The "fair to the strongest Austrian" discipline is maintained throughout.** Controversy 6 ends by asking you to engage with Boettke & Candela's 2023 critique of technosocialism as a real failure-mode test for your own simulation. If after building a working planned-economy model you still can't articulate where the Austrians have a point, you haven't worked the project hard enough.

**The project specs are designed to actually be buildable.** The Controversy 6 capstone is ambitious (four versions, ~1000 lines of Python probably, SFC accounting discipline at every step), but every piece of it uses tools you'll have from Weeks 6-9 and Controversies 1-5. Nothing is introduced out of order. If you do the full 10 weeks + 6 controversies, the capstone is a natural culmination, not a cliff.

If you want Controversy 7 after all — Boettke-Candela as a direct engagement, or something like *Climate-Constrained Planning* using Cockshott-Cottrell-Dapprich 2022 "Economic Planning in an Age of Climate Crisis" — let me know. Otherwise this is the complete document.

---

### Human (Apr 21, 2026, 10:44 AM):

OHHHH "Climate-Constrained Planning using Cockshott-Cottrell-Dapprich 2022 "Economic Planning in an Age of Climate Crisis" is a great find! I feel like thats a great addition but then we can wrap this up, I'll take the doc and commit it to a repo and get to work

---

### Claude:

Great call — that's the perfect capstone-after-the-capstone. Let me verify the book is findable and what shape the best readings take, then I'll write it up.Excellent — I have the full table of contents and two substantial critical reviews (Michael Roberts in *thenextrecession* and Cosmonaut). The book is self-published via Amazon which means no free PDF, but it's cheap. Also found an interesting detail: the Cosmonaut review is titled "How (Not) to Economically Plan in the Age of Climate Crisis," which I should include as the critical counterweight. Let me add Controversy 7.Now I'll add a final "where this lands" section to replace the bridge text that previously closed Controversy 6, since that wrap-up language actually belongs after Controversy 7:Done. The document is now 602 lines / 114KB. Final structure is 10 weeks + 7 controversies + wrap-up + 3 appendices.

Quick notes on Controversy 7:

**Book accessibility.** The Cockshott-Cottrell-Dapprich 2022 book is self-published through Amazon KDP — there's no free legal PDF, but it's about $10 on Kindle. I flagged this explicitly so you're not surprised. Chapters 6, 7, and 8 are the core for your purposes; 1-3 are climate science background; 4-5 are the UK wartime-planning historical case which is genuinely interesting even if you skim.

**Both critical reviews included.** Michael Roberts (sympathetic-with-reservations) and Cosmonaut (sharply critical from within the planning-sympathetic left, titled "How (Not) to Economically Plan in the Age of Climate Crisis"). The Cosmonaut review is the more important one — it's the strongest left-internal critique, and reading it will make your own implementation more honest. I framed it as "read this *especially* if you're sympathetic to the authors," which is the right disposition.

**Half-Earth Socialism as the adjacent project.** Vettese and Pendergrass's 2022 Verso book is the most-read left climate-planning alternative, uses LP directly, has an interactive simulation at <https://half.earth> you can play with. Including it keeps you from treating the Cockshott tradition as the only game in town.

**The project is the real capstone.** Five parts (A through E), extending your Week 8 + Controversy 6 Version 4 machinery with emissions coefficients, a tightening cap, explicit green investment dynamics, carbon-pricing comparison, and three stress tests for the critical arguments from prior controversies. The Austrian stress test (randomize emissions coefficients to simulate planner error about technology) is the one that most directly confronts Boettke-Candela on their strongest ground.

**The "Where this lands" section got rewritten.** I moved the wrap-up out of Controversy 6 (where it was premature) and into its own closing section after Controversy 7. It explicitly notes that what you'll end up with — six different working computational models tied together — is genuinely rare, and points at three concrete next-step paths: publishing, academic-adjacent modeling work, or building real tooling that Left organising could use (which, given your FreeCell gaming platform work and Ansible infrastructure chops, is probably the most natural fit).

Good luck with the work. Commit it to the repo. If you ever want to come back and add Controversy 8 (options I can think of: ecological-unequal-exchange theories à la Hickel, monetary-sovereignty/MMT-as-fiscal-space-for-planning, or Piketty-style distribution dynamics), just ping me. Otherwise — go build.

---

### Human (Apr 21, 2026, 12:20 PM):

Before we do that, something quick ... in the original convo I had, we were going to for Weeks 5–6
Use Chiang, Fundamental Methods of Mathematical Economics as your main text here. IT seems that got lost along the way. Can we re-integrate that text back into the syllabus but not take anythign out?

---

### Claude:

Let me verify Chiang quickly and then add it back in as a supplementary anchor text for Weeks 5-6 without removing anything.Chiang is verified. The table of contents is exactly what you'd want: Ch 9 is unconstrained optimization (Week 5 core), Ch 11 "The Case of More than One Choice Variable" and Ch 12 "Optimization with Equality Constraints" map directly to Weeks 2 and 5, and Ch 13 "Further Topics in Optimization" covers KKT and inequality constraints (the heart of Week 5). Ch 15-17 cover differential equations (Week 9). It also has a classic economist-oriented treatment of matrix algebra in Ch 4-5 that pairs well with Strang's Week 3 material.

Let me add Chiang to the master resource list and then thread it through the relevant weeks without disturbing anything else.Now I'll thread Chiang into the resource schedules for Weeks 2, 5, 6, and 9 where it's most useful. Week 5 is the strongest fit — it's where the economist-oriented treatment of KKT and economic optimization really pays off over Boyd's more engineering-flavored convex optimization exposition.Now Week 6, where Chiang Ch 13 extends into LP duality territory, and where his economist framing helps the transition from abstract duality to shadow-price interpretation:Now Week 2, where Chiang Ch 12 on equality-constrained optimization is the natural companion to MIT 18.02's Lagrange multiplier sessions:Finally, Week 9, where Chiang's differential equations treatment is economist-focused:Done. Chiang & Wainwright is now threaded through five places:

1. **Master resource list** — added as the first entry under "Books worth buying," with a paragraph explaining what it is (the canonical math-econ textbook, what graduate programs use for math camp) and where in the syllabus it's most useful.
2. **Week 2 (Constrained Optimization)** — Ch 12 as companion to the MIT 18.02 Lagrange material. Chiang's bordered Hessian exposition is specifically called out because it's clearer than most.
3. **Week 5 (Economic Optimization)** — this is where Chiang actually gets promoted to **primary text** for the week. Chapters 9, 11, 12, 13 together cover the entire KKT/convex optimization arc with economic examples throughout, which is the framing that helps this material stick in a way that Boyd's engineering flavor doesn't quite match. I kept Boyd in as the supplementary resource for the mathematical depth, but Chiang is now the anchor.
4. **Week 6 (LP and Duality)** — Ch 13 continues from Week 5 directly into LP territory. The framing I used: LP is the specialization of KKT where objective and constraints are all linear, and Chiang's economist-flavored treatment of how shadow prices emerge from the Lagrangian makes the economic interpretation of the LP dual click without extra explanation.
5. **Week 9 (Differential Equations)** — Chapters 15, 16, and 17 as companion to MIT 18.03. I specifically flagged Ch 17 on discrete-time difference equations as valuable because MIT 18.03 is continuous-time only, and a lot of the economics literature (including the Solow model's discrete-time formulation you'll meet in Week 10) is discrete-time.

Nothing was removed — every resource from every prior version of the document is still in place. The file grew from 602 to 607 lines / 114KB to 117KB.

That's the complete syllabus. 10 weeks of math plus 7 controversies, with Chiang as the math-economics textbook anchor, Strang for pure linear algebra, Morishima and Cockshott-Cottrell-Dapprich as the heterodox-economic destinations, and Godley-Lavoie and Keen for the monetary side. Go commit it. Good luck with the work.

---

