"""01 Foundations (B1) - nouns and countability, articles, determiners,
pronouns, adjectives, adverbs."""

from ._base import gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla, badge

D = "01 Foundations (B1)::"
DN, DA, DD, DP, DJ, DV = D + "Nouns and Countability", D + "Articles", \
    D + "Determiners and Quantifiers", D + "Pronouns and Reference", \
    D + "Adjectives", D + "Adverbs"

# ===================================================== NOUNS AND COUNTABILITY

gap(DN, "How ___ sugar do you need?", "much", nivel="B1",
    cue="uncountable", forma="much sugar",
    regla="<b>Uncountable nouns</b> have no plural and are quantified with "
          "<b>much / little / some / a lot of / a bit of / plenty of</b>. "
          "They can NEVER take <i>a few</i> or <i>many</i>.",
    ejemplos=ex("I need <b>much</b> sugar.", "How <b>much</b> time do we have?",
                "She has <b>a little</b> patience with children."),
    notas=ul("<b>Common uncountables</b>: <i>advice, information, furniture, "
             "luggage, news, progress, research, staff, evidence, knowledge, "
             "money, traffic, weather, work</i> (as a total), homework.",
             "Test: if English uses <b>of</b> after it (a <i>piece</i> of), it "
             "is almost always uncountable: <i>a piece of advice, a loaf of "
             "bread, a glass of water, a chance of rain</i>.",
             "Exception: <b>work</b> is uncountable in general but countable as "
             "'a work of art': <i>two works by Picasso</i>."),
    tags="nouns countability")

gap(DN, "There aren't ___ eggs left in the fridge.", "many", nivel="B1",
    cue="negative + plural countable", forma="many eggs",
    regla="In negatives and questions, <b>plural countables</b> take "
          "<b>many / few</b>. In positives, <b>many / a lot of / lots of / "
          "plenty of</b>.",
    ejemplos=ex("There aren't <b>many</b> people at the party.",
               "Not many students passed the exam.",
               "There are a <b>lot of</b> people here."),
    notas=ul("<b>Many/few</b> count; <b>much/little</b> measure. "
             "<i>How many books / How much money</i>.",
             "Safe in all contexts: <b>a lot of, lots of, plenty of</b> (both "
             "countable and uncountable)."),
    tags="nouns quantifiers")

gap(DN, "She's got ___ friends in London.", "a few", nivel="B1",
    cue="3-4, positive", forma="a few friends",
    regla="<b>a few</b> = some (3-4), positive. <b>few</b> = hardly any, "
          "negative. <b>a little</b> = a bit (uncountable), <b>little</b> = "
          "almost none, negative.",
    ejemplos=ex("I have <b>a few</b> questions.",
               "We have <b>little</b> time left.",
               "She's got <b>few</b> friends here (optional)."),
    notas="In negatives, <b>a few</b> changes meaning: <i>I don't have many "
          "friends</i> (not many) is more negative than <i>I don't have a few "
          "friends</i> (= not the ones I have), which is unacceptable.",
    tags="quantifiers a-few")

gap(DN, "Two ___ were injured in the crash.", "men", nivel="B1",
    cue="irregular plural", forma="men",
    regla="Irregular plurals: <b>man/men, woman/women, child/children, "
          "foot/feet, tooth/teeth, goose/geese, mouse/mice, person/people</b>.",
    ejemplos=ex("Three <b>children</b> were waiting outside.",
               "The <b>women</b> from HR resigned."),
    notas=ul("<b>People</b> is irregular, but <b>person</b> can also take "
             "<b>persons</b> (formal/legal): <i>persons unknown</i>.",
             "Invariant: <b>sheep, series, species, fish, deer, aircraft</b>.",
             "Plural-only: <b>scissors, trousers, glasses, jeans, clothes, "
             "goods, belongings, surroundings</b> — used with a plural verb: "
             "<i>The scissors <b>are</b> on the table.</i>"),
    tags="plurals irregular")

gap(DN, "The police ___ looking for the thief.", "are", nivel="B1",
    cue="plural, invariant noun", forma="are",
    regla="Plural nouns that take no <b>-s</b>: <b>police, staff, clergy, "
          "cavalry, fish, series, species, aircraft, swine</b> → plural verb.",
    ejemplos=ex("<b>The police</b> <b>are</b> investigating.",
               "The <b>staff</b> <b>were</b> very supportive."),
    notas="With <b>the</b> + plural → plural noun and plural verb: <i>the "
          "police, the rich, the elderly, the blind, the dead</i>. Without "
          "<b>the</b>, or with <b>a / of</b> → singular: <i>a police station, "
          "police officers, blind people, elderly care</i>.",
    tags="plurals")

