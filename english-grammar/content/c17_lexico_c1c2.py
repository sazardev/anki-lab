"""17 Lexis (C1-C2) - suffixes and prefixes, false friends, precise
opposites, compound nouns and high-level adjectives."""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "17 Lexis (C1-C2)::"
S, P, FO, OP, CP = D + "Suffixes and Prefixes", D + "False Friends", \
    D + "Precise Opposites", D + "Compound Nouns", \
    D + "High-level Adjectives"

# ================================================ SUFFIXES AND PREFIXES

tabla(S, ["Suffix", "Meaning", "Example"],
     [["-tion / -sion / -ment", "action or result",
       "<b>ac<b>tion</b></b>, deci<b>sion</b>, argu<b>ment</b>, "
       "<b>develop<b>ment</b></b>, treat<b>ment</b>"],
      ["-ity / -ty", "quality or state",
       "qual<b>ity</b>, safe<b>ty</b>, responsi<b>bility</b>, "
       "abund<b>ance</b> / abundan<b>cy</b>, capa<b>city</b>"],
      ["-ness", "quality",
       "kind<b>ness</b>, dark<b>ness</b>, willing<b>ness</b>, selfish<b>ness</b>"],
      ["-ment / -ant / -ent / -ee / -er", "the person who does it",
       "govern<b>ment</b>, assist<b>ant</b>, compet<b>ent</b>, "
       "employ<b>ee</b> / employ<b>er</b>"],
      ["-ful / -less", "full of / without",
       "beaut<b>iful</b>, success<b>ful</b>, use<b>less</b>, hope<b>less</b>, "
       "care<b>less</b>"],
      ["-ive / -ous / -ious", "having the quality of",
       "creat<b>ive</b>, expans<b>ive</b>, danger<b>ous</b>, ser<b>ious</b>, "
       "prev<b>ious</b>"],
      ["-able / -ible", "that can be",
       "read<b>able</b>, comfort<b>able</b>, flex<b>ible</b>, respons<b>ible</b>"],
      ["-al / -ial", "related to",
       "natur<b>al</b>, person<b>al</b>, financ<b>ial</b>, polit<b>ical</b>"],
      ["-ic / -ical / -ish / -y", "related to / slightly / quality",
       "econom<b>ic</b>, techn<b>ical</b>, child<b>ish</b>, self<b>ish</b>, "
       "rain<b>y</b>, honest<b>y</b>"],
      ["-ly", "in a ... way (adverb from adjective)",
       "quick<b>ly</b>, care<b>ful</b>ly, real<b>ly</b>, prob<b>ably</b>"],
      ["-ise / -ify", "to make into",
       "modern<b>ise</b>, real<b>ise</b>, simpl<b>ify</b>, legal<b>ise</b>, "
       "fertil<b>ise</b>"],
      ["-en", "to make / to become",
       "short<b>en</b>, length<b>en</b>, widen, strength<b>en</b>, dark<b>en</b>"],
      ["un- / in- / im- / il- / ir-", "negation",
       "<b>un</b>happy, <b>in</b>correct, <b>im</b>possible, <b>il</b>legal, "
       "<b>ir</b>regular, <b>un</b>believable"]],
     titulo="Suffixes and prefixes: the fast way to decode new words",
     nivel="C1",
     nota=ul("<b>If you know the suffix</b>, you already have 60% of the meaning "
             "of a word you have never seen. It is the most profitable skill of "
             "an English reader.",
             "<b>Key prefixes</b>: <b>re-</b> (repeat: rewrite, rebuild), "
             "<b>pre-</b> (before: preview, pre-war), <b>over-</b> (too much: "
             "overwork, overestimate), <b>under-</b> (insufficient: "
             "underestimate, underpaid), <b>dis-</b> (negation: dislike, "
             "disable), <b>mis-</b> (wrong: mistake, mislead).",
             "<b>Suffix errors</b>: <i>an <b>unhappiness</b></i> is wrong; "
             "<b>unhappiness</b> is right. <i>irregular<b>ity</b></i> is wrong; "
             "<b>irregularity</b> is right."))

