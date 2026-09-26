"""23 Exam Traps - the errors that cost the most marks in B2 and C1 exams."""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "23 Exam Traps::"
T = D + "The Errors That Cost the Most Marks"

serie_gap(T, [
    ("I've lived here ___ 2015.", "since", "since 2015",
     "<b>Since</b> + a point, <b>for</b> + a duration. This is error #1 at B2.",
     ex("I've lived here <b>since</b> 2015. / <s>since five years</s> is WRONG → "
        "<b>for</b> five years.")),
    ("If I ___ more time, I'd travel.", "had", "had more time",
     "The <b>second conditional</b> in the negative and with <b>wish</b> uses the "
     "<b>past simple</b> (or <b>were</b>). NEVER <i>will</i>.",
     ex("If I <b>had</b> more time, I'd travel. / "
        "<s>If I will have more time</s> is WRONG. / "
        "<s>If I had more time, I will travel</s> is WRONG.")),
    ("I'd rather you ___ smoke here.", "didn't", "didn't smoke",
     "<b>Would rather + subject + Past Simple</b> for the past. "
     "<b>Would rather + base</b> for yourself.",
     ex("I'd <b>rather you didn't smoke</b> here. / <s>I'd rather you not to "
        "smoke</s> is WRONG / <s>I'd rather you don't</s> is WRONG.")),
    ("The report needs ___ before Friday.", "to be checked", "to be checked",
     "<b>need / must / should + be + V3</b> for the passive. Also "
     "<b>needs checking</b> (without <i>to be</i>).",
     ex("The report needs <b>to be checked</b>. / <b>The report needs "
        "checking</b>. / <b>must be checked</b> / <b>should be signed</b>")),
    ("I'm looking forward ___ the results.", "to", "to the results",
     "<b>look forward to + V-ing</b>. The <b>to</b> is a preposition. "
     "<b>be looking forward to hearing from you</b>.",
     ex("I'm looking forward <b>to hearing</b> the results. / <s>to hear</s> is "
        "WRONG. / <s>I look forward to see you</s> is WRONG.")),
    ("She suggested ___ the meeting.", "postponing", "postponing",
     "<b>suggest / recommend / advise / propose / insist + V-ing</b> or "
     "<b>+ that + clause</b>. Never <b>to</b>.",
     ex("She suggested <b>postponing</b> the meeting. / <s>She suggested to "
        "postpone</s> is WRONG. / She suggested that we (should) postpone it.")),
    ("___ he is rich, he isn't happy.", "Although", "although",
     "<b>Although / though / even though + clause</b>. "
     "<b>Despite / in spite of + -ing / noun</b>.",
     ex("<b>Although</b> he is rich, he isn't happy. / <s>Despite he is rich</s> "
        "is WRONG → <b>Despite his wealth</b> / <b>Despite being rich</b>.")),
    ("There ___ been a lot of changes.", "has", "there has been",
     "<b>There has been</b> (singular) when the real subject is 'change' or the "
     "fact itself. NEVER <i>there have been changes</i> with that meaning.",
     ex("There <b>has been</b> a lot of change. / <b>There have been</b> changes "
        "(concrete changes). / <b>There is</b> a problem / <b>There are</b> problems.")),
    ("Neither of the answers ___ correct.", "is", "is",
     "<b>Neither of / either of / none of + of</b> → singular verb (BrE) or plural "
     "(AmE). In an exam: singular.",
     ex("Neither of the answers <b>is</b> correct. / <b>Neither of them is</b> "
        "(singular) / in AmE <b>are</b> is also heard.")),
    ("The number of students ___ increasing.", "is", "is increasing",
     "<b>The number of + plural</b> → singular verb. "
     "<b>A number of + plural</b> → plural verb.",
     ex("The number of students <b>is</b> increasing. / <b>A number of</b> "
        "students <b>are</b> absent. (several)")),
    ("She's the only person who ___ the answer.", "knows", "knows",
     "A <b>non-defining</b> clause with <b>who</b> takes a plural verb if "
     "<b>who</b> is plural. With <b>the only one who + singular</b> it is singular.",
     ex("She's the only person who <b>knows</b> the answer. / <b>the only one who "
        "knows</b> (singular) / <b>the people who know</b> (plural).")),
    ("He was arrested and charged ___ murder.", "with", "charged with",
     "<b>charged with</b> = accused of a crime. <b>accused of</b> = accused of. "
     "<b>blamed for</b> = blamed for.",
     ex("He was charged <b>with</b> murder. / <b>charged with</b> (a crime) / "
        "<b>accused of</b> / <b>blamed for</b>")),
    ("I can't afford ___ a new car.", "to buy", "to buy",
     "<b>can't afford + to + base</b> or <b>can't afford + noun</b>. NEVER "
     "<i>can't afford buying</i>.",
     ex("I can't afford <b>to buy</b> a new car. / <b>can't afford a car</b> / "
        "<s>can't afford buying</s> is WRONG.")),
    ("___ matters is that we don't have time.", "What", "what matters is",
     "<b>What + clause</b> = 'what'. Mind the punctuation: <b>What matters is</b> "
     "(no comma).",
     ex("<b>What matters is</b> that we don't have time. / <b>What you need</b> is "
        "a wh-cleft with no comma. / <s>What, matters is</s> is WRONG.")),
    ("She's good ___ children.", "with", "good with",
     "<b>good with</b> (people) vs <b>good at</b> (skills). This error is worth "
     "marks in every exam.",
     ex("She's good <b>with</b> children. / <b>good at maths</b> / "
        "<b>good with kids</b> / <b>good at speaking</b>")),
    ("I only found out ___ .", "yesterday", "yesterday",
     "Time adverbs at the <b>end</b> of the clause: <b>yesterday, today, "
     "tomorrow, tonight, last night, next week, last year</b>.",
     ex("I only found out <b>yesterday</b>. / <b>last night</b> (not <i>yesterday "
        "night</i>). / <b>the other day</b> = the other day.")),
    ("___ enough time, we'd have helped.", "Had we had", "had we had",
     "The <b>third conditional</b> can be inverted by fronting the auxiliary: "
     "<b>Had we had enough time…</b> (C1, elegant).",
     ex("<b>Had we had</b> enough time, we'd have helped. / If the clause is "
        "fronted, <b>if</b> disappears and the auxiliary moves: <i><b>Were I</b> "
        "you... / <b>Should you need</b>...</i>")),
    ("It's ___ that we don't have enough staff.", "clear", "it's clear that",
     "<b>It is + adj + that + clause</b>: <b>clear, obvious, essential, vital, "
     "important, likely, possible, surprising, unlikely</b>. With <b>for</b>: "
     "<b>It is difficult for someone TO…</b>.",
     ex("It's <b>clear that</b> we don't have enough staff. / "
        "«It is <b>clear for</b> we...» is WRONG. / "
        "«It's <b>difficult for me to</b> concentrate» (with <b>for</b>).")),
    ("She's the tallest woman ___ has ever won the prize.", "to",
     "to have ever",
     "<b>the + superlative + person + to have + participle</b> = the most ... "
     "that. A very typical B2 error.",
     ex("She's the tallest woman <b>to have</b> ever won the prize. / "
        "<s>the tallest woman who has ever won</s> is grammatical but less "
        "precise; <i>the tallest woman TO have won</i> is better.")),
    ("How much ___ it cost?", "does", "does it cost",
     "Indirect questions: no inversion, statement word order. "
     "<b>How much does it cost? / Could you tell me how much it costs?</b>",
     ex("How much <b>does</b> it cost? / Could you tell me how much it costs? / "
        "<s>How much costs it</s> is WRONG (only valid with <b>be</b>: "
        "<i>How much is it?</i>).")),
    ("I'd prefer ___ the plane to the train.", "taking", "taking",
     "<b>prefer / would prefer + V-ing / to + base</b>. NEVER <b>to + V</b> "
     "after <b>prefer</b> (but YES with <b>prefer A to B</b>!).",
     ex("I'd prefer <b>taking</b> the plane to the train. / "
        "<b>prefer A to B</b> (this one does take to) / <s>prefer taking to "
        "take</s> is WRONG")),
    ("The police ___ arrived yet.", "haven't", "haven't arrived yet",
     "In the present with <b>yet</b> you use the <b>Present Perfect</b> "
     "(<b>haven't arrived yet</b>). NEVER <i>haven't arrived already</i>.",
     ex("The police <b>haven't arrived yet</b>. / <b>already</b> goes with a "
        "positive perfect: <b>have already arrived</b>. <b>yet</b> goes with a "
        "negative or a question.")),
    ("There's no point ___ about it.", "in arguing", "in arguing",
     "<b>There is no point in + V-ing</b>. <b>There's no point <b>to</b> argue</b> "
     "is WRONG.",
     ex("There's no point <b>in arguing</b> about it. / <b>What's the point of</b> "
        "arguing? = what's the point of arguing?")),
    ("She's used to ___ in a big city.", "living", "living",
     "<b>be used to + noun / V-ing</b> = be used to. <b>used to + base</b> = "
     "used to. Never confuse them.",
     ex("She's used to <b>living</b> in a big city. / <b>used to live</b> = used "
        "to live / <s>She's used to live</s> is WRONG.")),
    ("I'd rather you ___ the offer.", "accepted", "accepted",
     "<b>would rather + past simple</b> for inferences about someone else's past. "
     "<b>would rather not + base</b> for yourself.",
     ex("I'd <b>rather you accepted</b> the offer. / «Would rather <b>to</b> "
        "accept» is WRONG. / «I'd <b>rather not go</b>» is correct, not «to go».")),
    ("The more I practise, ___ I get.", "the better", "the better",
     "<b>The + comparative, the + comparative</b>. NEVER <b>more better</b>.",
     ex("The more I practise, <b>the better</b> I get. / <b>The more</b>…, "
        "<b>the more</b>… / <b>The less</b>…, <b>the less</b>… / "
        "<s>more better</s> is WRONG.")),
    ("He apologised ___ breaking the promise.", "for", "for",
     "<b>apologise for + V-ing / noun</b>. <b>apologise to someone</b> (to a person).",
     ex("He apologised <b>for breaking</b> the promise. / <b>apologise to</b> + "
        "person / <b>apologise for</b> + thing.")),
    ("___ you have any questions, please let me know.", "Should",
     "should you have",
     "<b>Should + subject + base</b> = in case (formal inversion). C1 and very "
     "common in papers.",
     ex("<b>Should</b> you have any questions, please let me know. / In informal "
        "English no (i.e. <i>in case you have</i>). In papers, journals and "
        "presentations: yes.")),
], nivel="C1", tags=["exam-trap"])

cloze(T, "I'm looking forward to {{c1::hearing}} from you.",
      extra="<div class='box warn'><span class='lbl'>Trap #1</span>"
            "<b>to</b> is a PREPOSITION → always <b>-ing</b>. "
            "<i>to hear</i> is an error in any exam.</div>",
      tags="c1-c2 trap cloze")
