"""14 Register and Style (C1-C2) - formal vs informal, hedges, discourse
markers, academic language and level upgrading."""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "14 Register and Style (C1-C2)::"
F, I, H, DM, UP = D + "Formal vs Informal", D + "Hedges and Boosters", \
    D + "Discourse Markers", D + "Academic Language", \
    D + "Level Upgrades (B1 to C2)"

# =============================================== FORMAL VS INFORMAL

gap(F, "I couldn't ___ to your email.", "reply", nivel="B1", cue="reply to",
     regla="<b>Register</b>: <i>reply to an email</i> is formal/neutral. "
     "<i>answer your email</i> is more informal. <i>get back to you</i> is "
     "informal.",
     ejemplos=ex("<b>reply to</b> your email (formal)",
                 "<b>get back to</b> you (informal)",
                 "Please <b>find attached</b> the invoice (very formal)."),
     notas=ul("<b>I look forward to hearing from you</b> is the standard email "
              "formula. <b>I look forward to</b> (no <i>to hear</i>).",
              "<b>Please find attached / enclosed</b> (formal) vs <b>I've "
              "attached</b> (informal).",
              "<b>As per our conversation</b> (formal) vs <b>As we "
              "discussed</b> (neutral) vs <b>Like we said</b> (informal).",
              "<b>Yours sincerely / Yours faithfully</b> (UK)."),
    tags="register formal")

gap(F, "___ the meantime, we've found a solution.", "In", nivel="C1",
    cue="in the meantime",
     regla="<b>High register</b>: <b>in the meantime, however, therefore, furthermore, "
     "moreover, nevertheless, consequently, regarding, aforementioned</b>.",
     ejemplos=ex("<b>In the meantime</b>, we've found a solution.",
                 "<b>Regarding</b> your query... <b>With regard to</b>..."),
     notas="In natural language these can sound robotic. Use them sparingly.",
    tags="register formal")

gap(F, "Can you ___ me know if you can come?", "let", nivel="B1",
     cue="let me know",
     regla="<b>Let me know</b> = let me know (neutral/informal). "
     "<b>Please be advised</b> / <b>Kindly inform</b> = very formal.",
     ejemplos=ex("<b>Let me know</b> if you can come (informal).",
                 "<b>Please be advised that</b> the meeting is postponed."),
     notas="<b>Let me know</b> is so natural that it is used even in work "
           "emails.",
    tags="register formal")

# =================================================== HEDGES AND BOOSTERS

gap(H, "___ you be right, but I disagree.", "I", nivel="C1",
     cue="I might be right",
     regla="<b>Hedges</b> to sound more careful and polite: <b>might, may, could, "
     "seem, tend to, appear to, arguably, to some extent, to a certain "
     "degree, it's possible that, one might argue</b>.",
     ejemplos=ex("<b>I might be</b> right, but I disagree.",
                 "<b>It would seem that</b> the plan is failing.",
                 "<b>To some extent</b>, I agree."),
     notas="In English, NOT using hedges can sound <b>arrogant</b>. A native "
           "B1 speaker is more direct than a textbook suggests.",
    tags="hedge c1")

gap(H, "This is ___ the most important point.", "arguably", nivel="C1",
    cue="arguably",
     regla="<b>Arguably</b> = it can be argued that. <b>Undoubtedly, certainly, "
     "definitely</b> = undoubtedly (boosters).",
     ejemplos=ex("This is <b>arguably</b> the most important point.",
                 "<b>Undoubtedly</b>, the best option."),
     notas="Combining a hedge and a booster gives a very C1 tone: <i>It is "
           "<b>arguably</b> the most important factor, and it is "
           "<b>undoubtedly</b> the most overlooked.</i>",
    tags="hedge booster c1")

gap(H, "___ the fact that he lied, I think it's fair.", "Given", nivel="C1",
    cue="given that",
     regla="<b>Given (that) + clause</b> = given that. <b>Seeing that</b> = seeing "
     "that. <b>Now that</b> = now that. <b>In that</b> = in that.",
     ejemplos=ex("<b>Given the fact that</b> he lied, I think it's fair.",
                 "<b>Seeing that</b> you're tired, let's stop."),
     notas="<b>Given</b> also means 'given' + noun: <i><b>Given</b> the "
           "circumstances...</i>",
    tags="concession c1")