serie_gap(S, [
    ("The situation is really ___ .", "tense", "tense",
     "C1 adjectives for emotional atmosphere: <b>tense, uneasy, awkward, "
     "strained, fraught, charged, draining, exhausting, rewarding, "
     "fulfilling</b>.",
     ex("The situation is <b>tense</b>. / a <b>fraught</b> situation / "
        "a <b>draining</b> week / a <b>rewarding</b> experience")),
    ("The project was a ___ experience.", "rewarding", "rewarding",
     "<b>rewarding, fulfilling, enlightening, worthwhile, gratifying, "
     "uneventful, mundane, tedious, gruelling</b>.",
     ex("The project was a <b>rewarding</b> experience. / a <b>demanding</b> "
        "course / a <b>mundane</b> task / a <b>thought-provoking</b> talk")),
    ("The negotiations were ___ .", "fraught", "fraught with difficulties",
     "<b>Fraught with</b> = full of (problems, risks). <b>Tense</b> = tense. "
     "<b>Awkward</b> = forced, uncomfortable.",
     ex("The negotiations were <b>fraught with</b> difficulties. / "
        "an <b>awkward</b> silence / a <b>tense</b> atmosphere")),
    ("She gave a ___ speech.", "inspiring", "inspiring",
     "<b>inspiring, moving, heartwarming, touching, thought-provoking, "
     "gripping, compelling, persuasive, eloquent</b>.",
     ex("She gave an <b>inspiring</b> speech. / a <b>thought-provoking</b> "
        "lecture / a <b>compelling</b> story / an <b>eloquent</b> speaker")),
    ("The topic is rather ___ .", "sensitive", "a sensitive issue",
     "<b>sensitive, controversial, contentious, thorny, delicate, "
     "polarising, subjective, impartial</b>.",
     ex("The topic is rather <b>sensitive</b>. / a <b>controversial</b> issue / "
        "a <b>polarising</b> debate / an <b>impartial</b> judge")),
    ("His explanation was ___ .", "convoluted", "convoluted",
     "<b>convoluted, intricate, elaborate, straightforward, lucid, cogent, "
     "obscure, abstruse, terse, succinct</b>.",
     ex("His explanation was <b>convoluted</b>. / a <b>straightforward</b> "
        "answer / a <b>cogent</b> argument / a <b>succinct</b> summary")),
    ("The results were ___ .", "disappointing", "disappointing",
     "<b>disappointing, underwhelming, mixed, modest, remarkable, astounding, "
     "staggering, notable</b>.",
     ex("The results were <b>disappointing</b>. / <b>underwhelming</b> / "
        "<b>astounding</b> / <b>staggering</b> growth")),
    ("The situation is ___ . We must act now.", "critical", "critical",
     "<b>critical, pressing, urgent, paramount, grave, dire, precarious, "
     "stable, sustainable</b>.",
     ex("The situation is <b>critical</b>. We must act now. / a <b>pressing</b> "
        "issue / a <b>precarious</b> position / a <b>sustainable</b> solution")),
    ("She made a ___ remark.", "tactless", "tactless",
     "<b>tactless, diplomatic, insensitive, thoughtful, considerate, "
     "outspoken, candid, blunt, rude</b>.",
     ex("She made a <b>tactless</b> remark. / a <b>diplomatic</b> answer / "
        "a <b>considerate</b> gesture / an <b>outspoken</b> critic")),
    ("The company is doing ___ financially.", "well", "doing well",
     "<b>well, badly, poorly, satisfactorily</b> (adverbs after <b>doing</b>/"
     "<b>going</b>).",
     ex("The company is doing <b>well</b> financially. / doing <b>badly</b> / "
        "doing <b>satisfactorily</b>")),
], nivel="C1", tags=["adjective c1"])

# ======================================================= FALSE FRIENDS

