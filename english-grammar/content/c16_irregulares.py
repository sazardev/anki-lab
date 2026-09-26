"""16 Irregular Verbs - the four forms of each, with usage notes.

A regular verb only needs -ed. An irregular one must be memorised whole,
and it cannot be deduced: it has to be learned. This module works it with
two card types per verb:
  - one reference card (all four forms at a glance)
  - a 4-deletion cloze (one card per form)
"""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "16 Irregular Verbs::"
F = D + "Irregular Forms"
N = D + "Stative Verbs (no continuous)"

# (base, 3ª persona, pasado, participio, -ing, meaning)
VERBOS = [
    ("be", "is", "was/were", "been", "being", "be"),
    ("become", "becomes", "became", "become", "becoming", "become"),
    ("begin", "begins", "began", "begun", "beginning", "begin"),
    ("bend", "bends", "bent", "bent", "bending", "bend"),
    ("bet", "bets", "bet", "bet", "betting", "bet"),
    ("bind", "binds", "bound", "bound", "binding", "bind"),
    ("bite", "bites", "bit", "bitten", "biting", "bite"),
    ("bleed", "bleeds", "bled", "bled", "bleeding", "bleed"),
    ("blow", "blows", "blew", "blown", "blowing", "blow"),
    ("break", "breaks", "broke", "broken", "breaking", "break"),
    ("breed", "breeds", "bred", "bred", "breeding", "breed"),
    ("bring", "brings", "brought", "brought", "bringing", "bring"),
    ("broadcast", "broadcasts", "broadcast", "broadcast", "broadcasting",
     "broadcast"),
    ("build", "builds", "built", "built", "building", "build"),
    ("burn", "burns", "burnt/burned", "burnt/burned", "burning", "quemar"),
    ("burst", "bursts", "burst", "burst", "bursting", "burst"),
    ("buy", "buys", "bought", "bought", "buying", "buy"),
    ("catch", "catches", "caught", "caught", "catching", "catch"),
    ("choose", "chooses", "chose", "chosen", "choosing", "choose"),
    ("come", "comes", "came", "come", "coming", "come"),
    ("cost", "costs", "cost", "cost", "costing", "cost"),
    ("creep", "creeps", "crept", "crept", "creeping", "creep"),
    ("cut", "cuts", "cut", "cut", "cutting", "cut"),
    ("deal", "deals", "dealt", "dealt", "dealing", "deal"),
    ("dig", "digs", "dug", "dug", "digging", "dig"),
    ("do", "does", "did", "done", "doing", "do"),
    ("draw", "draws", "drew", "drawn", "drawing", "draw"),
    ("drink", "drinks", "drank", "drunk", "drinking", "drink"),
    ("drive", "drives", "drove", "driven", "driving", "drive"),
    ("eat", "eats", "ate", "eaten", "eating", "eat"),
    ("fall", "falls", "fell", "fallen", "falling", "fall"),
    ("feed", "feeds", "fed", "fed", "feeding", "feed"),
    ("feel", "feels", "felt", "felt", "feeling", "feel"),
    ("fight", "fights", "fought", "fought", "fighting", "fight"),
    ("find", "finds", "found", "found", "finding", "find"),
    ("flee", "flees", "fled", "fled", "fleeing", "flee"),
    ("fling", "flings", "flung", "flung", "flinging", "fling"),
    ("fly", "flies", "flew", "flown", "flying", "fly"),
    ("forbid", "forbids", "forbade", "forbidden", "forbidding", "forbid"),
    ("forget", "forgets", "forgot", "forgotten", "forgetting", "forget"),
    ("forgive", "forgives", "forgave", "forgiven", "forgiving", "forgive"),
    ("freeze", "freezes", "froze", "frozen", "freezing", "freeze"),
    ("get", "gets", "got", "got/gotten", "getting", "get"),
    ("give", "gives", "gave", "given", "giving", "give"),
    ("go", "goes", "went", "gone", "going", "go"),
    ("grind", "grinds", "ground", "ground", "grinding", "grind"),
    ("grow", "grows", "grew", "grown", "growing", "grow"),
    ("hang", "hangs", "hung", "hung", "hanging", "hang"),
    ("have", "has", "had", "had", "having", "have"),
    ("hear", "hears", "heard", "heard", "hearing", "hear"),
    ("hide", "hides", "hid", "hidden", "hiding", "hide"),
    ("hit", "hits", "hit", "hit", "hitting", "hit"),
    ("hold", "holds", "held", "held", "holding", "hold"),
    ("hurt", "hurts", "hurt", "hurt", "hurting", "hurt"),
    ("keep", "keeps", "kept", "kept", "keeping", "keep"),
    ("kneel", "kneels", "knelt/kneeled", "knelt/kneeled", "kneeling",
     "kneel"),
    ("know", "knows", "knew", "known", "knowing", "know"),
    ("lay", "lays", "laid", "laid", "laying", "poner / Tender"),
    ("lead", "leads", "led", "led", "leading", "lead"),
    ("learn", "learns", "learnt/learned", "learnt/learned", "learning",
     "learn"),
    ("leave", "leaves", "left", "left", "leaving", "leave"),
    ("lend", "lends", "lent", "lent", "lending", "lend"),
    ("let", "lets", "let", "let", "letting", "let"),
    ("lie", "lies", "lay", "lain", "lying", "lie"),
    ("light", "lights", "lit/lighted", "lit/lighted", "lighting", "light"),
    ("lose", "loses", "lost", "lost", "losing", "lose"),
    ("make", "makes", "made", "made", "making", "make"),
    ("mean", "means", "meant", "meant", "meaning", "mean"),
    ("meet", "meets", "met", "met", "meeting", "meet"),
    ("mow", "mows", "mowed", "mowed/mown", "mowing", "mow"),
    ("overtake", "overtakes", "overtook", "overtaken", "overtaking",
     "overtake"),
    ("pay", "pays", "paid", "paid", "paying", "pay"),
    ("put", "puts", "put", "put", "putting", "put"),
    ("quit", "quits", "quit", "quit", "quitting", "quit"),
    ("read", "reads", "read /red/", "read /red/", "reading", "read"),
    ("rebuild", "rebuilds", "rebuilt", "rebuilt", "rebuilding", "rebuild"),
    ("rid", "rids", "rid", "rid", "ridding", "rid"),
    ("ring", "rings", "rang", "rung", "ringing", "ring"),
    ("rise", "rises", "rose", "risen", "rising", "rise"),
    ("run", "runs", "ran", "run", "running", "run"),
    ("say", "says", "said", "said", "saying", "say"),
    ("see", "sees", "saw", "seen", "seeing", "see"),
    ("seek", "seeks", "sought", "sought", "seeking", "seek"),
    ("sell", "sells", "sold", "sold", "selling", "sell"),
    ("send", "sends", "sent", "sent", "sending", "send"),
    ("set", "sets", "set", "set", "setting", "set"),
    ("sew", "sews", "sewed", "sewed/sewn", "sewing", "sew"),
    ("shake", "shakes", "shook", "shaken", "shaking", "shake"),
    ("shine", "shines", "shone", "shone", "shining", "shine"),
    ["shoot", "shoots", "shot", "shot", "shooting", "shoot"],
    ["show", "shows", "showed", "shown", "showing", "show"],
    ["shrink", "shrinks", "shrank", "shrunk", "shrinking", "shrink"],
    ["shut", "shuts", "shut", "shut", "shutting", "shut"],
    ["sing", "sings", "sang", "sung", "singing", "sing"],
    ["sink", "sinks", "sank", "sunk", "sinking", "sink"],
    ["sit", "sits", "sat", "sat", "sitting", "sit"],
    ["slay", "slays", "slew/slayed", "slain/slayed", "slaying", "slay"],
    ["sleep", "sleeps", "slept", "slept", "sleeping", "sleep"],
    ["slide", "slides", "slid", "slid", "sliding", "slide"],
    ["smell", "smells", "smelt/smelled", "smelt/smelled", "smelling", "smell"],
    ["speak", "speaks", "spoke", "spoken", "speaking", "speak"],
    ["speed", "speeds", "sped", "sped", "speeding", "speed"],
    ["spell", "spells", "spelt/spelled", "spelt/spelled", "spelling",
     "spell"],
    ["spend", "spends", "spent", "spent", "spending", "spend"],
    ["spill", "spills", "spilt/spilled", "spilt/spilled", "spilling",
     "spill"],
    ["spin", "spins", "spun", "spun", "spinning", "spin"],
    ["split", "splits", "split", "split", "splitting", "split"],
    ["spread", "spreads", "spread", "spread", "spreading", "extender /difundir"],
    ["spring", "springs", "sprang", "sprung", "springing", "spring"],
    ["stand", "stands", "stood", "stood", "standing", "stand"],
    ["steal", "steals", "stole", "stolen", "stealing", "steal"],
    ["stick", "sticks", "stuck", "stuck", "sticking", "stick"],
    ["sting", "stings", "stung", "stung", "stinging", "sting"],
    ["strike", "strikes", "struck", "stricken/struck", "striking",
     "strike"],
    ["swear", "swears", "swore", "sworn", "swearing", "swear"],
    ["sweep", "sweeps", "swept", "swept", "sweeping", "sweep"],
    ["swim", "swims", "swam", "swum", "swimming", "swim"],
    ["swing", "swings", "swung", "swung", "swinging", "swing"],
    ["take", "takes", "took", "taken", "taking", "take"],
    ["teach", "teaches", "taught", "taught", "teaching", "teach"],
    ["tear", "tears", "tore", "torn", "tearing", "tear"],
    ["tell", "tells", "told", "told", "telling", "tell"],
    ["think", "thinks", "thought", "thought", "thinking", "think"],
    ["throw", "throws", "threw", "thrown", "throwing", "throw"],
    ["understand", "understands", "understood", "understood", "understanding",
     "understand"],
    ["undergo", "undergoes", "underwent", "undergone", "undergoing",
     "undergo"],
    ["upset", "upsets", "upset", "upset", "upsetting", "upset"],
    ["wake", "wakes", "woke", "woken", "waking", "wake"],
    ["wear", "wears", "wore", "worn", "wearing", "wear"],
    ["weep", "weeps", "wept", "wept", "weeping", "weep"],
    ["win", "wins", "won", "won", "winning", "win"],
    ["withdraw", "withdraws", "withdrew", "withdrawn", "withdrawing",
     "withdraw"],
    ["write", "writes", "wrote", "written", "writing", "write"],
]

