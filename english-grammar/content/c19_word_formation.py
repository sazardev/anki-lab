"""19 Determiners, Nouns and Pronouns (B2-C2)."""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "19 Determiners and Nouns::"
Q1, Q2, N1, N2, P1 = D + "Advanced Quantifiers", D + "Quantity and Degree", \
    D + "Nouns: Number", D + "Nouns: Countability", \
    D + "Pronouns and Reference"

# ============================================ ADVANCED QUANTIFIERS

serie_gap(Q1, [
    ("___ of the students passed.", "None", "none of",
     "<b>None of / neither of / either of / all of / some of / most of / "
     "many of / few of / both of / half of / none of / each of / every one "
     "of</b> + <b>of</b> + <b>the / my / your / these / those</b>.",
     ex("<b>None of</b> the students passed. / <b>Neither of</b> the two books "
        "is new. / <b>All of</b> them agree.")),
    ("___ of the two answers is correct.", "Neither", "neither of",
     "<b>Neither of</b> = neither of two. <b>Either of</b> = one of two. "
     "<b>None of</b> = none of three or more.",
     ex("<b>Neither of</b> the two answers is correct. / <b>Either of</b> the "
        "two methods would work.")),
    ("I have ___ money left.", "barely any", "barely any",
     "Quantifiers with <b>any</b>: <b>hardly any, barely any, scarcely any, "
     "almost no, next to no, none of</b>. Singular: <b>hardly a, barely a</b>.",
     ex("I have <b>barely any</b> money left. / <b>Hardly any</b> people came. / "
        "There was <b>almost no</b> food.")),
    ("___ students failed this year.", "Few", "few",
     "Scarcity quantifiers: <b>few, a few, little, a little, hardly any, "
     "scarcely any, next to no, only, mere, a mere</b>.",
     ex("<b>Few</b> students failed. / <b>A few</b> passed. / only <b>a handful "
        "of</b> people / a <b>mere</b> 5% of the class")),
    ("The police are investigating ___ matters.", "the matter", "the matter",
     "<b>of + singular noun</b> = the matter. Plural: <b>matters, issues, "
     "affairs</b>. Fixed: <b>a matter of concern, a matter of fact, no "
     "matter, a matter of life and death</b>.",
     ex("The police are investigating <b>the matter</b>. / a <b>matter of</b> "
        "concern / <b>matters</b> of mutual interest / <b>no matter</b> what")),
    ("___ of the work is done.", "Half", "half of",
     "<b>All, most, much, many, some, any, no, none, half, all, both, "
     "three-quarters, a third, a quarter</b> + <b>of</b> + plural.",
     ex("<b>Half</b> of the work is done. / <b>Two-thirds of</b> the class "
        "passed. / <b>Most of</b> the work.")),
    ("___ of the students have their own lunch.", "All of", "all of",
     "<b>All of + the + plural</b> = all of. <b>All</b> alone = all (in general).",
     ex("<b>All of</b> the students have their own lunch. / <b>All</b> students "
        "must register (in general).")),
    ("She has ___ friends in Rome.", "a handful of", "a handful of",
     "<b>A handful of, a couple of, a number of, a great deal of, a great "
     "many, a large number of, a small number of, a total of</b>.",
     ex("She has <b>a handful of</b> friends in Rome. / <b>a great deal of</b> "
        "(uncountable) / <b>a great many</b> (countable)")),
], nivel="C1", tags=["quantifier advanced"])

# ============================================== QUANTITY AND DEGREE

