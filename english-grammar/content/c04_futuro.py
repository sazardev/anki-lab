"""04 Future (B1-C2) - the five ways to talk about the future and when to
use each one."""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge

D = "04 Future::"
DF1, DF2, DF3, DF4 = D + "Will vs Going To", D + "Present and Past for the Future", \
    D + "Future Perfect", D + "Time Expressions"

# ===================================================================== WILL

gap(DF1, "I think it ___ rain tomorrow.", "will", nivel="B1",
    cue="opinion / spontaneous prediction", forma="will rain",
    regla="<b>will + base</b> for opinions, predictions, promises, threats, "
          "offers, requests and decisions made spontaneously.",
    ejemplos=ex("I think it <b>will</b> rain tomorrow.",
               "I'll help you (offer).", "I'll pay for it (promise)."),
    notas=ul("<b>will</b> = 100% with no commitment ('I will do it').",
             "Used for <b>decisions taken at the moment of speaking</b>: "
             "<i>The phone's ringing. — <b>I'll</b> answer it.</i>",
             "For predictions <b>based on data</b>, use <b>going to</b>.",
             "Negative: <b>won't</b> (not <i>will not</i> in speech)."),
    tags="will future")

gap(DF1, "Look at those dark clouds! It's ___ rain.", "going to", nivel="B1",
    cue="visible evidence now", forma="going to rain",
    regla="<b>going to + base</b> for predictions <b>based on present "
          "evidence</b> or for plans already decided.",
    ejemplos=ex("Look at those clouds — it's <b>going to rain</b>.",
               "She's <b>going to</b> study medicine (already decided)."),
    notas="<b>will</b> = no evidence. <b>going to</b> = evidence. In practice "
          "both are used almost interchangeably; <b>will</b> is safer in exams.",
    tags="going-to future")

gap(DF1, "I promise I ___ pay you back tomorrow.", "will", nivel="B1",
    cue="promise (a real commitment)", forma="will pay",
    regla="<b>Promises</b> with <b>will</b> or <b>shall</b> (formal/legal).",
    ejemplos=ex("I promise I <b>will</b> pay you back.",
               "I <b>shall</b> return the books on Monday (formal)."),
    notas="<b>shall</b> is only used for offers/help or in British legal "
          "language. With <i>I</i> it is archaic: use <i>will</i>.",
    tags="will promise")

gap(DF1, "The phone's ringing. — ___ , thanks.", "I'll get it", nivel="B1",
    cue="offer / spontaneous decision", forma="I'll get it",
    regla="Offers and decisions made at the moment of speaking → <b>I'll</b> + base.",
    ejemplos=ex("— The phone's ringing. — <b>I'll</b> get it.",
               "— We haven't got any bread. — <b>I'll</b> go and buy some."),
    notas="Answering an offer or a question, <b>will</b> is normally <b>not</b> "
          "used: <i>Would you like tea? — <s>Yes, I will</s>. Yes, please / "
          "Yes, I <b>would</b> (love to).</i>",
    tags="will offer")

# =================================================== PRESENT AND PAST FOR THE FUTURE

gap(DF2, "I ___ (go) to the cinema tomorrow.", "am going", nivel="B1",
    cue="a plan already made", forma="am going",
    regla="<b>Present Simple</b> for timetables and calendars: timetables, "
          "public transport, sports fixtures, fixed appointments.",
    ejemplos=ex("The train <b>leaves</b> at 7 tomorrow.",
               "The film <b>starts</b> at 9:30."),
    notas="If you add <b>with my friends, because, on Monday + a place</b>, use "
          "<b>going to</b> or the continuous. If you say <b>at 7 / next / when "
          "the train arrives</b>, use the <b>Present Simple</b>.",
    tags="future present-simple timetables")