NOTES = {
    "be": "The most irregular verb: <i>am/is/are/was/were/been/being</i>. "
          "In the present it always takes <b>have</b> as an auxiliary: "
          "<i>I've <b>been</b> here</i>.",
    "get": "In the perfect, <b>got</b> is more common in BrE, "
           "<b>gotten</b> in AmE: <i>I've <b>got</b> / <b>gotten</b> it.</i>",
    "read": "Same spelling, different pronunciation: present <b>/riːd/</b>, "
            "past <b>/red/</b>. A classic error in written exams.",
    "lie": "Homophones: <b>lie</b> (tumbarse) = <b>lay - lain</b>; "
           "<b>lie</b> (to lie) = <b>lied - lied</b>. Just as in other languages.",
    "lay": "<b>lay - laid - laid</b> is <b>to lay</b>, not 'to lie down' "
           "(which is <i>lie - lay - lain</i>).",
    "ring": "BrE: <i>ring - rang - rung</i> (to ring). Also to call by phone. "
            "AmE: <i>call - called - called</i>.",
    "shoot": "Past and participle are <b>shot</b>, never <i>shooted</i>.",
    "leave": "Do not confuse with <b>live</b> (to live). <i>I'm leaving</i> = "
             "I'm going away. <i>I live in Madrid</i> = I live in Madrid.",
    "make": "<b>made</b> is both the past and the participle, never <i>maked</i>.",
    "hurt": "Identical in all four forms. Also 'to hurt'.",
    "cost": "Identical in all four forms.",
    "cut": "Identical in all four forms.",
    "put": "Identical in all four forms.",
    "set": "Identical in all four forms.",
    "let": "Identical in all four forms.",
    "quit": "BrE: <i>quit - quit - quit</i>. AmE also allows "
            "<i>quitted</i>.",
    "wind": "Cuidado: <b>wind</b> (viento, sustantivo) / <b>wind</b> (enrollar, "
            "verbo) = <b>wind - wound - wound</b>, distinto de "
            "<i>wound</i> (herida).",
}


