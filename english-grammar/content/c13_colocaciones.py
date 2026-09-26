"""13 Collocations (B1-C2) - the words that only go together in English.

A typical error is 'I make a decision' for 'I take a decision'. In English
words 'marry': you cannot swap one without breaking the phrase.
This is the most useful module for natural, fluent English.
"""

from ._base import (gap, rule, prod, cloze, ex, ul, ol, table, tl, tabla,
                    badge, serie, serie_gap)

D = "13 Collocations::"
V, A, N, ADV, C = D + "Verb + Noun", D + "Adjective + Noun", \
    D + "Noun + Noun", D + "Adverb + Adjective", D + "Common Word Errors"

# ============================================== VERB + NOUN

serie_gap(V, [
    ("Can you ___ a decision?", "make", "make a decision",
     "Verbs that are NOT 'do/take' for this.",
     ex("<b>make a decision</b> (not <i>do</i>/<i>take</i> a decision).",
        "Vocabulary: <b>make</b> a decision, <b>make</b> progress, <b>make</b> "
        "a mistake, <b>make</b> an effort, <b>make</b> money, <b>make</b> a "
        "difference, <b>make</b> sense, <b>make</b> friends, <b>make</b> a "
        "reservation, <b>make</b> an appointment, <b>make</b> an assumption, "
        "<b>make</b> a fuss, <b>make</b> a scene.")),
    ("She ___ progress in her English.", "has made", "has made progress",
     "<b>make progress</b> = make progress. NEVER <i>do progress</i>.",
     ex("She's <b>made</b> great <b>progress</b>. / Has <b>made</b> any <b>progress</b>?")),
    ("He ___ a mistake.", "made", "made a mistake",
     "<b>make a mistake</b>. NEVER <i>do a mistake</i>.",
     ex("Everyone <b>makes mistakes</b>. / I <b>made</b> a big <b>mistake</b>.")),
    ("We need to ___ an effort.", "make", "make an effort",
     "<b>make an effort</b>. NEVER <i>do an effort</i>.",
     ex("You should <b>make an effort</b> to be on time. / <s>Do an effort</s> is WRONG.")),
    ("It doesn't ___ sense.", "make", "make sense",
     "<b>make sense</b> = make sense. <b>make a difference</b> = make a difference.",
     ex("That <b>makes sense</b>. / It <b>makes a difference</b> to me.")),
    ("She ___ a reservation for 8pm.", "made", "make a reservation",
     "<b>make a reservation / booking</b>. NEVER <i>do a reservation</i>.",
     ex("I've <b>made a booking</b> for 8pm. / The hotel is fully <b>booked</b>.")),
    ("The company ___ a lot of money.", "makes", "make money",
     "<b>make money</b> = make money. <b>earn money</b> also works but is more "
     "formal and more about merit.",
     ex("They <b>make</b> a fortune. / She <b>earns</b> a good salary.")),
    ("Can you ___ me a favour?", "do", "do a favour",
     "<b>do a favour</b>. NEVER <i>make a favour</i>.",
     ex("Can you <b>do me a favour</b>? / <s>Make me a favour</s> is WRONG.")),
    ("She ___ research on climate change.", "does", "do research",
     "<b>do research / a study / an experiment / homework / business / the "
     "dishes / maths</b>.",
     ex("She's <b>doing research on</b> climate change. / <b>Do</b> your <b>homework</b>.")),
    ("You should ___ your best.", "do", "do your best",
     "<b>do your best / your worst / your duty / your best to help</b>.",
     ex("<b>Do your best</b>. / Please <b>do</b> your <b>duty</b>.")),
    ("He made ___ impression on everyone.", "an", "make an impression",
     "<b>make an impression (on someone)</b>.",
     ex("She <b>made a strong impression on</b> us. / <b>Make a good/bad impression</b>.")),
    ("They reached ___ agreement.", "an", "reach an agreement",
     "<b>reach an agreement / a conclusion / a decision / a compromise</b>. "
     "NEVER <i>make an agreement</i>.",
     ex("They <b>reached an agreement</b>. / <b>Come to</b> an <b>agreement</b>.")),
    ("I'll ___ my best to help.", "do", "do my best",
     "<b>do one's best</b> = do one's best. NEVER <i>make my best</i>.",
     ex("I'll <b>do my best</b> to help. / <s>Make my best</s> is WRONG.")),
], nivel="B2", tags=["collocation verb-noun"])

