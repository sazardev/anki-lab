"""20 Complex Sentences (B2-C2) - indirect questions, clefts, inversion,
ellipsis, substitution and 'there' constructions."""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "20 Complex Sentences (B2-C2)::"
IQ, CL, IN, EL, TH = D + "Indirect Questions", D + "Cleft and Pseudo-cleft", \
    D + "Inversion", D + "Ellipsis and Substitution", D + "There and Special Forms"

# =============================================== INDIRECT QUESTIONS

serie_gap(IQ, [
    ("Could you tell me ___ the film starts?", "what time", "what time",
     "NO INVERSION in indirect questions: word order is that of a statement.",
     ex("Could you tell me <b>what time</b> the film starts? / "
        "<s>Could you tell me what time does the film start</s> is WRONG.")),
    ("Do you know ___ he comes tonight?", "whether", "whether",
     "<b>if / whether</b> = whether. <b>What, where, when, why, how, who, "
     "which</b> = indirect interrogatives.",
     ex("Do you know <b>whether</b> he comes tonight? / "
        "<s>Do you know does he come</s> is WRONG.")),
    ("I wonder ___ they will agree to the terms.", "if/whether", "whether",
     "<b>I wonder if/whether..., It depends on whether..., The question is "
     "whether..., It is not clear if...</b>.",
     ex("I wonder <b>if/whether</b> they will agree. / <b>Whether</b> before "
        "<i>or not</i> always: <i>whether or not</i>.")),
    ("She asked me ___ I had finished.", "if/whether", "if/whether",
     "Question verbs: <b>ask, wonder, know, want to know, see, find out, "
     "understand, remember, forget, doubt</b>.",
     ex("She asked me <b>if/whether</b> I had finished. / <b>Ask</b> always takes "
        "<b>if/whether</b> (not <i>what</i>).")),
    ("Could you explain ___ this happens?", "why", "why",
     "<b>Could you explain why...? / What does this mean? / How does this "
     "work? / What if...?</b> The <b>Wh-</b> keeps the normal word order.",
     ex("Could you explain <b>why</b> this happens? / <b>What does this mean?</b>")),
    ("___ you give me a hand with this?", "Would", "would you",
     "<b>Would you...? Could you...? Can you...? Will you...? Have you ever...? "
     "Do you mind...? Would you mind...? I was wondering if you could...?</b>",
     ex("<b>Would</b> you give me a hand? / <b>I was wondering if</b> you could "
        "help. (a very soft indirect request)")),
], nivel="B2", tags=["indirect-question"])

# ============================================= CLEFT AND PSEUDO-CLEFT

serie_gap(CL, [
    ("It was in the office ___ I left my keys.", "that", "that",
     "<b>It cleft</b>: <b>It + be + element + that + the rest</b>.",
     ex("It was in the office <b>that</b> I left my keys. / <b>It was</b> Ana "
        "<b>that</b> called. / <b>It was</b> yesterday <b>that</b> I saw him.")),
    ("What I need ___ a break.", "is", "is",
     "<b>Wh-cleft</b>: <b>What + clause + verb</b>. Extremely useful to "
     "<b>focus</b>, <b>correct</b> and <b>summarise</b>.",
     ex("What I need <b>is</b> a break. / What I meant <b>was</b> that we should "
        "leave. / What happened <b>was</b> that we ran out of money.")),
    ("___ he meant was that the plan was failing.", "What", "what",
     "<b>What ... was/were</b> = pseudo-cleft. Ideal for correcting someone "
     "politely.",
     ex("<b>What</b> he meant <b>was</b> that the plan was failing. / What I "
        "object to <b>is</b> the deadline, not the salary.")),
    ("It wasn't until 3pm ___ the meeting started.", "that", "that",
     "With <b>not until / only after / only when / not since</b>: "
     "<b>It + be + adverb + that</b> (no inversion).",
     ex("It wasn't until 3pm <b>that</b> the meeting started. / <b>Only after</b> "
        "lunch <b>did</b> they arrive (with inversion).")),
    ("The problem isn't money. ___ is time.", "What", "what",
     "<b>Neg-cleft</b>: <b>What ... isn't + subject</b>.",
     ex("The problem isn't money. <b>What</b> it <b>is</b> is time. / What he "
        "wants <b>isn't</b> money, <b>it's</b> recognition.")),
], nivel="C1", tags=["cleft c1"])