serie_gap(Q2, [
    ("I couldn't ___ hear what she said.", "barely", "barely",
     "Degree adverbs: <b>barely, hardly, scarcely, just, even just, only just, "
     "rather, quite, fairly, extremely, deeply, highly, utterly, totally, "
     "absolutely</b>.",
     ex("I couldn't <b>barely</b> hear what she said. / <b>Only just</b> = by "
        "a very small margin / <b>Even just</b> = even only.")),
    ("The results were ___ conclusive.", "nowhere near", "nowhere near",
     "<b>Nowhere near + adjective/adverb</b> = nowhere near. "
     "<b>By no means</b> = by no means.",
     ex("The results were <b>nowhere near</b> conclusive. / <b>By no means</b> "
        "= by no means / <b>Under no circumstances</b> = under no circumstances")),
    ("___ he tried, he couldn't do it.", "However", "however hard he tried",
     "<b>However + adverb + subject + verb</b> (concession). "
     "<b>No matter how + adverb + clause</b>.",
     ex("<b>However</b> hard he tried, he couldn't do it. / <b>No matter how "
        "hard</b> he tried...")),
    ("The film was ___ . I fell asleep.", "so boring that", "so boring that",
     "Result structures: <b>so + adj + that + clause</b> / <b>such + (a) + "
     "noun + that</b> / <b>too + adj + to + base</b>.",
     ex("The film was <b>so boring that</b> I fell asleep. / It was <b>such a "
        "boring film that</b> I fell asleep. / It was <b>too boring to</b> watch.")),
    ("___ he is, he'll always be a good friend.", "Whatever", "whatever",
     "<b>Whatever, wherever, whoever, whenever, however</b> = no matter what / "
     "where / who / when / how.",
     ex("<b>Whatever</b> he is, he'll always be a good friend. / "
        "<b>Wherever</b> you go... / <b>Whoever</b> you are...")),
    ("It's ___ late to start now.", "far", "far too late",
     "With <b>far/much</b> + superlative, or with <b>too</b>.",
     ex("It's <b>far</b> too late to start now. / <b>Much</b> better / "
        "<b>far</b> the best / <b>far</b> more expensive")),
], nivel="C1", tags=["degree quantity"])

# ======================================================= NOUNS: NUMBER

serie_gap(N1, [
    ("Two ___ were injured in the accident.", "men", "men",
     "Irregular plurals: <b>man/men, woman/women, child/children, foot/feet, "
     "tooth/teeth, goose/geese, mouse/mice, louse/lice, person/people, "
     "ox/oxen</b>.",
     ex("Two <b>men</b> were injured. / <b>Children</b> / <b>feet</b> / "
        "<b>teeth</b> / <b>people</b>")),
    ("The scissors are on the table.", "are", "are",
     "Plural-only nouns: <b>scissors, trousers, jeans, glasses, clothes, "
     "pyjamas, briefs, goods, belongings, customs, funds, premises, supplies, "
     "surroundings, stairs, tongs, shears, pliers, clippers</b>.",
     ex("The <b>scissors are</b> on the table. / a <b>pair of scissors</b> / "
        "my <b>trousers are</b> too long")),
    ("There are many ___ in the lake.", "fish", "fish",
     "Invariant: <b>fish, sheep, series, species, aircraft, deer, offspring, "
     "swine, means</b>.",
     ex("There are many <b>fish</b> in the lake. / two <b>sheep</b> / a "
        "<b>series</b> of events / three <b>aircraft</b>")),
    ("___ news is that he got the job.", "The", "the news",
     "<b>News</b> is singular and takes <b>the</b>: <b>the news</b>. Also: "
     "<b>the weather, the work, the damage, the furniture, the luggage, the "
     "progress, the information, the advice, the evidence, the research</b>.",
     ex("<b>The news</b> is that he got the job. / <b>The</b> news <b>is</b> "
        "good. NEVER <i>the news are</i>.")),
    ("How ___ luggage have you got?", "much", "much luggage",
     "Uncountables that look countable: <b>luggage, work, furniture, "
     "information, advice, research, progress, evidence, knowledge, money, "
     "staff, traffic, weather, homework, housework</b>.",
     ex("How <b>much luggage</b> have you got? / <b>A piece of</b> luggage / "
        "<b>two pieces of</b> luggage")),
], nivel="B1", tags=["noun number"])

# ============================================= NOUNS: COUNTABILITY

serie_gap(N2, [
    ("I need some ___ , not a whole one.", "advice", "some advice",
     "Uncountables that are countable in other languages: <b>advice, "
     "information, knowledge, progress, research, evidence, furniture, "
     "luggage, work, feedback, training</b>.",
     ex("I need some <b>advice</b>, not a whole one. / <b>a piece of advice</b> / "
        "<b>a piece of information</b> / <b>a piece of research</b>")),
    ("Three ___ of advice were given.", "pieces", "three pieces",
     "Countable conversion: <b>advice → a piece of advice / pieces of advice</b>; "
     "<b>information → an item of information</b>; <b>research → a piece of "
     "research</b>; <b>evidence → a piece of evidence</b>; <b>feedback → a "
     "piece of feedback</b>; <b>training → a training session</b>.",
     ex("Three <b>pieces of advice</b> were given. / <b>a piece of</b> bread / "
        "<b>a slice of</b> bread / <b>a glass of</b> water")),
    ("She's a ___ of mine.", "friend", "a friend of mine",
     "Possessive pronouns with <b>a/an + noun + of mine/yours/his/ours</b>: "
     "<b>a friend of mine, a cousin of hers, two colleagues of ours</b>.",
     ex("She's a <b>friend of mine</b>. / a <b>brother of his</b> / a "
        "<b>colleague of ours</b>")),
    ("I need ___ .", "some advice", "some advice",
     "Quick rule: if the noun takes <b>of</b> in your language, it is "
     "uncountable in English.",
     ex("I need <b>some advice</b>. / <b>a piece of advice</b> / <b>a bit of advice</b>")),
    ("The company made a ___ of profit.", "lot", "a lot of",
     "Measure: <b>a lot of, a great deal of, plenty of, tons of, a large "
     "amount of, a high proportion of, a small amount of, a total of</b>.",
     ex("The company made <b>a lot of</b> profit. / <b>a large amount of</b> data / "
        "<b>a high proportion of</b> students")),
], nivel="B2", tags=["noun countability"])