def note_of(v):
    return NOTES.get(v, "")


for v in VERBOS:
    base, third, past, part, ing, es = v[0], v[1], v[2], v[3], v[4], v[5]
    # 1) reference card: the four forms
    rule(F,
         front='<div class="q"><b>%s</b> <span class="badge b1">%s</span></div>'
               '<div class="prompt">Complete the four irregular forms</div>'
               % (base, es),
         back='<span class="ans">%s → %s → %s</span> &nbsp;·&nbsp; '
              '<i>-ing: %s</i>' % (base, past, part, ing),
         regla=table(["Base", "3ª persona (-s)", "Pasado", "Part. Perf.", "-ing"],
                     [[base, third, past, part, ing]]),
         ejemplos=ex("Yesterday I <b>%s</b> it." % past.split("/")[0].strip(),
                     "I have <b>%s</b> it." % part.split("/")[0].strip()),
         notas=note_of(base),
         tags=["irregular", base])
    # 2) production card
    prod(F,
         prompt='<div class="q"><b>%s</b> <span class="badge b1">%s</span></div>'
                '<div class="prompt">Write the PAST SIMPLE</div>' % (base, es),
         respuesta='<span class="ans">%s</span>' % past,
         pista=' participle: <i>%s</i> &nbsp;·&nbsp; -ing: <i>%s</i>'
               % (part, ing),
         ejemplos=ex("Yesterday she <b>%s</b>." % past.split("/")[0].strip(),
                     "I have <b>%s</b> it twice.</i>" % part.split("/")[0].strip()),
         tags=["irregular", base, "production"])
    # 3) 4-form cloze = 4 cards (no answer given on the front)
    cloze(F,
          "<b>{{c1::%s}}</b> &nbsp;·&nbsp; ella {{c2::%s}} &nbsp;·&nbsp; "
          "tiene {{c3::%s}} &nbsp;·&nbsp; {{c4::%s}}"
          % (base, past.split("/")[0].strip(),
             part.split("/")[0].strip(), es),
          extra=("<div class='box warn'><span class='lbl'>Ojo</span>%s</div>"
                 % note_of(base)) if note_of(base) else "",
          tags=["irregular", base, "cloze"])