# ============================================ ADJECTIVE + NOUN

serie_gap(A, [
    ("It was a ___ mistake.", "serious", "a serious mistake",
     "<b>serious mistake, big mistake, terrible mistake</b>.",
     ex("It was a <b>serious mistake</b>. / a <b>terrible mistake</b> / a <b>big mistake</b>.")),
    ("We need a ___ solution.", "practical", "a practical solution",
     "<b>practical solution, feasible solution, viable option, workable "
     "solution</b>.",
     ex("We need a <b>practical solution</b>. / a <b>viable option</b> / a "
        "<b>workable solution</b>.")),
    ("She's very ___ at interviews.", "good", "good at",
     "<b>good at, bad at, brilliant at, hopeless at</b> + a skill or activity.",
     ex("She's <b>good at</b> interviews. / He's <b>hopeless at</b> maths.")),
    ("It's a ___ mistake to sign that.", "grave", "a grave mistake",
     "<b>grave / serious / fatal / costly / painful / awkward / embarrassing</b> "
     "mistake.",
     ex("It'd be a <b>grave mistake</b> to sign that. / a <b>painful</b> / "
        "<b>awkward</b> mistake.")),
    ("He's under ___ arrest.", "arrest", "under arrest",
     "<b>under arrest</b> (the law). NEVER <i>under the arrest</i>.",
     ex("He was taken <b>under arrest</b>. / The police placed him <b>under arrest</b>.")),
    ("He's in ___ charge of the project.", "in", "in charge of",
     "<b>in charge of</b> = responsible. <b>in control of</b> = in command. "
     "<b>in the middle of</b> = in the middle of.",
     ex("She's <b>in charge of</b> the project. / He's <b>in control of</b> the team.")),
    ("She's ___ by a deadline.", "under", "under a deadline",
     "<b>under pressure, under control, under investigation, under arrest, "
     "under construction, under repair, under a deadline</b>.",
     ex("She's <b>under pressure</b>. / The road is <b>under repair</b>.")),
    ("The report was ___ .", "confidential", "a confidential report",
     "<b>confidential report, classified information, sensitive issue, private "
     "matter, public record, official statement</b>.",
     ex("This report is <b>confidential</b>. / a <b>sensitive issue</b> / a "
        "<b>private matter</b>.")),
    ("We need a ___ solution to the traffic problem.", "long-term",
     "a long-term solution",
     "<b>long-term / short-term solution, long-term goal, sustainable growth, "
     "economic downturn, breakthrough, turning point</b>.",
     ex("We need a <b>long-term solution</b>. / a <b>turning point</b> / a "
        "<b>breakthrough</b>.")),
    ("She's ___ by the news.", "shaken", "shaken by",
     "<b>shaken, stunned, devastated, thrilled, overwhelmed, puzzled, "
     "outraged</b> + by.",
     ex("She was <b>shaken by</b> the news. / <b>overwhelmed by</b> / "
        "<b>outraged by</b>.")),
], nivel="B2", tags=["collocation adjective-noun"])

# ============================================ NOUN + NOUN