serie_gap(FO, [
    ("___ the meeting at 3pm.", "Let's postpone", "postpone",
     "FALSE FRIEND: <b>to postpone</b> = postpone. <b>To imagine</b> = to "
     "imagine. <b>To expect</b> = to expect. <b>To suspect</b> = to suspect.",
     ex("<b>Let's postpone</b> the meeting. / <s>Let's imagine the meeting</s> "
        "(= let's picture it) / <s>Let's expect the meeting</s> (= let's wait "
        "for it).")),
    ("She's very ___ with her kids.", "patient", "patient",
     "FALSE FRIEND: <b>patient</b> = patient. <b>Patient</b> is NOT "
     "'impatient' (that is <i>impatient</i>). <b>Sensible</b> = sensible, not "
     "'sensitive' (sensitive = <i>sensitive</i>).",
     ex("She's very <b>patient</b> with her kids. / <s>She's very impatient</s> "
        "= impatient (the opposite).")),
    ("We need to ___ the problem carefully.", "assess", "assess",
     "FALSE FRIEND: <b>to assess</b> = to assess. <b>To assist</b> = to assist. "
     "<b>To attend</b> = to attend (an event). <b>To attend to</b> = to attend "
     "to. <b>To assure</b> = to assure someone. <b>To ensure</b> = to make "
     "sure.",
     ex("We need to <b>assess</b> the problem carefully. / <b>assist</b> = help "
        "/ <b>attend</b> a meeting / <b>assure someone</b> / "
        "<b>ensure something</b>")),
    ("The results were ___ to what we expected.", "contrary", "contrary to",
     "FALSE FRIEND: <b>contrary to</b> = contrary to. <b>Contrary</b> is not "
     "'setback' (that is <i>setback</i>). <b>Eventually</b> = eventually, not "
     "'occasionally' (occasionally = <i>occasionally</i>).",
     ex("The results were <b>contrary to</b> what we expected. / "
        "<i>eventually</i> = in the end / <i>occasionally</i> = sometimes.")),
    ("He's very ___ about the new plan.", "enthusiastic", "enthusiastic",
     "FALSE FRIEND: <b>enthusiastic</b> = enthusiastic. <b>Enthusiastic</b> is "
     "not <i>emotional</i> (emotional). <b>Actual</b> = actual/real, not 'on "
     "TV'. <b>Adequate</b> = adequate. <b>Decent</b> = decent.",
     ex("He's very <b>enthusiastic</b> about the new plan. / <b>actual</b> facts "
        "(real) / a <b>decent</b> salary")),
    ("The library has a ___ collection.", "extensive", "extensive",
     "FALSE FRIEND: <b>extensive</b> = extensive. <b>Expensive</b> = expensive "
     "(similar but different!). <b>Intensive</b> = intensive. "
     "<b>Expansive</b> = expansive.",
     ex("The library has an <b>extensive</b> collection. / <b>expensive</b> = "
        "costly / <b>intensive</b> course")),
    ("I'll ___ you that you're right.", "grant", "grant",
     "FALSE FRIEND: <b>to grant</b> = to grant. <b>To grant</b> is not "
     "<i>to guarantee</i> (to guarantee). <b>To award</b> = to award. "
     "<b>To prize</b> = to prize.",
     ex("I'll <b>grant</b> you that you're right. / <b>guarantee</b> = to "
        "guarantee / <b>award</b> = to award")),
    ("The economy is ___ at the moment.", "stagnant", "stagnant",
     "FALSE FRIEND: <b>stagnant</b> = stagnant. <b>Stagnant</b> is not "
     "<i>extinct</i> (extinct). <b>To depreciate a currency</b> vs "
     "<b>to depreciate someone</b> (to look down on).",
     ex("The economy is <b>stagnant</b> at the moment. / <b>extinct</b> = extinct / "
        "<b>depreciate a currency</b> vs <b>depreciate someone</b>")),
    ("She ___ the proposal immediately.", "rejected", "rejected",
     "FALSE FRIEND: <b>to reject</b> = to reject. <b>To refuse</b> = to refuse. "
     "<b>To resist</b> = to resist. <b>To deny</b> = to deny. To refuse a gift "
     "is <i>to decline</i>.",
     ex("She <b>rejected</b> the proposal. / <b>refuse to do</b> (to refuse to "
        "do) / <b>decline</b> (to decline a gift)")),
    ("We need to ___ the deadline.", "meet", "meet",
     "FALSE FRIEND: <b>to meet</b> = to meet (a deadline) or to meet. "
     "<b>To meet</b> is not <i>meat</i>. <b>To reach</b> = to reach (an "
     "agreement). <b>To hit</b> = to hit (a record).",
     ex("We need to <b>meet</b> the deadline. / <b>reach</b> an agreement / "
        "<b>hit</b> a target")),
], nivel="B2", tags=["false-friend"])

# ================================================== PRECISE OPPOSITES

