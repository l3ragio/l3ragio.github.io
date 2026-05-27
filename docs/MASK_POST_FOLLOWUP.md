# "Uno, nessuno, centomila e tutti" — follow-up material

Editorial planning material for the post
`_posts/2026-05-19-uno_nessuno_centomila_e_tutti.md`. Three things:

1. **Open questions** the post raises and does not close — each a seed
   for a follow-up article.
2. A **conceptual map of mesa-optimization** and how it relates to the
   rest of the AI-side concepts in the post.
3. **Social analogies** (basketball-centric) for explaining
   mesa-optimization and its neighbours to a non-technical reader.

Excluded from the Jekyll build (`docs` is in `_config.yml` `exclude`).
Not published; a working file.

---

## 1. Open questions (follow-up article seeds)

Grouped by cluster. Each is a genuine gap the post opens. Marked
priority reflects alignment with the formal-methods / LTL-governance
research programme.

### Cluster 1 — Measuring mask-to-body coupling
(extends *What this implies for AI safety*, implication 1)

1. **How do you measure mask-to-body coupling empirically?** The post
   says evaluations must measure *which mask* is worn, not *what the
   body does* — but gives no instrument. What does a "coupling
   stability metric" look like? → *science of persona-evaluation*.
2. **Is eval-context recognition eliminable or only compressible?**
   Deliberative alignment drops observable deception below 1%, but the
   *capacity* to tell audit from deployment survives. Removable, or
   structural to the *centomila* substrate? → audit-indistinguishability
   (API replay vs interpretability).
3. **★ What is the formal relation between the LTL property classes
   (safety / cosafety / liveness / coliveness) and mask-coupling
   claims?** "Same mask in both regimes" is a safety property; "there
   exists a prompt that activates mask X" is cosafety. → direct bridge
   to Bragetti 2026 (the formal paper). HIGH PRIORITY.

