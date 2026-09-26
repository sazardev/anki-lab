"""03 Past and Perfect (B1-C2) - past simple/continuous, perfect aspect,
past perfect, and the aspect choice that costs the most marks at B1."""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge

D = "03 Past and Perfect::"
DPS, DPC, DP1, DP2, DP3, DEF = D + "Past Simple", D + "Past Continuous", \
    D + "Present Perfect", D + "Perfect Continuous", \
    D + "Past Perfect", D + "Choosing the Aspect"

# ============================================================== PAST SIMPLE

gap(DPS, "I ___ to Rome last summer.", "went", nivel="B1",
    cue="closed past (not repeated)", forma="went",
    regla="<b>Past Simple</b> for completed actions at a definite past moment. "
          "Negatives and questions use <b>didn't / did</b> + base verb.",
    ejemplos=ex("I <b>went</b> to Rome last summer.", "I <b>didn't go</b> to Rome.",
               "<b>Did</b> you <b>go</b>?"),
    notas=ul("Golden rule: <b>did + base verb</b>. The past only appears if "
             "there is NO <i>did / didn't</i>.",
             "Spelling: ends in <b>e</b> → +<b>d</b> (<i>live → lived</i>); "
             "consonant + <b>y</b> → <b>-ied</b> (<i>study → studied, carry → "
             "carried</i>); one-syllable CVC → <b>-ed</b> doubled "
             "(<i>stop → stopped</i>).",
             "<b>Did</b> emphasises the action; the plain past is neutral."),
    tags="past-simple")

gap(DPS, "I ___ my keys. I can't find them anywhere.", "lost", nivel="B1",
    cue="past with a present result", forma="lost",
    regla="<b>Past Simple</b> when the past <b>explains the present</b>.",
    ejemplos=ex("I <b>lost</b> my keys.", "She <b>broke</b> her leg (and that's why she's limping)."),
    notas="If the past <b>still matters</b> or the situation <b>continues</b>, "
          "use the <b>Present Perfect</b>: <i>I <b>have lost</b> my keys (and I "
          "still haven't found them).</i>",
    tags="past-simple result")

gap(DPS, "When ___ you get married?", "did", nivel="B1", cue="when + past",
    forma="did you get",
    regla="Past questions asking <b>when</b> (a fixed point) use the "
          "<b>Past Simple</b>: <b>When did you get married?</b>",
    ejemplos=ex("<b>When did you get married</b>?", "What time <b>did</b> the film <b>start</b>?"),
    notas="<b>What time</b> and <b>when</b> ask for a POINT in the past → "
          "<b>Past Simple</b>. Ask for a duration or period (<i>How long, How "
          "often, this year</i>) → <b>Present Perfect</b>.",
    tags="past-simple questions")

# ========================================================= PAST CONTINUOUS

gap(DPC, "I ___ dinner when the phone rang.", "was having", nivel="B1",
    cue="action in progress, interrupted", forma="was having",
    regla="<b>Past Continuous</b> = <b>was/were + V-ing</b>. Use 1: an action "
          "in progress that another one interrupts (two pasts overlap).",
    ejemplos=ex("I <b>was having</b> dinner when the phone <b>rang</b>.",
               "I <b>was studying</b> when they <b>arrived</b>."),
    notas="The verb that <b>interrupts</b> goes in the <b>Past Simple</b>; the "
          "one in progress goes in the <b>Past Continuous</b>.",
    tags="past-continuous interruption")

gap(DPC, "I ___ when the lights went out.", "was reading", nivel="B1",
    cue="background scene", forma="was reading",
    regla="Use 2: <b>background scene</b> while the main action happens. It is "
          "the tense of <b>narrative</b>.",
    ejemplos=ex("It was a beautiful day. People <b>were walking</b> in the "
                "park, children <b>were playing</b>..."),
    notas="In narration and description: <i>The sun <b>was shining</b>, the "
          "birds <b>were singing</b>.</i>",
    tags="past-continuous narrative")

gap(DPC, "She ___ the piano for 20 minutes. Then she got bored.",
    "had been playing", nivel="B2", cue="long duration before an event",
    forma="had been playing",
    regla="If the ongoing action had <b>already been going on for a while</b> "
          "when the event occurred (<b>then, at that moment, when</b>), use the "
          "<b>Past Perfect Continuous</b>: <b>had been + V-ing</b>.",
    ejemplos=ex("She <b>had been playing</b> the piano for 20 minutes when she got bored.",
               "I <b>had been waiting</b> for an hour before he finally arrived."),
    notas="The key difference: <b>was waiting</b> = started waiting a while ago, "
          "that's all. <b>had been waiting for an hour</b> = had been waiting "
          "for one hour when he arrived (it stresses the duration).",
    tags="past-perfect-continuous")