gap(DN, "Could I have some ___ , please? I'm really ___ about it.",
    "bread, hungry", nivel="B1", cue="two gaps: bread / hungry",
    forma="bread, hungry",
    regla="Countable↔uncountable shift: <b>bread</b> (uncountable) → "
          "<i>a loaf of bread, two loaves</i>. And the fixed collocation: "
          "<b>hungry</b> goes with bread, not with a made-up noun.",
    ejemplos=ex("<i>two loaves of bread, a slice of bread, a piece of bread</i>",
                "I'm <b>hungry</b> / I'm <b>starving</b> / I'm <b>peckish</b>"),
    notas=ul("Uncountables that have a count form: <b>paper→a paper, "
             "work→a work, hair→a hair</b> (a single item).",
             "Uncountables keep a zero plural: <i>no information, no advice</i> "
             "after <i>give</i> in negatives."),
    tags="countable-uncountable")

gap(DN, "The news ___ terrible.", "is", nivel="B1", cue="news (uncountable)",
    forma="is", regla="<b>The news</b> is uncountable → singular verb. Same "
    "for <i>information, advice, research, progress, weather, luggage, work, "
    "furniture, evidence</i>.",
    ejemplos=ex("<b>The news</b> <b>is</b> bad.", "<b>The information</b> <b>is</b> useful."),
    notas="<i>News</i> never takes -s: <i>no news is good news</i>.",
    tags="uncountables")

gap(DN, "___ bookshop is just round the corner.", "the", nivel="B1",
    cue="a specific shop", forma="the",
    regla="A singular countable noun that can only be identified one way "
          "(from context or shared knowledge) takes <b>the</b>.",
    ejemplos=ex("Close the <b>window</b> please.", "Look at <b>the</b> sun!"),
    notas=ul("Always <b>the</b>: <i>the sun, the moon, the earth, the "
             "internet, the news, the government, the police, the environment, "
             "the economy, the sky, the equator, the middle of the night</i>.",
             "Compare: <i>the sun</i> (the one sun) vs <i>a sun</i> (a star)."),
    tags="articles the")

# ================================================================== ARTICLES

gap(DA, "She is ___ engineer.", "an", nivel="B1", cue="vowel sound", forma="an engineer",
    regla="<b>a</b> before a consonant sound, <b>an</b> before a vowel sound. "
          "The rule is about the <b>SOUND</b>, not the letter.",
    ejemplos=ex("<b>a</b> university, <b>a</b> European, <b>a</b> one-euro coin",
                "<b>an</b> hour, <b>an</b> honest man, <b>an</b> MBA"),
    notas=ul("Exceptions: <b>a</b> + <i>hour, honest, honour, honourable, "
             "heir, MBA, MA, MS, PhD, FRS, MD</i> (silent h).",
             "Silent h disappears before an aspirated h: <i>an hour</i> but "
             "<i>a hotel, a huge, a humble, a half-hour</i>.",
             "Acronyms read letter by letter: <b>an</b> FBI agent, <b>an</b> "
             "MP3 player, <b>an</b> MP file, <b>a</b> URL, <b>a</b> USB cable."),
    tags="articles a-an")

gap(DA, "I'll be there in ___ hour.", "an", nivel="B1", cue="silent h", forma="an hour",
    regla="<b>an</b> + <i>hour, honest, honour, heir</i>: the silent h is "
          "already a vowel sound.",
    ejemplos=ex("Wait <b>an</b> hour and then call me.",
               "He made <b>an</b> honest mistake."),
    notas="The silent h is lost before an aspirated h: <i>an hour</i> but "
          "<i>a hotel</i>, <i>a huge</i>, <i>a half-hour</i>.",
    tags="articles a-an")

gap(DA, "There's ___ water in the bottle.", "a", nivel="B1",
    cue="a quantity of water", forma="a water",
    regla="You cannot say <i>a sugar</i>. To express quantity you need one of: "
          "<b>a piece of, a glass/bottle of, a little, some</b>.",
    ejemplos=ex("I'd like <b>a glass of</b> water.", "There's <b>some</b> milk left."),
    notas=ul("<b>a piece of</b> + countable: a piece of bread / a piece of cake.",
             "<b>a glass of</b> water, milk, juice, wine; <b>a cup of</b> tea; "
             "<b>a bottle of</b> beer.",
             "<b>a bar of</b> soap / chocolate; <b>a slice of</b> bread / "
             "pizza / cake; <b>a packet of</b> cigarettes / tea; <b>a sheet "
             "of</b> paper; <b>a loaf of</b> bread; <b>a bunch of</b> grapes / "
             "keys."),
    tags="countable-uncountable")