serie_gap(OP, [
    ("I'm not ___ , I'm very tired.", "wide awake", "wide awake",
     "<b>Fixed opposites</b>: <b>wide awake</b> (not 'awake'), hardly any, "
     "barely any, rather, quite, in spite of, no longer, neither...nor, "
     "sparse, dense, meagre, broad, narrow, raise, rise, lie, lay</b>.",
     ex("I'm not asleep, I'm <b>wide awake</b>. / <b>hardly any</b> water = "
        "almost none / <b>quite</b> interesting = fairly interesting")),
    ("There was ___ any food left.", "hardly", "hardly any",
     "<b>hardly any / hardly ever</b> = almost none / almost never. No "
     "<b>any</b> after it.",
     ex("There was <b>hardly any</b> food left. / She <b>hardly ever</b> eats meat.")),
    ("He ___ likes coffee, but she does.", "hardly", "hardly",
     "<b>Hardly</b> in medial position = 'barely'. It does not take <b>ever</b> "
     "after it (that would be <i>hardly ever</i>).",
     ex("He <b>hardly</b> likes coffee, but she does. / "
        "<s>He hardly ever likes coffee</s> = he almost never likes it.")),
    ("That's a ___ question. Let's not get into it.", "loaded", "a loaded question",
     "<b>loaded question</b> = a loaded question. <b>Leading question</b> = a "
     "biased question. <b>Rhetorical question</b> = a rhetorical question.",
     ex("That's a <b>loaded question</b>. / a <b>leading question</b> in an interview")),
    ("The instructions were ___ .", "ambiguous", "ambiguous",
     "<b>ambiguous, vague, unclear, precise, explicit</b>.",
     ex("The instructions were <b>ambiguous</b>. / <b>precise</b> / <b>explicit</b> "
        "= precise / explicit")),
    ("He has ___ views on the subject.", "strong", "strong views",
     "<b>strong views, firm views, strong opinions, strongly opposed, "
     "firmly convinced</b>.",
     ex("He has <b>strong</b> views on the subject. / <b>firmly convinced</b> / "
        "<b>strongly opposed</b>")),
    ("The evidence is ___ .", "circumstantial", "circumstantial",
     "<b>circumstantial evidence, preliminary findings, conclusive proof, "
     "overwhelming evidence, credible witness, dubious claim</b>.",
     ex("The evidence is <b>circumstantial</b>. / <b>conclusive</b> proof / "
        "<b>preliminary</b> findings")),
    ("His excuse sounded ___ .", "flimsy", "flimsy",
     "<b>flimsy excuse, dubious claim, plausible story, compelling argument, "
     "weak excuse, lame excuse</b>.",
     ex("His excuse sounded <b>flimsy</b>. / a <b>plausible story</b> / "
        "a <b>compelling argument</b>")),
    ("The market is very ___ .", "competitive", "competitive",
     "<b>competitive market, fierce competition, saturated market, niche "
     "market, emerging market</b>.",
     ex("The market is very <b>competitive</b>. / a <b>saturated</b> market / "
        "a <b>niche</b> market / an <b>emerging</b> market")),
    ("His explanation didn't ___ to me.", "add up", "didn't add up",
     "Colloquial 'to make sense': <b>not add up, not make sense, not ring a "
     "bell, not be up to, not cut it, not be my cup of tea</b>.",
     ex("His explanation didn't <b>add up</b> to me. / It <b>doesn't ring a "
        "bell</b> = I don't recognise it / <b>not my cup of tea</b>")),
    ("That's a ___ . I won't do it.", "no-go", "a no-go",
     "Fixed opinion expressions: <b>no-go, deal-breaker, a done deal, off the "
     "table, on the table, in the bag, out of the question</b>.",
     ex("That's a <b>no-go</b>. / <b>a done deal</b> / <b>off the table</b> / "
        "<b>in the bag</b>")),
    ("We need to ___ this problem once and for all.", "address", "address",
     "<b>address a problem, tackle a problem, address an issue, get to grips "
     "with, deal with, resolve, sort out, iron out, nip in the bud</b>.",
     ex("We need to <b>address</b> this problem once and for all. / "
        "<b>iron out</b> / <b>nip in the bud</b>")),
], nivel="C1", tags=["opposites c1"])

# =================================================== COMPOUND NOUNS

