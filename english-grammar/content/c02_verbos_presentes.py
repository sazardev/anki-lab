"""02 Verb System (B1-B2) - present tenses, modals basics, do-support."""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge

D = "02 Verb System::"
DS, DC, DM, DQ = D + "Present Simple", D + "Present Continuous", \
    D + "Modals: Basics", D + "Questions and Do-support"

# ========================================================== PRESENT SIMPLE

gap(DS, "Water ___ at 100 degrees Celsius.", "boils", nivel="B1",
    cue="3rd person (habit / general truth)", forma="boils",
    regla="<b>Present Simple</b> for habits, routines, general truths, "
          "scheduled future events. In the 3rd person (he/she/it) add "
          "<b>-s / -es</b>.",
    ejemplos=ex("The <b>boils</b> at 100°C (general truth).",
               "She <b>works</b> in a hospital (routine).",
               "I <b>don't drink</b> coffee (negative)."),
    notas=ul("3rd person singular: <b>+s</b> (-o → -es): <i>work→works, "
             "play→plays, like→likes</i>.",
             "After <b>-ch, -sh, -ss, -x, -o, -z</b> → <b>-es</b>: "
             "<i>watch→watches, go→goes, fix→fixes, pass→passes</i>.",
             "<b>have → has</b> and <b>do → does</b> are irregular."),
    tags="present-simple 3rd-person")

gap(DS, "___ he like sushi?", "Does", nivel="B1", cue="yes/no question",
    forma="Does he like",
    regla="To form questions and negatives in the <b>Present Simple</b>, use "
          "the auxiliary <b>do / does / did</b>, and the main verb returns to "
          "its <b>base form</b>.",
    ejemplos=ex("<b>Does</b> he <b>like</b> sushi?",
               "She <b>doesn't live</b> here.", "<b>Do</b> you <b>work</b> on Fridays?"),
    notas=ul("The <b>-s</b> moves onto the auxiliary: <i>Does he <s>like</s></i> "
             "→ <i><b>Does</b> he <b>like</b></i>.",
             "In a positive 3rd-person statement you do NOT use <i>do</i>: "
             "<i>She works</i> (not <s>She does work</s>).",
             "Answer with <b>do / don't / doesn't</b>: <i>Yes, I do. / No, I "
             "don't. / No, he doesn't.</i>"),
    tags="do-support questions")

gap(DS, "How often ___ you go to the gym?", "do", nivel="B1",
    cue="how often", forma="do you go",
    regla="<b>How often / How much / How long / What time</b> questions in the "
          "present take <b>do</b> + base verb.",
    ejemplos=ex("<b>How often do you go</b> to the gym?",
               "<b>How long does it take</b>?"),
    notas="After an auxiliary the main verb is always in base form: "
          "<i>How long <b>does</b> it <b>take</b>?</i>",
    tags="do-support questions")

# ======================================================== PRESENT CONTINUOUS

gap(DC, "Look! The baby ___ right now.", "is crying", nivel="B1",
    cue="right now", forma="is crying",
    regla="<b>Present Continuous</b> = <b>am/is/are + V-ing</b>. Used for "
          "actions in progress now, for temporary periods (this week, these "
          "days), and for near-future arrangements.",
    ejemplos=ex("Listen! It's <b>raining</b>.", "We're <b>working</b> on a new project <b>this week</b>.",
               "I'm <b>meeting</b> Ana at 8 <b>tomorrow</b> (arrangement)."),
    notas=ul("<b>now, at the moment, right now, currently, today, this week, "
             "this month, this year, these days</b> → continuous.",
             "Also for irritation: <i>You're <b>always</b> losing your keys!</i>",
             "Used for states/situations: <i>We're <b>having</b> a great time.</i>"),
    tags="continuous now")

gap(DC, "I ___ my car. I can't stop.", "am repairing", nivel="B1",
    cue="in progress, not interruptible", forma="am repairing",
    regla="The continuous marks <b>limited temporality</b>: the action is "
          "happening in a defined period and will not go on.",
    ejemplos=ex("The shop is <b>having</b> a sale <b>this week</b>.",
               "She's <b>studying</b> for her exams <b>this month</b>."),
    notas="This is the key difference from the <b>Present Simple</b>: "
          "<i>I'm <b>reading</b> <b>this week</b></i> (I will read this week, "
          "no more) vs <i>I <b>read</b> every week</i> (habit).",
    tags="continuous temporary")

