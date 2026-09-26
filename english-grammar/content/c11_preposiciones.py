"""11 Prepositions (B1-C2) - time, place, movement, and the fixed
verb+preposition / adjective+preposition combinations that cause most errors."""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "11 Prepositions::"
T, L, M, F1, F2 = D + "Time", D + "Place", D + "Movement", \
    D + "Verb + Preposition", D + "Adjective + Preposition"

# =================================================================== TIME

serie_gap(T, [
    ("I'll see you ___ Monday.", "on", "on Monday",
     "<b>on</b> + days, specific dates, parts of the day.",
     ex("<b>on</b> Monday, <b>on</b> 5 May, <b>on</b> Friday morning.")),
    ("I'll see you ___ the morning of the 5th.", "on", "on the morning of the 5th",
     "<b>on</b> + <i>the</i> + day/date + <i>of</i>.",
     ex("<b>on</b> the morning of the 5th, <b>on</b> the day of the wedding.")),
    ("I was born ___ 1990.", "in", "in 1990",
     "<b>in</b> + years, months, seasons, centuries, decades.",
     ex("<b>in</b> 1990, <b>in</b> July, <b>in</b> winter, <b>in</b> the 90s.")),
    ("The meeting is ___ 3 o'clock.", "at", "at 3 o'clock",
     "<b>at</b> + specific times and expressions like <i>noon, midnight, "
     "night, weekend, Christmas</i>.",
     ex("<b>at</b> 3 o'clock, <b>at</b> noon, <b>at</b> midnight, <b>at</b> night.")),
    ("She's been here ___ two weeks.", "for", "for two weeks",
     "<b>for</b> + duration.",
     ex("<b>for</b> two weeks, <b>for</b> a long time, <b>for</b> ages.")),
    ("I haven't seen her ___ we met.", "since", "since we met",
     "<b>since</b> + starting point. Note: <b>since</b> needs <b>for</b> for "
     "duration: <i>she's worked <s>for</s> 2019</i> is WRONG → <b>since</b> 2019.",
     ex("<b>since</b> Monday, <b>since</b> I was a child, <b>since</b> we met.")),
    ("The class begins ___ 9 a.m. ___ Monday.", "at, on", "at 9 a.m. on Monday",
     "<b>at</b> for the time, <b>on</b> for the day.",
     ex("The class begins <b>at</b> 9 a.m. <b>on</b> Monday.")),
    ("We're leaving ___ Friday morning.", "on", "on Friday morning",
     "<b>on</b> + day + part of the day. NEVER <i>in Friday morning</i>.",
     ex("<b>on</b> Friday morning, <b>on</b> Sunday afternoon.")),
    ("It happens ___ summer.", "in", "in summer",
     "<b>in</b> + seasons (BrE). In AmE <b>at</b>: <i>at summertime, at "
     "Christmas, at night, at the weekend, at my grandma's</i>.",
     ex("<b>in</b> summer (UK) / <b>at</b> summer (US).")),
    ("The train leaves ___ ten minutes.", "in", "in ten minutes",
     "<b>in</b> + a future period = 'in' (within).",
     ex("See you <b>in</b> a week. / I'll be back <b>in</b> two hours.")),
    ("He arrived home late ___ the night.", "at", "at night",
     "<b>at night</b> always. NEVER <i>in the night</i> (except 'during the "
     "night' in a general sense).",
     ex("It was <b>at</b> night. / <b>In</b> the night I had a dream.")),
    ("I was born ___ October.", "in", "in October",
     "<b>in</b> + months. NEVER <i>on October</i>.",
     ex("<b>in</b> January, <b>in</b> September.")),
    ("I'll be 30 ___ next June.", "on", "on 1 June",
     "<b>on</b> + a specific date. <b>In</b> if there is no day.",
     ex("<b>on</b> 1 June. / <b>In</b> June I'll be 30.")),
    ("I work ___ night and sleep ___ day.", "at, during", "at night / during the day",
     "<b>at night</b> / <b>in the day</b> (or <b>during the day</b>).",
     ex("I work <b>at night</b> and rest <b>in the day</b>.")),
    ("The exam is ___ 3rd ___ 15th of May.", "between, and", "between the 3rd and the 15th",
     "<b>between</b> ... <b>and</b> = between (two limits). "
     "<b>from</b> ... <b>to/till</b> = from...until.",
     ex("<b>between</b> 2010 <b>and</b> 2015 / <b>from</b> 2010 <b>to</b> 2015.")),
    ("I'm busy ___ the end of the month.", "until", "until the end of the month",
     "<b>until / till</b> = up to (same meaning).",
     ex("Wait <b>until</b> Friday. <b>Till</b> is identical, more colloquial.")),
    ("It took me two hours ___ get there.", "to", "to get",
     "<b>to</b> + base verb = the time an action takes.",
     ex("It took me ten minutes <b>to</b> finish. / How long did it take you <b>to</b> get there?")),
    ("See you ___ lunchtime.", "at", "at lunchtime",
     "<b>at</b> + meals (UK): <i>at breakfast, at lunch, at dinner, at supper</i>. "
     "In AmE <b>in</b> is used for lunch/breakfast.",
     ex("<b>at</b> lunch (UK) / <b>in</b> lunch (US) is possible.")),
], nivel="B1", tags=["preposition time"])