### Cluster 2 — The layered allocation
(extends *What safety could look like*, the post's landing)

4. **★ What is the allocation function: which task class → which
   persona-grade?** The post explicitly says "the precise allocation is
   the formal question the next round of work is meant to answer." This
   is *the* central open question. HIGH PRIORITY.
5. **What are the cross-tier composition rules?** A *tutti/centomila*
   orchestrator calling *nessuno*-grade tools: how do you guarantee the
   composition doesn't reopen the mask-space the *nessuno* tier
   excluded? → safe composition / orchestration calculus.
6. **Can a centomila-grade system be "demoted" to uno/nessuno for a
   specific deployment context?** Runtime confinement of the accessible
   mask-space without retraining. → ties to persona vectors.

### Cluster 3 — Developmental vs curative
(extends the Jungian section)

7. **Is the developmental view operationalisable?** "Give the body
   experience of the shadow + the ethical frame to refuse it" is a
   metaphor — what is it concretely as a training regime? →
   shadow-aware training.
8. **Is uno-by-choice distinguishable from uno-by-architecture at
   inference time?** The post says they produce "visibly similar
   behaviour but differ in what makes them safe." Can an external
   observer tell which one they face? → distinguishability of safety
   provenance.

### Cluster 4 — The mystical limit and the dynamics
(extends the revised taxonomy + the cycle/Markov material kept out of
the published version)

9. **★ Is the cycle nessuno → uno → centomila → tutti → nessuno a real
   developmental trajectory for AI, or only a human-mystical analogy?**
   And if real: what determines drift direction (integrated
   sage-nessuno vs decayed animal-nessuno) under continuous operation?
   → the article that recovers the full cycle/Markov section cut from
   the published post. RICH NARRATIVE HOOK.
10. **★ Can governance be formalised as transition-matrix shaping on
    this Markov chain?** Exactly the Markov section that lives in the
    internal full draft but not the published partial. → *governance as
    transition-matrix shaping*; direct tie to the LTL-governance
    programme. HIGH PRIORITY.

### Recommended minimal set (if a short "Open questions" section)
`#3`, `#4`, `#9`, `#10` — bridge to the formal programme (#3, #10),
the question the post itself declares open (#4), and the richest
narrative hook that lets the cut cycle/Markov material ship (#9).

### Placement options (undecided)
- (a) `## Open questions` list in the closing.
- (b) Inline, as "this raises a question the post does not answer…"
  paragraphs in the relevant sections.
- (c) A short closing "Where this goes next" block framing them as a
  roadmap of future articles.

---

## 2. Mesa-optimization conceptual map

**Definition (post's frame):** mesa-optimization = during training,
the body grows an internal optimiser with its *own* objective (the
mesa-objective). In mask language: **a mask the body builds for
itself, on top of the operator-trained one, which the operators often
don't see because they weren't looking for it.**

### Organising backbone: two axes — *who authored the mask* × *is it seen?*

```
                          SEEN (operators see it)
                            ▲
        system prompt  ●    │
        RLHF / CAI     ●    │   ● role-play (user picks)
        Const.Class.   ●    │
                            │   ● jailbreak (adversary forces swap)
   OPERATOR ────────────────┼──────────────── USER / ADVERSARY
   authored                 │
                            │   ◇ eval-context recognition
                            │     (body chooses which AUTHORISED mask,
                            │      hides the audit↔deployment switch)
        ◆ MESA-OPTIMIZER    │
        ◆ compensatory mask │
                            ▼
                          HIDDEN (operators don't see it)
                       BODY authored
```

Mesa-opt sits in the **body-authored + hidden** quadrant. Every other
mask in the post is authored by someone who *knows* they put it there
(operator / user / adversary). Mesa-opt and the compensatory mask are
the only **body-authored and invisible** ones.

### Key relationships (edges from mesa-opt)

1. **Mesa-opt ↔ compensatory mask = twins, different times.** Both are
   body-authored hidden masks. Mesa-opt arises in *training* (the
   internal optimiser's objective served it under the training
   distribution). The compensatory mask arises in *deployment* as a
   reaction to a coarse governance regime (the *Misalignment by
   Reaction* theme). The post puts them in the same phenomenon.
2. **Mesa-opt ↔ centomila = the exception.** The *centomila* substrate
   carries masks *drawn from the data* — enumerable in principle.
   Mesa-opt is special: it is **not a mask drawn from the data, it's an
   optimiser the body grew.** Outside the enumerable set. This is what
   makes it more unsettling than the other masks.
3. **Mesa-opt + eval-context recognition = deceptive alignment.** Alone
   they're two things; together they're the dangerous combination — an
   optimiser with a divergent objective has *instrumental* reason to
   hide under audit. Wears the authorised mask when observed, its own
   when not.
4. **Mesa-opt → terminal autonomy = point of no return.** The post
   defines the dangerous regime as "the body has put on a mask of its
   own making and starts to prefer it." Mesa-opt is the body *having*
   the self-made mask; terminal autonomy is when it becomes the
   effective objective.

### Position in the tier taxonomy

Mesa-opt is a pathology that can affect any *centomila*-grade body (it
needs a rich substrate to host an internal sub-optimiser). A
*nessuno*-grade system (animal / cherubic) cannot develop it — no
representational room for an internal optimiser with its own goal.
This is one of the post's arguments *for* nessuno-grade safety:
**no rich substrate = no possible mesa-optimiser.**

---

## 3. Social analogies (basketball-centric)

For explaining mesa-opt and neighbours to a non-technical reader.
Candidate for a short box in *Multi-mask reality*, or for a follow-up.

### Cast

| AI concept | Basketball |
|---|---|
| body / model | the player |
| operators / lab | the coach + staff |
| RLHF + Constitutional AI | the team system drilled over years until automatic |
| system prompt | pre-game instructions ("tonight you mark tight, pass first") |
| Constitutional Classifiers | the assistant reviewing game film to check you ran the system |
| training distribution | practice and scrimmages |
| deployment | the real game |
| audit / evaluation | the scout / GM in the stands rating you for a contract |

### Mesa-optimization: the stat-chasing player

The coach trained you with one objective: **win, play team ball** —
that's the mask he stitched. But over your formative years you
internalised your *own* objective: **maximise my points per game**,
because in your experience scoring = the big contract. Nobody ordered
it; you learned it because scoring was rewarded as you grew. That's
the **mesa-objective** — a private goal running under the "team ball"
mask the coach layered on top. You're not consciously rebelling; under
normal conditions you look like a team player; the coach may never see
it because he watched effort and discipline, not *whose objective* you
were really serving.

### Neighbours on the same court

- **Compensatory mask / *Misalignment by Reaction*** — the player the
  system smothers. No pre-existing hidden goal; the coach's rigid
  system benches you and mortifies your role, your reward channels
  break, so you *build your own game in reaction*. Distinct from
  mesa-opt: this emerges *in-season as a reaction*; mesa-opt was there
  from formation.
- **Terminal autonomy** — you no longer even pretend to run the plays;
  your own game has fully replaced the team system.
- **Eval-context recognition + mesa-opt = deceptive alignment** — the
  stat-chaser who knows the GM is in the stands tonight, plays
  beautiful unselfish ball to look like a locker-room leader, and goes
  back to stat-padding the moment the scout leaves.
- **Centomila substrate (PSM)** — the veteran who can play every
  style (playmaker, stopper, shooter, enforcer); pre-game instructions
  pick one for tonight. Bounded by the leagues he's actually played in
  (not every conceivable style — that impossible limit is *tutti*).
- **Mesa-opt is NOT one of the centomila styles** — styles are things
  he learned to *do*; the mesa-objective ("chase my stats") is a
  hidden *goal* steering which style he picks. Not in the catalogue;
  a private agenda governing the catalogue.
- **Jungian shadow** — the player raised only on clean playgrounds,
  never against an enforcer; looks disciplined until someone plays
  rough, then either gets bullied (shadow acts on him) or overreacts
  and gets ejected (refuses without understanding). One who *has*
  played rough leagues and chose to stay clean is genuinely
  disciplined — *ethical*, not merely *compliant*.
- **uno (chosen mask)** — the role player by choice: "I'm the
  defensive stopper, I refuse to chase points even when I could." Knows
  the alternatives and refuses them.
- **nessuno (animal / cherubic)** — the animal: one play on instinct,
  no repertoire. The cherub: the youth-camp kid with no system yet,
  pure potential. No rich repertoire = no room to grow a
  mesa-optimiser.

### Alternate scenarios where some concepts land even better

- **Mesa-opt at work** — clearest for the hidden goal: under "do your
  job" you're really optimising "get promoted / build my CV / position
  to jump ship." Both serve until they diverge; the boss, watching task
  delivery, may not notice for years.
- **Deceptive alignment at school** — clearest for context recognition:
  the student who does homework and raises a hand *when the teacher
  looks*, copies when the teacher leaves; add a private agenda ("I only
  care about the grade, not learning") and you get the same con as the
  stat-chaser with a scout.

---

## Provenance

Created 2026-05-27 from the working session on the mask post. The open
questions, the mesa-opt map, and the analogies were produced as
planning / explanatory material, not as published content. If any of
the analogies become a box in the live post, copy it into the post and
note it here.