# =========================================================== PRESENT PERFECT

gap(DP1, "I ___ in this company for 15 years.", "have worked", nivel="B1",
    cue="started in the past, still true now", forma="have worked",
    regla="<b>Present Perfect</b> = <b>have/has + participle</b>. With "
          "<b>for + period</b> or <b>since + point</b>: the action started in "
          "the past and <b>continues now</b>.",
    ejemplos=ex("I <b>have worked</b> here <b>for</b> 15 years.",
               "I <b>have worked</b> here <b>since</b> 2010.",
               "She <b>has been</b> married <b>since</b> 2015."),
    notas=ul("<b>for</b> + duration (<i>for three years, for a long time, for "
             "ages</i>). <b>since</b> + starting point (<i>since Monday, since "
             "2010, since I was a child, since we met</i>).",
             "Also in negatives and questions: <i>I <b>haven't seen</b> him "
             "<b>since</b> March.</i>",
             "Also with <i>this week / this month / today / this year</i>: "
             "<i>I <b>have seen</b> her three times <b>this week</b>.</i>"),
    tags="present-perfect for-since")

gap(DP1, "I ___ him since we were at university.", "haven't seen", nivel="B1",
    cue="negative + since", forma="haven't seen",
    regla="Negative <b>Present Perfect</b>: <b>haven't / hasn't + participle</b>. "
          "It works exactly like the affirmative.",
    ejemplos=ex("I <b>haven't seen</b> him <b>since</b> we were at university.",
               "She <b>hasn't finished</b> yet.", "<b>Have</b> you <b>ever been</b> to Japan?"),
    notas="Markers exclusive to the Perfect: <b>ever, never, just, already, "
          "yet, so far, recently, lately, since, for, this..., how long</b>.",
    tags="present-perfect negative")

gap(DP1, "___ you ever ___ Japan?", "Have, been", nivel="B1", cue="ever",
    forma="Have, been",
    regla="<b>Have + subject + ever + participle?</b>",
    ejemplos=ex("<b>Have</b> you ever <b>been</b> to Japan?",
               "<b>Have</b> you <b>finished</b> yet?"),
    notas="<b>ever</b> in questions and negatives; <b>never</b> = <i>have + "
          "participle + never</i>, but the natural order is <i>I have <b>never</b> "
          "been</i>.",
    tags="present-perfect ever")

gap(DP1, "He has ___ finished. Let's go now.", "already", nivel="B1",
    cue="sooner than expected", forma="already",
    regla="<b>Already</b> = sooner than expected. With a positive "
          "<b>Present Perfect</b> and in <b>not...yet</b> structures.",
    ejemplos=ex("He has <b>already</b> finished.", "I <b>haven't</b> eaten <b>yet</b>."),
    notas="Position: <b>already</b> goes right before the participle: "
          "<i>He has <b>already</b> left.</i>",
    tags="already yet markers")

gap(DP1, "I ___ my passport. I need to renew it.", "have lost", nivel="B1",
    cue="past with a present consequence", forma="have lost",
    regla="If the past <b>connects with the present</b> and you <b>do not "
          "mention the time</b>, use the <b>Present Perfect</b>.",
    ejemplos=ex("I <b>have lost</b> my passport.", "<b>She's broken</b> her arm (hence the cast)."),
    notas="If you say <b>WHEN</b> (<i>when, yesterday, last year, in 2020, at "
          "5pm</i>) → <b>Past Simple</b>: <i>I <b>lost</b> my passport "
          "<b>yesterday</b>.</i>",
    tags="present-perfect vs past-simple")

# ======================================================= PERFECT CONTINUOUS

gap(DP2, "I've been waiting ___ 40 minutes!", "for", nivel="B2",
    cue="emphatic duration", forma="for 40 minutes",
    regla="<b>Present Perfect Continuous</b> = <b>have/has been + V-ing</b>. It "
          "emphasises the <b>duration</b> and the <b>relevance now</b>.",
    ejemplos=ex("I've <b>been waiting for</b> 40 minutes!",
               "It's <b>been raining since</b> this morning.",
               "She's <b>been working</b> here <b>for</b> ten years."),
    notas=ul("<b>since + point</b> / <b>for + duration</b> belong here, not in "
             "the Perfect Simple (<i>I've waited <s>for</s> 40 minutes</i> → "
             "better: <i>I've <b>been waiting for</b> 40 minutes</i>).",
             "Used to say the activity is still going on, or to complain.",
             "<b>How long have you been working here?</b> — this question only "
             "accepts the Perfect Continuous."),
    tags="perfect-continuous duration")