# ============================================================= INVERSION

serie_gap(IN, [
    ("Never ___ I seen such talent.", "have", "have I",
     "A negative adverb at the start of the clause → <b>auxiliary + subject + "
     "verb</b>.",
     ex("<b>Never have</b> I seen such talent. / <b>Seldom / Rarely / Hardly / "
        "Little / Nowhere</b> + inversion.")),
    ("Not only ___ she apologise, but she also paid.", "did", "did she",
     "<b>Not only</b> + strong inversion.",
     ex("<b>Not only did</b> she apologise, but she also paid. / <b>Not only</b> + "
        "<b>aux + subject + V</b>, and the main clause in normal order.")),
    ("___ I known about the meeting, I would have come.", "Had", "had I known",
     "<b>Had I known</b> = if I had known. <b>If</b> disappears in mixed "
     "inversions.",
     ex("<b>Had I known</b> about the meeting, I would have come. / <b>Were I</b> "
        "you... = if I were you. <b>Should you need</b>... = if you need.")),
    ("___ we to continue the meeting for another hour, we'd have finished.",
     "Were we to continue", "were we to continue",
     "<b>Were we to + base</b> (formal) = if we were to. <b>Should</b> + base.",
     ex("<b>Were we to continue</b> the meeting for another hour, we'd have "
        "finished. / <b>Should you require</b> further information, please "
        "contact me.")),
    ("So ___ the noise that we couldn't hear.", "loud", "so loud",
     "<b>So + adj + auxiliary + subject + verb</b>. With a <b>plural</b> "
     "subject the auxiliary is NOT inverted.",
     ex("<b>So loud was</b> the noise that we couldn't hear. / <b>So many books "
        "were</b> on the table (plural = no inversion).")),
    ("___ he is, he won't change his mind.", "No matter how", "no matter how",
     "<b>No matter how + adj/adverb + clause</b> (the modal is NOT inverted: "
     "<b>no matter how hard <b>he tries</b></b>).",
     ex("<b>No matter how</b> clever he is, he won't change his mind. / "
        "<b>However hard</b> he tries, he fails. / <b>Whatever</b> he does, she "
        "supports him.")),
], nivel="C1", tags=["inversion c1"])

# =========================================== ELLIPSIS AND SUBSTITUTION

serie_gap(EL, [
    ("I think she's French. — Do you ___ ?", "think so", "think so",
     "Substitution with <b>so / not</b>: <i>I think so, I don't think so, I hope "
     "so, I'm afraid so, I suppose so, I don't suppose so, I should think so</i>.",
     ex("I think she's French. — Do you <b>think so</b>? / — Will you come? — "
        "<b>I don't think so</b>. / <b>I hope so</b>.")),
    ("___ you coming tonight?", "Are", "are you coming",
     "A question with <b>be</b> (<b>so</b> is dropped): <b>Are you coming? / "
     "Is he going? / Have you finished? / Did you know?</b>",
     ex("— Will you come tonight? — <b>Are</b> you coming tonight? / "
        "— Did you know? — <b>Did</b> you? (not <i>Did you know it</i>)")),
    ("He drinks tea. She ___ coffee.", "drinks", "drinks",
     "Verb ellipsis: the verb is repeated when the subject changes.",
     ex("He drinks tea. She <b>drinks</b> coffee. / She can swim and he can "
        "<b>swim</b> too.")),
    ("The first book was good. ___ was the second.", "The second", "the second",
     "Substitution with <b>one / ones / the other / do so</b> and "
     "phrase ellipsis.",
     ex("The first book was good. <b>The second</b> was better. / I can swim and "
        "so <b>can she</b>. / He works here and so <b>do I</b>.")),
    ("I don't like horror films. ___ does my brother.", "Neither", "neither",
     "Short answers with <b>so / neither / nor</b> + auxiliary: <b>so do I / "
     "neither do I / nor do I / so have I / neither have I</b>.",
     ex("I don't like horror films. <b>Neither does</b> my brother. / — She can "
        "drive. — <b>So can I</b>. / — He didn't go. — <b>Neither did I</b>.")),
], nivel="B2", tags=["ellipsis substitution"])

# =========================================== THERE AND SPECIAL FORMS

