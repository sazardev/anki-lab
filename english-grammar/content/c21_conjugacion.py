"""21 Verb Conjugation - the 12-tense table for every verb.

Inflection engine: from the base form and the irregular forms it computes the
rest of the table. Each verb produces 1 reference card (all 12 tenses at a
glance) + 4 cloze production cards.
"""

from ._base import gap, rule, prod, cloze, ex, ul, table, badge

D = "21 Verb Conjugation::"
T = D + "12-tense Tables"

VOWELS = "aeiou"
IRREG = {
    "be": ("am/is/are", "was/were", "been", "being"),
    "become": ("becomes", "became", "become", "becoming"),
    "begin": ("begins", "began", "begun", "beginning"),
    "bend": ("bends", "bent", "bent", "bending"),
    "bet": ("bets", "bet", "bet", "betting"),
    "bind": ("binds", "bound", "bound", "binding"),
    "bite": ("bites", "bit", "bitten", "biting"),
    "blow": ("blows", "blew", "blown", "blowing"),
    "break": ("breaks", "broke", "broken", "breaking"),
    "breed": ("breeds", "bred", "bred", "breeding"),
    "bring": ("brings", "brought", "brought", "bringing"),
    "build": ("builds", "built", "built", "building"),
    "burn": ("burns", "burned/burnt", "burned/burnt", "burning"),
    "burst": ("bursts", "burst", "burst", "bursting"),
    "buy": ("buys", "bought", "bought", "buying"),
    "catch": ("catches", "caught", "caught", "catching"),
    "choose": ("chooses", "chose", "chosen", "choosing"),
    "come": ("comes", "came", "come", "coming"),
    "cost": ("costs", "cost", "cost", "costing"),
    "cut": ("cuts", "cut", "cut", "cutting"),
    "deal": ("deals", "dealt", "dealt", "dealing"),
    "do": ("does", "did", "done", "doing"),
    "draw": ("draws", "drew", "drawn", "drawing"),
    "drink": ("drinks", "drank", "drunk", "drinking"),
    "drive": ("drives", "drove", "driven", "driving"),
    "eat": ("eats", "ate", "eaten", "eating"),
    "fall": ("falls", "fell", "fallen", "falling"),
    "feed": ("feeds", "fed", "fed", "feeding"),
    "feel": ("feels", "felt", "felt", "feeling"),
    "fight": ("fights", "fought", "fought", "fighting"),
    "find": ("finds", "found", "found", "finding"),
    "flee": ("flees", "fled", "fled", "fleeing"),
    "fly": ("flies", "flew", "flown", "flying"),
    "forget": ("forgets", "forgot", "forgotten", "forgetting"),
    "forgive": ("forgives", "forgave", "forgiven", "forgiving"),
    "freeze": ("freezes", "froze", "frozen", "freezing"),
    "get": ("gets", "got", "got/gotten", "getting"),
    "give": ("gives", "gave", "given", "giving"),
    "go": ("goes", "went", "gone", "going"),
    "grow": ("grows", "grew", "grown", "growing"),
    "hang": ("hangs", "hung", "hung", "hanging"),
    "have": ("has", "had", "had", "having"),
    "hear": ("hears", "heard", "heard", "hearing"),
    "hide": ("hides", "hid", "hidden", "hiding"),
    "hit": ("hits", "hit", "hit", "hitting"),
    "hold": ("holds", "held", "held", "holding"),
    "hurt": ("hurts", "hurt", "hurt", "hurting"),
    "keep": ("keeps", "kept", "kept", "keeping"),
    "know": ("knows", "knew", "known", "knowing"),
    "lay": ("lays", "laid", "laid", "laying"),
    "lead": ("leads", "led", "led", "leading"),
    "leave": ("leaves", "left", "left", "leaving"),
    "lend": ("lends", "lent", "lent", "lending"),
    "let": ("lets", "let", "let", "letting"),
    "lie": ("lies", "lay", "lain", "lying"),
    "lose": ("loses", "lost", "lost", "losing"),
    "make": ("makes", "made", "made", "making"),
    "mean": ("means", "meant", "meant", "meaning"),
    "meet": ("meets", "met", "met", "meeting"),
    "pay": ("pays", "paid", "paid", "paying"),
    "put": ("puts", "put", "put", "putting"),
    "read": ("reads", "read", "read", "reading"),
    "ride": ("rides", "rode", "ridden", "riding"),
    "ring": ("rings", "rang", "rung", "ringing"),
    "rise": ("rises", "rose", "risen", "rising"),
    "run": ("runs", "ran", "run", "running"),
    "say": ("says", "said", "said", "saying"),
    "see": ("sees", "saw", "seen", "seeing"),
    "seek": ("seeks", "sought", "sought", "seeking"),
    "sell": ("sells", "sold", "sold", "selling"),
    "send": ("sends", "sent", "sent", "sending"),
    "set": ("sets", "set", "set", "setting"),
    "shake": ("shakes", "shook", "shaken", "shaking"),
    "shine": ("shines", "shone", "shone", "shining"),
    "shoot": ("shoots", "shot", "shot", "shooting"),
    "show": ("shows", "showed", "shown", "showing"),
    "sing": ("sings", "sang", "sung", "singing"),
    "sink": ("sinks", "sank", "sunk", "sinking"),
    "sit": ("sits", "sat", "sat", "sitting"),
    "sleep": ("sleeps", "slept", "slept", "sleeping"),
    "slide": ("slides", "slid", "slid", "sliding"),
    "speak": ("speaks", "spoke", "spoken", "speaking"),
    "spend": ("spends", "spent", "spent", "spending"),
    "stand": ("stands", "stood", "stood", "standing"),
    "steal": ("steals", "stole", "stolen", "stealing"),
    "stick": ("sticks", "stuck", "stuck", "sticking"),
    "swim": ("swims", "swam", "swum", "swimming"),
    "take": ("takes", "took", "taken", "taking"),
    "teach": ("teaches", "taught", "taught", "teaching"),
    "tear": ("tears", "tore", "torn", "tearing"),
    "tell": ("tells", "told", "told", "telling"),
    "think": ("thinks", "thought", "thought", "thinking"),
    "throw": ("throws", "threw", "thrown", "throwing"),
    "understand": ("understands", "understood", "understood", "understanding"),
    "wake": ("wakes", "woke", "woken", "waking"),
    "wear": ("wears", "wore", "worn", "wearing"),
    "win": ("wins", "won", "won", "winning"),
    "write": ("writes", "wrote", "written", "writing"),
}