gap(DP2, "How long ___ you ___ here?", "have, been living", nivel="B2",
    cue="how long", forma="have, been living",
    regla="<b>How long + have/has + subject + been + V-ing?</b>",
    ejemplos=ex("<b>How long have you been living</b> here?",
               "<b>How long has</b> he <b>been studying</b>?"),
    notas="Answer: <i>I've <b>been living here for ten years</b>.</i>",
    tags="perfect-continuous how-long")

gap(DP2, "I ___ my car. It's full of keys.", "have been looking for",
    nivel="B2", cue="recent activity with a result", forma="have been looking for",
    regla="The Perfect Continuous is used when an activity <b>recently "
          "started or intensified</b> and the <b>result is now</b>.",
    ejemplos=ex("I've <b>been looking for</b> my keys — they're in your bag.",
               "Prices <b>have been rising</b> all year."),
    notas="Subtle difference: <i>I <b>have looked for</b> it</i> (I have "
          "searched, a complete search) vs <i>I've <b>been looking for</b> "
          "it</i> (I have been searching for a while, no result).",
    tags="perfect-continuous result")

# ============================================================ PAST PERFECT

gap(DP3, "By the time I arrived, the film ___.", "had already started",
    nivel="B2", cue="the earlier of two past actions",
    forma="had already started",
    regla="<b>Past Perfect</b> = <b>had + participle</b>. Marks the <b>earlier</b> "
          "of two past actions. With <b>by the time, by 2020, already, before, "
          "after, when</b>.",
    ejemplos=ex("By the time I arrived, the film <b>had already started</b>.",
               "She realised she <b>had left</b> her keys at home."),
    notas=ul("In spoken English the Perfect is often dropped when the order is "
             "obvious: <i>When I arrived, the film <b>started</b></i>.",
             "<b>before / after</b> + clause: <i>After I had dinner, I called "
             "her.</i>",
             "With <b>the first time, the last time, the second time</b> the "
             "Perfect Simple is often used: <i>It was the first time I <b>saw</b> "
             "her.</i>"),
    tags="past-perfect")

gap(DP3, "She was angry because he ___ her.", "had forgotten", nivel="B2",
    cue="reason for a past event", forma="had forgotten",
    regla="The <b>Past Perfect</b> explains <b>why</b> something happened in "
          "the past.",
    ejemplos=ex("She was angry because he <b>had forgotten</b> the meeting.",
               "I couldn't open the door because I <b>had lost</b> my keys."),
    notas="Key B2 structure: <b>past + because + Past Perfect</b>.",
    tags="past-perfect cause")

# =================================================== CHOOSING THE ASPECT

gap(DEF, "I ___ here ___ 2019. I know her very well.", "have lived, since",
    nivel="B1", cue="since 2019, still true", forma="have lived, since",
    regla="<b>Since + point / For + duration</b> with the situation <b>still "
          "holding</b> → <b>Present Perfect</b>.",
    ejemplos=ex("I <b>have lived here since 2019</b> (still here).",
               "I <b>lived there for three years</b> and then I moved (not any more)."),
    notas="This is THE aspect distinction that earns marks at B2. If the "
          "situation <b>continues</b> → Perfect. If it <b>ended</b> → Simple.",
    tags="aspect for-since")

gap(DEF, "I ___ to Paris three times ___ 2019.", "have been, in", nivel="B1",
    cue="three times since 2019", forma="have been, in",
    regla="<b>Experience with no time reference</b> → <b>Present Perfect</b> + "
          "<b>times</b>.",
    ejemplos=ex("I've <b>been to</b> Paris <b>three times</b>.",
               "I <b>went to</b> Paris <b>three times</b> <b>in 2019</b>."),
    notas="Key: if you give the year or period (<i>in 2019, last year, in June</i>) "
          "→ <b>Past Simple</b>. If it is <i>this week, this year, so far</i> or "
          "unspecified → <b>Present Perfect</b>.",
    tags="aspect frequency")

gap(DEF, "I ___ here ___ 2019, but now I live in Berlin.", "lived, since",
    nivel="B1", cue="no longer lives here", forma="lived, since",
    regla="If the period is <b>already over</b>, use the <b>Past Simple</b>, even "
          "with <b>for/since</b>.",
    ejemplos=ex("I <b>lived here for 5 years</b> and then I moved.",
               "She <b>had lived in Madrid</b> before moving to Paris."),
    notas="<b>For/since</b> do NOT force the Perfect. What decides is whether "
          "the situation <b>still holds</b>.",
    tags="aspect for-since")