gap(DC, "I ___ here since 2015.", "have lived", nivel="B1",
    cue="stative verb (not continuous)", forma="have lived",
    regla="<b>Stative verbs</b> (states, not actions) do not take the "
          "continuous in their literal sense. Use the <b>Present Perfect</b> "
          "or the <b>Simple</b>.",
    ejemplos=ex("I <b>have known</b> her for years.", "She <b>lives</b> in Madrid.",
               "I <b>love</b> Italian food."),
    notas=ul("<b>Never in the continuous (normal meaning)</b>: <b>know, "
             "believe, understand, remember, forget, want, need, like, love, "
             "hate, prefer, wish, own, belong, seem, appear, contain, consist, "
             "depend, matter, cost, weigh, lack, resemble, fit, suit, deserve, "
             "involve, mean, exist, die, arrive, come, go, fall, rise, lie, "
             "sit, stand</b>.",
             "<b>But</b> yes with a different, figurative meaning: "
             "<i>I'm not <b>believing</b> this story.</i> (I don't believe it).",
             "Some verbs change meaning: <i>He's <b>thinking</b> about "
             "moving</i> = he is considering it (not meditating)."),
    tags="stative-verbs continuous")

gap(DC, "He ___ smoke. He gave it up last year.", "doesn't", nivel="B1",
    cue="past habit he no longer has", forma="doesn't smoke",
    regla="A past habit that still holds but can change: <b>Present Simple</b> "
          "negative. A <b>temporary</b> break uses the continuous: "
          "<i>He's <b>not smoking</b> (anymore / at the moment)</i>.",
    ejemplos=ex("<b>Doesn't smoke</b> → does not smoke in general.",
               "<b>Isn't smoking</b> → not smoking right now (he has quit)."),
    notas="In practice natives use the negative continuous to say they've "
          "quit: <i>I <b>don't smoke</b> anymore</i> or <i>I'm <b>not "
          "smoking</b> anymore</i>. Both are fine.",
    tags="habit state")

# ============================================================ MODALS: BASICS

gap(DM, "You ___ smoke here. It's forbidden.", "must not", nivel="B1",
    cue="prohibition", forma="must not",
    regla="<b>must not / mustn't</b> = <b>PROHIBITION</b> (an external rule). "
          "<b>don't have to / doesn't have to</b> = <b>not necessary</b> (you "
          "may, it's just not needed).",
    ejemplos=ex("You <b>mustn't</b> smoke here.", "You <b>don't have to</b> come (if you don't want to).",
               "You <b>must</b> wear a helmet."),
    notas=ul("<b>must</b> = external obligation (law, rule). <b>have to</b> = "
             "external obligation (circumstance) = 'have to'.",
             "<b>should</b> = your own obligation, advice, recommendation: "
             "<i>You <b>should</b> see a doctor.</i>",
             "<b>mustn't</b> ≠ <b>don't have to</b> — the classic B1 error. "
             "<i>You mustn't worry</i> = don't worry (it's forbidden to "
             "worry); <i>You don't have to worry</i> = there's no need to worry."),
    tags="modals prohibition")

gap(DM, "It's 9pm. You ___ go to bed.", "should", nivel="B1",
    cue="advice", forma="should go",
    regla="<b>should</b> = advice, recommendation, what is sensible or "
          "desirable. Add <b>not</b> to advise against something.",
    ejemplos=ex("You <b>should</b> go to bed.", "You <b>shouldn't</b> eat so much sugar."),
    notas="<b>ought to</b> means the same but is more formal and rarer in "
          "speech: <i>You <b>ought to</b> apologise.</i>",
    tags="modals advice")

gap(DM, "You ___ be tired. You've been working 12 hours.", "must", nivel="B2",
    cue="strong deduction", forma="must be",
    regla="<b>must</b> for <b>deduction</b> (almost certain). "
          "<b>might / may</b> for possibility. <b>can't</b> for certain "
          "negation.",
    ejemplos=ex("She <b>must be</b> tired.", "She <b>might be</b> tired.",
               "She <b>can't be</b> tired."),
    notas=ul("Certainty scale: <b>must</b> (95%) &gt; <b>should/ought to</b> "
             "(80%) &gt; <b>may/might/could</b> (50%) &gt; <b>can't</b> (impossible).",
             "<b>May</b> and <b>might</b> are interchangeable in most "
             "contexts. <b>May</b> is used for permissions (<i>You <b>may</b> "
             "park here</i>) and suggestions (<i>You <b>may</b> want to check</i>).",
             "<b>mustn't</b> = forbidden, NEVER negative deduction. To negate "
             "a deduction use <b>can't + infinitive</b>.",
             "<b>must + have + participle</b> = deduction about the past: "
             "<i>She <b>must have forgotten</b>.</i>"),
    tags="modals deduction")