serie_gap(N, [
    ("He works in the ___ industry.", "car", "the car industry",
     "<b>car industry, tourism industry, fashion industry, banking industry, "
     "tech industry, oil industry, film industry</b>.",
     ex("He works in the <b>car industry</b>. / the <b>tourism</b> / "
        "<b>entertainment</b> industry.")),
    ("She's a ___ consultant.", "management", "a management consultant",
     "<b>management consultant, financial adviser, tax consultant, career coach</b>.",
     ex("She's a <b>management consultant</b>. / a <b>financial adviser</b> / "
        "a <b>tax adviser</b>.")),
    ("He gave a ___ speech.", "keynote", "a keynote speech",
     "<b>keynote speech, welcome speech, closing speech, wedding speech, "
     "toast</b>.",
     ex("She gave the <b>keynote speech</b>. / the <b>welcome speech</b> at the conference.")),
    ("It's a ___ issue.", "sensitive", "a sensitive issue",
     "<b>sensitive issue, controversial topic, thorny issue, hot topic, grey area</b>.",
     ex("It's a <b>sensitive issue</b>. / a <b>thorny issue</b> / a <b>hot topic</b>.")),
    ("She gave birth ___ a healthy baby.", "to", "give birth to",
     "<b>give birth to, take care of, pay attention to, pay homage to, come up "
     "with, get rid of, do without, run out of, look after, look forward to, "
     "apply for, account for, blame for</b>.",
     ex("She <b>gave birth to</b> a healthy baby. / She's learning <b>to take "
        "care of</b> him.")),
    ("He has a ___ interest in art.", "keen", "a keen interest",
     "<b>keen interest, vested interest, personal interest, strong opinion, "
     "point of view, change of heart</b>.",
     ex("He has a <b>keen interest in</b> art. / a <b>point of view</b> / a "
        "<b>change of heart</b>.")),
    ("She has a strong ___ .", "opinion", "a strong opinion",
     "<b>strong opinion, weak point, selling point, key factor, main reason, "
     "common ground, worst case scenario</b>.",
     ex("She has a <b>strong opinion on</b> it. / the <b>key factor</b> / "
        "the <b>main reason</b> / <b>common ground</b>.")),
    ("He's under ___ .", "pressure", "under pressure",
     "<b>under pressure, in danger, in trouble, at risk, out of danger, on "
     "hold, off duty, on sale</b>.",
     ex("He's <b>under pressure</b> at work. / The project is <b>at risk</b>. / "
        "The item is <b>on sale</b>.")),
    ("She has ___ in common with her sister.", "a lot", "a lot in common",
     "<b>have a lot in common, have nothing in common, get on well with, keep "
     "in touch with, catch up with, look up to, put up with, come across as</b>.",
     ex("They <b>have a lot in common</b>. / I <b>get on well with</b> her.")),
    ("The talks broke ___ .", "down", "break down",
     "<b>break down, break out, break through, break up, break in, break into</b>.",
     ex("The talks <b>broke down</b>. / She <b>broke through</b> the barrier.")),
], nivel="C1", tags=["collocation noun-noun"])

# ============================================ ADVERB + ADJECTIVE