gap(DEF, "When ___ you ___ the news?", "did, hear", nivel="B1",
    cue="when (a fixed moment)", forma="did, hear",
    regla="<b>When</b> asks for an exact moment → <b>Past Simple</b>.",
    ejemplos=ex("<b>When did you hear</b> the news?",
               "<b>When have you heard</b> from her?"),
    notas="Exam question: if the answer is <i>last Tuesday</i> → <b>did ... hear</b>. "
          "If the answer is <i>two days ago</i> → <b>have ... heard</b>.",
    tags="aspect questions")

gap(DEF, "She's been a doctor ___ 2005.", "for", nivel="B1",
    cue="since 2005, still a doctor", forma="for 2005",
    regla="<b>Present Perfect</b> when the situation <b>is still true now</b>.",
    ejemplos=ex("She's <b>been</b> a doctor <b>for/since 2005</b>.",
               "She <b>was</b> a doctor for 10 years (not any more)."),
    notas="<b>She's been a doctor since 2005</b> (still is) vs <b>She was a "
          "doctor for 10 years</b> (no longer is).",
    tags="aspect state")

gap(DEF, "I've known her ___ 2015 and we still talk every day.", "since",
    nivel="B1", cue="since 2015, still going", forma="since 2015",
    regla="<b>Present Perfect</b> + <b>still</b> = the situation continues.",
    ejemplos=ex("I've <b>known</b> her <b>since 2015</b> and we <b>still</b> talk every day.",
               "He <b>has worked</b> here <b>for</b> 20 years <b>and he's still</b> there."),
    notas="<b>Still</b> with the Perfect indicates continuity. With the Past "
          "Simple: <i>He worked here for 20 years <b>and he left</b> last year.</i>",
    tags="aspect still")

# ============================================================= MASTER TABLE

tabla(DEF, ["Situation", "Tense", "Example"],
     [["A definite past moment", "<b>Past Simple</b>",
       "<i>I <b>lost</b> my keys yesterday.</i>"],
      ["A period that has <b>ended</b>", "<b>Past Simple</b> + for/since",
       "<i>I <b>lived</b> in Rome <b>for</b> 3 years.</i>"],
      ["Happening <b>now</b>", "<b>Past Continuous</b>",
       "<i>I <b>was having</b> dinner at 8.</i>"],
      ["Started in the past, <b>still true now</b>", "<b>Present Perfect</b>",
       "<i>I <b>have worked</b> here <b>for</b> 15 years.</i>"],
      ["Past with a <b>present result</b>", "<b>Present Perfect</b>",
       "<i>I <b>have lost</b> my keys.</i>"],
      ["Emphasises the <b>duration</b>", "<b>Perfect Continuous</b>",
       "<i>I've <b>been working</b> here <b>for</b> 15 years.</i>"],
      ["The <b>earlier</b> of two past actions", "<b>Past Perfect</b>",
       "<i>When I arrived, it <b>had started</b>.</i>"],
      ["Life experience, <b>no time given</b>", "<b>Present Perfect</b>",
       "<i>I've <b>been</b> to Japan <b>twice</b>.</i>"],
      ["With a <b>concrete time</b>", "<b>Past Simple</b>",
       "<i>I <b>went</b> to Japan <b>in 2019</b>.</i>"]],
     titulo="Master table: which tense for which situation",
     nivel="B2",
     nota="This table is <b>90% of the marks</b> in any B2 exam on verb tenses. "
          "If you know it by heart, you will stop making this error.")

# =================================================================== CLOZE

cloze(DP1, "I {{c1::have}} been here {{c2::since}} 2019.",
      extra="<div class='box rule'><span class='lbl'>for vs since</span>"
            "<b>for</b> + duration (for 5 years, for ages). <b>since</b> + "
            "starting point (since 2019, since Monday, since I met her).</div>",
      tags="c1-c2 for-since cloze")

cloze(DP1, "I've {{c1::already}} seen it. / I {{c1::haven't}} seen it {{c2::yet}}.",
      extra="<div class='box note'><span class='lbl'>Perfect markers</span>"
            "<b>already, yet, ever, never, just, so far, recently, lately</b> "
            "→ <b>Present Perfect</b> only.</div>",
      tags="c1-c2 markers cloze")

cloze(DP3, "By the time we arrived, the film {{c1::had already started}}.",
      extra="<div class='box rule'><span class='lbl'>Past Perfect</span>"
            "<b>had + participle</b> for the earlier past action. With "
            "<b>by the time, by + year, before, after, already</b>.</div>",
      tags="c1-c2 past-perfect cloze")