gap(DA, "She is ___ most intelligent girl in class.", "the", nivel="B1",
    cue="superlative", forma="the most intelligent",
    regla="Superlatives and equality comparisons (the two -est) take "
          "<b>the</b>: <i>the tallest, the most expensive, the best</i>.",
    ejemplos=ex("He is <b>the</b> best player here.",
               "She's <b>the</b> most reliable person I know."),
    notas="Only when you are picking the extreme out of a group. "
          "<i>She's the tallest in her class</i> (but <i>She's very tall</i> "
          "without <b>the</b>).",
    tags="superlative the")

gap(DA, "___ water boils at 100 degrees.", "Water", nivel="B1",
    cue="general statements", forma="Water",
    regla="<b>No article</b> in general statements: zero plurals, "
          "uncountables, measurements, job names, countries, cities, days, "
          "meals, sports, languages.",
    ejemplos=ex("<b>Life</b> is beautiful.", "<b>Bacon and eggs</b> for breakfast, please."),
    notas=ul("Plural: <b>My job</b> vs <b>Jobs</b> (in general).",
             "With <b>the</b> for specifics: <b>Life</b> is beautiful vs "
             "<b>The life</b> of a nurse is stressful.",
             "<i>Salsa</i> is spicy vs <i>The salsa</i> is spicy (that sauce)."),
    tags="zero-article")

gap(DA, "He plays ___ guitar and she plays ___ violin.", "the, the",
    nivel="B1", cue="musical instruments", forma="the guitar, the violin",
    regla="Musical instruments always take <b>the</b>.",
    ejemplos=ex("She plays <b>the</b> piano beautifully.",
               "Can you play <b>the</b> drums?"),
    notas=ul("With <b>by</b> or <b>on</b> + a generic instrument, no <b>the</b>: "
             "<i>He plays <b>by</b> guitar <b>on</b> stage.</i>",
             "<i>I love <b>guitar</b> music.</i>",
             "Compare: <i>play <b>the</b> piano</i> vs <i>play <b>guitar</b></i> "
             "(generic)."),
    tags="zero-article instruments")

gap(DA, "He came ___ car yesterday.", "by", nivel="B1", cue="by car",
    forma="by car",
    regla="Transport (no article) with <b>by</b>: <i>by car/bus/train/plane/"
          "bike/boat/taxi</i>; <b>on foot</b>.",
    ejemplos=ex("She goes to work <b>by</b> train.",
               "We travelled <b>on foot</b> / <b>by</b> taxi."),
    notas=ul("<b>by</b> + transport: <i>by bus, by plane, by ship, by bike, by "
             "underground</i>.",
             "<b>on</b> + the means: <i>on <b>foot</b>, on <b>horseback</b>, "
             "on <b>wheels</b></i>.",
             "<b>in</b> + a specific vehicle: <i>in <b>a</b> car, in <b>my</b> "
             "car, in <b>the</b> taxi</i>."),
    tags="prepositions by-in-on")

# =============================================== DETERMINERS AND QUANTIFIERS

gap(DD, "___ students passed the exam.", "Most", nivel="B1", cue="the majority",
    forma="Most students",
    regla="<b>Quantifiers</b>, no article, plural noun: <b>most, many, much, "
          "few, little, some, any, all, both, half, several, enough</b>. "
          "Singular (= 'one of'): <b>each, every, either, neither, another, "
          "one, no</b>.",
    ejemplos=ex("<b>Most</b> people here are Spanish.", "<b>Few</b> people knew the answer."),
    notas=ul("<b>each</b> = each one (2+), <b>every</b> = each (3+); both "
             "singular: <i>each of us, every one of them</i>.",
             "<b>either</b> / <b>neither of</b> = out of two: <i>either of the "
             "two books, neither of the answers</i>.",
             "<b>another</b> = one more, <b>the other</b> = the remaining one "
             "of two: <i>one is cheap, <b>the other</b> is expensive</i>."),
    tags="quantifiers")

gap(DD, "There's ___ milk in the fridge.", "some", nivel="B1",
    cue="affirmative", forma="some milk",
    regla="<b>Some</b> in affirmatives, <b>any</b> in negatives and questions, "
          "<b>no</b> in total negations.",
    ejemplos=ex("I've got <b>some</b> questions.", "Have you got <b>any</b> questions?",
               "I haven't got <b>any</b> questions.", "I've got <b>no</b> questions."),
    notas=ul("Exceptions: <i>Would you like <b>some</b> coffee?</i> "
             "(positive invitation), <i>It's <b>some</b> of a mess</i>, "
             "<i>You're <b>some</b> kind of...</i>. With <b>not</b> (not all): "
             "<i>not <b>some</b>...</i>.",
             "Fixed phrases: <b>any more, any other, anyone, anything, "
             "anywhere, hardly any, barely any, just any, any kind of</b>."),
    tags="some-any-no")

