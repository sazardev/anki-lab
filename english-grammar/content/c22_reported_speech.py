"""22 Reported Speech (B1-C2) - rules, pronouns, tenses, questions, backshift
and conditionals."""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "22 Reported Speech::"
R1, R2, R3 = D + "Basic Rules", D + "Pronouns and Tenses", \
    D + "Questions and Backshift"

# ============================================================ BASIC RULES

serie_gap(R1, [
    ("'I am tired', she said. → She said she ___ tired.", "was", "was",
     "In reported speech <b>presents and past simple</b> shift to the "
     "<b>past</b> (<i>backshift</i>).",
     ex("«I am tired», she said. → She said she <b>was</b> tired. / "
        "«I live here» → He said he <b>lived</b> here. / "
        "«I have a car» → He said he <b>had</b> a car.")),
    ("'I will call you', he said. → He said he ___ call me.", "would",
     "he would call me",
     "<b>will</b> → <b>would</b>. <b>am/is/are</b> → <b>was/were</b>. "
     "<b>can</b> → <b>could</b>. <b>may</b> → <b>might</b>.",
     ex("«I will call you» → He said he <b>would</b> call me. / "
        "«I can swim» → He said he <b>could</b> swim. / "
        "«She may come» → She said she <b>might</b> come.")),
    ("'Where are you going?' → He asked where I ___ going.", "was", "was",
     "In reported <b>questions</b> the statement word order is kept and the "
     "question mark disappears.",
     ex("«Where are you going?» → He asked where I <b>was</b> going. / "
        "«What time does it start?» → She asked what time <b>it started</b>.")),
    ("'Let's go now', he said. → He suggested ___ now.", "going", "going",
     "«Let's + base» → <b>suggested + V-ing</b> or <b>suggested that we should + "
     "base</b>.",
     ex("«Let's go now» → He suggested <b>going</b> now. / "
        "<s>He suggested to go</s> is WRONG.")),
    ("'Don't touch it!', she said. → She told me ___ touch it.", "not to",
     "not to touch",
     "«Don't + base» → <b>told/asked someone not to + base</b>.",
     ex("«Don't touch it!» → She told me <b>not to touch</b> it. / "
        "«Don't be late» → He warned me <b>not to be</b> late.")),
    ("'I have finished', she said. → She said she ___ finished.", "had",
     "had finished",
     "<b>Present Perfect</b> → <b>Past Perfect</b>.",
     ex("«I have finished» → She said she <b>had</b> finished. / "
        "«I have been here since 9» → She said she <b>had been</b> there since 9.")),
    ("'I'm going to visit my aunt', he said. → He said he ___ visit his aunt.",
     "was going to", "was going to",
     "<b>Futures</b> also shift: <b>will → would</b>, <b>going to → was going "
     "to</b>, <b>Present Continuous → was -ing</b>.",
     ex("«I'm going to visit my aunt» → He said he <b>was going to</b> visit his "
        "aunt. / «I'm seeing her tonight» → He said he <b>was seeing</b> her "
        "that night.")),
], nivel="B2", tags=["reported-speech"])

# ================================================ PRONOUNS AND TENSES

serie_gap(R2, [
    ("'I saw him yesterday', she said. → She said she ___ him the day before.",
     "had seen", "had seen him",
     "The backshift of <b>yesterday</b> is <b>the day before</b>. <b>Today</b> → "
     "<b>that day</b>. <b>Tomorrow</b> → <b>the next day</b>. <b>Last week</b> → "
     "<b>the previous week</b>. <b>Next year</b> → <b>the following year</b>.",
     ex("«I saw him yesterday» → She said she <b>had seen</b> him <b>the day "
        "before</b>. / «today» → <b>that day</b> / «tomorrow» → <b>the next "
        "day</b> / «here» → <b>there</b>")),
    ("'I can see you from here', he said. → He said he could see me ___ .",
     "there", "there",
     "<b>Deictics</b> change point of view: <b>here → there</b>, <b>this → "
     "that</b>, <b>these → those</b>, <b>now → then</b>, <b>today → that day</b>, "
     "<b>tonight → that night</b>.",
     ex("«I can see you from here» → He said he could see me <b>there</b>. / "
        "«this book» → <b>that book</b> / «these books» → <b>those books</b>")),
    ("'I don't have time', she said. → She said she ___ have time.", "didn't",
     "didn't have",
     "<b>Negatives</b>: <b>don't/doesn't/didn't</b> stay + base verb. "
     "<b>Auxiliaries</b> are not duplicated.",
     ex("«I don't have time» → She said she <b>didn't have</b> time. / "
        "<s>She said she doesn't have time</s> is WRONG / "
        "<s>She said she hadn't have time</s> is WRONG")),
    ("'I didn't go', he said. → He said he ___ gone.", "hadn't", "hadn't gone",
     "<b>didn't + base</b> → <b>hadn't + participle</b>.",
     ex("«I didn't go» → He said he <b>hadn't gone</b>. / "
        "«She didn't come» → He said she <b>hadn't come</b>.")),
    ("'If I had time, I'd travel', she said. → She said if she ___ time, she "
     "___ travel.", "had, would", "had time, would travel",
     "<b>Conditionals</b> stay: type 2 (<i>if + were, would</i>) and type 3 "
     "(<i>if + had, would have</i>). <b>Would</b> never changes.",
     ex("«If I had time, I'd travel» → She said if she <b>had</b> time, she "
        "<b>would</b> travel. / «If I had known, I would have told you» → She "
        "said if she <b>had known</b>, she <b>would have told</b> me.")),
], nivel="C1", tags=["reported-speech backshift"])

