"""09 Relative and Noun Clauses (B1-C2)."""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge

D = "09 Relative Clauses::"
R1, R2, R3, R4 = D + "Defining", D + "Non-defining", \
    D + "Relative Pronouns", D + "Relatives with Adverbs"
DN = D + "Noun Clauses"

# ================================================================ DEFINING

gap(R1, "The woman ___ is standing there is my aunt.", "who", nivel="B1",
    cue="identifies the woman", forma="who",
    regla="A <b>defining</b> relative clause identifies the noun. It takes NO commas.",
    ejemplos=ex("The man <b>who</b> called you is here.",
               "The book <b>that</b> I bought is great."),
    notas="<b>that</b> can be a person or a thing (it is the most common "
          "relative). <b>who</b> only people. <b>which</b> only things.",
    tags="relative who")

gap(R1, "The house ___ I grew up is for sale.", "that", nivel="B1",
    cue="the house", forma="that",
    regla="<b>that</b> = people and things. It is far more common than most "
          "learners realise: it is the most frequent relative pronoun.",
    ejemplos=ex("The film <b>that</b> we saw last night was great.",
               "She's the only person <b>that</b> I trust."),
    notas="It can be <b>omitted</b> if it is the subject: <i>The film (that) we "
          "saw was great.</i>",
    tags="relative that")

gap(R1, "This is the reason ___ I left.", "why", nivel="B2",
    cue="the reason", forma="why",
    regla="<b>why</b> replaces <i>the reason that / for which</i>. It is used "
          "after abstract nouns such as <b>reason</b>.",
    ejemplos=ex("That's the reason <b>why</b> I left.",
               "The reason <b>why</b> he quit isn't clear."),
    notas="<b>reason why</b> (without <b>the</b>) also works: <i>The reason I "
          "left...</i> (without <b>why</b>).",
    tags="relative why")

gap(R1, "I still remember the day ___ we met.", "when", nivel="B1",
    cue="the day (a time)", forma="when",
    regla="<b>when</b> = an adverb of time in defining clauses. Equivalent to "
          "<i>on which / in which</i>.",
    ejemplos=ex("I remember the day <b>when</b> we met.",
               "That was the year <b>when</b> everything changed."),
    notas="<b>that</b> cannot replace <b>when</b> after a time noun: <i>the day "
          "<s>that</s> we met</i> is WRONG.",
    tags="relative when")

gap(R1, "He failed the exam ___ he worked too hard.", "because", nivel="B2",
    cue="reason", forma="because",
    regla="Relative adverbs of <b>reason</b>: <b>because, since, as</b>. They are "
          "mainly used in <b>non-defining</b> clauses.",
    ejemplos=ex("He failed the exam <b>because</b> he worked too hard.",
               "She was late, <b>as</b> the train was delayed."),
    notas="Also with <b>the reason (that)</b>: <i>The reason (that) he failed is "
          "that he worked too hard.</i>",
    tags="relative reason")

# ============================================================ NON-DEFINING

gap(R2, "My sister, ___ lives in Lima, is a doctor.", "who", nivel="B1",
    cue="with commas = extra information", forma="who",
    regla="A <b>non-defining</b> clause (with commas) adds extra information. It "
          "practically only allows <b>who / which / whose</b> (and <b>where / "
          "when</b> in standard English).",
    ejemplos=ex("My sister, <b>who</b> lives in Lima, is a doctor.",
               "That's a great book, <b>which</b> I read last year."),
    notas="In defining clauses <b>that</b> is used. In non-defining clauses "
          "<b>that</b> is possible in some varieties but <b>who/which</b> is "
          "preferred: <i>My sister, <s>that</s> lives in Lima</i> is unusual in "
          "BrE, normal in informal AmE.",
    tags="relative non-defining")

gap(R2, "I bought a jacket, ___ was very cheap.", "which", nivel="B1",
    cue="the jacket (a thing)", forma="which",
    regla="<b>which</b> for things, always in non-defining clauses.",
    ejemplos=ex("I bought a jacket, <b>which</b> was very cheap.",
               "She plays tennis, <b>which</b> I don't."),
    notas="<b>which</b> can replace a whole <b>clause</b> (a cataphora): "
          "<i>He passed the exam, <b>which</b> surprised me.</i> (which = which fact).",
    tags="relative which cataphora")

gap(R2, "I don't have a car, ___ means I use the bus.", "which", nivel="C1",
    cue="a whole clause", forma="which",
    regla="<b>Cataphora</b>: <b>which</b> stands for an entire clause.",
    ejemplos=ex("She failed the exam, <b>which</b> surprised everyone.",
               "He was rude, <b>which</b> I didn't like."),
    notas="C1: <b>which</b> + comma is a linker (= and therefore). Also "
          "<b>and this is why / and this is how</b>.",
    tags="relative cataphora c1")

gap(R2, "That's the house ___ I grew up.", "where", nivel="B2",
    cue="the house (a place)", forma="where",
    regla="<b>where</b> = in which / at which (place). It can be replaced by "
          "<b>in which</b>.",
    ejemplos=ex("That's the house <b>where</b> I grew up.",
               "The city <b>where</b> I was born is beautiful."),
    notas="In non-defining clauses <b>where</b> is correct in moderate English, "
          "but the safest exam form is <b>which</b> (<i>The city <b>which</b> I "
          "was born in</i>).",
    tags="relative where")

# ==================================================== RELATIVE PRONOUNS

gap(R3, "This is the book ___ I told you about.", "that", nivel="B1",
    cue="replaces 'which'", forma="that",
    regla="<b>that / which / it</b> (informal) can replace the relative pronoun "
          "when it is the object.",
    ejemplos=ex("This is the book <b>that</b> I told you about.",
               "The house <b>that</b> I bought is nice."),
    notas="<b>it</b> is informal and only as an object: <i>The book <b>it</b> I "
          "told you about</i> (non-standard but heard).",
    tags="relative-pronoun")