gap(DF2, "I'm ___ (meet) my boss at 3pm tomorrow.", "meeting", nivel="B1",
    cue="a fixed arrangement", forma="meeting",
    regla="<b>Present Continuous</b> for <b>arrangements and plans</b> with "
          "someone.",
    ejemplos=ex("I'm <b>meeting</b> the client at 3.",
               "She's <b>flying</b> to Rome tomorrow morning."),
    notas="It is the most formal and business-like future: emails and meetings.",
    tags="future continuous arrangements")

gap(DF2, "What ___ you ___ (do) this weekend?", "are, doing", nivel="B1",
    cue="plans", forma="are doing",
    regla="Questions about forthcoming plans → <b>Present Continuous</b>.",
    ejemplos=ex("What <b>are you doing</b> this weekend?", "<b>Are</b> you <b>coming</b> tonight?"),
    notas="If it is an <b>agreement</b>, use the <b>Present Simple</b>: "
          "<i>Are you coming? — Yes, <b>I'm coming</b>. (decided) / <i>I think "
          "<b>I'll</b> come.</i> (not decided yet)</i>",
    tags="future continuous plans")

gap(DF2, "I was going to call you, but I forgot.", "was going to", nivel="C1",
    cue="a past intention that never happened", forma="was going to",
    regla="<b>was/were going to</b> = a past intention that was interrupted.",
    ejemplos=ex("I <b>was going to</b> call you but I forgot.",
               "She <b>was going to</b> move abroad but changed her mind."),
    notas="Very useful for talking about the past: <i>I <b>was going to</b> "
          "study medicine, but I changed my mind.</i>",
    tags="was-going-to intention")

gap(DF2, "I used to smoke, but I ___ (stop) two years ago.", "stopped",
    nivel="B2", cue="a past habit that is over", forma="stopped",
    regla="<b>used to + base</b> = an abandoned past habit. Negative: "
          "<b>didn't use to</b>.",
    ejemplos=ex("I <b>used to smoke</b> but I stopped.",
               "She <b>didn't use to like</b> sushi."),
    notas=ul("<b>used to</b> also = 'there used to be' for states: "
             "<i>There <b>used to be</b> a cinema here.</i>",
             "<b>be used to + noun/V-ing</b> = 'be used to': "
             "<i>I'm <b>used to getting</b> up early.</i> (completely different).",
             "<b>use to</b> (without -d) exists but is informal: "
             "<i>I use to live in Rome.</i>"),
    tags="used-to habits")

# ========================================================== FUTURE PERFECT

gap(DF3, "By June, I ___ (live) here for ten years.", "will have lived",
    nivel="C1", cue="projected future duration", forma="will have lived",
    regla="<b>Future Perfect</b> = <b>will have + participle</b>. Projects the "
          "past from the future. With <b>by + time, by the time, in + future, "
          "before</b>.",
    ejemplos=ex("By June I <b>will have lived</b> here for ten years.",
               "By the time you arrive, I <b>will have finished</b>."),
    notas="Used for predictions: <i>By 2030, most people <b>will have "
          "stopped</b> using cash.</i>",
    tags="future-perfect")

gap(DF3, "By next year you ___ (work) here for 20 years.", "will have been working",
    nivel="C1", cue="projected future duration (emphatic)",
    forma="will have been working",
    regla="<b>Future Perfect Continuous</b> = <b>will have been + V-ing</b>. "
          "Projects the duration.",
    ejemplos=ex("By next year I <b>will have been working</b> here for 20 years.",
               "By tomorrow, it <b>will have been raining</b> all day."),
    notas="In the negative it is the only way to <b>cancel</b> a plan: "
          "<i>By Friday she <b>will have finished</b> — actually, she <b>won't "
          "have finished</b>.</i>",
    tags="future-perfect-continuous")

# ========================================================= TIME EXPRESSIONS

