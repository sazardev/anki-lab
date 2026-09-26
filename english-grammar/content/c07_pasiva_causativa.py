"""07 Passive and Causative (B1-C2) - the passive in all tenses, passive
modals, have/get causatives and causative verbs."""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge

D = "07 Passive and Causative::"
DF, DT, DM, DC, DV = D + "Passive: Form", D + "Passive: When to Use It", \
    D + "Passive: Tenses and Modals", D + "Causative have/get", \
    D + "Causative Verbs"

# ================================================================== FORM

gap(DF, "The bridge ___ (build) in 1890.", "was built", nivel="B1",
    cue="passive, past", forma="was built",
    regla="<b>Passive</b> = <b>be + past participle</b>. The object of the "
          "active clause becomes the subject. The agent is expressed with "
          "<b>by</b>.",
    ejemplos=ex("The bridge <b>was built</b> in 1890.",
               "The window <b>was broken</b> by my brother."),
    notas=ul("Present: <b>am/is/are + participle</b>.",
             "Past: <b>was/were + participle</b>.",
             "With modals: <b>modal + be + participle</b>.",
             "The <b>agent</b> (who does the action) goes with <b>by</b> only if "
             "it matters; otherwise it is dropped."),
    tags="passive form")

gap(DF, "English ___ (speak) all over the world.", "is spoken", nivel="B1",
    cue="present passive", forma="is spoken",
    regla="<b>Present passive</b> = <b>am/is/are + participle</b>.",
    ejemplos=ex("English <b>is spoken</b> all over the world.",
               "The results <b>are announced</b> tomorrow."),
    notas="Very useful when the object is the <b>topic</b> and the agent is "
          "unknown or irrelevant.",
    tags="passive present")

gap(DF, "This letter ___ (must / sign) by the manager.", "must be signed",
    nivel="B2", cue="passive with a modal", forma="must be signed",
    regla="<b>Modal + be + participle</b>. The <b>be</b> always goes between "
          "the modal and the participle.",
    ejemplos=ex("This letter <b>must be signed</b> by the manager.",
               "The door <b>can't be opened</b> from outside."),
    notas="One of the most useful passive structures. Note: <b>must be + "
          "participle</b>, never <i>must been</i> or <i>must signed</i>.",
    tags="passive modal")

gap(DF, "The results ___ (announce / tomorrow) ___ (passive).", "will be announced",
    nivel="B2", cue="future passive", forma="will be announced",
    regla="<b>Future passive</b> = <b>will be + participle</b>.",
    ejemplos=ex("The results <b>will be announced</b> tomorrow.",
               "A new stadium <b>will be built</b> here."),
    notas="Also: <b>going to be + participle, must be + participle, should be + "
          "participle, could be + participle</b>.",
    tags="passive future")

# ========================================================== WHEN TO USE IT

gap(DT, "My bike ___ (steal) last night.", "was stolen", nivel="B1",
    cue="agent unknown", forma="was stolen",
    regla="Use the passive when the agent is <b>unknown, unimportant, or "
          "obvious</b>.",
    ejemplos=ex("My bike <b>was stolen</b>.", "He <b>was arrested</b> last week (the police, obviously)."),
    notas="As soon as you say <b>by</b> + a person, the <b>active</b> is usually "
          "better: <i>Someone <b>stole</b> my bike.</i>",
    tags="passive use")

gap(DT, "The report ___ (write) by the wrong team.", "was written",
    nivel="C1", cue="agent known but delayed", forma="was written",
    regla="The passive also <b>delays</b> the agent and gives prominence to the "
          "information.",
    ejemplos=ex("The report <b>was written</b> by the wrong team.",
               "<b>It is widely believed</b> that he is innocent."),
    notas="C1: <b>It is said/believed/reported/thought that...</b> — the "
          "impersonal passive for rumours and opinions.",
    tags="passive c1")

gap(DT, "___ (not / allow) smoking in this building.", "Smoking is not allowed",
    nivel="B1", cue="rules and signs", forma="Smoking is not allowed",
    regla="The passive is the language of <b>rules, notices and labels</b>.",
    ejemplos=ex("<b>Smoking is not allowed</b> here.",
               "<b>Photography is prohibited</b> in this museum."),
    notas="On signs: <b>No parking allowed / No entry / Employees only / Do not "
          "touch</b>.",
    tags="passive rules")

# ============================================================== TENSES

gap(DM, "The work ___ (finish) by next Friday.", "will have been finished",
    nivel="C1", cue="future perfect passive", forma="will have been finished",
    regla="<b>will have been + participle</b> = future perfect passive.",
    ejemplos=ex("The work <b>will have been finished</b> by Friday.",
               "By then, everything <b>will have been checked</b>."),
    notas="Also <b>should have been + participle</b> (passive reproach): "
          "<i>The email <b>should have been sent</b> yesterday.</i>",
    tags="passive future-perfect")

gap(DM, "He was told ___ (do / not / lie).", "not to lie", nivel="B2",
    cue="passive + to-infinitive", forma="not to lie",
    regla="<b>to + someone + to do</b> or <b>for someone + to do</b> replace the "
          "agent in the passive.",
    ejemplos=ex("He was told <b>not to lie</b>.", "She was asked <b>to wait</b> outside."),
    notas="Also: <b>It is easy/hard/difficult for someone <b>to</b> do</b>: "
          "<i>It's hard for me to concentrate.</i>",
    tags="passive to-infinitive")

