"""06 Conditionals (B1-C2) - the four types, mixed conditionals, and
wish / if only."""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge

D = "06 Conditionals::"
D0, D1, D2, D3, DM = D + "Zero and Certainty", D + "First Conditional", \
    D + "Second Conditional", D + "Third Conditional", D + "Mixed and Wish"

# ================================================== ZERO / CERTAINTY

gap(D0, "Water ___ (freeze) at 0°C.", "freezes", nivel="B1",
    cue="always true", forma="freezes",
    regla="<b>Zero conditional</b> = <b>if + present, present</b>. For general "
          "truths, laws, habits and generalisations.",
    ejemplos=ex("If you <b>heat</b> ice, it <b>melts</b>.",
               "If I <b>don't sleep</b>, I <b>feel</b> tired (habit)."),
    notas=ul("Type 0: <b>if + present simple</b>, <b>present simple</b>. No "
             "<b>will</b>.",
             "With <b>can/could/must</b> instead of the present: <i>If you "
             "<b>can't</b> sleep, take a hot shower.</i>",
             "In the <b>first conditional</b> (likely) there IS a <b>will</b>: "
             "<i>If you heat ice, it <b>will</b> melt.</i>",
             "Never use <i>if</i> with <b>will</b>: <i>If you <b>will</b> "
             "come...</i> is WRONG."),
    tags="zero-conditional")

gap(D0, "If you mix blue and yellow, you ___ (get) green.", "get", nivel="B1",
    cue="inevitable result", forma="get",
    regla="<b>Zero conditional</b>: the condition is true and the result is "
          "always the same.",
    ejemplos=ex("If you mix blue and yellow, you <b>get</b> green.",
               "If he calls, tell him I'm out."),
    notas="This type is badly under-used. In real English it is used a lot for "
          "rules and inevitable consequences.",
    tags="zero-conditional")

# ==================================================== FIRST CONDITIONAL

gap(D1, "If it ___ (rain) tomorrow, we ___ (stay) at home.", "rains, will stay",
    nivel="B1", cue="real and likely", forma="rains, will stay",
    regla="<b>First conditional</b> = <b>if + present, will + base</b>. A "
          "<b>possible</b> situation in the future.",
    ejemplos=ex("If it <b>rains</b>, we <b>will stay</b> at home.",
               "If you <b>lose</b> your keys, I'll <b>help</b> you."),
    notas="Never use <b>will</b> in the result. In the condition, <b>present "
          "simple</b> (never <i>will</i>).",
    tags="first-conditional")

gap(D1, "If you don't hurry, you ___ (miss) the train.", "will miss", nivel="B1",
    cue="likely consequence", forma="will miss",
    regla="<b>First conditional</b> with <b>will</b> in the result.",
    ejemplos=ex("If you don't hurry, you <b>will miss</b> the train.",
               "If she studies, she <b>will pass</b> the exam."),
    notas="<b>Going to</b> or the <b>Present Simple</b> are also possible in the "
          "result, but <b>will</b> is the standard.",
    tags="first-conditional")

# =================================================== SECOND CONDITIONAL

gap(D2, "If I ___ (be) you, I would accept the job.", "were", nivel="B1",
    cue="unreal hypothesis (speaking about you)", forma="were",
    regla="<b>Second conditional</b> = <b>if + were/past simple, would + "
          "base</b>. An <b>improbable or imaginary</b> situation in the present "
          "or future.",
    ejemplos=ex("If I <b>were</b> you, I would accept.",
               "If we <b>lived</b> in Paris, we would love it."),
    notas=ul("After <b>if</b>, <b>were</b> is used for <b>all</b> persons: "
             "<i>If <b>he were</b> here...</i> (BrE). In AmE <i>if he <b>was</b></i> "
             "is also heard.",
             "In most contexts <b>were</b> and <b>past simple</b> are "
             "interchangeable: <i>If I <b>had</b> money...</i> / <i>If I <b>were</b> "
             "rich...</i>",
             "In the negative: <i>If I <b>weren't</b> so busy...</i>"),
    tags="second-conditional")