# ============================================ QUESTIONS AND EXPRESSIONS

serie_gap(R3, [
    ("'Will you help me?' → He asked if I ___ help him.", "would", "would help",
     "Yes/no questions → <b>if / whether</b> + statement word order. "
     "<b>Wh-</b> questions keep the <b>Wh-</b>.",
     ex("«Will you help me?» → He asked <b>if I would</b> help him. / "
        "«Where do you live?» → She asked <b>where I lived</b>.")),
    ("'Are you coming?' → She asked ___ I was coming.", "if/whether", "if/whether",
     "Questions with a <b>preposition</b> in the original: the preposition moves "
     "in front of the <b>Wh-</b>.",
     ex("«What are you waiting for?» → She asked <b>what I was waiting for</b>. / "
        "«Who did you talk to?» → He asked <b>who I had talked to</b> / "
        "<b>to whom I had talked</b> (formal).")),
    ("'I would like a coffee', he said. → He said he ___ like a coffee.",
     "would", "would like",
     "<b>would like</b> is a <b>fixed phrase</b>: no backshift.",
     ex("«I would like a coffee» → He said he <b>would like</b> a coffee. / "
        "«Could I help?» stays <b>could</b> (= could).")),
    ("'What a pity!', she said. → She said ___ .", "it was a pity",
     "it was a pity",
     "Exclamations and <b>modals</b> in reported speech: <b>must → had to, "
     "should → should/ought to, might → might, ought to → should</b>.",
     ex("«What a pity» → She said <b>it was a pity</b>. / «He must be tired» → "
        "She said he <b>must</b> be tired. / «must leave» → He said he <b>had to</b> "
        "leave.")),
    ("'Thank you', he said. → He ___ me.", "thanked", "thanked",
     "Fixed expressions that become verbs: <b>Thank you → thank, Goodbye → say "
     "goodbye, Sorry → apologise, Congratulations → congratulate, Happy birthday → "
     "wish</b>.",
     ex("«Thank you» → He <b>thanked</b> me. / «Congratulations!» → She "
        "<b>congratulated</b> me. / «Happy birthday!» → She <b>wished me a happy "
        "birthday</b>.")),
], nivel="C1", tags=["reported-speech questions"])

tabla(R1, ["Direct (present)", "Reported (past)", "Direct (past)",
           "Reported (past)"],
     [["I <b>am</b>", "he said he <b>was</b>", "I <b>was</b>",
       "he said he <b>had been</b>"],
      ["I <b>have</b>", "he said he <b>had</b>", "I <b>had</b>",
       "he said he <b>had had</b>"],
      ["I <b>do</b>", "he said he <b>did</b>", "I <b>did</b>",
       "he said he <b>had done</b>"],
      ["I <b>will</b>", "he said he <b>would</b>", "I <b>would</b>",
       "he said he <b>would</b> (no change)"],
      ["I <b>can</b>", "he said he <b>could</b>", "I <b>could</b>",
       "he said he <b>could</b> (no change)"],
      ["I <b>may</b>", "he said he <b>might</b>", "I <b>might</b>",
       "he said he <b>might</b> (no change)"],
      ["I <b>must</b> (obligation)", "he said he <b>had to</b>", "I <b>had to</b>",
       "he said he <b>had to</b> (no change)"],
      ["I <b>must</b> (deduction)", "he said he <b>must</b>", "I <b>must</b>",
       "he said he <b>must</b> (no change)"],
      ["I <b>am going to</b>", "he said he <b>was going to</b>",
       "I <b>was going to</b>", "he said he <b>was going to</b>"],
      ["I <b>am</b> doing", "he said he <b>was</b> doing", "I <b>was</b> doing",
       "he said he <b>was</b> doing"]],
     titulo="Backshift: the table to memorise",
     nivel="B2",
     nota=ul("<b>No change</b>: <b>would, could, should, might, had better, "
             "ought, used to</b> (the <i>used to</i> meaning 'as a habit').",
             "<b>Conditionals never change</b>: <i>if I were → if I were</i>; "
             "<i>if I had → if I had</i>.",
             "<b>Careful with must</b>: obligation → <b>had to</b>; deduction → "
             "<b>must</b> stays.",
             "<b>Spoken</b>, backshift is often NOT applied: natives say <i>She "
             "said she <b>is</b> coming</i> all the time. It is correct, but in "
             "a written exam USE the past."))
cloze(R1, "«I <b>am</b> tired», she said. → She said she {{c1::was}} tired.",
      extra="<div class='box rule'><span class='lbl'>Backshift</span>"
            "<b>am/is/are</b> → <b>was/were</b> · <b>will</b> → <b>would</b> · "
            "<b>can</b> → <b>could</b> · <b>have + V3</b> → <b>had + V3</b> · "
            "<b>didn't + V</b> → <b>hadn't + V3</b>.</div>",
      tags="c1-c2 reported-speech cloze")