gap(H, "I would ___ suggest changing the plan.", "strongly", nivel="C1",
    cue="strongly suggest",
     regla="<b>would strongly suggest / would tentatively suggest / would "
     "hesitantly suggest / would be inclined to think</b>.",
     ejemplos=ex("I would <b>strongly suggest</b> changing the plan.",
                 "She would <b>be inclined to think</b> it's a bad idea."),
     notas="<b>would tend to + base</b> = to tend to. "
           "<i>People <b>tend to</b> agree.</i> (not <i>used to</i> here).",
    tags="hedge c1")

# ================================================== DISCOURSE MARKERS

serie_gap(DM, [
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
        "mainly spoken in Spain. / <b>Similarly</b> = similarly. "
        "<b>By contrast</b> = by contrast.")),
    ("He is a doctor. ___, he teaches at university.", "Besides", "besides",
     "<b>Besides</b> + noun/-ing. <b>Besides that / Apart from that</b> + clause.",
     ex("<b>Besides</b> being a doctor, he teaches at university. / "
        "<b>Apart from</b> that, he speaks three languages.")),
    ("The film was slow, ___ the acting was excellent.", "but", "but",
     "ADDING INSIDE A SENTENCE: <b>but, yet, though, although</b> (with a "
     "comma, with the verb right after).",
     ex("The film was slow, <b>but</b> the acting was excellent. / "
        "<b>Although</b> the film was slow, the acting was excellent.")),
    ("Owing to the heavy rain, the match was cancelled. ___, it was already "
     "in a poor state.", "Moreover", "moreover",
     "ADDING with a consequence: <b>moreover, besides, in addition, "
     "furthermore, plus, what is more</b>.",
     ex("<b>Moreover</b>, the field was in a poor state.")),
    ("The plan is expensive. ___, it might be worth it.", "Admittedly",
     "admittedly",
     "CONCESSION: <b>admittedly, granted, admittedly, it is true that, sure, "
     "yes, of course, certainly</b>.",
     ex("<b>Admittedly</b>, it might be worth it. / <b>Granted</b>, it is "
        "expensive. / <b>It is true that</b>...")),
    ("He gets on my nerves. ___, he never says thank you.", "And yet",
     "and yet",
     "CONCESSION + contrast: <b>and yet, yet, nevertheless, still, "
     "nonetheless, even so, all the same</b>.",
     ex("<b>And yet</b>, he never says thank you. / <b>Even so</b> = even so. "
        "<b>Still</b> = all the same.")),
    ("___ the high costs, few people can afford it.", "Despite", "despite",
     "CONTRADICTION: <b>despite, in spite of, notwithstanding, regardless of</b> "
     "+ noun/-ing. Or <b>although, though, even though, while, whereas</b> + clause.",
     ex("<b>Despite</b> the high costs, few people can afford it. / "
        "<b>Although</b> the costs are high, few people can afford it.")),
], nivel="C1", tags=["discourse-marker"])

# ================================================== ACADEMIC LANGUAGE

gap(DM + "", "The data ___ a significant increase in sales.", "show",
    nivel="C1", cue="the data show", forma="showed",
    regla="Academic verbs: <b>show, reveal, suggest, indicate, demonstrate, "
          "illustrate, highlight, underline, point to, account for, attribute "
          "to, correlate with, coincide with</b>.",
    ejemplos=ex("The data <b>show</b> a significant increase.",
               "This <b>highlights</b> the need for reform."),
    notas="Academic nouns: <b>research, data, evidence, findings, study, "
          "analysis, impact, factor, issue, aspect, criteria, phenomenon, "
          "trend, framework, methodology</b>.",
    tags="academic c1")

gap(DM + "", "___ , this is a widely held belief.", "Generally",
    nivel="C1", cue="generally speaking", forma="Generally",
    regla="<b>Generally speaking / broadly speaking / on the whole / in "
          "principle / as a rule / in most cases / to a large extent</b>.",
    ejemplos=ex("<b>Generally speaking</b>, this is a widely held belief.",
                "<b>On the whole</b>, the results are positive."),
    notas="<b>By and large</b> = by and large. <b>To some extent</b> = to some "
          "extent (a hedge).",
    tags="academic c1")

# ================================================ LEVEL UPGRADES

gap(UP, "There are a ___ people at the conference.", "lot of",
     nivel="C1", cue="plenty of",
     regla="<b>B1 → B2/C1</b>: instead of <i>a lot of</i>: <b>plenty of, "
           "loads of, tons of, a great deal of, a great many, a considerable "
           "number of, a wide range of</b>.",
     ejemplos=ex("<b>Plenty of</b> people attended.",
                "<b>A considerable number of</b> studies support this."),
     notas="<b>Plenty of</b> works with countables and uncountables. "
           "<b>A great many</b> only with plural countables.",
    tags="upgrade b1 c1")

