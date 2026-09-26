"""18 Cohesion (B2-C2) - the linkers a writing exam rewards.

In a B2/C1 exam 25% of the mark is 'cohesion and coherence'. Knowing lots of
linkers is useless if you do not know WHICH one to use. This module organises
them by FUNCTION, not as a random word list.
"""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "18 Cohesion::"
CA, CS, CC, CE, CQ, CD = D + "Adding and Comparing", D + "Cause and Effect", \
    D + "Contrast and Concession", D + "Examples and Evidence", \
    D + "Sequence and Time", D + "Conclusion and Opinion"

# ============================================== ADDING AND COMPARING

serie_gap(CA, [
    ("___ the cost of housing, ___ people are moving away.",
     "Furthermore, moreover", "moreover",
     "ADDING: <b>moreover, furthermore, in addition, besides, what is more, "
     "additionally, likewise, similarly</b>.",
     ex("<b>Furthermore</b>, the cost of housing is rising. / "
        "<b>In addition</b>, we should consider the environment.")),
    ("___ English is widely spoken, ___ Spanish is spoken mainly in Spain.",
     "While, whereas", "whereas",
     "COMPARING: <b>while, whereas, by contrast, similarly, likewise, on the "
     "other hand, in comparison, compared with/to</b>.",
     ex("<b>While</b> English is widely spoken, <b>whereas</b> Spanish is "
        "mainly spoken in Spain. / <b>Similarly</b> = in the same way. "
        "<b>By contrast</b> = by contrast.")),
    ("He is a doctor. ___, he teaches at university.", "Besides", "besides",
     "<b>Besides</b> + noun/-ing. <b>Besides that / Apart from that</b> + clause.",
     ex("<b>Besides</b> being a doctor, he teaches at university. / "
        "<b>Apart from</b> that, he speaks three languages.")),
    ("The film was slow, ___ the acting was excellent.", "but", "but",
     "ADDING INSIDE A SENTENCE: <b>but, yet, though, although</b> (with a "
     "comma and the verb right after).",
     ex("The film was slow, <b>but</b> the acting was excellent. / "
        "<b>Although</b> the film was slow, the acting was excellent.")),
], nivel="B2", tags=["linker adding"])

# =============================================== CAUSE AND EFFECT

serie_gap(CE, [
    ("___ the heavy rain, the match was cancelled.", "Owing to", "owing to",
     "FORMAL CAUSE: <b>owing to, due to, on account of, on the grounds that, "
     "given that, seeing that, now that, since</b>.",
     ex("<b>Owing to</b> the heavy rain, the match was cancelled. / "
        "<b>On account of</b> the rain... / <b>On the grounds that</b>...")),
    ("The roads were blocked, ___ people couldn't get to work.", "so", "so",
     "RESULT: <b>so, therefore, thus, hence, as a result, consequently, "
     "accordingly, for this reason</b>.",
     ex("The roads were blocked, <b>so</b> people couldn't get to work. / "
        "<b>Therefore</b> is more formal. <b>Hence</b> = hence (formal).")),
    ("___ inflation is rising, wages cannot keep up.", "As", "as",
     "CAUSE with <b>as, since, as a result of, owing to</b>. <b>As</b> + clause "
     "= since/because.",
     ex("<b>As</b> inflation is rising, wages cannot keep up. / "
        "<b>As</b> here does not mean 'when'.")),
    ("The policy failed. ___ , we must reconsider it.", "Accordingly",
     "accordingly",
     "<b>Accordingly, consequently, thus, hence, therefore</b> = accordingly.",
     ex("The policy failed. <b>Accordingly</b>, we must reconsider it. / "
        "<b>Thus</b> and <b>hence</b> are also formal.")),
    ("___ you improve your sleep, you'll feel more energetic.", "Unless",
     "unless",
     "NEGATED CONDITION: <b>unless, if not, provided that, as long as, on "
     "condition that, in case</b>.",
     ex("<b>Unless</b> you improve your sleep, you'll feel more energetic. / "
        "<b>As long as</b> = as long as / <b>Provided that</b> = provided that")),
    ("___ the case is closed, we can proceed.", "Provided", "provided that",
     "<b>provided (that), as long as, on condition that, supposing, assuming</b>.",
     ex("<b>Provided (that)</b> the case is closed, we can proceed. / "
        "<b>As long as</b> = while / <b>Supposing</b> = supposing that")),
    ("___ you have any questions, let me know.", "Should", "should",
     "INVERSION FORMAL: <b>should, were, should you, were you, should there "
     "be, in the event that</b>.",
     ex("<b>Should</b> you have any questions, let me know. / "
        "<b>Were</b> I you, I would accept. / <b>In the event that</b>...")),
], nivel="C1", tags=["linker cause"])

