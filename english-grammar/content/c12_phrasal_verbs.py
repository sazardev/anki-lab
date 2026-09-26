"""12 Phrasal Verbs (B1-C2) - verbs with a particle, separable and
inseparable, and particles with their own meaning."""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "12 Phrasal Verbs::"
P1, P2, P3, P4 = D + "Separable", D + "Inseparable", \
    D + "Particles with Meaning", D + "Fixed Combinations"

# ============================================================== SEPARABLE

serie_gap(P1, [
    ("Turn ___ the lights.", "off", "switch off",
     "Separable: the object can go <b>between</b> verb and particle or "
     "<b>after</b> it.",
     ex("Turn <b>off</b> the lights. / Turn the lights <b>off</b>.")),
    ("Please ___ up the music.", "turn", "turn up",
     "<b>turn up / turn down / turn on / turn off</b> + the object.",
     ex("Turn <b>up</b> the TV. / Turn the volume <b>down</b>.")),
    ("Please ___ down the volume.", "turn", "turn down",
     "<b>turn down</b> = lower the volume. <b>turn up</b> = raise it.",
     ex("Can you <b>turn down</b> the music? / <b>Turn it down</b>, please.")),
    ("Can you ___ up the volume?", "turn", "turn up",
     "<b>turn up</b> = raise. Without an object it means 'turn up the volume'.",
     ex("Turn <b>up</b> the radio. / It was hard to <b>turn up</b>.")),
    ("I'm trying to ___ out the meaning.", "find", "find out",
     "<b>find out / work out / sort out / figure out</b> + object.",
     ex("I need to <b>find out</b> the truth. / <b>Figure it out</b>.")),
    ("I need to ___ out how much it costs.", "work", "work out",
     "<b>work out</b> = calculate, solve, exercise.",
     ex("<b>Work out</b> the answer. / She <b>worked out</b> the problem.")),
    ("Let's ___ out the details tomorrow.", "sort", "sort out",
     "<b>sort out</b> = clarify, organise, resolve.",
     ex("We need to <b>sort out</b> the mess. / <b>Sort it out</b>.")),
    ("She tried to ___ up an excuse.", "make", "make up",
     "<b>make up</b> (an excuse, a story) = invent. <b>make up</b> (the face) = "
     "put on make-up.",
     ex("He <b>made up</b> a story. / She <b>made up</b> her face.")),
    ("They ___ up after two years.", "fell", "fall out",
     "<b>fall out with someone</b> = have a row.",
     ex("They <b>fell out</b> with each other. / She <b>fell out with</b> him.")),
    ("He ___ off sleeping during the lecture.", "dozed", "doze off",
     "<b>doze off / nod off / fall asleep</b>.",
     ex("He <b>dozed off</b> in class. / I <b>nodded off</b> at 3pm.")),
    ("I can't ___ on this laptop.", "rely", "rely on",
     "<b>rely on / count on / depend on</b>.",
     ex("I <b>rely on</b> you. / We <b>count on</b> your help.")),
    ("Please ___ off your shoes.", "take", "take off",
     "<b>take off</b> = remove (clothes). <b>put on</b> = put on.",
     ex("<b>Take off</b> your jacket. / <b>Put on</b> your shoes.")),
    ("He ___ out the light before leaving.", "switched", "switch off",
     "<b>switch off / turn off / put out</b> = to put out.",
     ex("<b>Switch off</b> the TV. / <b>Put out</b> the candle.")),
    ("Let's ___ up a meeting for Friday.", "set", "set up",
     "<b>set up / set out / set off</b>.",
     ex("Let's <b>set up</b> a call. / She <b>set up</b> her own company.")),
    ("The teacher ___ out a task.", "handed", "hand out",
     "<b>hand out / hand over / hand in</b>.",
     ex("<b>Hand out</b> the leaflets. / <b>Hand in</b> your homework.")),
    ("Please ___ off the light when you leave.", "turn", "turn off",
     "<b>turn off</b> — in the imperative the object follows.",
     ex("<b>Turn off</b> the light. / <b>Turn the light off</b>.")),
    ("Can you ___ me up at 6?", "wake", "wake up",
     "<b>wake up</b> = to wake. It is <b>reflexive</b>: <i>I wake up at 6</i>.",
     ex("She <b>woke me up</b> at 6. / I <b>wake up</b> early.")),
    ("She ___ to when she saw the bill.", "reacted", "react to",
     "<b>react badly to</b> = react badly to.",
     ex("He <b>reacted badly to</b> the news.")),
    ("They've ___ out the difference in prices.", "pointed", "point out",
     "<b>point out</b> = to point out / to draw attention to.",
     ex("She <b>pointed out</b> that we were late.")),
    ("I need to ___ up on my Spanish.", "catch", "catch up on",
     "<b>catch up on + subject matter</b>. <b>catch up with</b> + person.",
     ex("I need to <b>catch up on</b> my sleep. / <b>Catch up with</b> the others.")),
], nivel="B1", tags=["phrasal-verb separable"])

