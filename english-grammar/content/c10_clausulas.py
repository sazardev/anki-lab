"""10 Sentences (B1-C2) - questions, tag questions, inversion, clefts,
concession and adverbials."""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge

D = "10 Sentences::"
Q, I, X, O, A = D + "Questions and Tag", D + "Inversion", D + "Cleft and Focus", \
    D + "Concession and Contrast", D + "Adverbs"

# ============================================================== QUESTIONS

gap(Q, "___ you ever been to Norway?", "Have", nivel="B1", cue="ever",
    forma="Have you ever been",
    regla="<b>Have + subject + ever + participle?</b> With <b>ever / never</b> "
          "always the <b>Present Perfect</b>.",
    ejemplos=ex("<b>Have</b> you <b>ever been</b> to Norway?",
               "<b>Have</b> you <b>ever eaten</b> sushi?"),
    notas="<b>Did you ever go</b> to Norway? is correct if you ask about a "
          "specific moment in the past.",
    tags="questions ever")

gap(Q, "What time ___ the film start?", "does", nivel="B1", cue="what time",
    forma="does the film start",
    regla="<b>What time + does + subject + base verb?</b>",
    ejemplos=ex("<b>What time does</b> the film <b>start</b>?",
               "<b>What time did</b> the film <b>start</b>?"),
    notas="<i>What time is the film starting?</i> is also correct (continuous). "
          "With <b>will</b>: <i>What time will it start?</i>",
    tags="questions what-time")

gap(Q, "You don't smoke, ___ ?", "do you", nivel="B1", cue="tag with don't",
    forma="do you",
    regla="Negative main clause → <b>positive</b> tag.",
    ejemplos=ex("You don't smoke, <b>do you</b>?", "She hasn't called, <b>has she</b>?"),
    notas="With <b>never, hardly, few, little</b> the tag is also positive: "
          "<i>He never calls, <b>does he</b>?</i>",
    tags="tag-questions")

gap(Q, "Nobody phoned, ___ ?", "did they", nivel="B1", cue="tag with nobody",
    forma="did they",
    regla="Unaccountable subjects (<b>nobody, everyone, someone, something, "
          "nothing, anybody</b>) take a <b>plural</b> verb, and the tag uses "
          "<b>they / they did</b>.",
    ejemplos=ex("Nobody phoned, <b>did they</b>?", "Everything is fine, <b>isn't it</b>?"),
    notas="NEVER <i>didn't he</i> after <i>nobody</i>: <s>Nobody phoned, didn't "
          "he?</s> is WRONG.",
    tags="tag-questions")

gap(Q, "How long ___ you ___ in this job?", "have, been", nivel="B2",
    cue="how long", forma="have, been",
    regla="<b>How long + have/has + subject + been + V-ing?</b>",
    ejemplos=ex("<b>How long have you been</b> in this job?",
               "<b>How long have</b> they <b>known</b> each other?"),
    notas="Answer: <i>I've <b>been here for</b> five years.</i>",
    tags="questions how-long")

# ============================================================== INVERSION

gap(I, "Never ___ I seen such a mess.", "have", nivel="C1",
    cue="negative adverb first", forma="have I",
    regla="If a <b>negative adverb</b> (<b>never, rarely, seldom, not only, "
          "hardly, no sooner, little, nowhere</b>) opens the clause, the order is "
          "<b>inverted</b>: auxiliary + subject + verb.",
    ejemplos=ex("<b>Never have</b> I seen such a mess.",
               "<b>Rarely does</b> he complain.",
               "<b>Not only did</b> she apologise, but she also paid."),
    notas=ul("If the clause has no auxiliary, add <b>do/does/did</b>: "
             "<i>Never <b>have</b> I seen...</i> / <i>Never <b>did</b> I see...</i>",
             "Also with <b>only</b>: <i><b>Only after</b> the exam <b>did</b> I "
             "realise...</i>",
             "In questions with <b>never</b>: <i><b>Have</b> you <b>ever</b>...? "
             "— No, never.</i>",
             "With <b>hardly / scarcely</b> + <b>when</b>: <i><b>Hardly had</b> I "
             "left <b>when</b> it started to rain.</i>"),
    tags="inversion negation c1")