serie_gap(TH, [
    ("___ been a delay in the project.", "There has", "there has been",
     "<b>There + be</b> = there is. Past: <b>there was / there were</b>. "
     "Future: <b>there will be</b>.",
     ex("<b>There has</b> been a delay. / <b>There was</b> a problem. / "
        "<b>There will be</b> a change.")),
    ("___ no point in waiting.", "There's", "there's no point",
     "Fixed: <b>there's no point in + V-ing</b>, <b>there's no sense in + "
     "V-ing</b>, <b>there's no need to + base</b>, <b>it's no use + V-ing</b>, "
     "<b>it's worth + V-ing</b>.",
     ex("<b>There's no point in</b> waiting. / <b>There's no need to</b> worry. / "
        "<b>It's worth</b> trying.")),
    ("___ you ever tried the Italian restaurant?", "Have", "have you ever",
     "Short answers: <b>So have I / Neither have I / Nor have I / So did I / "
     "Neither did I</b>.",
     ex("— <b>Have</b> you ever tried the Italian restaurant? / — Have you? — "
        "<b>So have I</b>. / <b>Neither have I</b>.")),
    ("It's the second time ___ you've been late.", "that", "that",
     "Fixed: <b>it's the first/second/last time (that)..., it's high time "
     "(that)..., it's about time (that)...</b>.",
     ex("It's the second time <b>that</b> you've been late. / <b>It's high time</b> "
        "we left. = it is high time we left.")),
    ("I prefer tea ___ coffee.", "to", "to",
     "<b>Prefer A to B</b>. NEVER <i>prefer A than B</i>. Also <b>would rather + "
     "A than + B</b>.",
     ex("I prefer tea <b>to</b> coffee. / I prefer <b>walking to</b> taking the "
        "bus. / I'd rather tea <b>than</b> coffee.")),
], nivel="B2", tags=["there constructions"])

tabla(TH, ["Structure", "Meaning", "Example"],
     [["<b>There is/are</b>", "existence", "<i>There <b>is</b> a problem.</i>"],
      ["<b>There must be</b>", "there must be", "<i>There <b>must be</b> a reason.</i>"],
      ["<b>There should be</b>", "there should be", "<i>There <b>should be</b> more staff.</i>"],
      ["<b>There is no point in</b>", "there is no point in", "<i>There's <b>no point in</b> arguing.</i>"],
      ["<b>There is a tendency to</b>", "there is a tendency to", "<i>There <b>is a tendency to</b> overwork.</i>"],
      ["<b>There is no doubt that</b>", "there is no doubt that", "<i>There's <b>no doubt that</b> he tried.</i>"],
      ["<b>There is no denying that</b>", "there is no denying that", "<i>There's <b>no denying that</b> it failed.</i>"],
      ["<b>It is worth + V-ing</b>", "it is worth", "<i>It <b>is worth</b> waiting.</i>"],
      ["<b>It is no use + V-ing</b>", "it is no use", "<i>It's <b>no use</b> crying.</i>"],
      ["<b>It is high time + clause</b>", "it is high time", "<i>It's <b>high time</b> we left.</i>"],
      ["<b>It is a shame that</b>", "it is a shame that", "<i>It's <b>a shame that</b> he left.</i>"],
      ["<b>It goes without saying that</b>", "it goes without saying that",
       "<i>It <b>goes without saying that</b> it matters.</i>"]],
     titulo="There and It constructions (C1): 12 you must control",
     nivel="C1",
     nota="These structures are <b>the C1 hallmark</b>. In a B2 exam, writing "
          "<i>There must be a reason</i> or <i>It goes without saying that</i> "
          "immediately raises your Language mark.")

cloze(CL, "{{c1::What}} I need {{c1::is}} a break.",
      extra="<div class='box rule'><span class='lbl'>Wh-cleft</span>"
            "<b>What + clause + verb</b>. It is used to <b>correct</b> someone "
            "politely: <i>What I meant <b>was</b>...</i></div>",
      tags="c1-c2 cleft cloze")

cloze(IQ, "Could you tell me {{c1::what time}} the film starts?",
      extra="<div class='box warn'><span class='lbl'>No inversion</span>"
            "In indirect questions the word order is that of a STATEMENT: "
            "<i>what time <b>the film starts</b></i>, never "
            "<i>what time <b>does</b> the film start</i>.</div>",
      tags="c1-c2 indirect-question cloze")