# =================================================================== PLACE

serie_gap(L, [
    ("She lives ___ Madrid.", "in", "in Madrid",
     "<b>in</b> + big cities, countries, continents, districts.",
     ex("live <b>in</b> Madrid, <b>in</b> Spain, <b>in</b> Europe, <b>in</b> the city centre.")),
    ("They live ___ a small village.", "in", "in a village",
     "<b>in</b> for any inhabited area.",
     ex("<b>in</b> a village, <b>in</b> a small town, <b>in</b> the countryside.")),
    ("He's waiting ___ the bus stop.", "at", "at the bus stop",
     "<b>at</b> + a precise point: <i>the bus stop, the door, the entrance, the "
     "station, the airport</i>.",
     ex("Meet me <b>at</b> the station. / He's <b>at</b> the door.")),
    ("The keys are ___ the table.", "on", "on the table",
     "<b>on</b> + surfaces: <i>the table, the wall, the floor, the ceiling, the "
     "shelf</i>.",
     ex("The book is <b>on</b> the desk. / A fly <b>on</b> the ceiling.")),
    ("He fell asleep ___ the sofa.", "on", "on the sofa",
     "<b>on</b> for a horizontal or vertical contact surface. Also <b>in</b> for "
     "sleeping/lying positions.",
     ex("He lay <b>on</b> the bed. / She's asleep <b>on</b> the sofa.")),
    ("There's a picture ___ the wall ___ the sofa.", "on, above", "on the wall above the sofa",
     "<b>on</b> (on the surface) + <b>above</b> (higher, not touching). "
     "<b>Over</b> also works but overlaps with <b>above</b> in vertical use.",
     ex("The lamp is <b>above</b> the table. <b>Over</b> = covering.")),
    ("She's ___ the kitchen.", "in", "in the kitchen",
     "<b>in</b> + rooms and enclosed spaces.",
     ex("<b>in</b> the kitchen, <b>in</b> the bathroom, <b>in</b> bed, <b>in</b> the car.")),
    ("The cat is hiding ___ the bed.", "under", "under the bed",
     "<b>under / underneath</b> = below, covered. <b>below</b> = below, not "
     "touching.",
     ex("The ball rolled <b>under</b> the car. / It's <b>below</b> the window.")),
    ("Sit ___ me, please.", "next to", "next to me",
     "<b>next to, beside, by</b> = next to.",
     ex("Sit <b>beside</b> me. / <b>By</b> the window.")),
    ("The shop is ___ the bank.", "opposite", "opposite the bank",
     "<b>opposite</b> = across from. NEVER <i>in front to</i>.",
     ex("The pharmacy is <b>opposite</b> the school. / <b>in front of</b> the school (in front of).")),
    ("He fell ___ the horse.", "off", "off the horse",
     "<b>off</b> = falling from a surface or a vehicle.",
     ex("He fell <b>off</b> the horse. / She got <b>off</b> the bus.")),
    ("It's stuck ___ the door.", "behind", "behind the door",
     "<b>behind</b> = behind. <b>in front of</b> = in front of. "
     "<b>Beside</b> = next to.",
     ex("The keys are <b>behind</b> the door. / He parked <b>in front of</b> the house.")),
    ("There's a hole ___ the wall.", "in", "in the wall",
     "<b>in</b> for holes in surfaces. <b>on</b> for things resting on it.",
     ex("a hole <b>in</b> the wall / a picture <b>on</b> the wall.")),
    ("She's standing ___ the queue.", "in", "in the queue",
     "<b>in</b> + a queue or line: <i>in a queue/line, in a row</i>.",
     ex("stand <b>in</b> a line. / He's <b>in</b> the queue for tickets.")),
    ("The village is ___ the mountains.", "among", "among the mountains",
     "<b>among</b> = among several (uncultivated). <b>between</b> = between two.",
     ex("<b>among</b> the trees / <b>between</b> the two houses.")),
], nivel="B1", tags=["preposition place"])