# ============================================ CONTRAST AND CONCESSION

serie_gap(CC, [
    ("___ the high costs, few people can afford it.", "Despite", "despite",
     "CONTRADICTION: <b>despite, in spite of, notwithstanding, regardless of</b> "
     "+ noun/-ing. Or <b>although, though, even though, while, whereas</b> + clause.",
     ex("<b>Despite</b> the high costs, few people can afford it. / "
        "<b>Although</b> the costs are high, few people can afford it.")),
    ("The plan is expensive. ___ , it might be worth it.", "Admittedly",
     "admittedly",
     "REAL CONCESSION: <b>admittedly, granted, it is true that, sure, yes, of "
     "course, certainly</b>.",
     ex("The plan is expensive. <b>Admittedly</b>, it might be worth it. / "
        "<b>Granted</b>, it is expensive. / <b>It is true that</b>...")),
    ("He's very talented. ___ , he never gets promoted.", "And yet", "and yet",
     "CONCESSION + contrast: <b>and yet, yet, nevertheless, still, "
     "nonetheless, even so, all the same, in spite of that</b>.",
     ex("He's very talented. <b>And yet</b>, he never gets promoted. / "
        "<b>Even so</b> = even so / <b>Still</b> = all the same.")),
    ("___ he is only 20, he runs a company.", "Even though", "even though",
     "CONCESSION: <b>even though, despite the fact that, notwithstanding that, "
     "in spite of the fact that, albeit</b>.",
     ex("<b>Even though</b> he is only 20, he runs a company. / "
        "<b>Despite the fact that</b> he is only 20...")),
    ("___ being tired, she finished the marathon.", "Despite", "despite being",
     "<b>Despite + V-ing</b> / <b>Despite + noun</b> / <b>Even + V-ing</b> "
     "(different meaning: 'even').",
     ex("<b>Despite being</b> tired, she finished the marathon. / "
        "<b>Even knowing</b> the risk, she went. = even knowing the risk, she went.")),
    ("He didn't get the job. ___, he wasn't surprised.", "Unsurprisingly",
     "unsurprisingly",
     "NUANCE: <b>unsurprisingly, surprisingly, predictably, unexpectedly, "
     "arguably, admittedly, ironically, tellingly</b>.",
     ex("He didn't get the job. <b>Unsurprisingly</b>, he wasn't surprised. / "
        "<b>Ironically</b> = ironically. <b>Tellingly</b> = tellingly.")),
], nivel="C1", tags=["linker contrast"])

# ========================================== EXAMPLES AND EVIDENCE

serie_gap(CC, [
    ("___ , the data confirms the theory. For example, 80% agreed.",
     "In other words", "in other words",
     "CLARIFYING: <b>in other words, that is to say, to put it another way, "
     "in plain terms, namely, i.e.</b>.",
     ex("<b>In other words</b>, the data confirms the theory. / "
        "<b>That is to say</b> = that is to say / <b>Namely</b> = namely")),
    ("There are many reasons for this. ___, the cost of living has risen.",
     "To begin with", "to begin with",
     "ENUMERATING: <b>to begin with, first of all, firstly, to start with, "
     "first and foremost</b>.",
     ex("<b>To begin with</b>, the cost of living has risen. / "
        "<b>First of all / Firstly / To start with</b> = first of all")),
    ("This affects everyone. ___ students, ___ retirees.", "Both, and",
     "both...and",
     "DISTINGUISHING: <b>both...and, either...or, neither...nor, not only...but "
     "also, whether...or not, whereas, while</b>.",
     ex("This affects <b>both</b> students <b>and</b> retirees. / "
        "<b>Not only</b> X <b>but also</b> Y. <b>Neither...nor</b>.")),
    ("The policy has many drawbacks. ___ , it is very popular.", "On the other hand",
     "on the other hand",
     "<b>On the other hand, conversely, that said, alternatively, in contrast, "
     "on the contrary, then again</b>.",
     ex("The policy has many drawbacks. <b>On the other hand</b>, it is very "
        "popular. / <b>On the contrary</b> = on the contrary (denies the "
        "previous statement).")),
    ("He is not only intelligent ___ he is hard-working.", "but also", "but also",
     "<b>not only...but also</b> to emphasise.",
     ex("He is <b>not only</b> intelligent <b>but also</b> hard-working. / "
        "<b>not only</b> + inversion: <b>Not only is he intelligent, but he "
        "is also hard-working.</b>")),
], nivel="B2", tags=["linker examples"])