# regular B1 verbs worth conjugating
REGULARES = ["work", "study", "call", "play", "walk", "talk", "look", "help",
             "live", "use", "try", "ask", "need", "turn", "start", "reach",
             "watch", "follow", "listen", "learn", "open", "close", "offer",
             "remember", "consider", "improve", "realise", "organise",
             "decide", "believe", "happen", "matter", "seem", "appear",
             "expect", "prefer", "explain", "enjoy", "avoid", "admit"]

VOWEL_C = set("wxy")   # consonante + y: study -> studied
DOUBLE = set("bcdfgklmnprstz")


def third(base):
    if base in IRREG:
        return IRREG[base][0]
    if base.endswith(("s", "sh", "ch", "x", "o", "z")):
        return base + "es"
    if base.endswith("y") and base[-2] not in VOWELS:
        return base[:-1] + "ies"
    return base + "s"


def ing(base):
    if base in IRREG:
        return IRREG[base][3]
    if base.endswith("ie"):
        return base[:-2] + "ying"
    if base.endswith("e") and not base.endswith(("ee", "ye", "oe")):
        return base[:-1] + "ing"
    if (len(base) >= 3 and len(base) <= 5
            and base[-1] not in VOWELS and base[-2] in VOWELS
            and base[-3] not in VOWELS and base[-1] in DOUBLE):
        return base + base[-1] + "ing"
    return base + "ing"


def ed(base):
    if base in IRREG:
        return IRREG[base][1]
    if base.endswith("e"):
        return base + "d"
    if base.endswith("y") and base[-2] not in VOWELS:
        return base[:-1] + "ied"
    if (len(base) >= 3 and len(base) <= 5
            and base[-1] not in VOWELS and base[-2] in VOWELS
            and base[-3] not in VOWELS and base[-1] in DOUBLE):
        return base + base[-1] + "ed"
    return base + "ed"


def part(base):
    return IRREG[base][2] if base in IRREG else ed(base)


def formas(base):
    i = ing(base)
    e = ed(base)
    p = part(base)
    return {
        "Presente simple": f"{third(base)}",
        "Presente continuo": f"am/is/are {i}",
        "Pasado simple": e,
        "Pasado continuo": f"was/were {i}",
        "Pasado perfecto": f"had {p}",
        "Pasado perfecto cont.": f"had been {i}",
        "Futuro": f"will {base}",
        "Futuro continuo": f"will be {i}",
        "Presente perfecto": f"have/has {p}",
        "Presente perf. cont.": f"have/has been {i}",
        "Futuro perfecto": f"will have {p}",
        "Pasiva (pres.)": f"am/is/are {p}",
    }