# =============================================================== MOVEMENT

serie_gap(M, [
    ("I'm going ___ the cinema.", "to", "to the cinema",
     "<b>to</b> = direction, destination. Without <b>to</b> there is no movement.",
     ex("go <b>to</b> work, come <b>to</b> my house, fly <b>to</b> Paris.")),
    ("He jumped ___ the river.", "into", "into the river",
     "<b>into</b> = inwards. <b>out of</b> = outwards. <b>on</b> = on top. "
     "<b>off</b> = from the top.",
     ex("jumped <b>into</b> the water / ran <b>out of</b> the house / "
        "climbed <b>on</b> the roof / fell <b>off</b> the wall.")),
    ("She walked ___ the bridge.", "across", "across the bridge",
     "<b>across</b> = side to side. <b>through</b> = through (inside). "
     "<b>along</b> = along. <b>over</b> = over.",
     ex("<b>across</b> the field / <b>through</b> the tunnel / "
        "<b>along</b> the road / <b>over</b> the hill.")),
    ("The plane took off ___ the runway.", "from", "from the runway",
     "<b>from</b> = starting point. <b>to</b> = destination.",
     ex("depart <b>from</b> Madrid / arrive <b>in</b> Barcelona / fly <b>to</b> Paris.")),
    ("He climbed ___ the ladder.", "up", "up the ladder",
     "<b>up / down</b> go WITH a preposition (<b>up the stairs</b>) or WITHOUT "
     "it (<b>climb up</b>, <b>go down</b>).",
     ex("climb <b>up</b> the stairs / go <b>down</b> the hill / run <b>up</b> the road.")),
    ("The cat jumped ___ the table.", "onto", "onto the table",
     "<b>on</b> = position. <b>onto</b> = movement onto. <b>off</b> = from the "
     "top outwards.",
     ex("jump <b>onto</b> the table / get <b>on</b> the bus / "
        "take <b>off</b> the shoes / get <b>off</b> the bus.")),
    ("They drove ___ the tunnel.", "through", "through the tunnel",
     "<b>through</b> = passing through a space. <b>across</b> = over a surface.",
     ex("drive <b>through</b> the tunnel / walk <b>across</b> the grass.")),
    ("The plane is flying ___ the Atlantic.", "over", "over the Atlantic",
     "<b>over</b> = above, not touching.",
     ex("fly <b>over</b> the Atlantic / build a bridge <b>over</b> the river.")),
    ("She walked ___ the street to the station.", "down", "down the street",
     "<b>along / down / up</b> + street/road = direction along it.",
     ex("walk <b>down</b> the street / go <b>along</b> this road.")),
], nivel="B2", tags=["preposition movement"])