# =============================================== SEQUENCE AND TIME

serie_gap(CQ, [
    ("___ the project started, the team was restructured.", "Soon after",
     "soon after",
     "SEQUENCE: <b>soon after, shortly after, shortly afterwards, in the wake "
     "of, in the aftermath of, before long, in due course, subsequently, "
     "previously, prior to, once, as soon as, meanwhile</b>.",
     ex("<b>Soon after</b>, the project was restructured. / <b>Prior to</b> the "
        "project, they worked in marketing. / <b>Meanwhile</b> = meanwhile.")),
    ("___ the meeting ended, everyone felt exhausted.", "By the time",
     "by the time",
     "<b>By the time + clause, once, as soon as, no sooner...than, hardly...when, "
     "meanwhile, in the meantime, subsequently, eventually, finally, lastly, "
     "in conclusion</b>.",
     ex("<b>By the time</b> the meeting ended, everyone felt exhausted. / "
        "<b>Eventually / Finally / Lastly</b> = finally / last.")),
    ("___ of the report, we should analyse the data.", "Prior to", "prior to",
     "<b>Prior to + noun/V-ing</b> (formal) = before. <b>Before</b> = before. "
     "<b>Until</b> = until.",
     ex("<b>Prior to analysing</b> the report, we should review the data. / "
        "<b>Before</b> the meeting / <b>Until</b> tomorrow")),
    ("The project was a success. ___, it took six months longer.", "However",
     "however",
     "TEMPORAL CONTRAST: <b>however, nevertheless, on the other hand, all in "
     "all, on balance, overall, in the event, as it happens, ultimately, "
     "eventually</b>.",
     ex("The project was a success. <b>However</b>, it took six months longer. / "
        "<b>All in all / On balance / Overall</b> = on balance / "
        "<b>As it happens</b> = as it happens.")),
    ("She is very talented, ___ she is only 20 years old.", "and", "and",
     "ADDING with <b>and, as well as, alongside, plus, in addition to, not to "
     "mention, let alone, coupled with</b>.",
     ex("She is very talented, <b>and</b> she is only 20 years old. / "
        "<b>Not to mention</b> = not to mention. <b>Let alone</b> = let alone.")),
], nivel="B2", tags=["linker sequence"])

# ============================================= CONCLUSION AND OPINION

serie_gap(CD, [
    ("___ , the project was worth the effort.", "All in all", "all in all",
     "CONCLUSION: <b>all in all, on balance, overall, to sum up, to conclude, "
     "in conclusion, in short, in brief, ultimately, in the final analysis, "
     "in hindsight</b>.",
     ex("<b>All in all</b>, the project was worth the effort. / "
        "<b>In hindsight</b> = in hindsight.")),
    ("___ I think we should implement the change now.", "Personally",
     "personally",
     "OPINION: <b>personally, in my view, in my opinion, from my point of "
     "view, to my mind, as far as I'm concerned, if you ask me</b>.",
     ex("<b>Personally</b>, I think we should implement the change now. / "
        "<b>If you ask me</b> (informal) = if you ask me.")),
    ("___ this approach, I would say the evidence is compelling.", "On the whole",
     "on the whole",
     "<b>On the whole, in general, broadly speaking, in principle, for the "
     "most part, by and large, in most cases, generally speaking</b>.",
     ex("<b>On the whole</b>, the evidence is compelling. / <b>In principle</b> "
        "= in principle / <b>For the most part</b> = for the most part.")),
    ("___ this is the best option available.", "To sum up", "to sum up",
     "<b>To sum up, to conclude, in conclusion, in short, all things "
     "considered, taken together, on the whole, ultimately</b>.",
     ex("<b>To sum up</b>, this is the best option available. / "
        "<b>All things considered</b> = all things considered.")),
    ("The rules should be changed. ___, the current system works well.",
     "Having said that", "having said that",
     "NUANCE: <b>having said that, that said, that being said, admittedly, "
     "granted, it must be said, for all that</b>.",
     ex("The rules should be changed. <b>Having said that</b>, the current "
        "system works well. / <b>It must be said that</b> = it must be said that.")),
    ("___ the crisis, unemployment has fallen.", "Despite", "despite",
     "NUANCED OPINION: <b>despite, notwithstanding, arguably, admittedly, if "
     "anything, in all likelihood, presumptively</b>.",
     ex("<b>Despite</b> the crisis, unemployment has fallen. / <b>If anything</b> "
        "= if anything / <b>In all likelihood</b> = in all likelihood.")),
], nivel="C1", tags=["linker conclusion"])

# =============================================== DEFINITION AND CLASSIFICATION