gap(D2, "If we ___ (travel) more, we would understand other cultures.",
    "travelled", nivel="B1", cue="impossible recommendation", forma="travelled",
    regla="The <b>second conditional</b> is also used to <b>recommend</b> or "
          "<b>suggest</b> things that are not possible.",
    ejemplos=ex("If you <b>read</b> more, you would learn faster.",
               "If she <b>asked</b> him, he'd tell her."),
    notas="It is the tense of impossible advice: <i>You <b>should</b> travel "
          "more</i> (a direct order) vs <i>If you <b>travelled</b> more, "
          "you'd understand more</i> (gentle advice).",
    tags="second-conditional advice")

gap(D2, "I'd help you if I ___ (can).", "could", nivel="B2",
    cue="if I could", forma="could",
    regla="<b>If I could</b> = I would like to be able to. <b>If I had</b> = if "
          "only I had (about quantities, possessions).",
    ejemplos=ex("I'd help you if I <b>could</b>.", "If I <b>had</b> a car, I'd drive you there."),
    notas="Wish structures with <b>if</b> (almost <i>wish</i>): "
          "<b>If I had</b> = I wish I had. <b>If I were</b> = I wish I were. "
          "<b>If I could</b> = I wish I could. <b>If I would</b> = I wish you would.",
    tags="if-had if-could wishes")

# ==================================================== THIRD CONDITIONAL

gap(D3, "If I had studied harder, I ___ (pass) the exam.", "would have passed",
    nivel="B2", cue="unreal past (it did not happen)", forma="would have passed",
    regla="<b>Third conditional</b> = <b>if + had + participle, would have + "
          "participle</b>. About the past: the condition <b>did not happen</b>, "
          "so neither did the result.",
    ejemplos=ex("If I had studied harder, I <b>would have passed</b>.",
               "If you had told me, I <b>would have helped</b>."),
    notas=ul("It is the past of <i>If I were you → I would accept</i>: "
             "<i>If I had been you, I would have accepted</i>.",
             "You can use <b>past perfect</b> instead of <b>would have</b> in "
             "the result: <i>If I had studied, I <b>had passed</b>.</i>",
             "Never <b>would</b> + a bare future: <i>If I had known, I <b>would "
             "do</b></i> is WRONG → <b>would have done</b>."),
    tags="third-conditional")

gap(D3, "If she ___ (not / be) so shy, she would have asked you.",
    "hadn't been", nivel="B2", cue="negative in the unreal past",
    forma="hadn't been",
    regla="<b>hadn't</b> = had not. In the negative result: "
          "<b>wouldn't have + participle</b>.",
    ejemplos=ex("If she <b>hadn't been</b> shy, she would have asked.",
               "If I <b>hadn't drunk</b> so much, I <b>wouldn't have</b> crashed."),
    notas="Contractions: <b>hadn't</b> = had not, <b>wouldn't have</b> = would "
          "not have.",
    tags="third-conditional negative")

# =========================================================== MIXED

gap(DM, "If I had studied medicine, I ___ (work) in a hospital now.",
    "would be working", nivel="C1", cue="past cause, present effect",
    forma="would be working",
    regla="<b>Mixed conditionals</b>: when the cause is <b>past</b> and the "
          "effect is <b>present</b> (or vice versa).",
    ejemplos=ex("If I had studied medicine, I <b>would be working</b> in a hospital now.",
               "If you come tomorrow, I <b>will be</b> free."),
    notas=ul("Rule: the tense of each part depends on <b>WHEN</b> you place the "
             "consequence.",
             "Past cause + present effect: <b>if + had + participle</b> → "
             "<b>would + verb / continuous</b>.",
             "Present cause + past effect: <b>if + present</b> → <b>would have + "
             "participle</b>: <i>If you <b>are</b> more careful, you <b>would "
             "have passed</b>.</i>",
             "With <b>wish</b>: <i>I wish I <b>hadn't said</b> that</i> = "
             "If I hadn't said that (contrary to fact)."),
    tags="mixed-conditionals")

