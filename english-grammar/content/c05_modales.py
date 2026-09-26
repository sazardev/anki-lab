"""05 Modals (B2-C2) - speculation, modal pasts, and the subjunctive
(wish, if only, would rather, as if)."""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge

D = "05 Modals (B2-C2)::"
D1, D2, D3, D4 = D + "Certainty Scale", D + "Modals in the Past", \
    D + "Wish and the Subjunctive", D + "Shortcuts and Special Forms"

# ========================================================== CERTAINTY SCALE

gap(D1, "He ___ (be) at home. It's 11pm and his car is in the drive.",
    "must be", nivel="B2", cue="almost certain deduction", forma="must be",
    regla="<b>must</b> = I'm 95% sure. <b>may/might</b> = 50%. <b>could</b> = "
          "possibly. <b>can't</b> = I'm sure it ISN'T.",
    ejemplos=ex("He <b>must be</b> at home.", "He <b>might be</b> at home.",
               "He <b>can't be</b> at home — I saw him at the gym."),
    notas=ul("Scale: <b>must</b> &gt; <b>should/ought to</b> &gt; "
             "<b>may/might/could</b> &gt; <b>can't</b>.",
             "<b>May</b> and <b>might</b> are interchangeable in most "
             "contexts. <b>May</b> is used for permissions (<i>You <b>may</b> "
             "park here</i>) and suggestions (<i>You <b>may</b> want to check</i>).",
             "<b>mustn't</b> = forbidden, NEVER negative deduction. To negate a "
             "deduction use <b>can't + infinitive</b>.",
             "<b>must + have + participle</b> = deduction about the past: "
             "<i>She <b>must have left</b> already.</i>"),
    tags="modals certainty")

gap(D1, "It's 2pm. He ___ be at home — he's always at the office.",
    "can't", nivel="B2", cue="certain negation", forma="can't be",
    regla="To <b>rule something out</b> use <b>can't / couldn't</b> + infinitive. "
          "<b>mustn't</b> means 'forbidden', not 'impossible'.",
    ejemplos=ex("He <b>can't be</b> at home.", "It <b>couldn't</b> have been Ana. She was in Berlin."),
    notas="This is one of the most damaging errors: saying <i>He mustn't be at "
          "home</i> means 'he is forbidden to be at home', which is bizarre. "
          "The correct form is <b>can't be</b>.",
    tags="modals negation")

gap(D1, "You ___ tell someone that. It's a secret.", "mustn't", nivel="B2",
    cue="prohibition", forma="mustn't tell",
    regla="<b>mustn't</b> = forbidden by a rule. <b>don't have to</b> = not "
          "necessary.",
    ejemplos=ex("You <b>mustn't</b> tell anyone.", "You <b>don't have to</b> come if you're tired."),
    notas="Structure: <b>mustn't + base</b> (no <i>to</i>). "
          "<i>must not to</i> and <i>mustn't to</i> do not exist.",
    tags="modals prohibition")

gap(D1, "Could you ___ the window? It's freezing.", "open", nivel="B1",
    cue="request / permission", forma="open",
    regla="<b>Can / Could / May</b> to ask for permission or make requests.",
    ejemplos=ex("<b>Could</b> you <b>open</b> the window?", "<b>May I use</b> your phone?"),
    notas="<b>May I ...?</b> is the classic way to ask permission (formal). "
          "<b>Can I ...?</b> is more informal between equals. "
          "<b>Could I ...?</b> is the softest of all.",
    tags="modals requests")

# ==================================================== MODALS IN THE PAST

gap(D2, "You ___ have told me. I would have helped you.", "should",
    nivel="B2", cue="reproach about the past", forma="should have",
    regla="<b>should have + participle</b> = reproach for what you failed to "
          "do. <b>shouldn't have</b> = what you did and it was a mistake.",
    ejemplos=ex("You <b>should have</b> told me (you didn't).",
               "You <b>shouldn't have</b> said that (you did)."),
    notas="This is the key B2 structure for talking about <b>regret</b>.",
    tags="should-have reproach")

gap(D2, "I ___ you were coming. I'd have waited.", "wish", nivel="B2",
    cue="unfulfilled wish about the past", forma="wish",
    regla="<b>wish + Past Simple</b> (or <b>could/would</b>) to regret or to "
          "wish for something that did not happen.",
    ejemplos=ex("I <b>wish</b> I <b>were</b> there (but I wasn't).",
               "I <b>wish</b> I <b>had known</b>."),
    notas=ul("The <b>past wish</b> rule: <b>wish + were + subject + base / "
             "had + participle</b>.",
             "<b>wish + could + base</b> for requests: <i>I <b>wish</b> I "
             "<b>could speak</b> English better.</i>",
             "<b>wish + would</b> for requests: <i>I <b>wish</b> he "
             "<b>would call</b>.</i>"),
    tags="wish past")