# =========================================================== INSEPARABLE

serie_gap(P2, [
    ("I look ___ to my teacher.", "up", "look up to",
     "Inseparable: the particle <b>always</b> follows the verb, and it "
     "<b>always</b> takes a preposition.",
     ex("<b>Look up</b> the word in a dictionary. / She <b>looks up to</b> her parents.")),
    ("I can't ___ on the exam.", "pass", "pass an exam",
     "<b>pass an exam</b> = to pass. <b>fail an exam</b> = to fail.",
     ex("She <b>passed</b> the exam. / He <b>failed</b> his driving test.")),
    ("I can't ___ with him.", "put", "put up with",
     "<b>put up with</b> = tolerate. NEVER <i>put with</i>.",
     ex("I can't <b>put up with</b> the noise. / She <b>puts up with</b> a lot.")),
    ("He ___ off work at 5.", "gets", "get off work",
     "<b>get off</b> (finish work) / <b>get on</b> (board a vehicle).",
     ex("I <b>get off</b> work at 5. / <b>Get on</b> the bus at the stop.")),
    ("She ___ up with a great job.", "came", "come up with",
     "<b>come up with</b> = have an idea. <b>come across</b> = meet by chance.",
     ex("She <b>came up with</b> the idea. / I <b>came across</b> your book.")),
    ("The meeting was ___ off.", "called", "call off",
     "<b>call off</b> = cancel. <b>call on</b> = visit someone. "
     "<b>call in</b> = phone the company.",
     ex("They <b>called off</b> the meeting. / She <b>called on</b> me.")),
    ("We're ___ out for dinner.", "going", "go out",
     "<b>go out / go over / go through / go on</b>.",
     ex("We <b>go out</b> on Fridays. / She's <b>going over</b> to London.")),
    ("The plan didn't ___ up.", "work", "work out",
     "<b>work out</b> (to work well) is easily confused with <b>work out</b> "
     "(to calculate). With <b>there is no / it doesn't</b> = to function.",
     ex("Everything <b>worked out</b> fine. / The plan <b>didn't work out</b>.")),
    ("Let's ___ on with the meeting.", "carry", "carry on",
     "<b>carry on + V-ing</b> = continue. <b>keep on + V-ing</b> = keep on "
     "doing something repeatedly.",
     ex("Let's <b>carry on</b> with the work. / She <b>kept on asking</b> questions.")),
    ("He belongs ___ the club.", "to", "belong to",
     "<b>belong to</b> is inseparable. NEVER <i>belong in</i> (though 'belong "
     "in' is heard informally for places).",
     ex("He <b>belongs to</b> the club. / It <b>belongs to</b> me.")),
    ("She takes ___ her studies.", "seriously", "take seriously",
     "<b>take ... seriously, take ... for granted, take advantage of, take "
     "care of, take part in, take place, take turns</b>.",
     ex("She <b>takes her studies seriously</b>. / He <b>took advantage of</b> the offer.")),
    ("I need to ___ after my dog.", "look", "look after",
     "<b>look after</b> = care for. <b>look for</b> = search for. "
     "<b>look forward to</b> = await.",
     ex("She <b>looks after</b> her cat. / I'm <b>looking for</b> my keys.")),
    ("The plane took ___ three hours late.", "off", "take off",
     "<b>take off</b> = to take off (a plane). Different from <i>take off "
     "clothes</i> (to remove).",
     ex("The plane <b>took off</b> at 6. / <b>Take off</b> your shoes.")),
    ("He ran ___ of time and missed the bus.", "out", "run out of",
     "<b>run out of + noun</b> = run out. <b>run out</b> (without <b>of</b>) = "
     "run out of time.",
     ex("We <b>ran out of</b> milk. / Time is <b>running out</b>.")),
    ("She's been ___ on for 3 hours.", "on", "insist on",
     "<b>insist on + noun/V-ing</b>. NEVER <i>insist to</i>.",
     ex("She <b>insisted on paying</b>. / He <b>insists on seeing you</b>.")),
    ("I agree ___ you completely.", "with", "agree with",
     "<b>agree with</b> = agree with a person. <b>agree to</b> = accept a "
     "proposal. <b>agree on</b> = settle a price.",
     ex("I <b>agree with</b> you. / We <b>agreed to</b> the plan. / "
        "<b>agreed on</b> a price.")),
], nivel="B2", tags=["phrasal-verb inseparable"])