serie_gap(CD, [
    ("A ___ is a person who treats sick animals.", "veterinarian",
     "a veterinarian",
     "DEFINITION: <b>A/An + noun + is/are + clause</b>.",
     ex("A <b>veterinarian</b> is a person who treats sick animals. / "
        "<b>A</b> + singular countable + <b>is</b> + definition.")),
    ("___ term for this is 'cohesion'.", "The", "the",
     "DEFINITION: <b>The + term for / The word / The term used</b>.",
     ex("<b>The</b> term for this is 'cohesion'. / "
        "<b>What</b> do you mean by that? = what do you mean by that?")),
    ("There are three types: A, B ___ C.", "and", "and",
     "CLASSIFICATION: <b>and, as well as, along with, together with, plus, "
     "besides</b>.",
     ex("There are three types: A, B <b>and</b> C. / A, B <b>as well as</b> C.")),
    ("___ is more effective: A ___ B. It's a matter of taste.", "Whether, or",
     "whether...or",
     "DEFINING: <b>whether...or not, if...or, what...is called, known as, "
     "referred to as, termed, so-called</b>.",
     ex("<b>Whether</b> A is more effective <b>or</b> B is a matter of taste. / "
        "It is a <b>so-called</b> paradox.")),
], nivel="B2", tags=["linker definition"])

# =================================================================== CLOZE

cloze(CD, "{{c1::In conclusion}}, the project was a success.",
      extra="<div class='box rule'><span class='lbl'>Conclusion linkers</span>"
            "<b>all in all, on balance, overall, to sum up, to conclude, in "
            "conclusion, in short, ultimately, in the final analysis</b>. In a "
            "B2/C1 exam, <b>To sum up / In conclusion</b> in the last sentence "
            "= free marks.</div>",
      tags="c1-c2 cohesion cloze")

cloze(CE, "{{c1::Owing to}} the heavy rain, the match was cancelled.",
      extra="<div class='box note'><span class='lbl'>Formal cause</span>"
            "<b>owing to, due to, on account of, on the grounds that, given "
            "that, seeing that, now that</b> + noun/clause.</div>",
      tags="c1-c2 cohesion cloze")

tabla(CD, ["Function", "Linkers (most formal first)"],
     [["ADDING", "<b>furthermore, moreover, in addition, besides, "
                "additionally, likewise, not to mention</b>"],
      ["ADDING (inside a sentence)", "<b>and, plus, as well as, along with, "
                                      "coupled with</b>"],
      ["CONTRAST", "<b>however, nevertheless, nonetheless, on the other "
                   "hand, in contrast, conversely, by contrast</b>"],
      ["CONTRAST (in a sentence)", "<b>but, yet, still</b> (informal)"],
      ["CONCESSION", "<b>admittedly, granted, that said, having said that, "
                     "it must be said that</b>"],
      ["CONCESSION (clause)", "<b>although, though, even though, "
                               "notwithstanding that, albeit</b>"],
      ["CAUSE", "<b>owing to, due to, on account of, on the grounds that, "
                "given that, seeing that, now that</b>"],
      ["RESULT", "<b>therefore, thus, hence, consequently, accordingly, "
                 "as a result</b>"],
      ["CONDITION", "<b>unless, provided that, as long as, on condition "
                    "that, should, in the event that</b>"],
      ["EXAMPLE / CLARIFICATION", "<b>for example, for instance, in other "
                                   "words, that is to say, namely, such as</b>"],
      ["SEQUENCE", "<b>subsequently, soon after, shortly afterwards, "
                    "in the wake of, prior to, once, meanwhile</b>"],
      ["OPINION", "<b>personally, in my view, from my point of view, as "
                  "far as I'm concerned</b>"],
      ["CONCLUSION", "<b>all in all, on balance, overall, to sum up, in "
                     "conclusion, in short, ultimately, in hindsight</b>"],
      ["EMPHASIS", "<b>indeed, in fact, actually, certainly, undoubtedly, "
                   "arguably, ironically</b>"]],
     titulo="Linker map by FUNCTION (what the exam asks for)",
     nivel="C1",
     nota=ul("<b>Exam tip</b>: do not use ten different linkers in the same "
             "text; that sounds unnatural. Choose 3-4 families and vary within "
             "them.",
             "<b>Formal</b> = paper/university (furthermore, moreover, "
             "consequently, in conclusion).",
             "<b>Informal</b> = speech/email (but, so, anyway, plus, actually, "
             "by the way).",
             "<b>Never</b> start a formal paragraph with 'In my opinion': better "
             "<i>It is arguable that...</i> or <i>There is a case for...</i>."))