gap(I, "So ___ the news that nobody spoke.", "was", nivel="B1",
    cue="so ... that", forma="was the news",
    regla="<b>So + adjective + Auxiliary + subject + verb</b>. If the clause has "
          "<b>only</b> or <b>just</b>, <b>that</b> is used and there is no "
          "inversion.",
    ejemplos=ex("<b>So angry was</b> she that she couldn't speak.",
               "<b>So cold is</b> the water that my hands hurt."),
    notas="<b>So + adjective + a + noun + plural</b> is NOT inverted: "
          "<i><b>So many books</b> there are on this desk.</i> / <i>There are "
          "<b>so many</b> books.</i>",
    tags="inversion so")

gap(I, "Not until midnight ___ he finish the report.", "did", nivel="C1",
    cue="not until", forma="did he",
    regla="<b>Not until / Only after / No sooner</b> → inversion with the "
          "auxiliary.",
    ejemplos=ex("<b>Not until</b> midnight <b>did</b> he <b>finish</b> the report.",
               "<b>No sooner had</b> I arrived <b>than</b> it started to rain."),
    notas="<b>No sooner... than</b> (not <i>when</i>). "
          "<b>Hardly/Scarcely... when</b> (not <i>than</i>).",
    tags="inversion not-until")

# ================================================================== CLEPT

gap(X, "It was in the office ___ I left my keys.", "that", nivel="C1",
    cue="it was in the office that", forma="that",
    regla="<b>It cleft</b> = <b>It + be + element + that/who + the rest</b>. It "
          "exists to <b>focus</b> on one piece of information.",
    ejemplos=ex("<b>It was</b> Ana <b>that</b> called me.",
               "<b>It was</b> in 2019 <b>that</b> I moved here."),
    notas=ul("With people: <b>that</b> or <b>who</b>. With things: <b>that</b> or "
             "<b>which</b>.",
             "Negative: <i><b>It wasn't</b> me <b>that</b> called.</i>",
             "<b>Wh-</b> clefts: <b>What I need is time.</b> / <b>What happened "
             "was that we ran out of money.</b> / <b>Where we met was in Paris.</b>"),
    tags="cleft focus c1")

gap(X, "What I need ___ a break.", "is", nivel="C1", cue="what I need is",
    forma="is",
    regla="<b>Wh-cleft</b>: <b>What + clause + verb</b>. Extremely useful to "
          "<b>focus</b>, <b>correct</b> and <b>summarise</b>.",
    ejemplos=ex("<b>What I need is</b> a break.",
               "<b>What happened was</b> that we ran out of money."),
    notas="Very useful for <b>focus</b>, <b>correction</b> and <b>summarising</b> "
          "in speaking and in exam writing.",
    tags="wh-cleft c1")

gap(X, "It wasn't until 3pm ___ the meeting started.", "that", nivel="C1",
    cue="not until", forma="that",
    regla="With <b>until/before/only</b> use the construction <b>It + be + "
          "adverb + that</b> (no inversion).",
    ejemplos=ex("<b>It wasn't until</b> 3pm <b>that</b> the meeting started.",
               "<b>It was only after</b> lunch <b>that</b> they arrived."),
    notas="<b>Only</b> goes <b>after</b> the verb: <i>It was only <b>after</b> "
          "lunch that they arrived.</i> / <i>They arrived <b>only after</b> "
          "lunch.</i>",
    tags="only cleft c1")

# ============================================================== CONCESSION

gap(O, "___ being poor, she never complained.", "Despite", nivel="B2",
    cue="despite being poor", forma="Despite",
    regla="<b>Despite / In spite of / Even though</b>.",
    ejemplos=ex("<b>Despite being</b> poor, she never complained.",
               "<b>In spite of</b> the rain, we went out."),
    notas="<b>Despite + -ing / noun</b>. <b>Even though + clause</b> (subject + "
          "verb).",
    tags="concession")

gap(O, "The film was boring. ___, I enjoyed it.", "However", nivel="B2",
    cue="however", forma="However",
    regla="Contrast linkers: <b>however, although, though, whereas, "
          "nevertheless, on the other hand, yet, still, in contrast</b>.",
    ejemplos=ex("The film was boring. <b>However</b>, I enjoyed it.",
               "<b>Although</b> it was boring, I enjoyed it."),
    notas="<b>However</b> and <b>therefore / thus / moreover</b> normally go "
          "between commas or as a separate sentence. <b>But</b> is informal only.",
    tags="linkers contrast")