# ==================================== PARTICLES WITH THEIR OWN MEANING

serie_gap(P3, [
    ("Look ___ the word in a dictionary.", "up", "look up",
     "<b>look up</b> = consult. <b>look after</b> = care for. <b>look for</b> "
     "= search for. <b>look into</b> = investigate. <b>look forward to</b> = "
     "await with pleasure.",
     ex("<b>Look up</b> a word. / <b>Look into</b> the problem.")),
    ("The company is looking ___ new markets.", "into", "look into",
     "<b>look into</b> = investigate thoroughly. NEVER <i>investigate for</i>.",
     ex("They're <b>looking into</b> the complaints.")),
    ("The kids were jumping ___ with excitement.", "up", "jump up",
     "<b>up</b> with emotion verbs = with great intensity: <b>jump up, cheer "
     "up, brighten up, perk up, warm up, dress up</b>.",
     ex("She <b>cheered up</b> when she heard. / <b>Dress up</b> = to dress up.")),
    ("Let's ___ up the meeting until 3pm.", "put", "put off",
     "<b>put off</b> = postpone. <b>put on</b> = put on. <b>put up with</b> = "
     "tolerate. <b>put out</b> = extinguish. <b>put up</b> = erect.",
     ex("They <b>put off</b> the meeting. / <b>Put up</b> a poster.")),
    ("The fire was finally ___ out.", "put", "put out",
     "<b>put out</b> = extinguish (fire, candle). <b>turn off</b> = switch off "
     "(machines, lights).",
     ex("<b>Put out</b> the fire. / <b>Turn off</b> the TV.")),
    ("She knows ___ to be polite.", "up", "know how",
     "<b>know / find / get / work out + how + clause</b> = to know how.",
     ex("I don't <b>know how to</b> drive. / <b>Find out how to</b> do it.")),
    ("He's fed ___ with his boss.", "up", "fed up with",
     "<b>fed up with + noun/V-ing</b> = fed up (AmE). BrE: <b>fed up with/of</b>.",
     ex("I'm <b>fed up with</b> the rain. / <b>Tired of</b> waiting.")),
    ("The plane is coming ___ .", "in", "come in",
     "<b>come in</b> = to come in. <b>come on</b> = come on. <b>come out</b> = "
     "come out. <b>come across</b> = come across. <b>come up with</b> = have an "
     "idea.",
     ex("She <b>came in</b> and sat down. / <b>Come up with</b> an idea.")),
    ("He's really ___ about the new project.", "keen", "keen on",
     "<b>keen on</b> = keen on. <b>keen to do</b>. <b>upset about</b> = upset "
     "about. <b>excited about</b> = excited about.",
     ex("She's <b>keen on</b> swimming. / He's <b>upset about</b> the news.")),
    ("He won't ___ down.", "give", "give up",
     "<b>give up</b> = give up. <b>give in</b> = give in. <b>give away</b> = "
     "give away. <b>give back</b> = give back.",
     ex("Don't <b>give up</b>! / <b>Give in</b> to temptation.")),
    ("She gave ___ her password to a stranger.", "away", "give away",
     "<b>give away</b> = reveal a secret, or give as a gift.",
     ex("He <b>gave away</b> the ending. / <b>Give it away</b> = it's a gift.")),
    ("We're ___ down the blame on others.", "put", "put the blame on",
     "<b>put the blame on someone, put up with, put off</b>.",
     ex("He <b>put the blame on</b> me. / Don't <b>put up with</b> it.")),
    ("She broke ___ laughing.", "out", "burst out",
     "<b>burst out laughing, break out, break up, break down, break in</b>.",
     ex("They <b>broke out laughing</b>. / <b>Break down</b> = to break down.")),
    ("The engine ___ down in the middle of the road.", "broke", "break down",
     "<b>break down</b> = break down (a machine) / to break down (a person). "
     "<b>break out</b> = break out. <b>break up</b> = break up. "
     "<b>break into</b> = break into.",
     ex("The car <b>broke down</b>. / She <b>broke down</b> and cried.")),
    ("The negotiations ___ down last week.", "broke", "break down",
     "<b>break down</b> = break down (negotiations, relationships, health).",
     ex("Talks <b>broke down</b>. / They <b>broke off</b> the engagement.")),
    ("He suddenly ___ out laughing in the meeting.", "burst", "burst out",
     "<b>burst out laughing / burst into tears / burst out</b> = to burst out.",
     ex("She <b>burst into tears</b>. / He <b>burst out laughing</b>.")),
    ("Let's ___ up the meeting a bit.", "put", "put off",
     "<b>put off</b> = to put off.",
     ex("They <b>put off</b> the meeting until Friday.")),
    ("She turned ___ the offer.", "down", "turn down",
     "<b>turn down</b> = turn down (an offer) / turn down (the volume). "
     "<b>turn up</b> = turn up (arrive earlier). <b>turn into</b> = turn into.",
     ex("She <b>turned down</b> the job offer. / He <b>turned into</b> a celebrity.")),
], nivel="B2", tags=["phrasal-verb particle"])