# ==================================================== VERB + PREPOSITION

serie_gap(F1, [
    ("It depends ___ the weather.", "on", "depend on",
     "<b>depend on, rely on, count on, insist on, concentrate on</b>.",
     ex("It <b>depends on</b> the weather. / I <b>rely on</b> you.")),
    ("She succeeded ___ the exam.", "in", "succeed in doing",
     "<b>succeed in + V-ing / noun</b>.",
     ex("She <b>succeeded in passing</b> the exam.")),
    ("He blamed his boss ___ the error.", "for", "blame for",
     "<b>blame A for B</b>.",
     ex("Don't <b>blame me for</b> that. / She <b>blamed him for</b> the delay.")),
    ("They apologised ___ the delay.", "for", "apologise for",
     "<b>apologise for + noun/V-ing</b>.",
     ex("We <b>apologised for the inconvenience</b>.")),
    ("She objected ___ the plan.", "to", "object to",
     "<b>object to + noun/V-ing</b>.",
     ex("Nobody <b>objected to</b> the plan.")),
    ("He referred ___ the manager.", "to", "refer to",
     "<b>refer to + noun / that-clause</b>.",
     ex("I was told to <b>refer to</b> the manager.")),
    ("They agreed ___ a new price.", "on", "agree on",
     "<b>agree on + noun</b> (a mutual agreement) / <b>agree to + V</b> "
     "(accepting a proposal).",
     ex("We <b>agreed on</b> the price. / She <b>agreed to meet</b> at 8.")),
    ("He escaped ___ prison.", "from", "escape from",
     "<b>escape from, flee from, suffer from, recover from</b>.",
     ex("He <b>escaped from</b> prison. / She <b>suffered from</b> a cold.")),
    ("It consists ___ three parts.", "of", "consist of",
     "<b>consist of, be made of</b> (material), <b>be made from</b> "
     "(transformation).",
     ex("It <b>consists of</b> 3 parts. / It's <b>made of</b> wood / <b>made from</b> grapes.")),
    ("He prefers tea ___ coffee.", "to", "prefer X to Y",
     "<b>prefer A to B</b>. NEVER <i>prefer A than B</i>.",
     ex("I <b>prefer tea to coffee</b>. / I <b>prefer walking to taking the bus</b>.")),
    ("She's afraid ___ dogs.", "of", "afraid of",
     "<b>afraid of, scared of, fond of, proud of, aware of, capable of, "
     "guilty of, jealous of, tired of</b>.",
     ex("She's <b>afraid of</b> dogs. / <b>Proud of</b> his daughter.")),
    ("He insisted ___ paying.", "on", "insist on",
     "<b>insist on + V-ing</b>. NEVER <i>insist to pay</i>.",
     ex("She <b>insisted on driving</b>.")),
    ("They took part ___ the protest.", "in", "take part in",
     "<b>take part in, take part in, join, attend</b>.",
     ex("He <b>took part in</b> the meeting. / <b>join</b> takes no <b>in</b>.")),
    ("I look forward ___ hearing from you.", "to", "look forward to",
     "<b>look forward to + noun/V-ing</b>. Here <b>to</b> is a preposition, so "
     "it takes <b>-ing</b>.",
     ex("I <b>look forward to seeing</b> you. / <s>to see</s> is WRONG.")),
    ("She apologised ___ breaking the vase.", "for", "apologise for",
     "<b>apologise for + V-ing</b>.",
     ex("He <b>apologised for being late</b>.")),
    ("He applied ___ the job.", "for", "apply for",
     "<b>apply for + a post</b> / <b>apply to + a university</b>.",
     ex("She <b>applied for</b> the job at Google.")),
    ("I'm banking ___ winning.", "on", "count on",
     "<b>bank on, count on, rely on, depend on</b>.",
     ex("I <b>count on</b> seeing you tomorrow.")),
    ("He was accused ___ theft.", "of", "accused of",
     "<b>accuse of, blame for, suspect of, be charged with</b>.",
     ex("He was <b>accused of theft</b>.")),
    ("They benefit ___ exercise.", "from", "benefit from",
     "<b>benefit from, profit from, result from, suffer from, die from</b>.",
     ex("You <b>will benefit from</b> more practice.")),
    ("She warned me ___ the dogs.", "about", "warn about",
     "<b>warn about/of, remind about/of, inform of/about</b>.",
     ex("He <b>warned me about</b> the traffic.")),
    ("I'm used ___ waking up early.", "to", "be used to",
     "<b>be used to + noun/V-ing</b> (be accustomed). "
     "<b>used to + base</b> (used to). Never confuse them.",
     ex("I'm <b>used to getting</b> up early. / I <b>used to get</b> up late.")),
    ("He insisted ___ the car was fine.", "that", "insist that",
     "<b>insist that + clause</b>, <b>suggest that</b>, <b>demand that</b>, "
     "<b>recommend that</b>.",
     ex("She <b>insisted that</b> she was right.")),
    ("It reminds me ___ my childhood.", "of", "remind someone of",
     "<b>remind someone of something</b>.",
     ex("This song <b>reminds me of</b> my grandmother.")),
    ("She objected ___ being interrupted.", "to", "object to",
     "<b>object to + V-ing</b>.",
     ex("She <b>objected to being interrupted</b>.")),
    ("The film is based ___ a true story.", "on", "based on",
     "<b>based on, built on, founded on, concentrated on, focused on</b>.",
     ex("The novel is <b>based on</b> a real case.")),
    ("He walked ___ the street without stopping.", "down", "down the street",
     "<b>down / along / up</b> + street/road.",
     ex("walk <b>down</b> the road / go <b>along</b> the river.")),
    ("I couldn't get ___ the phone.", "to", "get to",
     "<b>get to + a place</b> = arrive. <b>get + object</b> = obtain.",
     ex("I need to <b>get to</b> the station. / I <b>got a job</b>.")),
    ("He ran ___ of time.", "out", "run out of",
     "<b>run out of, run into, get rid of, get out of</b>.",
     ex("We <b>ran out of</b> milk. / <b>get rid of</b> the rubbish.")),
], nivel="B2", tags=["verb-preposition"])