gap(DD, "___ of my friends is coming.", "None", nivel="B1",
    cue="none of", forma="None of my friends",
    regla="<b>none of</b> = 0 out of N (3+). <b>neither of</b> = neither of "
          "two. <b>either of</b> = one of two. All take <b>of</b> + "
          "<b>the / my / your / these / those</b>.",
    ejemplos=ex("<b>None of</b> my friends <b>is</b> coming.",
               "<b>Neither of</b> the answers <b>is</b> right."),
    notas="BrE usually takes a singular verb (<i>none of them <b>is</b> "
          "coming</i>, >70%); AmE allows plural. In exams, singular is safest.",
    tags="none-neither-either")

gap(DD, "___ of the two options is acceptable.", "Neither", nivel="B1",
    cue="neither of two", forma="Neither of the two options",
    regla="<b>Neither of</b> / <b>either of</b> with two; <b>none of</b> with "
          "three or more. <b>Neither</b> = zero, <b>either</b> = one.",
    ejemplos=ex("<b>Either of</b> the two days would work.",
               "<b>Neither of</b> them called me."),
    notas="Reply to 'Which one?': <i><b>Both / Neither / Both</b> (neither) / "
          "<b>Both</b></i>.",
    tags="none-neither-either")

gap(DD, "I have ___ money left. I spent ___ on lunch.", "little, some",
    nivel="B1", cue="two gaps: little / some", forma="little, some",
    regla="<b>little</b> = almost nothing (negative evaluation). "
          "<b>a little</b> = a bit (neutral). For neutral 'some', use "
          "<b>some</b>.",
    ejemplos=ex("I have <b>little</b> time.", "I have <b>a little</b> time."),
    notas="<i>a few / a little</i> = a small number (positive). "
          "<i>few / little</i> = hardly any (negative).",
    tags="little-a-little")

gap(DD, "The room is too small. We need ___ space.", "more", nivel="B1",
    cue="comparative before a noun", forma="more space",
    regla="With nouns: <b>more / less</b> + noun for comparatives, and "
          "<b>most / least</b> + noun for superlatives.",
    ejemplos=ex("We need <b>more space</b>.", "We need <b>more rooms</b>."),
    notas="With nouns use <b>many/much</b> for 'a lot' and <b>few/little</b> "
          "for 'not much'. With adjectives never use <b>more/fewer</b> for "
          "'less': <i>more interesting</i>, <i>fewer books</i> but "
          "<i>less interesting</i>.",
    tags="comparatives nouns")

gap(DD, "I've got ___ three hours before the meeting.", "about",
    nivel="B1", cue="approximately", forma="about three hours",
    regla="Approximating: <b>about, around, roughly, nearly, or just over "
          "three hours</b>.",
    ejemplos=ex("<b>About</b> fifty people came.",
               "<b>Roughly</b> speaking, it's a twenty-minute walk."),
    notas="<b>Nearly</b> / <b>almost</b> = 'almost' with no number implied: "
          "<i><b>Nearly</b> everyone agrees.</i>",
    tags="approximation")

gap(DD, "He gave me ___ useful advice: 'Don't do that.'", "some",
    nivel="B2", cue="uncountable plural", forma="some useful advice",
    regla="<b>Some</b> + uncountable plural nouns: <i>some advice, some "
          "luggage, some information, some research, some progress, some "
          "work, some equipment, some furniture</i>.",
    ejemplos=ex("I need <b>some advice</b> about my career.",
               "They did <b>some research</b> on the topic."),
    notas="Singular verb with these nouns: <i>The advice <b>is</b> good.</i>",
    tags="some-any-no")

gap(DD, "How ___ time will you need?", "much", nivel="B1",
    cue="how much?", forma="much time",
    regla="<b>much / little</b> for uncountables; <b>many / few</b> for "
          "countables. In questions both are fine.",
    ejemplos=ex("<b>How many</b> people? / <b>How much</b> money?",
               "There isn't <b>much water</b> left."),
    notas="<b>How much of + noun</b>: <i>How much of the cake do you want?</i> "
          "<b>How many of + plural</b>: <i>How many of you are coming?</i>",
    tags="much-many-how")

gap(DD, "Would you like ___ sugar in your coffee?", "any", nivel="B1",
    cue="question", forma="any sugar",
    regla="In questions and negatives, <b>any</b>. In <b>offers and wishes</b>, "
          "<b>some</b> ('there is some!').",
    ejemplos=ex("Would you like <b>some</b> cake?",
               "Would you like <b>any</b> help?"),
    notas="Fixed: <b>any more, any other, anyone, anything, anywhere, either, "
          "neither, hardly any, barely any, just any, any kind of</b>.",
    tags="some-any-no")