# ============================================ PRONOUNS AND REFERENCE

serie_gap(P1, [
    ("The dog wagged ___ tail.", "its", "its",
     "<b>Its</b> = of it (non-human). <b>It's</b> = it is / it has. The single "
     "most confused pair in English.",
     ex("The dog wagged <b>its tail</b>. / <s>The dog wagged it's tail</s> is "
        "WRONG. NEVER with an apostrophe.")),
    ("Everyone should bring ___ own laptop.", "their", "their",
     "<b>Their</b> = of them (plural or neutral singular). <b>Theirs</b> = a "
     "noun on its own.",
     ex("Everyone should bring <b>their</b> own laptop. / This book is "
        "<b>theirs</b>, not mine.")),
    ("___ of you is coming to the party?", "Which", "which",
     "<b>Which of</b> = which of (a group). <b>What of</b> = what of (rarely "
     "used). <b>Who of</b> = who of.",
     ex("<b>Which of</b> you is coming? / <b>What</b> colour? / <b>Which</b> colours?")),
    ("The blue car is mine. ___ is his.", "The red one", "the red one",
     "Substitution with <b>one / ones</b> to avoid repetition: <b>the red one, "
     "the big one, the cheaper one, my sister's, the one on the left</b>.",
     ex("The blue car is mine. <b>The red one</b> is his. / I prefer <b>the "
        "cheaper one</b>. / <b>the one on the left</b>")),
    ("Between Alice and Bob, ___ is taller?", "the latter", "the latter",
     "<b>The former</b> = the first. <b>The latter</b> = the second. Only with "
     "two items.",
     ex("Between Alice and Bob, <b>the latter</b> is taller? / <b>The former</b> "
        "= the first (Alice)")),
    ("John hurt ___ .", "himself", "himself",
     "Reflexives: <b>myself, yourself, himself, herself, itself, ourselves, "
     "yourselves, themselves</b>. <b>By myself</b> = by myself. "
     "<b>By himself</b> = on his own.",
     ex("John hurt <b>himself</b>. / <b>By myself</b> = alone (I) / "
        "<b>On his own</b> = alone (he)")),
    ("She prefers to drive ___ .", "herself", "herself",
     "<b>By + reflexive</b> = alone. <b>Ourselves</b> = ourselves.",
     ex("She prefers to drive <b>herself</b>. / We did it <b>ourselves</b> = we "
        "did it ourselves.")),
    ("Everyone must bring ___ own towel.", "his or her", "his or her",
     "Formal style: <b>his or her / he or she / him or herself</b>. Current "
     "style: <b>their</b>.",
     ex("Everyone must bring <b>his or her</b> own towel. / <b>Everyone must "
        "bring their own towel</b> (current).")),
], nivel="B2", tags=["pronoun advanced"])

cloze(Q1, "{{c1::None of}} the students passed.",
      extra="<div class='box rule'><span class='lbl'>Quantifiers + of</span>"
            "<b>none of, neither of, either of, all of, both of, half of, most "
            "of, some of, any of, each of, every one of, a number of</b> + "
            "<b>of</b> + <b>the / my / these</b>.</div>",
      tags="c1-c2 quantifier cloze")

cloze(P1, "The dog wagged {{c1::its}} tail.",
      extra="<div class='box warn'><span class='lbl'>its / it's</span>"
            "<b>its</b> = possessive of <i>it</i>. <b>it's</b> = <i>it is</i> / "
            "<i>it has</i>. NEVER <i>it's tail</i>.</div>",
      tags="c1-c2 pronoun cloze")