serie_gap(ADV, [
    ("The film was ___ acted.", "poorly", "poorly acted",
     "<b>-ly</b> adverbs go with <b>-ed</b> adjectives (never with <b>-ing</b>).",
     ex("<b>badly acted</b> is WRONG → <b>poorly acted</b>. / a "
        "<b>beautifully</b> <b>danced</b> / <b>beautifully</b> <b>expensive</b> "
        "(never).")),
    ("She's ___ qualified for the job.", "highly", "highly qualified",
     "<b>highly qualified, highly unlikely, highly controversial, deeply "
     "disappointed, deeply rooted, widely known, badly affected, badly "
     "designed, newly built, highly competitive, strongly opposed</b>.",
     ex("She's <b>highly qualified</b>. / <b>deeply</b> <b>disappointed</b> / "
        "<b>badly</b> <b>affected</b> / <b>widely</b> <b>known</b>.")),
    ("The results were ___ surprising.", "hardly", "hardly surprising",
     "<b>hardly</b> = hardly. <b>barely</b> = barely.",
     ex("The results were <b>hardly surprising</b>. / <b>hardly any</b> / "
        "<b>barely anyone</b>.")),
    ("It was a ___ flawed plan.", "badly", "badly flawed",
     "<b>badly designed, badly written, badly made, well designed, well "
     "written, highly controversial, widely criticised</b>.",
     ex("a <b>badly</b> <b>designed</b> website / a <b>well written</b> essay / "
        "<b>highly controversial</b> issue.")),
    ("She's ___ known in the industry.", "widely", "widely known",
     "<b>widely known, widely used, widely available, widely criticised, widely "
     "regarded as, widely believed</b>.",
     ex("She's <b>widely known</b> in the industry. / a <b>widely held</b> belief.")),
    ("The film was ___ received.", "poorly", "poorly received",
     "<b>poorly received, badly damaged, well received, long overdue, so far so good</b>.",
     ex("The film was <b>poorly received</b>. / <b>long overdue</b> / "
        "<b>so far so good</b>.")),
    ("They're ___ employed now.", "gainfully", "gainfully employed",
     "<b>gainfully employed, financially viable, commercially viable, "
     "politically correct, socially acceptable, legally binding</b>.",
     ex("They're <b>gainfully employed</b>. / a <b>financially viable</b> option / "
        "<b>legally binding</b> contract.")),
    ("The road is ___ maintained.", "poorly", "poorly maintained",
     "<b>poorly maintained, well maintained, badly designed, highly "
     "sensitive, strictly speaking, generally speaking</b>.",
     ex("The road is <b>poorly maintained</b>. / a <b>highly sensitive</b> issue / "
        "<b>strictly speaking</b>.")),
    ("The word is ___ used in physics.", "widely", "widely used",
     "<b>widely used, widely spoken, rarely used, commonly known, previously "
     "unknown, highly unlikely</b>.",
     ex("The word is <b>widely used</b> in physics. / a <b>rarely used</b> phrase.")),
    ("The results were ___ expected.", "widely", "widely expected",
     "<b>widely expected, widely reported, widely regarded, largely "
     "responsible, partly responsible, highly recommended</b>.",
     ex("The results were <b>widely expected</b>. / a <b>highly recommended</b> hotel.")),
    ("The whole thing is ___ confusing.", "rather", "rather confusing",
     "<b>rather confusing, quite confusing, rather expensive, quite a few, "
     "rather a lot, quite frankly, quite simply</b>.",
     ex("The whole thing is <b>rather confusing</b>. / <b>quite a few</b> people / "
        "<b>quite frankly</b>.")),
    ("She's ___ aware of the problem.", "well", "well aware",
     "<b>well aware, well aware of, well suited, well connected, well "
     "established, well dressed</b>.",
     ex("She's <b>well aware of</b> the problem. / <b>well established</b> / "
        "<b>well suited</b> for the role.")),
    ("He's ___ informed about the risks.", "poorly", "poorly informed",
     "<b>poorly informed, badly informed, well informed, politically "
     "motivated, financially motivated</b>.",
     ex("He's <b>poorly informed about</b> the risks. / <b>well informed</b> / "
        "<b>politically motivated</b>.")),
    ("The deadline is ___ approaching.", "fast", "fast approaching",
     "<b>fast approaching, hard to believe, difficult to imagine, easy to use, "
     "simple to use</b>.",
     ex("The deadline is <b>fast approaching</b>. / <b>difficult to imagine</b> / "
        "<b>easy to use</b>.")),
    ("She's ___ to succeed if she keeps trying.", "bound",
     "bound to succeed",
     "<b>bound to, unlikely to, certain to, likely to, free to, faithful to, "
     "similar to, close to, aware of</b>.",
     ex("She's <b>bound to succeed</b>. / <b>unlikely to</b> / <b>free to</b> / "
        "<b>faithful to</b>.")),
], nivel="C1", tags=["collocation adverb-adjective"])

# ================================================ COMMON WORD ERRORS