# ==================================================== PRONOUNS AND REFERENCE

gap(DP, "Every student must bring ___ own laptop.", "their", nivel="B1",
    cue="possessive (everyone)", forma="their own",
    regla="<b>Their</b> is the plural/neutral singular possessive. "
          "<b>Theirs</b> is a noun on its own.",
    ejemplos=ex("They are <b>their own</b> bosses.",
               "This is <b>theirs</b>, not mine."),
    notas=ul("<b>She</b> = she; <b>her</b> = her possessive or object; "
             "<b>hers</b> = alone.",
             "<b>It</b> = non-human / thing. Never <i>The car it is</i>.",
             "<b>They</b> = plural or neutral singular. <b>Them</b> = object. "
             "<b>Theirs</b> = noun possessive. <b>Their</b> = determiner."),
    tags="possessives")

gap(DP, "John and Mary are good friends. ___ often travel together.", "They",
    nivel="B1", cue="plural", forma="They travel",
    regla="The plural of <b>he/she/it</b> is <b>they/them/their/theirs</b>. "
          "Also used for a non-binary person.",
    ejemplos=ex("<b>They</b> are <b>their</b> friends.", "<b>They</b> travel together."),
    notas="<b>Them</b> = object. <b>Theirs</b> = noun possessive. "
          "<b>Their</b> = determiner possessive.",
    tags="plurals")

gap(DP, "The cat is sleeping on ___ bed.", "its", nivel="B1",
    cue="possessive of a thing", forma="its bed",
    regla="<b>Its</b> = possessive of <b>it</b> (non-human). "
          "<b>It's</b> = <i>it is / it has</i>. The single most confused pair "
          "in English.",
    ejemplos=ex("The dog wagged <b>its tail</b>.", "It's a nice day.",
               "It's been a long week."),
    notas="NEVER <i>The dog wags it's tail</i>. Always <b>its</b>, no "
          "apostrophe. <i>Its</i> = its; <i>it's</i> = it is/has.",
    tags="its-its")

gap(DP, "___ of you is coming to the party?", "Which", nivel="B1",
    cue="interrogative (of a group)", forma="Which of you",
    regla="<b>Which</b> = out of a set (more than two). <b>What</b> = what "
          "thing (identity). <b>Who</b> = what person.",
    ejemplos=ex("<b>Which</b> colour do you prefer?",
               "<b>What</b> is your name? / <b>Who</b> is he?"),
    notas="Answer: <b>Which</b> → 'this one' (<i>the first one</i>). "
          "<b>What</b> → a thing (<i>a sandwich</i>). <b>Who</b> → a person "
          "(<i>my sister</i>).",
    tags="interrogatives")

gap(DP, "The blue one is nicer. I'll take ___ .", "the latter", nivel="C1",
    cue="the second of two", forma="the latter",
    regla="<b>The former</b> = the first. <b>The latter</b> = the second. "
          "Only with two items.",
    ejemplos=ex("Between Alice (former) and Bob (latter), Bob is taller."),
    notas="With three or more: <i>A, B and C - <b>the former</b> (A), <b>the "
          "latter</b> (B and C)</i>. Or better: <i>A is X, B and C are Y</i>.",
    tags="determiner the-former")

gap(DP, "Everyone should bring ___ own towel.", "his or her", nivel="B2",
    cue="singular they (formal)", forma="his or her own",
    regla="Formal style: <b>his or her / he or she / him or herself</b>. "
          "Current style: <b>their</b>.",
    ejemplos=ex("Everyone should bring <b>his or her</b> ID (formal).",
               "Everyone should bring <b>their</b> ID (current)."),
    notas="For mixed or unspecified groups, singular <b>they</b> has been "
          "standard since 2019.",
    tags="possessives")

# ================================================================= ADJECTIVES