gap(DM, "Could you ___ the window, please?", "open", nivel="B1",
    cue="polite request", forma="Could you open",
    regla="Polite requests: <b>Could / Would you...?  Would you mind + V-ing?</b>",
    ejemplos=ex("<b>Could you open</b> the window, please?",
               "<b>Would you mind opening</b> the window?"),
    notas="<b>Could</b> sounds softer and less direct than <i>Can you</i>. "
          "<b>Would you</b> for offers: <i>Would you like a coffee?</i>",
    tags="modals requests")

gap(DM, "You ___ finish this by Friday. It's a deadline.", "have to", nivel="B1",
    cue="external obligation (deadline)", forma="have to finish",
    regla="<b>have to / has to</b> = obligation imposed by circumstances (the "
          "boss, the deadline, the law). <b>must</b> = obligation the speaker "
          "expresses, moral or legal.",
    ejemplos=ex("I <b>have to</b> go to work early tomorrow.",
               "I <b>must</b> finish this report today."),
    notas="<b>mustn't</b> = forbidden; <b>don't have to</b> = not necessary. "
          "That is the key B1/B2 distinction.",
    tags="have-to must")

# ========================================================= DO-SUPPORT

gap(DQ, "___ you mind if I sit here?", "Would", nivel="B1",
    cue="Would you mind", forma="Would you mind",
    regla="<b>Would you mind + V-ing?</b> signals that the action is a "
          "trouble or an inconvenience. Reply: <i>Not at all. / No, not "
          "really. / I'd rather not.</i>",
    ejemplos=ex("<b>Would you mind if I sat here?</b>",
               "<b>Would you mind closing</b> the door?"),
    notas="<b>Do you mind + V-ing?</b> = the same, slightly more informal. "
          "<b>Do you mind if + present?</b> = more formal. "
          "<i>I'd rather + base verb</i> = I'd prefer (not <i>I'd rather to go</i>).",
    tags="mind requests")

gap(DQ, "You look great, ___ ?", "don't you", nivel="B1",
    cue="tag question, positive", forma="don't you",
    regla="<b>Tag questions</b> use the auxiliary of the main verb: positive "
          "statement → <b>negative</b> tag (asking for confirmation), negative "
          "statement → <b>positive</b> tag (genuine doubt).",
    ejemplos=ex("You're coming, <b>aren't you</b>?",
               "She doesn't like it, <b>does she</b>? (rhetorical: 'sure she doesn't')",
               "Nobody called, <b>did they</b>?"),
    notas=ul("Special verbs with no <b>do</b>: <b>be, have, will, can, should, "
             "must, may, ought, need</b>.",
             "If the main clause has a lexical verb, the tag uses "
             "<b>do/does/did</b>: <i>You <b>live</b> here, <b>don't you</b>?</i>",
             "With unaccountables: <i>It's cold, <b>isn't it</b>?</i>",
             "With <b>I</b>: <i>I'm tired, <b>aren't I</b>?</i> (used)."),
    tags="tag-questions")

gap(DQ, "How much ___ it cost?", "does", nivel="B1",
    cue="subject question", forma="does it cost",
    regla="When the question has a <b>subject</b> (who, what, how much, how "
          "many), the main verb needs no auxiliary: <b>How much does it "
          "cost?</b>",
    ejemplos=ex("How much <b>does</b> it <b>cost</b>?", "What <b>do you want</b>?"),
    notas="<i>How much is it?</i> — with <b>be</b> no auxiliary. "
          "<i>What did he say?</i> — in the past, <b>did</b> is obligatory.",
    tags="questions subject")

# ================================================================ REFERENCE