gap(UP, "The film was ___ . I loved it.", "fantastic", nivel="C1",
    cue="outstanding",
     regla="<b>B1 → C1</b>: replaces <i>very good</i>: <b>outstanding, "
           "brilliant, superb, remarkable, exceptional, phenomenal, "
           "extraordinary</b>. For bad: <b>dreadful, appalling, atrocious, "
           "horrendous</b>.",
     ejemplos=ex("The film was <b>outstanding</b>.", "The service was <b>appalling</b>."),
     notas="And <b>very big</b> → <b>enormous, vast, immense, massive, "
           "substantial, considerable</b>.",
    tags="upgrade c1")

gap(UP, "___ , he dropped out of university.", "Eventually", nivel="C1",
    cue="eventually",
     regla="<b>B1 → C1</b>: replaces <i>finally / at last / in the end</i>: "
           "<b>eventually, ultimately, in the long run, sooner or later, in "
           "the end</b>.",
     ejemplos=ex("<b>Eventually</b>, he dropped out.",
                 "<b>In the long run</b>, it will pay off."),
     notas="<b>Ultimately / in the long run</b> = in the long run. "
           "<b>Sooner or later</b> = sooner or later.",
    tags="upgrade c1")

gap(UP, "It's ___ that we finish on time.", "essential", nivel="C1",
    cue="essential",
     regla="<b>B1 → C1</b>: <i>very important</i> → <b>crucial, vital, "
           "essential, indispensable, paramount, pivotal</b>.",
     ejemplos=ex("It's <b>crucial</b> that we finish on time.",
                 "<b>Vital</b> / <b>essential</b> / <b>indispensable</b> for survival."),
     notas="With <b>essential / vital / crucial</b> use <b>It is + adj + that "
           "+ clause</b> (no <i>for</i>).",
    tags="upgrade c1")

gap(UP, "I have a ___ number of questions.", "considerable", nivel="C1",
    cue="a considerable number of",
     regla="<b>B1 → C1</b>: <i>a lot of</i> → <b>a considerable number of, a "
           "significant number of, a growing number of, a majority of, a "
           "minority of, a handful of, a wide range of</b>.",
     ejemplos=ex("I have <b>a considerable number of</b> questions.",
                "<b>A growing number of</b> people work from home."),
     notas="<b>A handful of</b> = a handful (few). <b>A majority of</b> = the "
           "majority.",
    tags="upgrade c1")

# =================================================================== CLOZE

cloze(H, "This is {{c1::arguably}} the most important point.",
      extra="<div class='box rule'><span class='lbl'>Hedge</span>"
            "<b>arguably, arguably, arguably</b> = it can be argued that. "
            "Natives use hedges to avoid sounding arrogant: "
            "<b>might, may, could, seem, tend to, arguably, to some extent, "
            "presumably, apparently</b>.</div>",
      tags="c1-c2 hedge cloze")

cloze(F, "I look forward to {{c1::hearing}} from you.",
      extra="<div class='box warn'><span class='lbl'>Email formula</span>"
            "<b>look forward to</b> + <b>-ing</b> (the <b>to</b> is a "
            "preposition). It is the standard email closing formula.</div>",
      tags="c1-c2 register cloze")

tabla(UP, ["B1 (basic)", "B2 (better)", "C1 (advanced)", "C2 (elegant)"],
     [["very good", "really good", "excellent", "outstanding"],
      ["very bad", "really bad", "dreadful", "execrable"],
      ["very big", "enormous", "immense", "colossal"],
      ["very important", "vital", "essential", "of vital importance"],
      ["very difficult", "complicated", "arduous", "strenuous"],
      ["very interesting", "fascinating", "compelling", "captivating"],
      ["a lot of", "much", "a considerable amount of", "a wealth of"],
      ["a few", "some", "no few", "no few"],
      ["I think", "in my opinion", "in my view", "if I may say so"],
      ["very good", "excellent", "outstanding", "outstanding"]],
     titulo="Upgrade table: how each level sounds",
     nivel="C1",
     nota="<b>Golden rule</b>: to move up a level do NOT add <i>very</i> in "
          "front of a strong adjective. Replace the adjective with a more "
          "precise one.")