gap(DJ, "She bought a ___ red leather handbag.", "beautiful", nivel="B1",
    cue="adjective order", forma="a beautiful red leather handbag",
    regla="Order: <b>Opinion → Size/Age → Shape → Colour → Origin → Material "
          "→ Purpose</b> → noun. Mnemonic: <b>OSASCOMP</b>.",
    ejemplos=ex("a <b>lovely little Italian silver</b> bracelet",
               "a <b>famous old blue French</b> painting",
               "three <b>beautiful large rectangular red Japanese wooden "
               "coffee</b> table"),
    notas=ul("Opinion: beautiful, lovely, ugly, wonderful, terrible, nice, "
             "awful, good, horrible.",
             "Size: big, small, little, huge, tiny, massive, enormous, "
             "medium-size, large.",
             "Shape: square, round, circular, rectangular, triangular, oval, "
             "pyramidal, spherical.",
             "Colour: red, blue, green, black, white, grey, orange, purple, "
             "pink, brown, golden, silver.",
             "Origin: American, Chinese, Egyptian, Filipino, Greek, Indian, "
             "Japanese, Mexican, Norwegian, Pakistani, Peruvian, Russian, "
             "Thai, Turkish, Vietnamese.",
             "Material: wood, wooden, silk, plastic, iron, paper, card, "
             "cardboard, glass, leather, steel, stone, cloth, wool, cotton, "
             "nylon, rubber.",
             "Purpose: hiking, walking, driving, sleeping, running, typing, "
             "housework."),
    tags="adjective-order")

gap(DJ, "This is ___ than that one.", "better", nivel="B1", cue="irregular (good)",
    forma="better than",
    regla="Irregular comparatives: <b>good/well → better → best</b>; "
          "<b>bad/badly → worse → worst</b>; <b>far → farther/further → "
          "farthest/furthest</b>; <b>little → less → least</b>; "
          "<b>much/many → more → most</b>; <b>late → later → latest</b>.",
    ejemplos=ex("This one is <b>better than</b> that one.",
               "She runs <b>faster than</b> me.", "He did <b>better than</b> expected."),
    notas="Use <b>than</b> (not <i>as...than</i>). Bigger takes a doubled "
          "consonant: <i>bigger</i> = big + er.",
    tags="comparatives irregular")

gap(DJ, "The film was ___ . I really enjoyed it.", "brilliant", nivel="C1",
    cue="B1 → C1 (not 'very good')", forma="brilliant",
    regla="Avoid <i>very good / very bad / very big</i>. Upgrade with: "
          "<b>excellent, outstanding, brilliant, superb, remarkable, "
          "exceptional, appalling, dreadful, huge, massive, tiny</b>.",
    ejemplos=ex("The film was <b>brilliant</b>.", "The service was <b>appalling</b>.",
               "It's a <b>huge</b> problem."),
    notas="Also: <b>fantastic, terrific, dreadful, terrible, outstanding, "
          "superb, phenomenal</b>. And instead of <i>a lot of</i>: "
          "<b>plenty of, tons of, loads of, a great deal of, a great many</b>.",
    tags="upgrade c1")

gap(DJ, "She's ___ with her students.", "patient", nivel="B1",
    cue="adjective + preposition", forma="patient with",
    regla="Many adjectives are fixed with a preposition: <b>patient with, "
          "angry at/about, interested in, good at, bad at, fond of, tired of, "
          "worried about, proud of, responsible for, similar to, different "
          "from, famous for, full of, surprised at/by, annoyed with, "
          "disappointed in/with</b>.",
    ejemplos=ex("She's <b>patient with</b> kids.", "He's <b>interested in art</b>.",
               "I'm <b>good at</b> maths."),
    notas="Typical errors: <i>good <s>en</s> maths</i> (must be <b>at</b>), "
          "<i>interested <s>of</s></i> (must be <b>in</b>).",
    tags="adjective-preposition")

gap(DJ, "The opposite of 'expensive' is ___ .", "cheap", nivel="B1",
    cue="antonym", forma="cheap",
    regla="Irregular antonyms: <b>expensive/cheap, big/small, good/bad, "
          "hot/cold, high/low, old/young, fat/thin, long/short, hard/soft, "
          "wide/narrow, deep/shallow, rich/poor, heavy/light, clean/dirty, "
          "new/old, up/down</b>.",
    ejemplos=ex("The hotel was <b>expensive</b> but the food was <b>cheap</b>.",
               "He's <b>short</b> and she's <b>tall</b>."),
    notas="Nouns: <i>price, cost, expense</i> (high) vs <i>a bargain, a steal, "
          "value, a discount</i> (cheap).",
    tags="antonyms")

gap(DJ, "She's the ___ person I've ever met.", "kindest", nivel="B1",
    cue="short superlative", forma="the kindest",
    regla="One syllable and -y adjectives take <b>-est</b> (kindest, tallest, "
          "biggest, funniest, easiest, nicest). Three or more syllables take "
          "<b>the most + adjective</b>.",
    ejemplos=ex("He's the <b>tallest</b> in the room.",
               "It's the <b>most interesting</b> book I've read."),
    notas="Irregular superlatives: <b>good → best, bad → worst, far → "
          "farthest/furthest, little → least, many/much → most</b>.",
    tags="superlatives")