# ================================================== CRITICAL FIXED COMBINATIONS

serie_gap(P4, [
    ("I need to ___ up with this headache.", "put", "put up with",
     "<b>put up with</b> = tolerate. Never separated.",
     ex("I can't <b>put up with</b> the noise.")),
    ("She was ___ out by the time we arrived.", "worn", "worn out",
     "<b>worn out</b> = worn out. <b>used up</b> = used up. <b>fed up</b> = fed up.",
     ex("She was completely <b>worn out</b>.")),
    ("The meeting was ___ off until next week.", "put", "put off",
     "<b>put off</b> = put off. <b>put on</b> = put on. <b>put away</b> = put away.",
     ex("The match was <b>put off</b> due to rain.")),
    ("Can you ___ after my plants while I'm away?", "look", "look after",
     "<b>look after</b> = look after. <b>look for</b> = look for. "
     "<b>look forward to</b> = look forward to.",
     ex("Can you <b>look after</b> my dog?")),
    ("I'm really looking ___ to the weekend.", "forward", "look forward to",
     "<b>look forward to + noun/V-ing</b>. NEVER <i>to + V</i>.",
     ex("I <b>look forward to hearing</b> from you.")),
    ("He filled ___ the form and signed it.", "in", "fill in",
     "<b>fill in / fill out / fill up</b> = fill in.",
     ex("<b>Fill in</b> the form. / She <b>filled out</b> the application.")),
    ("The plane is taking ___ in ten minutes.", "off", "take off",
     "<b>take off</b> = take off / take off (clothes). <b>take over</b> = take "
     "over. <b>take up</b> = take up (a hobby).",
     ex("The plane <b>took off</b>. / She <b>took up</b> running.")),
    ("She's thinking of taking ___ a new sport.", "up", "take up",
     "<b>take up</b> = take up an activity. <b>take over</b> = take over a role.",
     ex("He <b>took up</b> golf last year.")),
    ("Let me ___ this to you.", "point", "point out",
     "<b>put up with, point out, get on with, come up with, do without, go "
     "without, rule out, set up, work out</b>.",
     ex("Let me <b>point out</b> that we disagree.")),
    ("I can ___ with it for a while.", "do", "do without",
     "<b>do without / go without / manage without</b> = do without.",
     ex("We <b>do without</b> a car.")),
    ("We should ___ out the plan before the meeting.", "rule", "rule out",
     "<b>rule out</b> = rule out (a possibility).",
     ex("We can't <b>rule out</b> rain.")),
    ("Let's ___ the drinks for the party.", "set", "set up",
     "<b>set up / set off / set out</b>.",
     ex("They <b>set out</b> early. / <b>Set up</b> a meeting.")),
    ("She's really ___ up with her studies.", "fed", "fed up with",
     "<b>fed up with + noun/V-ing</b> = fed up with.",
     ex("I'm <b>fed up with</b> waiting.")),
    ("We need to ___ down the price a bit.", "bring", "bring down",
     "<b>bring down / cut down on / cut off / turn down / knock down</b>.",
     ex("<b>Cut down on</b> sugar. / They <b>cut off</b> electricity.")),
    ("I can't ___ the idea of leaving.", "stand", "can't stand",
     "<b>can't stand</b> = can't stand. <b>can't bear + V-ing</b>. "
     "<b>can't get enough of</b>.",
     ex("I <b>can't stand</b> the heat. / <b>Can't bear waiting</b>.")),
], nivel="C1", tags=["phrasal-verb fixed"])