NOTAS = {
    "be": "El verbo <b>más irregular</b>: <i>am/is/are/was/were/been/being</i>. "
          "En presente necesita <b>have</b> como auxiliar: <i>I've <b>been</b> here</i>.",
    "read": "Same spelling, different pronunciation: present <b>/riːd/</b>, "
            "past <b>/red/</b>. A classic error in written exams.",
    "lie": "Cuidado: <b>lie</b> (mentir) = lied/lied. <b>lie</b> (tumbarse) = "
           "lay/lain. <b>lay</b> (tender) = laid/laid.",
    "lay": "<b>lay - laid - laid</b> is <b>to lay</b>, not 'to lie down' "
           "(which is <i>lie - lay - lain</i>).",
    "ring": "BrE: <i>ring - rang - rung</i> (sonar, llamar). AmE: "
            "<i>call - called - called</i>.",
    "get": "Perfect: <b>got</b> (BrE) or <b>gotten</b> (AmE): "
           "<i>I've <b>got</b> / <b>gotten</b> it.</i>",
    "leave": "No confundir con <b>live</b> (vivir). "
             "<i>I'm leaving</i> = I'm leaving. <i>I live here</i> = I live here.",
    "shoot": "Pasado y participio <b>shot</b>, nunca <i>shooted</i>.",
    "hurt": "Identical in all four forms. Also 'to hurt'.",
    "cut": "Identical in all four forms.",
    "put": "Identical in all four forms.",
    "set": "Identical in all four forms.",
    "cost": "Identical in all four forms.",
    "let": "Identical in all four forms.",
    "quit": "BrE: <i>quit - quit - quit</i>. AmE also <i>quitted</i>.",
    "lend": "<b>lend - lent - lent</b> (to lend). Not to be confused with "
            "<i>to borrow</i> = to borrow.",
    "build": "There is also <b>rebuild - rebuilt - rebuilt</b>.",
}


def nota_de(v):
    return NOTAS.get(v, "")


TODOS = list(IRREG) + REGULARES

HUECO = '<span class="gap empty">&#8203;</span>'

for base in TODOS:
    f = formas(base)
    p_simple = f["Presente perfecto"].split(" ", 1)[1]
    # --- 1) tarjeta de referencia: frente con 6 huecos, reverso con las formas
    rule(T,
         front='<div class="q"><b>%s</b></div>'
               '<div class="prompt">3ª pers. &nbsp;%s&nbsp; pasado &nbsp;%s'
               '&nbsp; part. &nbsp;%s&nbsp; -ing &nbsp;%s&nbsp; '
               'perf. &nbsp;%s&nbsp; futuro &nbsp;%s</div>'
               % (base, HUECO, HUECO, HUECO, HUECO, HUECO, HUECO),
         back='<span class="ans">%s &nbsp;·&nbsp; %s &nbsp;·&nbsp; %s'
              ' &nbsp;·&nbsp; %s &nbsp;·&nbsp; %s &nbsp;·&nbsp; %s</span>'
              % (f["Presente simple"], f["Pasado simple"], p_simple,
                 ing(base), f["Presente perfecto"], f["Futuro"]),
         regla=table(["Tiempo", f"{base}…"], [[k, v] for k, v in f.items()]),
         ejemplos=ex("She <b>%s</b> every day." % f["Presente simple"],
                     "They <b>%s</b> yesterday." % f["Pasado simple"],
                     "They have <b>%s</b> it." % p_simple,
                     "They <b>%s</b> now." % f["Presente continuo"],
                     "They have been <b>%s</b> for years." % ing(base)),
         tags=["conjugation", base])
    # --- 2) 4 tarjetas cloze: drill de formas, sin regalar nada en el anverso
    cloze(T,
          "<b>{{c1::%s}}</b> &nbsp;·&nbsp; she {{c2::%s}} "
          "&nbsp;·&nbsp; she {{c3::%s}} &nbsp;·&nbsp; has {{c4::%s}}"
          % (base, f["Presente simple"], f["Pasado simple"], p_simple),
          extra=("<div class='box warn'><span class='lbl'>Ojo</span>%s</div>"
                 % nota_de(base)) if nota_de(base) else "",
          tags=["conjugation", base, "cloze"])


gap(T, "She ___ (work) here ___ 2019.", "has worked, since",
    nivel="B1", cue="two gaps", forma="has worked, since",
    regla="<b>Present Perfect</b> = a situation that <b>is still true</b>.",
    ejemplos=ex("She <b>has worked</b> here <b>since</b> 2019. "
                "|| Trabaja aquí desde 2019."),
    tags="conjugation perfect")

cloze(T, "{{c1::have}} seen. / She {{c1::has}} seen. / They {{c1::have}} seen.",
      extra="<div class='box rule'><span class='lbl'>have / has / had</span>"
            "<b>has</b> with he/she/it in the present. <b>had</b> in every "
            "past tense. The participle never changes: "
            "<i>has <b>gone</b></i> (not <i>has <b>goed</b></i>).</div>",
      tags="c1-c2 conjugation cloze")

cloze(T, "He {{c1::has been}} working here for 10 years.",
      extra="<div class='box note'><span class='lbl'>Perfecto continuo</span>"
            "<b>have/has been + V-ing</b> = duration. "
            "<b>has worked</b> = result. The difference is subtle but it is what "
            "separates a B1 from a B2 in any exam.</div>",
      tags="c1-c2 conjugation cloze")