gap(D2, "It's hot in here. ___ the window?", "Let's open", nivel="B1",
    cue="suggestion", forma="Let's open",
    regla="<b>Let's + base</b> = proposal. <b>Why don't we + base?</b> / "
          "<b>Why not + base?</b> / <b>How about + V-ing?</b> = alternatives.",
    ejemplos=ex("<b>Let's open</b> the window.", "<b>How about going</b> to the cinema?"),
    notas="<b>Shall we + base?</b> is the old-fashioned formal British version: "
          "<i>Shall we dance?</i>",
    tags="suggestions let")

gap(D2, "You ___ be quiet in the library. It's a rule.", "must not", nivel="B2",
    cue="prohibition / ability", forma="must not",
    regla="<b>Can't</b> can also mean <b>inability</b>: <i>I <b>can't swim</b></i> "
          "= I cannot swim. <b>Can't</b> can also mean a rule is being broken.",
    ejemplos=ex("I <b>can't speak</b> Japanese (no ability).",
               "You <b>can't use</b> your phone in here (prohibition)."),
    notas="In the first sense it is a skill; in the second, a norm. Context "
          "decides.",
    tags="modals ability")

gap(D2, "She's a doctor, so she ___ help you.", "can", nivel="B1",
    cue="ability / possibility", forma="can help",
    regla="<b>Can / could</b> = ability. <b>Be able to</b> = the same, more "
          "formal and available in all tenses.",
    ejemplos=ex("She <b>can</b> help you.", "I'll <b>be able to</b> come tomorrow (future possibility)."),
    notas="<b>Can't</b> + passive: <i>The meeting <b>can't be</b> postponed.</i>",
    tags="modals ability")

# ======================================================== WISH AND SUBJUNCTIVE

gap(D3, "I wish I ___ (be) taller.", "were", nivel="B2",
    cue="unreal wish (I)", forma="were",
    regla="<b>wish + were</b> to express a <b>impossible or unlikely</b> wish "
          "in the present. Use <b>were</b> for <b>all</b> persons, including "
          "<b>I / he / she</b>.",
    ejemplos=ex("I wish I <b>were</b> taller.", "I wish I <b>knew</b> the answer."),
    notas=ul("In wishes, <b>were</b> replaces <b>was</b> always: <i>I wish I "
             "<b>were</b> rich</i> (not <s>was</s>).",
             "A <b>real</b> but not possible wish uses <b>had</b>: <i>I wish I "
             "<b>had</b> more time</i>.",
             "<b>I wish I could + base</b> to make requests: <i>I wish I "
             "<b>could come</b> tonight.</i>"),
    tags="wish were")

gap(D3, "___ only I had more time!", "If", nivel="B2", cue="a wish",
    forma="If only",
    regla="<b>If only + Past Simple</b> = a stronger wish. "
          "<b>If only I had studied harder!</b>",
    ejemplos=ex("<b>If only I had</b> more time!", "<b>If only I knew</b> what to do."),
    notas="Almost the same as <i>wish</i>, but more emotional and with the "
          "implication that you are about to make a decision.",
    tags="if-only wishes")

gap(D3, "I'd ___ you stop shouting.", "rather", nivel="B2", cue="preference",
    forma="rather",
    regla="<b>would rather + base</b> = I would prefer. <b>would rather + "
          "subject + Past Simple</b> = I would prefer that (someone) did.",
    ejemplos=ex("I'd <b>rather</b> you stopped shouting.",
               "I'd <b>rather</b> stay at home tonight."),
    notas="<b>Would rather not</b> = I'd prefer not to. <i>I'd <b>rather not "
          "go</b></i> (not <s>to go</s>).",
    tags="would-rather")

gap(D3, "You look like you ___ a bad day.", "have had", nivel="C1",
    cue="as if", forma="have had",
    regla="<b>as if / as though</b> + a past form that is <b>not real</b>: "
          "<b>Past Simple</b> or <b>Past Perfect</b>.",
    ejemplos=ex("You look as if you <b>had had</b> a bad day.",
               "He acts as if he <b>knew</b> everything."),
    notas="If it is actually true, use the <b>present</b>: <i>He acts as if he "
          "<b>knows</b> everything</i> (and he does).",
    tags="as-if as-though")

# ============================================== SHORTCUTS AND SPECIAL FORMS