serie_gap(CP, [
    ("She's a ___ .", "self-made", "self-made",
     "Hyphenated compound adjectives: <b>self-made, state-of-the-art, "
     "well-off, off-putting, long-term, high-powered, far-reaching, "
     "wide-ranging, all-round, part-time, one-off, two-bedroom, "
     "record-breaking, cost-effective</b>.",
     ex("She's a <b>self-made</b> entrepreneur. / a <b>state-of-the-art</b> "
        "system / <b>cost-effective</b> / <b>far-reaching</b> reforms")),
    ("We need a ___ solution.", "cost-effective", "cost-effective",
     "<b>cost-effective, cost-cutting, money-saving, budget-friendly, "
     "time-saving, energy-efficient</b>.",
     ex("We need a <b>cost-effective</b> solution. / <b>budget-friendly</b> / "
        "<b>time-saving</b> / <b>energy-efficient</b>")),
    ("The company had a ___ year.", "record-breaking", "record-breaking",
     "<b>record-breaking, world-famous, award-winning, ground-breaking, "
     "thought-provoking, high-profile, low-profile</b>.",
     ex("The company had a <b>record-breaking</b> year. / a "
        "<b>ground-breaking</b> study / a <b>high-profile</b> figure")),
    ("She's looking for a ___ job.", "part-time", "part-time",
     "Noun modifiers: <b>part-time, full-time, short-term, long-term, "
     "well-paid, low-paid, high-powered, one-off, second-hand</b>.",
     ex("She's looking for a <b>part-time</b> job. / a <b>well-paid</b> job / "
        "a <b>short-term</b> contract")),
    ("The drug had ___ effects.", "side", "side effects",
     "<b>side effects, side issues, back door, deadline (back + line), "
     "brainstorm, feedback, drawback, outbreak, checkout, upkeep, income, "
     "outcome</b>.",
     ex("The drug had <b>side</b> effects. / a <b>drawback</b> = a drawback / "
        "<b>takeaway</b> = a takeaway")),
    ("Let's do a ___ of ideas.", "brainstorm", "brainstorm",
     "Nouns made of verb + object: <b>brainstorm, deadline, feedback, "
     "handshake, insight, breakdown, breakthrough, takeaway, drawback, "
     "outbreak, checkout, upkeep, income, outcome</b>.",
     ex("Let's do a <b>brainstorm</b> of ideas. / a <b>breakdown</b> = a "
        "breakdown / a <b>breakthrough</b> = a breakthrough")),
    ("The meeting had a lot of ___ .", "give-and-take", "give-and-take",
     "Fixed compounds: <b>give-and-take, back-and-forth, one-on-one, "
     "face-to-face, step-by-step, day-to-day, over-the-top, in-depth, "
     "up-to-date</b>.",
     ex("The meeting had a lot of <b>give-and-take</b>. / a <b>one-on-one</b> "
        "meeting / an <b>up-to-date</b> list / a <b>back-and-forth</b> "
        "discussion")),
    ("That's a ___ . Let me check.", "figure", "that's a figure",
     "<b>figure out, work out, sort out, find out, rule out, point out, lay "
     "off, lay out, pay off, set off, show off, take off, turn off, call off, "
     "carry out, carry off, put off, get rid of, drop out, fall out, back up, "
     "check up, hold up, look up, look into, look out, look over, look up to, "
     "look forward to, make up, make out, make up for, pass away, pass by, "
     "pass on, pass out, pull off, pull through, push through, put up, run out, "
     "set up, set out, take on, take over, take up, turn down, turn up, use up, "
     "wear out, work out</b>.",
     ex("That's a <b>figure</b>. Let me check. / Memorise them as "
        "<b>verb + particle</b>: <b>figure out = to work out</b>.")),
], nivel="C1", tags=["compound-noun"])

# ================================================ HIGH-LEVEL ADJECTIVES