gap(DJ, "I bought a ___ jacket. It was very ___ .", "leather, expensive",
    nivel="B1", cue="two gaps: material / expensive", forma="leather, expensive",
    regla="Material adjectives go <b>after</b> the noun in English: "
          "<i>a <b>leather</b> jacket</i>. Opinion adjectives go <b>before</b>.",
    ejemplos=ex("a <b>leather</b> sofa / a <b>wooden</b> table / a <b>silk</b> "
               "scarf / <b>wool</b> socks", "a <b>beautiful leather</b> jacket"),
    notas="Errors: <i>a jacket in leather</i> (rare), <i>a leather-jacket</i> "
          "(rare). Others: <i>a <b>black and white</b> photo, a <b>brand new</b> "
          "car</i>.",
    tags="adjective-order material")

# ==================================================================== ADVERBS

gap(DV, "He runs very ___ . He's really ___ .", "fast, fast", nivel="B1",
    cue="two gaps: fast / fast", forma="fast, fast",
    regla="<b>Fast, hard</b> and <b>late</b> are both adjective and adverb. "
          "<b>Good</b> and <b>well</b> are not: the adverb of <i>good</i> is "
          "<b>well</b>.",
    ejemplos=ex("He runs <b>fast</b>.", "She sings <b>well</b> (not 'good').",
               "He works <b>hard</b>."),
    notas="Spelling traps: <b>hardly</b> = almost not. <b>lately</b> = "
          "recently. <b>near</b> (close) vs <b>nearly</b> (almost). "
          "<b>late</b> vs <b>lately</b>.",
    tags="adverbs same-form")

gap(DV, "I only found out ___ .", "yesterday", nivel="B1",
    cue="adverb of time", forma="yesterday",
    regla="<b>Yesterday / today / tomorrow</b> are ADVERBS. They go at the end "
          "of the clause or before the verb.",
    ejemplos=ex("I saw her <b>yesterday</b>.", "I'll call you <b>tomorrow</b>.",
               "I'm seeing the dentist <b>today</b>."),
    notas="<i>Yesterday <b>morning</b></i> = yesterday morning. Say "
          "<b>last night</b>, not <i>yesterday night</i>.",
    tags="time-adverbs")

gap(DV, "She sings ___ than her sister.", "better", nivel="B1",
    cue="adverb comparative", forma="better than",
    regla="<b>-ly</b> adverbs use <b>more/most</b>: <i>more quickly, more "
          "easily, more carefully, most often</i>. Short ones use "
          "<b>-er/-est</b>: <i>harder, faster, earlier, later, better, worse</i>.",
    ejemplos=ex("He speaks <b>more fluently than</b> me.",
               "She arrived <b>earlier than</b> us."),
    notas="Never <i>more better</i>. <i>Bigger</i> = big + er (doubled "
          "consonant) or <i>more big</i> (colloquial, non-standard).",
    tags="comparatives adverbs")

gap(DV, "___ he is rich, he isn't happy.", "Although", nivel="B2",
    cue="concession", forma="Although he is rich",
    regla="<b>Although / Though / Even though</b> + a full CLAUSE (subject + "
          "verb). <b>Despite / In spite of</b> + a NOUN or <b>-ing</b> (never "
          "a clause).",
    ejemplos=ex("<b>Although</b> he is rich, he isn't happy.",
               "<b>Despite his wealth</b>, he isn't happy.",
               "<b>Despite being rich</b>, he isn't happy."),
    notas=ul("<i>Despite <s>he</s></i> is wrong → <b>Despite her being</b> / "
             "<b>Despite the fact that she</b>.",
             "<i>Although <s>of</s></i> is wrong → <b>Although she was</b>.",
             "Inverted with <b>though</b> at the end: <i>He's rich <b>though</b>.</i>"),
    tags="concession although-despite")

gap(DV, "I need to leave ___ the office before 5.", "for", nivel="B1",
    cue="purpose", forma="for the office",
    regla="Adverbials of purpose (single verb): <b>to + noun</b> = direction; "
          "<b>for + noun</b> = purpose / beneficiary.",
    ejemplos=ex("I went <b>to</b> London.", "I made it <b>for</b> you.",
               "She left early <b>to catch</b> the train."),
    notas="<b>to</b> = movement/destination. <b>for</b> = reason/beneficiary. "
          "<i>He went <b>to</b> the shop <b>for</b> milk.</i>",
    tags="to-for adverbs")