serie_gap(C, [
    ("I ___ a big mistake.", "made", "made a mistake",
     "WRONG: <i>do a mistake</i>. Correct: <b>make a mistake</b>.",
     ex("Everyone <b>makes mistakes</b>. / <s>Everyone does mistakes</s> is WRONG.")),
    ("He ___ research at university.", "does", "does research",
     "WRONG: <i>make research</i>. Correct: <b>do research</b>.",
     ex("She <b>does research on</b> cancer. / <s>Makes research</s> is WRONG.")),
    ("Please ___ me a hand.", "give", "give me a hand",
     "<b>give someone a hand</b> = to give someone a hand. NEVER <i>make a "
     "hand</i> or <i>do a hand</i>.",
     ex("<b>Give me a hand</b> with this box. / <b>Give me a break</b> = give me "
        "a break.")),
    ("I need to ___ an appointment.", "book", "book an appointment",
     "<b>make / book / arrange an appointment</b>. NEVER <i>do an appointment</i>.",
     ex("I need to <b>book an appointment</b>. / The receptionist <b>arranged</b> an appointment.")),
    ("She ___ me a favour last week.", "did", "did me a favour",
     "<b>do a favour</b>. NEVER <i>make a favour</i>.",
     ex("She <b>did me a favour</b>. / <s>Made me a favour</s> is WRONG.")),
    ("Let's ___ a deal.", "make", "make a deal",
     "<b>make a deal, make a decision, make a difference, make a mistake, make "
     "a reservation, make an effort, make progress</b>.",
     ex("Let's <b>make a deal</b>. / It <b>made a difference</b>.")),
    ("He's going to ___ his best to help.", "do", "do his best",
     "<b>do one's best</b>. NEVER <i>make one's best</i>.",
     ex("I'll <b>do my best</b> to help. / <s>Make my best</s> is WRONG.")),
    ("I need to ___ a shower.", "take", "take a shower",
     "<b>take a shower / bath</b> (AmE: <b>take a shower, take a bath</b>). BrE "
     "also <b>have a shower</b>.",
     ex("I need to <b>take a shower</b>. / I'm going to <b>take a bath</b>.")),
    ("The police made ___ arrest.", "an", "make an arrest",
     "<b>make an arrest</b> / <b>place someone under arrest</b>. NEVER "
     "<i>do an arrest</i>.",
     ex("The police <b>made an arrest</b>. / He was <b>placed under arrest</b>.")),
    ("I gave ___ to his proposal.", "in", "give in",
     "<b>give in</b> = to give in. <b>give up</b> = to give up. "
     "<b>give away</b> = to give away.",
     ex("She <b>gave in</b> to pressure. / Don't <b>give up</b>! / "
        "<b>Don't give away</b> the ending.")),
    ("The word derives ___ Latin.", "from", "derive from",
     "<b>derive from, result from, stem from, account for, consist of, insist "
     "on, depend on, rely on, base on</b>.",
     ex("The word <b>derives from</b> Latin. / The problem <b>stems from</b> poor planning.")),
    ("That's a ___ . I won't do it.", "no-go", "a no-go",
     "Fixed opinion expressions: <b>no-go, deal-breaker, a done deal, off the "
     "table, on the table, in the bag, out of the question</b>.",
     ex("That's a <b>no-go</b>. I won't do it. / <b>a done deal</b> / "
        "<b>off the table</b> / <b>in the bag</b>.")),
    ("We need to ___ this problem once and for all.", "address", "address",
     "<b>address a problem, tackle a problem, address an issue, get to grips "
     "with, deal with, resolve, sort out, iron out, nip in the bud</b>.",
     ex("We need to <b>address</b> this problem once and for all. / "
        "<b>iron out</b> / <b>nip in the bud</b>.")),
], nivel="C1", tags=["collocation common-error"])

# =================================================================== CLOZE

cloze(V, "Can you {{c1::make}} a decision?",
      extra="<div class='box rule'><span class='lbl'>make ≠ do/take</span>"
            "<b>make a decision, make progress, make a mistake, make an "
            "effort, make a reservation, make an appointment, make a "
            "difference</b>. With <b>do</b>: <b>do research, do homework, do "
            "business, do a favour, do one's best</b>.</div>",
      tags="c1-c2 collocation cloze")

cloze(C, "The whole thing is {{c1::utterly ridiculous}}.",
      extra="<div class='box note'><span class='lbl'>Degree adverbs</span>"
            "<b>utterly, totally, completely, highly, deeply, badly, well, "
            "wide, far</b> + adjective/participle. Very useful to push your "
            "level up to C1.</div>",
      tags="c1-c2 collocation cloze")