gap(O, "He gets ___ , ___ he never seems tired.", "on, yet", nivel="B2",
    cue="two gaps: on / yet", forma="on, yet",
    regla="<b>get / carry on + V-ing</b> = keep. <b>Yet</b> = however.",
    ejemplos=ex("He gets <b>on</b> my nerves.", "She works hard, <b>yet</b> she's never promoted."),
    notas="Fixed: <b>get on + nerves, carry on + V-ing, keep on + V-ing, go on + "
          "V-ing</b>.",
    tags="linkers contrast")

# ================================================================ ADVERBS

gap(A, "I only found out ___ .", "yesterday", nivel="B1", cue="only + yesterday",
    forma="yesterday",
    regla="<b>Focus adverbs</b> (<b>only, just, even, still, already, also, "
          "too, never, not</b>) go <b>before</b> the main verb.",
    ejemplos=ex("I <b>only</b> found out <b>yesterday</b> (emphasis).",
               "I found out <b>yesterday</b> (neutral)."),
    notas=ul("<b>Only</b> after the subject or the auxiliary: <i>I <b>only</b> saw "
             "him / I saw <b>only</b> him / <b>Only</b> I saw him.</i>",
             "<b>Just</b> = exactly: <i>I <b>just</b> arrived</i> (I have just "
             "arrived).",
             "<b>Hardly... when</b> / <b>No sooner... than</b> go with "
             "<b>inversion</b>: <i><b>Hardly had</b> I arrived <b>when</b>...</i>"),
    tags="adverbs focus")

gap(A, "She was so tired ___ she couldn't keep her eyes open.", "that",
    nivel="B1", cue="so... that", forma="that",
    regla="<b>so + adjective + that + result</b> (or <b>too + adjective + to + "
          "base</b>).",
    ejemplos=ex("She was <b>so</b> tired <b>that</b> she couldn't keep her eyes open.",
               "She was <b>too</b> tired <b>to</b> stay awake."),
    notas="With <b>such + a + noun</b>: <i>It was <b>such a</b> beautiful day "
          "that we walked.</i>",
    tags="so too such result")

# =================================================================== CLOZE

cloze(I, "{{c1::Never have}} I seen such a mess.",
      extra="<div class='box rule'><span class='lbl'>Negative inversion</span>"
            "A negative adverb at the start of the clause <b>forces</b> "
            "inversion: <b>auxiliary + subject + verb</b>.</div>",
      tags="c1-c2 inversion cloze")

cloze(X, "It was Ana {{c1::that}} called me.",
      extra="<div class='box note'><span class='lbl'>Cleft</span>"
            "<b>It + be + emphasis + that/who + the rest</b>. It exists to "
            "<b>highlight</b> one specific fact.</div>",
      tags="c1-c2 cleft cloze")

# =============================================================== REFERENCE

tabla(A, ["Adverb", "Position", "Example"],
     [["<b>always / never / often / sometimes</b>", "before the verb",
       "<i>She <b>always</b> arrives early.</i>"],
      ["<b>usually / normally / occasionally</b>", "before the verb",
       "<i>I <b>usually</b> take the bus.</i>"],
      ["<b>still / already / just / yet</b>", "with the verb",
       "<i>I've <b>already</b> finished.</i>"],
      ["<b>only / even</b>", "before the verb (for emphasis)",
       "<i>I <b>only</b> wanted to help.</i>"],
      ["<b>today / yesterday / tomorrow</b>", "end of clause or before the verb",
       "<i>See you <b>tomorrow</b>.</i>"],
      ["<b>here / there / abroad / upstairs</b>", "end of clause",
       "<i>He lives <b>abroad</b>.</i>"],
      ["<b>probably / possibly / certainly</b>", "before the verb",
       "<i>It <b>probably</b> won't rain.</i>"],
      ["<b>luckily / hopefully / sadly</b>", "start of the clause",
       "<i><b>Luckily</b>, nobody was hurt.</i>"],
      ["<b>suddenly / finally / eventually</b>", "before the verb",
       "<i>She <b>finally</b> arrived.</i>"]],
     titulo="Where each adverb goes (word order is not free)",
     nivel="B1",
     nota="<b>ONLY, JUST, EVEN</b> and <b>STILL</b> must go immediately before "
          "the verb (<i>He <b>still</b> lives here</i>). Putting them at the end "
          "is a very common error.")