# ================================================= ADJECTIVE + PREPOSITION

serie_gap(F2, [
    ("She's good ___ maths.", "at", "good at",
     "<b>good at, bad at, better at, skilled at</b>. NEVER <i>good in</i>.",
     ex("She's <b>good at</b> maths. / He's <b>bad at</b> directions.")),
    ("He's interested ___ art.", "in", "interested in",
     "<b>interested in, keen on, fond of, crazy about, into</b>. "
     "NEVER <i>interested of/on</i>.",
     ex("He's <b>interested in</b> art. / She's <b>keen on</b> skiing.")),
    ("He's different ___ his brother.", "from", "different from",
     "<b>different from</b> (BrE) / <b>different than</b> (AmE). "
     "<b>similar to, same as</b>.",
     ex("He's <b>different from</b> me. / It's <b>similar to</b> the last one.")),
    ("She's married ___ a doctor.", "to", "married to",
     "<b>married to</b> (not <i>with</i>).",
     ex("She's <b>married to</b> a German doctor. / <b>engaged to</b>, <b>related to</b>.")),
    ("I'm responsible ___ this project.", "for", "responsible for",
     "<b>responsible for, in charge of, guilty of, famous for, known for</b>.",
     ex("She's <b>responsible for</b> marketing. / <b>famous for</b> his novels.")),
    ("He was accused ___ murder.", "of", "accused of",
     "<b>accused of, proud of, aware of, capable of, jealous of</b>.",
     ex("He was <b>accused of</b> murder.")),
    ("She's proud ___ her son.", "of", "proud of",
     "<b>proud of, fond of, tired of, sick of, fed up with</b>.",
     ex("She's <b>proud of</b> her son. / I'm <b>tired of</b> this noise.")),
    ("The film was full ___ action.", "of", "full of",
     "<b>full of, free of, short of, fond of</b>.",
     ex("The film was <b>full of</b> action. / <b>free of</b> charge.")),
    ("I'm disappointed ___ the result.", "with", "disappointed with",
     "<b>disappointed with/about, satisfied with, annoyed with, surprised "
     "at/by, worried about</b>.",
     ex("I'm <b>disappointed with</b> the service. / <b>surprised at</b> the news.")),
    ("The children are afraid ___ the dark.", "of", "afraid of",
     "<b>afraid of, scared of, frightened of</b>.",
     ex("The kids are <b>afraid of</b> the dark.")),
    ("She's crazy ___ him.", "about", "crazy about",
     "<b>crazy about, keen on, crazy about</b>.",
     ex("I'm <b>crazy about</b> football. / <b>keen on</b> skiing.")),
    ("He was born ___ a poor family.", "into", "born into",
     "<b>born into</b> + family. <b>born with</b> + a condition. "
     "<b>born in</b> + a place.",
     ex("<b>born into</b> a wealthy family / <b>born with</b> blue eyes / "
        "<b>born in</b> Madrid.")),
    ("I'm fond ___ Italian food.", "of", "fond of",
     "<b>fond of, keen on, tired of</b>.",
     ex("I'm <b>fond of</b> Italian food.")),
    ("This medicine is good ___ headaches.", "for", "good for",
     "<b>good for, useful for, bad for, suitable for, responsible for</b>.",
     ex("Exercise is <b>good for</b> your health.")),
    ("He was found guilty ___ murder.", "of", "guilty of",
     "<b>guilty of, innocent of, aware of, convinced of</b>.",
     ex("He was found <b>guilty of</b> fraud.")),
    ("She's engaged ___ a pilot.", "to", "engaged to",
     "<b>engaged to, married to, related to, connected to</b>.",
     ex("She's <b>engaged to</b> a pilot. / They're <b>related to</b> the CEO.")),
    ("I'm worried ___ the results.", "about", "worried about",
     "<b>worried about, concerned about, anxious about, nervous about</b>.",
     ex("I'm <b>worried about</b> the results.")),
    ("She's very good ___ children.", "with", "good with",
     "<b>good with, kind to, nice to, friendly to, hard on</b> (people).",
     ex("She's <b>good with</b> kids. / He's <b>nice to</b> everyone.")),
    ("He's very good ___ languages.", "at", "good at",
     "<b>good at + skills</b> / <b>good with + people/things</b>. This "
     "difference is key.",
     ex("<b>good at maths</b> (skill) vs <b>good with kids</b> (people).")),
    ("I'm tired ___ waiting.", "of", "tired of",
     "<b>tired of, sick of, fed up with</b> + <b>V-ing</b>.",
     ex("I'm <b>tired of waiting</b>. / <b>Fed up with</b> + <b>V-ing</b>.")),
], nivel="B2", tags=["adjective-preposition"])

# =================================================================== CLOZE

cloze(T, "The class begins {{c1::at}} 9 a.m. {{c2::on}} Monday.",
      extra="<div class='box rule'><span class='lbl'>at = time / on = day</span>"
            "<b>at</b> + hour · <b>on</b> + day · <b>in</b> + month/year/season. "
            "Combined: <b>at</b> 9 a.m. <b>on</b> Monday.</div>",
      tags="c1-c2 preposition cloze")

cloze(F1, "I look forward to {{c1::hearing}} from you.",
      extra="<div class='box warn'><span class='lbl'>to + -ing</span>"
            "<b>look forward to, be used to, get used to, object to</b>: here "
            "<b>to</b> is a PREPOSITION, so it takes <b>-ing</b>. "
            "<i>to see</i> is WRONG.</div>",
      tags="c1-c2 preposition cloze")