gap(DF4, "The train ___ (leave) in 5 minutes.", "is going to leave",
    nivel="B1", cue="imminent", forma="is going to leave",
    regla="<b>in + period</b> (in 5 minutes, in a week, in 2025) → future. "
          "<b>after</b> + past = future. <b>until/till</b> = up to.",
    ejemplos=ex("The train <b>is going to leave</b> in 5 minutes.",
               "I'll call you <b>after</b> I <b>get</b> home.",
               "Wait <b>until</b> I <b>say</b> stop."),
    notas="<b>Until / till</b> only with the meaning 'up to': <i>I'll wait "
          "<b>until</b> tomorrow.</i> With <b>while</b>: <i>It was raining "
          "<b>while</b> we were at the cinema.</i>",
    tags="future time-expressions")

gap(DF4, "This time next year I ___ (live) in Berlin.", "will be living",
    nivel="C1", cue="projection in progress", forma="will be living",
    regla="<b>will be + V-ing</b> = an action in progress at a future point.",
    ejemplos=ex("This time next year I <b>will be living</b> in Berlin.",
               "At 9pm tomorrow, they <b>will be sleeping</b>."),
    notas="For <b>projections at the moment of speaking</b>: <i><b>will be</b></i> "
          "(not the continuous).</i>",
    tags="will-be-doing projection")

gap(DF4, "I promise I ___ (not / forget) the keys.", "won't forget", nivel="B1",
    cue="promise in the negative", forma="won't forget",
    regla="<b>won't = will not</b>. In the negative, <b>going to</b> cannot be "
          "used for promises.",
    ejemplos=ex("I promise I <b>won't forget</b> the keys.", "I <b>won't be</b> late (promise)."),
    notas="<b>Will not</b> = will not / a decision or promise. "
          "<b>Not going to</b> = plan cancelled: <i>I'm <b>not going to</b> "
          "wear that.</i>",
    tags="will-not negative")

tabla(DF1, ["Situation", "Form", "Example"],
     [["Spontaneous decision / offer / promise", "<b>will</b>",
       "<i>— It's cold. — <b>I'll close</b> the window.</i>"],
      ["Prediction with no evidence", "<b>will</b>",
       "<i>I think she <b>will pass</b> the exam.</i>"],
      ["Prediction with evidence", "<b>going to</b>",
       "<i>Look at the sky — it's <b>going to</b> storm.</i>"],
      ["Plan already decided", "<b>going to</b>",
       "<i>I'm <b>going to</b> start a new job in June.</i>"],
      ["Timetable / transport / fixed event", "<b>Present Simple</b>",
       "<i>The bus <b>leaves</b> at 6. / The shop <b>opens</b> at 9.</i>"],
      ["Agreed arrangement", "<b>Present Continuous</b>",
       "<i>I'm <b>seeing</b> the dentist on Monday.</i>"],
      ["Plans in general (questions)", "<b>Present Continuous</b>",
       "<i>What <b>are you doing</b> tonight?</i>"],
      ["Projection with future duration", "<b>Future Perfect</b>",
       "<i>By 2030 I <b>will have finished</b> my degree.</i>"],
      ["Abandoned past habit", "<b>used to</b>", "<i>I <b>used to</b> live in Berlin.</i>"],
      ["Past intention that never happened", "<b>was going to</b>",
       "<i>I <b>was going to</b> call but I forgot.</i>"]],
     titulo="Which future form to use: a decision table",
     nivel="B1",
     nota="If you master this table, the future stops being a problem. 90% of "
          "B1 future errors are <b>timetables with going to</b> or "
          "<b>promises with going to</b>.")

cloze(DF1, "— The phone's ringing! — {{c1::I'll}} get it.",
      extra="<div class='box rule'><span class='lbl'>will = decision at the moment</span>"
            "If the decision is taken <b>after</b> the conversation starts, it "
            "is <b>will</b>. If it was already taken, use <b>going to</b> or the "
            "<b>Present Simple</b>.</div>",
      tags="c1-c2 will future cloze")