gap(D4, "He ___ have left already — I saw his coat.", "can't", nivel="C1",
    cue="ruling out the past", forma="can't",
    regla="<b>can't + have + participle</b> = I'm sure it did NOT happen. "
          "To cancel plans, simply use <b>won't</b>.",
    ejemplos=ex("He <b>can't have left</b> — I saw his coat.", "She <b>won't come</b> any more (cancelling)."),
    notas="<b>Can't have + participle</b> = I'm sure it did NOT happen. "
          "<b>Must have + participle</b> = I'm sure it DID. This pair is a "
          "classic B2/C1 exam item.",
    tags="cant-have past")

gap(D4, "It might ___ already left.", "have", nivel="C1",
    cue="possibility about the past", forma="have",
    regla="<b>might / may / could + have + participle</b> = possibility about "
          "the past.",
    ejemplos=ex("She <b>might have already left</b>.", "You <b>could have told</b> me! (a soft reproach)."),
    notas="<b>Should have</b> = reproach. <b>Could have</b> = a soft reproach "
          "(or a lost ability: <i>I <b>could have swum</b> faster</i>).",
    tags="modals past possibility")

gap(D4, "___ be more careful next time.", "Should", nivel="B2", cue="advice",
    forma="Should",
    regla="For <b>advice</b>: <b>should + base</b>. For <b>reproach about the "
          "past</b>: <b>should have + participle</b>.",
    ejemplos=ex("You <b>should</b> be more careful next time.",
               "You <b>should have</b> been more careful."),
    notas="The key B2 difference: <b>should</b> looks forward, "
          "<b>should have</b> looks back at a mistake.",
    tags="should advice")

# ============================================================== REFERENCE

tabla(D1, ["Modal", "Meaning", "Example"],
     [["<b>will</b>", "future / offer / promise", "<i>It <b>will</b> rain.</i>"],
      ["<b>shall</b>", "formal offer (UK, legal)", "<i>I <b>shall</b> return it.</i>"],
      ["<b>can</b>", "ability / permission", "<i>I <b>can</b> swim.</i>"],
      ["<b>may</b>", "permission / possibility (formal)", "<i>You <b>may</b> park here.</i>"],
      ["<b>must</b>", "strong obligation / deduction", "<i>You <b>must</b> try it. / She <b>must be</b> tired.</i>"],
      ["<b>should</b>", "advice / recommendation", "<i>You <b>should</b> rest.</i>"],
      ["<b>ought to</b>", "= should, more formal", "<i>You <b>ought to</b> apologise.</i>"],
      ["<b>would</b>", "conditional / polite request", "<i>I <b>would</b> like a coffee.</i>"],
      ["<b>may/might</b>", "possibility (50%)", "<i>It <b>might</b> rain.</i>"],
      ["<b>could</b>", "possibility / politeness", "<i>It <b>could</b> rain. / <b>Could</b> you help?</i>"],
      ["<b>must</b> (deduction)", "95% sure (affirmative)", "<i>She <b>must be</b> home.</i>"],
      ["<b>can't</b> (deduction)", "surely NOT", "<i>She <b>can't be</b> home.</i>"],
      ["<b>used to</b>", "abandoned past habit", "<i>I <b>used to</b> smoke.</i>"],
      ["<b>had better</b>", "firm advice / warning", "<i>You <b>had better</b> leave now.</i>"],
      ["<b>needn't</b>", "not necessary", "<i>You <b>needn't</b> come.</i>"],
      ["<b>dare</b>", "dare", "<i>I <b>dare</b> say he's right.</i>"]],
     titulo="All the modals in one table",
     nivel="B2",
     nota=ul("<b>had better</b> = 'you'd better'. Used with both persons: "
             "<i>You <b>had better</b> not tell anyone.</i>",
             "<b>ought to</b> and <b>should</b> are equivalent; <i>ought to</i> "
             "is more formal and more British.",
             "<b>needn't</b> = not necessary. <b>mustn't</b> = forbidden. Do "
             "not confuse them: <i>You <b>needn't</b> worry</i> (no need) vs "
             "<i>You <b>mustn't</b> worry</i> (forbidden).",
             "In the negative, <b>can</b> can also mean permission: <i>You "
             "<b>can't</b> smoke in here.</i>"))

cloze(D2, "You {{c1::should have}} told me.",
      extra="<div class='box rule'><span class='lbl'>should vs should have</span>"
            "<b>should</b> = future advice. <b>should have + participle</b> = "
            "reproach about the past.</div>",
      tags="c1-c2 should-have cloze")

cloze(D1, "He {{c1::must be}} at home — his car's outside.",
      extra="<div class='box note'><span class='lbl'>Certainty scale</span>"
            "<b>must</b> &gt; <b>should</b> &gt; <b>may/might/could</b> &gt; "
            "<b>can't</b>. In the negative, <b>mustn't</b> = forbidden; to "
            "negate use <b>can't</b>.</div>",
      tags="c1-c2 modals cloze")