gap(DM, "A new library ___ (build / last year). ___ (be / by the mayor).",
    "was built, was", nivel="C1", cue="chained passives", forma="was built, was",
    regla="When two passives are chained, the second takes <b>to</b>: "
          "<b>A new library was built <b>to be</b> used as a community centre.</b>",
    ejemplos=ex("The app was designed <b>to be</b> used by children.",
               "The building was renovated <b>to improve</b> safety."),
    notas="The active alternative: <b>They built a new library for people to "
          "use.</b>",
    tags="passive chained")

# ============================================================ CAUSATIVES

gap(DC, "I ___ my hair cut yesterday.", "had", nivel="B1",
    cue="causative (have/get + object + participle)", forma="had",
    regla="<b>have/get + object + participle</b> = 'have someone do something' "
          "(the subject does NOT do the action).",
    ejemplos=ex("I <b>had</b> my hair <b>cut</b>.",
               "She's having her car <b>repaired</b>."),
    notas=ul("A classic mistake is thinking <i>I had cut my hair</i> means 'I "
             "cut it myself'. If you do it yourself, use the <b>reflexive</b>: "
             "<i>I <b>cut</b> my hair.</i>",
             "The passive is obligatory here: <b>have + object + participle</b>. "
             "Never <i>have + to cut</i>.",
             "<b>get + object + participle</b> is more informal: <i>I'm going "
             "to get my windows <b>replaced</b>.</i>",
             "Also causative: <b>have someone <b>do</b></b> = make someone do: "
             "<i>I'll have the manager <b>call</b> you.</i>"),
    tags="causative have get")

gap(DC, "I'm going to ___ my flat painted before I move.", "get", nivel="B2",
    cue="causative, informal", forma="get painted",
    regla="<b>get + object + participle</b> = the same as <b>have</b>, more "
          "informal and slightly more necessary in tone.",
    ejemplos=ex("I'm going to <b>get</b> my flat <b>painted</b>.",
               "She's going to <b>get</b> her teeth <b>whitened</b>."),
    notas="When <b>you</b> do the work, use the <b>reflexive</b>: <i>I "
          "<b>painted</b> my flat myself.</i>",
    tags="causative get")

gap(DC, "I'll ___ the manager send you the contract.", "have", nivel="C1",
    cue="have someone do", forma="have",
    regla="<b>have someone do something</b> = make <b>another person</b> do it.",
    ejemplos=ex("I'll <b>have</b> the manager <b>send</b> you the contract.",
               "I had him <b>check</b> the figures."),
    notas="Here the second verb is a <b>base form</b> (not a participle): "
          "<i>have him <b>check</b></i> vs <i>have the contract <b>signed</b></i>.",
    tags="causative have-someone-do")

# ====================================================== CAUSATIVE VERBS

gap(DV, "The news ___ me cry.", "made", nivel="B2",
    cue="causative (make + object + base)", forma="made",
    regla="<b>make / let / help + object + base</b>.",
    ejemplos=ex("The news <b>made</b> me cry.", "My parents <b>made</b> me study."),
    notas=ul("After <b>make</b> in the past, the infinitive takes <b>to</b>: "
             "<i>She <b>made me to wait</b></i> (past) → <i>She <b>makes me "
             "wait</b></i> (present).",
             "<b>Let</b> does NOT change: <i>She <b>let</b> me <b>wait</b></i> "
             "(past) = <i>She <b>lets</b> me <b>wait</b></i> (present).",
             "<b>Help</b> allows <b>to</b>: <i>She <b>helped me to</b> (to) "
             "clean</i> = <i>helped me (to) clean</i>.",
             "<b>Help + object + V-ing</b> = help to do: <i>Can you help me "
             "<b>carry</b> this?</i>"),
    tags="causative make let help")

gap(DV, "My parents ___ me work harder.", "made", nivel="B2",
    cue="make + object + base (past)", forma="made",
    regla="<b>make + object + base</b> in the present; in the past, "
          "<b>to + base</b>.",
    ejemplos=ex("She <b>makes</b> me work harder.", "She <b>made</b> me <b>to wait</b>."),
    notas="One of the commonest B2 errors: <i>She <s>made me to wait</s> made me "
          "wait</i> (present) / <i>She made me <b>to</b> wait</i> (past).",
    tags="causative make to")

gap(DV, "The teacher ___ the students write an essay.", "let", nivel="B2",
    cue="let + object + base", forma="let",
    regla="<b>let + object + base</b> = allow. <b>Let</b> never takes <b>to</b>.",
    ejemplos=ex("The teacher <b>let</b> the students <b>write</b> an essay.",
               "His parents <b>let</b> him <b>stay</b> out late."),
    notas="<i>She <s>lets to go</s></i> is WRONG. Always: <b>lets me go</b>.",
    tags="causative let")

# =================================================================== CLOZE

cloze(DF, "The letter {{c1::must be signed}} by the manager.",
      extra="<div class='box rule'><span class='lbl'>Passive with a modal</span>"
            "<b>modal + be + participle</b>. The <b>be</b> goes between the modal "
            "and the participle. Never <i>must signed</i>.</div>",
      tags="c1-c2 passive cloze")

cloze(DC, "I had my hair {{c1::cut}}.",
      extra="<div class='box warn'><span class='lbl'>Causative vs reflexive</span>"
            "<b>have/get + object + participle</b> = someone <b>else</b> did it "
            "(at the hairdresser's). <b>cut my hair</b> (reflexive) = <b>I</b> "
            "did it.</div>",
      tags="c1-c2 causative cloze")