gap(DM, "If I hadn't met her, I ___ (not / be) here now.", "wouldn't be",
    nivel="C1", cue="unreal past, real present", forma="wouldn't be",
    regla="<b>Mixed</b>: <b>if + had + participle</b> (past) → <b>would + "
          "verb</b> (present).",
    ejemplos=ex("If I hadn't met her, I <b>wouldn't be</b> here now.",
               "If she hadn't helped me, I <b>wouldn't have</b> finished."),
    notas="<b>would not / wouldn't + base</b> for the present; <b>would not "
          "have / wouldn't have + participle</b> for the past.",
    tags="mixed-conditionals")

# ============================================================== REFERENCE

tabla(D0, ["Type", "Meaning", "Structure", "Example"],
     [["<b>0</b> (zero)", "General truth / always true",
       "<b>if</b> + present, present", "<i>If you heat ice, it <b>melts</b>.</i>"],
      ["<b>1</b> (first)", "Real and likely in the future",
       "<b>if</b> + present, <b>will</b> + base",
       "<i>If it rains, we <b>will stay</b> in.</i>"],
      ["<b>2</b> (second)", "Improbable / imaginary (present-future)",
       "<b>if</b> + were/past, <b>would</b> + base",
       "<i>If I <b>were</b> rich, I'd travel.</i>"],
      ["<b>3</b> (third)", "Unreal past (it did not happen)",
       "<b>if</b> + had + participle, <b>would have</b> + participle",
       "<i>If I had asked, she <b>would have told</b> me.</i>"],
      ["<b>Mixed A</b>", "Past cause → present effect",
       "<b>if</b> + had + participle, <b>would</b> + verb",
       "<i>If I had slept, I <b>would feel</b> better.</i>"],
      ["<b>Mixed B</b>", "Present cause → past effect",
       "<b>if</b> + present, <b>would have</b> + participle",
       "<i>If you were taller, you <b>would have been</b> hired.</i>"]],
     titulo="The four conditionals (and the mixed ones) at a glance",
     nivel="B1",
     nota=ul("<b>Never</b> put <b>will</b> after <b>if</b>: <i>If you <b>will</b> "
             "come, I'll wait.</i> is WRONG → <i>If you <b>come</b>, I'll "
             "wait.</i>",
             "<b>Unless</b> = <i>if not</i>: <i>Unless you hurry, you'll be "
             "late.</i>",
             "<b>Otherwise / else</b> + result: <i>Hurry, otherwise you'll be "
             "late.</i> (uses <b>will</b>).",
             "<b>In case</b> + present for prevention: <i>Take an umbrella <b>in "
             "case</b> it rains.</i>"))

tabla(DM, ["Wish", "With wish", "With if"],
     [["I wish I had more time", "<i>I wish I <b>had</b> more time.</i>",
       "<i>If I <b>had</b> more time, I'd travel.</i>"],
      ["I wish I were taller", "<i>I wish I <b>were</b> taller.</i>",
       "<i>If I <b>were</b> taller, I'd play basketball.</i>"],
      ["I wish I could swim", "<i>I wish I <b>could</b> swim.</i>",
       "<i>If I <b>could</b> swim, I'd join the team.</i>"],
      ["I wish you would call", "<i>I wish you <b>would call</b>.</i>",
       "<i>If you <b>would call</b>, I'd be happy.</i>"]],
     titulo="Wish = an unfinished conditional",
     nivel="B2",
     nota="<b>Wish</b> and the <b>second/third conditional</b> are the same idea: "
          "talking about something that is <b>not</b> (or was <b>not</b>) real.")

cloze(D3, "If I {{c1::had studied}} harder, I {{c2::would have passed}}.",
      extra="<div class='box rule'><span class='lbl'>Third conditional</span>"
            "<b>if + had + participle</b> / <b>would have + participle</b>. About "
            "a past that <b>did not</b> happen.</div>",
      tags="c1-c2 conditional cloze")