serie_gap(OP, [
    ("He's a ___ speaker. He always talks slowly.", "methodical",
     "methodical",
     "<b>methodical, systematic, thorough, meticulous, painstaking, "
     "efficient, pragmatic</b>.",
     ex("He's a <b>methodical</b> speaker. / a <b>meticulous</b> researcher / "
        "a <b>thorough</b> analysis / a <b>pragmatic</b> approach")),
    ("The results were ___ .", "inconclusive", "inconclusive",
     "<b>inconclusive, conclusive, preliminary, final, substantial, "
     "marginal, negligible, significant</b>.",
     ex("The results were <b>inconclusive</b>. / <b>preliminary</b> findings / "
        "<b>negligible</b> difference")),
    ("She's very ___ about punctuality.", "particular", "particular",
     "<b>particular, fussy, picky, strict, lenient, easy-going, "
     "down-to-earth, stand-offish</b>.",
     ex("She's very <b>particular</b> about punctuality. / a <b>lenient</b> "
        "teacher / <b>easy-going</b> / <b>picky</b> eater")),
    ("He gave a ___ answer that satisfied everyone.", "conciliatory",
     "conciliatory",
     "<b>conciliatory, diplomatic, tactful, even-handed, balanced, "
     "pragmatic, non-committal</b>.",
     ex("He gave a <b>conciliatory</b> answer that satisfied everyone. / "
        "a <b>non-committal</b> answer = an evasive answer")),
    ("The data are ___ ; we need better studies.", "flawed", "flawed",
     "<b>flawed, dubious, questionable, sound, robust, reliable, "
     "speculative</b>.",
     ex("The data are <b>flawed</b>; we need better studies. / "
        "<b>speculative</b> claims / a <b>robust</b> methodology")),
    ("She has a ___ sense of humour.", "dry", "dry",
     "<b>dry humour, dark humour, deadpan, sarcastic, ironic, poignant, "
     "hilarious</b>.",
     ex("She has a <b>dry</b> sense of humour. / <b>dark</b> humour / "
        "a <b>poignant</b> story / <b>deadpan</b> delivery")),
    ("His argument was ___ and well structured.", "coherent", "coherent",
     "<b>coherent, cogent, lucid, convoluted, disjointed, terse, verbose</b>.",
     ex("His argument was <b>coherent</b> and well structured. / a <b>lucid</b> "
        "explanation / a <b>verbose</b> style / <b>disjointed</b> arguments")),
    ("The company faces ___ competition.", "fierce", "fierce",
     "<b>fierce competition, intense pressure, fierce rivalry, intense "
     "scrutiny, fierce debate</b>.",
     ex("The company faces <b>fierce</b> competition. / <b>intense</b> pressure / "
        "under <b>intense scrutiny</b>")),
    ("He has a ___ grasp of the subject.", "thorough", "thorough",
     "<b>thorough grasp, thorough understanding, thorough knowledge, "
     "rudimentary, superficial</b>.",
     ex("He has a <b>thorough</b> grasp of the subject. / a <b>rudimentary</b> "
        "knowledge = basic knowledge / a <b>superficial</b> understanding")),
    ("The transition was ___ and smooth.", "seamless", "seamless",
     "<b>seamless, smooth, gradual, abrupt, turbulent, rocky, uneventful</b>.",
     ex("The transition was <b>seamless</b> and smooth. / an <b>abrupt</b> "
        "change / a <b>turbulent</b> period / a <b>rocky</b> start")),
    ("That's a ___ claim without evidence.", "bold", "a bold claim",
     "<b>bold claim, sweeping generalisation, unsubstantiated claim, "
     "well-founded, groundless, misleading, credible, dubious</b>.",
     ex("That's a <b>bold</b> claim without evidence. / a <b>sweeping "
        "generalisation</b> / an <b>unsubstantiated</b> claim")),
    ("He has ___ tenure of the office.", "a long", "a long tenure",
     "<b>long tenure, lengthy process, extensive, brief, short-lived, "
     "fleeting</b>.",
     ex("He has <b>a long</b> tenure of the office. / a <b>lengthy</b> process / "
        "a <b>fleeting</b> moment")),
], nivel="C1", tags=["adjective c1-2"])

cloze(OP, "The evidence is {{c1::circumstantial}}.",
      extra="<div class='box note'><span class='lbl'>C1 vocabulary</span>"
            "<b>circumstantial evidence, preliminary findings, conclusive proof, "
            "credible witness, dubious claim, flawed methodology</b>. Words a C1 "
            "speaker uses to qualify studies and evidence.</div>",
      tags="c1-c2 lexis cloze")

cloze(FO, "The results were {{c1::contrary}} to what we expected.",
      extra="<div class='box warn'><span class='lbl'>False friend</span>"
            "<b>contrary to</b> = contrary to. It is not 'setback' (that is "
            "<i>setback</i>).</div>",
      tags="c1-c2 false-friend cloze")