# =================================================================== CLOZE

cloze(P1, "Turn {{c1::off}} the lights. / Turn the lights {{c1::off}}.",
      extra="<div class='box rule'><span class='lbl'>Separable</span>"
            "If the object is a <b>pronoun</b>, it always goes <b>between</b> "
            "verb and particle: <i>turn <b>it off</b></i>. If it is a noun, it "
            "can go anywhere: <i>turn off the lights</i> or <i>turn the lights "
            "off</i>.</div>",
      tags="c1-c2 phrasal cloze")

cloze(P2, "I can't {{c1::put up with}} this noise any more.",
      extra="<div class='box warn'><span class='lbl'>Inseparable</span>"
            "<b>put up with</b> = put up with. <b>look up</b> = look up. "
            "<b>get on with</b> = get on with. Never separated.</div>",
      tags="c1-c2 phrasal cloze")

tabla(P1, ["Verb", "Meaning", "Separable?"],
     [["<b>turn on / off</b>", "switch on / off", "yes"],
      ["<b>put off</b>", "postpone", "yes"],
      ["<b>put up with</b>", "tolerate", "<b>no</b>"],
      ["<b>look up</b>", "consult (a dictionary)", "no"],
      ["<b>look after</b>", "care for", "no"],
      ["<b>look forward to</b>", "await with pleasure", "no"],
      ["<b>give up</b>", "give up", "no"],
      ["<b>show off</b>", "show off", "yes"],
      ["<b>break down</b>", "break down", "no"],
      ["<b>call off</b>", "cancel", "no"],
      ["<b>come up with</b>", "have an idea", "no"],
      ["<b>get on with</b>", "get on with", "no"],
      ["<b>find out</b>", "find out", "yes"],
      ["<b>work out</b>", "calculate / function", "yes"],
      ["<b>turn down</b>", "reject / lower", "yes"],
      ["<b>take off</b>", "remove / take off", "yes"],
      ["<b>take after</b>", "take after (a parent)", "no"],
      ["<b>run out of</b>", "run out of", "no"],
      ["<b>set up</b>", "set up / arrange", "yes"],
      ["<b>sort out</b>", "sort out", "yes"],
      ["<b>make up</b>", "invent / put on make-up", "yes"],
      ["<b>do without</b>", "do without", "no"],
      ["<b>fed up with</b>", "fed up with", "no"],
      ["<b>look into</b>", "look into", "no"]],
     titulo="Phrasal verbs: separable or not (reference list)",
     nivel="B1",
     nota=ul("<b>Separable</b> = the object can go in the middle. "
             "<b>Inseparable</b> = always together.",
             "Look at the <b>particle</b> (<b>off, up, in, out, on, over, "
             "through</b>): if it is a real adverb, the verb is usually "
             "separable.",
             "<b>Object pronouns</b> always go in the middle with separable "
             "verbs: <i>turn <b>it</b> off</i>, never <i>turn off it</i>."))