# ============================================ VERBOS DE ESTADO (NO CONTINUO)
# ================================ STATIVE VERBS (NOT IN THE CONTINUOUS)

serie_gap(N, [
    ("I ___ here since 2015.", "have known", "to know (state)",
     "Stative verbs do not take the <b>continuous</b> in their literal "
     "sense: <b>know, believe, understand, remember, forget, want, need, "
     "like, love, hate, prefer, wish, own, belong, seem, appear, contain, "
     "consist, depend, matter, cost, weigh, lack, resemble, fit, suit, "
     "deserve, involve, mean, exist</b>.",
     ex("I <b>have known</b> her for years. / <s>I have been knowing her</s> is WRONG."),
     "I have known her since 2015."),
    ("Do you ___ what he means?", "understand", "to understand",
     "<b>understand</b> = a state of mind. NEVER <i>understanding</i> in that "
     "sense.",
     ex("I don't <b>understand</b>. / <b>Do you understand</b>? / "
        "<s>I am understanding</s> is WRONG."),
     "Do you understand what he means?"),
    ("She ___ a lot of money.", "owns", "to own",
     "<b>own</b> and <b>have</b> do not take the continuous. NEVER "
     "<i>owning</i> for 'owning'.",
     ex("She <b>owns</b> three companies. / <b>Does she own</b> a car? / "
        "<s>She is owning three companies</s> is WRONG."),
     "She owns a lot of money."),
    ("The team ___ United.", "consists", "to consist",
     "<b>consist of</b> always + <b>of</b>, and never in the continuous.",
     ex("The team <b>consists of</b> 12 players. / "
        "<s>The team is consisting of</s> is WRONG."),
     "The team consists of twelve players."),
    ("It ___ a lot to me.", "matters", "to matter",
     "<b>matter</b> is never in the continuous.",
     ex("It <b>matters</b> a lot to me. / Does it <b>matter</b>? / "
        "<s>It is mattering to me</s> is WRONG."),
     "It matters a lot to me."),
    ("Your explanation doesn't ___ to me.", "make sense", "to make sense",
     "<b>make sense, make a difference, make a mistake, make a decision</b>: "
     "never in the continuous.",
     ex("It doesn't <b>make sense</b>. / That <b>makes a difference</b>. / "
        "<s>It's making sense</s> is WRONG."),
     "Your explanation doesn't make sense."),
    ("I ___ to leave at 8, so let's order now.", "need", "to need",
     "<b>need, want, would like, hate, love, prefer, wish</b> express feeling "
     "or desire: NEVER in the continuous.",
     ex("I <b>need</b> to leave. / She <b>needs</b> more time. / "
        "<s>I'm needing to leave</s> is WRONG."),
     "I need to leave at 8, so let's order now."),
    ("He ___ from the south of Spain.", "comes", "to be from (origin)",
     "<b>come from, belong to, consist of, result from, depend on, rely on</b>: "
     "never in the continuous.",
     ex("He <b>comes from</b> the south of Spain. / It <b>depends on</b> you. / "
        "<s>He is coming from</s> = he is in the process of coming."),
     "He is from the south of Spain."),
    ("The book ___ 200 pages.", "contains", "to contain",
     "<b>contain, include, consist of, hold</b> (measurement, container).",
     ex("The book <b>contains</b> 200 pages. / The box <b>holds</b> 10 kilos. / "
        "<s>The book is containing</s> is WRONG."),
     "The book contains 200 pages."),
    ("You ___ that.", "owe", "to owe (money)",
     "<b>owe, belong to, resemble, suit, fit</b> are never in the continuous.",
     ex("I <b>owe</b> you 20 euros. / Does this <b>suit</b> you? / "
        "<s>I'm owing you</s> is WRONG."),
     "I owe you that."),
], nivel="B1", tags=["stative-verbs"])

# =================================================================== CLOZE

cloze(F, "{{c1::buy}} - {{c2::bought}} - {{c3::bought}}",
      extra="<div class='box note'><span class='lbl'>Regular past</span>"
            "If the base form and the participle are identical, the verb is "
            "probably regular in the past too: here <b>bought</b> = <b>bought</b>.</div>",
      tags="c1-c2 irregular cloze")

cloze(F, "{{c1::lie}} (to lie) - {{c2::lied}} - {{c3::lied}}",
      extra="<div class='box warn'><span class='lbl'>Homophones</span>"
            "<b>lie</b> (to lie, to tell a lie) = <b>lied - lied</b>. "
            "<b>lie</b> (to lie down) = <b>lay - lain</b>. "
            "<b>lay</b> (to lay something) = <b>laid - laid</b>. "
            "<b>lose</b> = <b>lost</b> / <b>loose</b> = <b>lost</b> (not tight).</div>",
      tags="c1-c2 irregular cloze")