gap(DV, "She's a ___ good memory.", "very", nivel="B1", cue="intensifier",
    forma="very good",
    regla="Adjectives that are ALREADY absolute in degree (good, bad, huge, "
          "tiny, terrible, wonderful, lovely) cannot take <b>very</b> in "
          "standard English. Use <b>really / absolutely / quite</b>.",
    ejemplos=ex("She's <b>a very good</b> singer.", "She's <b>a really good</b> singer.",
               "The film was <b>absolutely terrible</b>."),
    notas="Colloquially natives use <i>It was <b>really</b> good</i> all the "
          "time. In exams, <b>really</b> + absolute is fine.",
    tags="very-really degree")

gap(DV, "___ I studied hard, I failed.", "Despite", nivel="B2",
    cue="concession (-ing)", forma="Despite studying",
    regla="<b>Despite + -ing / noun</b> = although. <b>Although + clause</b> "
          "= although.",
    ejemplos=ex("<b>Despite studying</b> hard, I failed.",
               "<b>In spite of working</b> all night, he got it wrong.",
               "It's <b>despite the rain</b> that we won."),
    notas="Never <i>Despite he studied</i>. <b>In spite of</b> is the literal "
          "'in spite of'.",
    tags="concession")

gap(DV, "Speak ___ .", "clearly", nivel="B1", cue="adverb from -able",
    forma="clearly",
    regla="<b>-ly</b> adverbs: happy → happily, careful → carefully, true → "
          "truly, gentle → gently, awful → awfully, possible → possibly.",
    ejemplos=ex("He spoke <b>politely</b> to the customer.",
               "She <b>carefully</b> closed the door."),
    notas="Same pattern: <b>full → fully, true → truly, rare → rarely, similar "
          "→ similarly</b>.",
    tags="adverbs -ly")

gap(DV, "The train arrived ___ time.", "on", nivel="B1",
    cue="punctual / late", forma="on time",
    regla="Fixed: <b>on time</b> (punctual), <b>in time</b> (in good time), "
          "<b>late for</b>, <b>early for</b>, <b>on schedule</b>.",
    ejemplos=ex("The bus was <b>on time</b>.", "You're <b>late for</b> the meeting!"),
    notas="<i>in time</i> can mean 'with enough time to spare', but for "
          "'on schedule' use <b>on time</b>.",
    tags="fixed-phrases")

gap(DV, "I only ___ in the morning.", "wake up", nivel="B1",
    cue="reflexive verb", forma="wake up",
    regla="Many verbs are reflexives in English but not in other languages: "
          "<b>wake up, get up, get dressed, get married, get divorced, get on, "
          "get off, get in, get out, get used to, be born, be married, be "
          "named, be called, be situated, be located, be based, be known as, "
          "be made</b>.",
    ejemplos=ex("I <b>get up</b> at 7.", "She <b>got married</b> last year.",
               "He's <b>used to getting</b> up early."),
    notas="Consequence: the <b>perfect</b> becomes transitive: <i>She <b>has "
          "got married</b></i>. A non-reflexive English verb takes no "
          "reflexive pronoun: <i>She married him</i>.",
    tags="reflexive-verbs")

gap(DV, "It costs ___ 20 pounds to get there.", "about", nivel="B1",
    cue="approximately", forma="about 20 pounds",
    regla="With cost/speed/distance: <b>about, around, roughly, approximately, "
          "over, nearly, almost</b> + number.",
    ejemplos=ex("It costs <b>roughly</b> 50 euros.", "<b>Over</b> 100 people came."),
    notas="<b>Over/under</b> + number = more/less than. <b>Above/below</b> = "
          "above/below. <i>Nearly all of them</i> = almost all.",
    tags="approximation")

# ============================================================== SUPPORT CLOZE

cloze(DN, "{{c1::She}} {{c2::has}} {{c3::lived}} {{c4::here}} {{c5::since}} 2019.",
      extra="<div class='box rule'><span class='lbl'>Aspect test</span>"
            "Started in the past, still true now + <b>since / for</b> → "
            "<b>Present Perfect</b>.</div>",
      tags="c1-c2 perfect cloze")

cloze(DN, "He didn't {{c1::arrive}} until 10 p.m.",
      extra="<div class='box note'><span class='lbl'>until / till</span>"
            "<b>until</b> and <b>till</b> only with the meaning 'up to'. Also "
            "in questions and negatives, but then as 'for how long'.</div>",
      tags="c1-c2 until till cloze")

cloze(DA, "I saw {{c1::a}} {{c2::unusual}} {{c3::old}} {{c4::Italian}} "
      "{{c5::leather}} {{c6::handbag}}.",
      extra="<div class='box rule'><span class='lbl'>Adjective order</span>"
            "<b>O</b>pinion → si<b>Z</b>e → sh<b>A</b>pe → <b>C</b>olour → "
            "<b>O</b>rigin → <b>M</b>aterial → <b>P</b>urpose.</div>",
      tags="c1-c2 adjective-order cloze")