gap(R3, "The woman ___ car was stolen called the police.", "whose", nivel="B2",
    cue="whose", forma="whose",
    regla="<b>whose</b> = 'whose' (possession). It works with people <b>and</b> things.",
    ejemplos=ex("The woman <b>whose</b> car was stolen called the police.",
               "The man <b>whose</b> son is a doctor."),
    notas="Do not confuse <b>whose</b> (who owns it) with <b>who/that</b> (the "
          "agent): <i>The man <b>whose</b> car was stolen <b>was</b> angry</i> "
          "(his car) vs <i>The man <b>who</b> stole the car <b>was</b> angry</i>.",
    tags="relative whose")

gap(R3, "The man ___ I met yesterday is from Peru.", "whom", nivel="C1",
    cue="whom (formal object)", forma="whom",
    regla="<b>whom</b> = 'whom' (object, formal). <b>who</b> can also be an "
          "object in current usage.",
    ejemplos=ex("The man <b>whom</b> I met is from Peru.",
               "The people <b>whom</b> we help are grateful."),
    notas="<b>Whom</b> is used in formal writing and in questions: "
          "<i>To <b>whom</b> did you speak?</i> (formal) / <i>Who did you speak "
          "to?</i> (normal).",
    tags="relative whom")

# =========================================== RELATIVES WITH ADVERBS

gap(R4, "The project ___ we're working on is nearly done.", "which",
    nivel="C1", cue="the project (with a preposition)", forma="which",
    regla="When the relative takes a <b>preposition</b>, only <b>which</b> is "
          "possible (or <b>who/whom</b> for people). <b>NEVER</b> <b>that</b>.",
    ejemplos=ex("The project <b>which we're working on</b> is done.",
               "The person <b>whom I spoke to</b> was helpful.",
               "<i>The project <s>that</s> we're working <s>on</s></i> is WRONG. "
               "Options: <b>the project we're working on</b> or <b>the project on "
               "which we're working</b> (more formal)."),
    tags="relative preposition")

gap(R4, "She had a reason ___ she didn't tell anyone.", "for which", nivel="C1",
    cue="the reason (with a preposition)", forma="for which",
    regla="With an obligatory preposition, the relative must be <b>which</b>, "
          "<b>who</b> (people) or <b>whom</b>.",
    ejemplos=ex("She had a reason <b>for which</b> she didn't tell anyone (rare).",
               "The tool <b>with which</b> he opened it."),
    notas="More natural: <b>the reason (that)</b>. The form <b>for which</b> is "
          "dated except in very formal registers.",
    tags="relative preposition")

# ====================================================== NOUN CLAUSES

gap(DN, "I'm not sure ___ he will come.", "if/whether", nivel="B2",
    cue="whether", forma="if/whether",
    regla="<b>Noun clauses</b> work as subject, object or complement. "
          "<b>If / whether</b> for 'whether'.",
    ejemplos=ex("I don't know <b>if/whether</b> he will come.",
               "The question <b>is whether</b> we can afford it."),
    notas="<b>Whether</b> = if (doubt, decision). <b>If</b> = if (condition). "
          "Before <b>or not</b> only <b>whether</b>: <i>I don't know <b>whether "
          "or not</b> he agrees.</i>",
    tags="noun-clause")

gap(DN, "The problem ___ is that we don't have time.", "is", nivel="B2",
    cue="the problem is that", forma="is",
    regla="<b>that</b> introduces subject, object and complement clauses. "
          "<b>That</b> can be omitted.",
    ejemplos=ex("I believe <b>that</b> he's honest. / I believe he's honest.",
               "The problem <b>is that</b> we're late."),
    notas="After <b>verbs of opinion</b> (<i>think, believe, say, know, hope, "
          "suggest</i>) <b>that</b> is normally omitted.",
    tags="noun-clause that")

gap(DN, "It surprised me ___ he had already left.", "that", nivel="B2",
    cue="it surprised me that", forma="that",
    regla="<b>It + verb + that + clause</b>.",
    ejemplos=ex("<b>It surprised me that</b> he had left.",
               "<b>It is important that</b> we arrive on time."),
    notas="<b>It</b> is an <b>anticipatory</b> subject: it occupies the subject "
          "position and the clause follows. <b>that</b> is not used in "
          "non-defining clauses.",
    tags="noun-clause that")

gap(DN, "She insisted ___ the bill was wrong.", "that", nivel="C1",
    cue="insisted that", forma="that",
    regla="<b>insist / suggest / demand / recommend + that + clause</b>. With "
          "many of these verbs, <b>should</b> is used in the subjunctive.",
    ejemplos=ex("She <b>insisted that</b> the bill was wrong.",
               "He <b>suggested that</b> we (should) leave early."),
    notas="This is the <b>subjunctive</b> that survives in English: in informal "
          "style it disappears (<i>She insisted the bill was wrong</i>).",
    tags="noun-clause that subjunctive")

# =================================================================== CLOZE

cloze(R3, "The woman {{c1::whose}} car was stolen called the police.",
      extra="<div class='box rule'><span class='lbl'>whose</span>"
            "Indicates <b>possession</b>: whose it is. Works with people and "
            "things.</div>",
      tags="c1-c2 relative cloze")

cloze(R4, "The project {{c1::which}} we're working on is nearly done.",
      extra="<div class='box warn'><span class='lbl'>that + preposition = WRONG</span>"
            "If the relative takes a preposition it can only be <b>which</b> (or "
            "<b>who/whom</b> for people). Never <i>that</i>.</div>",
      tags="c1-c2 relative cloze")