tabla(DS, ["Base", "3rd person (-s)", "Past", "Past participle", "-ing", "Meaning"],
     [["be", "is", "was/were", "been", "being", "be"],
      ["become", "becomes", "became", "become", "becoming", "become"],
      ["begin", "begins", "began", "begun", "beginning", "begin"],
      ["break", "breaks", "broke", "broken", "breaking", "break"],
      ["come", "comes", "came", "come", "coming", "come"],
      ["do", "does", "did", "done", "doing", "do"],
      ["drink", "drinks", "drank", "drunk", "drinking", "drink"],
      ["drive", "drives", "drove", "driven", "driving", "drive"],
      ["eat", "eats", "ate", "eaten", "eating", "eat"],
      ["fall", "falls", "fell", "fallen", "falling", "fall"],
      ["feel", "feels", "felt", "felt", "feeling", "feel"],
      ["find", "finds", "found", "found", "finding", "find"],
      ["get", "gets", "got", "got/gotten", "getting", "get"],
      ["give", "gives", "gave", "given", "giving", "give"],
      ["go", "goes", "went", "gone", "going", "go"],
      ["grow", "grows", "grew", "grown", "growing", "grow"],
      ["have", "has", "had", "had", "having", "have"],
      ["hear", "hears", "heard", "heard", "hearing", "hear"],
      ["hold", "holds", "held", "held", "holding", "hold"],
      ["keep", "keeps", "kept", "kept", "keeping", "keep"],
      ["know", "knows", "knew", "known", "knowing", "know"],
      ["leave", "leaves", "left", "left", "leaving", "leave"],
      ["lose", "loses", "lost", "lost", "losing", "lose"],
      ["make", "makes", "made", "made", "making", "make"],
      ["meet", "meets", "met", "met", "meeting", "meet"],
      ["pay", "pays", "paid", "paid", "paying", "pay"],
      ["put", "puts", "put", "put", "putting", "put"],
      ["read", "reads", "read /red/", "read /red/", "reading", "read"],
      ["run", "runs", "ran", "run", "running", "run"],
      ["say", "says", "said", "said", "saying", "say"],
      ["see", "sees", "saw", "seen", "seeing", "see"],
      ["sell", "sells", "sold", "sold", "selling", "sell"],
      ["send", "sends", "sent", "sent", "sending", "send"],
      ["sing", "sings", "sang", "sung", "singing", "sing"],
      ["sit", "sits", "sat", "sat", "sitting", "sit"],
      ["speak", "speaks", "spoke", "spoken", "speaking", "speak"],
      ["take", "takes", "took", "taken", "taking", "take"],
      ["teach", "teaches", "taught", "taught", "teaching", "teach"],
      ["tell", "tells", "told", "told", "telling", "tell"],
      ["think", "thinks", "thought", "thought", "thinking", "think"],
      ["understand", "understands", "understood", "understood", "understanding", "understand"],
      ["wear", "wears", "wore", "worn", "wearing", "wear"],
      ["win", "wins", "won", "won", "winning", "win"],
      ["write", "writes", "wrote", "written", "writing", "write"]],
     titulo="The 50 irregular verbs you must memorise",
     nivel="B1",
     nota=ul("Regular verbs only need <b>-ed</b>. Irregular ones need full "
             "memorising, but the <b>-ed</b> and <b>-ing</b> follow the "
             "pattern: <i>stop → stopped → stopping</i>.",
             "The 3rd person <b>-s</b> is always regular: "
             "<i>go → goes, have → has, do → does</i>.",
             "<b>Read</b> is the same in writing but different in sound: "
             "present /riːd/, past /red/."))

# =================================================================== CLOZE

cloze(DS, "{{c1::She}} {{c2::works}} {{c3::in}} a hospital.",
      extra="<div class='box rule'><span class='lbl'>3rd person +s</span>"
            "he/she/it + verb in <b>-s</b>. After -ch/-sh/-ss/-x/-o → <b>-es</b>.</div>",
      tags="c1-c2 present-simple cloze")

cloze(DC, "I {{c1::am not}} reading. I {{c1::am not}} listening.",
      extra="<div class='box warn'><span class='lbl'>Negative continuous</span>"
            "<b>am/is/are + not + V-ing</b>. Never use <i>do not</i> with the "
            "continuous: <i>I <s>don't read</s></i> is the habit, "
            "<i>I <b>am not reading</b></i> is now.</div>",
      tags="c1-c2 continuous negative cloze")

cloze(DM, "You {{c1::mustn't}} smoke here. It's forbidden.",
      extra="<div class='box warn'><span class='lbl'>Prohibition vs necessity</span>"
            "<b>mustn't</b> = forbidden. <b>don't have to</b> = not "
            "necessary. <b>must</b> = obligatory.</div>",
      tags="c1-c2 modals cloze")
